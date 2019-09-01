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

