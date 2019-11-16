def readAll(d,encoding,delimiter):
    from MatricesM.setup.declare import declareColdtypes
    try:
        feats = []
        data = []
        
        if d[-4:] == ".csv":  
            import csv
            import itertools
            
            sample_head = ''.join(itertools.islice(open(d,"r",encoding=encoding), 6))
            header = csv.Sniffer().has_header(sample_head)

            with open(d,"r",encoding=encoding) as f:
                data = [line for line in csv.reader(f,delimiter=delimiter)]
                if header:
                    feats = data[0][:]
                    del data[0]
                

        else:
            with open(d,"r",encoding=encoding) as f:
                for lines in f:
                    row = lines.split(delimiter)
                    #Remove new line chars
                    while "\n" in row:
                        try:
                            i = row.index("\n")
                            del row[i]
                        except:
                            continue

                    data.append(row)

        dtyps = declareColdtypes(data)

    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory")
    except IndexError:
        f.close()
        raise IndexError("Directory is not valid")
    else:
        f.close()
        return (feats,data,dtyps)

def save_csv(mat,dr,newln,enc,opts):
    import csv
    with open(dr,"w",newline=newln,encoding=enc) as f:
        writer_obj = csv.writer(f)
        mm = mat.matrix
        use_labels = not "no_index" in opts
        use_names = not "no_name" in opts
        ind = mat.index
        labels = ind.labels
        feats = mat.features

        custom_iter = [[""]*(ind.level-1) + [feats.names[i-1]] + feats.get_level(i) for i in range(1,feats.level+1)] + [list(ind.names) + [""]*mat.d1] if (use_labels and use_names) \
                      else [list(ind.names) + [""]*mat.d1] if (use_labels) \
                      else [[feats.names[i-1]] + feats.get_level(i) for i in range(1,feats.level+1)] if (use_names) \
                      else []

        if use_labels:    
            for i in range(mat.d0):
                custom_iter.append(list(labels[i]) + mm[i])
        else:
            col_name_extracol = [""] if use_names else []
            for i in range(mat.d0):
                custom_iter.append(col_name_extracol+mm[i])

        writer_obj.writerows(custom_iter)

    print("File successfully created at path: "+dr,end="")

