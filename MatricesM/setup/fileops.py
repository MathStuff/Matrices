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

def save_csv(mat,dr,newln,enc,*args):
    import csv
    with open(dr,"w",newline=newln,encoding=enc) as f:
        writer_obj = csv.writer(f)
        mm = mat.matrix
        ind = mat.index
        labels = ind.labels

        custom_iter = [list(ind.names) + mat.features]
                
        for i in range(mat.d0):
            custom_iter.append(list(labels[i]) + mm[i])
        
        writer_obj.writerows(custom_iter)
    print("File successfully created at path: "+dr,end="")
    