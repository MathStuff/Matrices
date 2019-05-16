def readAll(d,head,dtyps):
    try:
        feats=[]
        if d[-4:] == ".csv":  
            import csv

            data=[]
            r=0
            with open(d) as f:
                fread  = csv.reader(f,delimiter=",")
                if head:
                    for i in fread:
                        feats = i[:]
                        del i
                        break
                
                if dtyps!=[]:
                    data = [[dtyps[i](row[i]) for i in range(len(row))] for row in fread]
                else:
                    data = [[row[i] for i in range(len(row))] for row in fread]

        else:
            data="" 
            with open(d,"r",encoding="utf8") as f:
                for lines in f:
                    data+=lines
    except FileNotFoundError as err:
        raise FileNotFoundError("No such file or directory :"+",".join(list(err.args)))
    except IndexError as err:
        f.close()
        raise IndexError("Directory is not valid :"+",".join(list(err.args)))
    else:
        f.close()
        return (data,feats)

