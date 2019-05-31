def readAll(d,head,dtyps):
    try:
        feats=[]
        if d[-4:] == ".csv":  
            import csv

            data=[]
            r=0
            with open(d) as f:
                fread  = list(csv.reader(f,delimiter=","))
                if head:
                    feats = fread[0]
                    fread = fread[1:]
                
                if dtyps!=[]:
                    for i in range(len(fread)):
                        j=0
                        data.append([])
                        while j<len(fread[i]):
                            try:
                                if dtyps[j] != type: 
                                    data[i].append(dtyps[j](fread[i][j]))
                                j+=1
                            except:
                                data[i].append(fread[i][j])
                                j+=1
                                continue
                else:
                    data = [[row[i] for i in range(len(row))] for row in fread]

        else:
            data="" 
            with open(d,"r",encoding="utf8") as f:
                for lines in f:
                    data+=lines
    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory")
    except IndexError:
        f.close()
        raise IndexError("Directory is not valid")
    else:
        f.close()
        return (data,feats)

