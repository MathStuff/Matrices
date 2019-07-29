def readAll(d,encoding,delimiter):
    def is_float(data):
        try:
            n = float(data)
            return True
        except:
            return False

    def is_int(data):
        try:
            if "." in data:
                return False
            n = int(data)
            return True
        except:
            return False

    try:
        feats = []
        data = []
        dtyps = []
        from random import sample

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

        #Choose dtypes for columns           
        samples = sample(data,30) if len(data)>30 else data

        ints = [[is_int(d) for d in row] for row in samples]
        floats = [[is_float(d) for d in row] for row in samples]

        objs = [int,float,str]
        
        for i in range(len(samples[0])):
            i_c,f_c = 0,0
            for j in range(len(samples)):
                if (ints[j][i] and floats[j][i]): #int
                    i_c += 1
                if (ints[j][i] or floats[j][i]): #float
                    f_c += 1

            #Decide the dtype for the column
            if (i_c >= f_c) and (i_c>=1):
                dtyps.append(int)
            elif (i_c < f_c) and (f_c>=1):
                dtyps.append(float)
            else:
                dtyps.append(str)

    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory")
    except IndexError:
        f.close()
        raise IndexError("Directory is not valid")
    else:
        f.close()
        return (feats,data,dtyps)

