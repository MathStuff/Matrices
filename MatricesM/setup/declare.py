def declareDim(mat):
    from MatricesM.customs.objects import null
    m = mat._matrix
    if m == None:
        mat._matrix = []
        return [0,0]
    try:
        rows = len(m)
        col_length = max([len(row) for row in m])
    except:
        raise IndexError("'data' parameter should get list of lists")
    else:
        for i in range(rows):
            row_length = len(m[i])
            if col_length != row_length:
                m[i] += [null for _ in range(col_length-row_length)]

        return [rows,col_length]
    
def declareRange(mat,lis):
    c={}
    d0,d1 = mat.dim
    feats = mat.features
    #Dataframe
    if mat._dfMat:
        colds = mat.coldtypes
        valid_feats_inds = [t for t in range(d1) if colds[t] in [float,int]]
        for cols in valid_feats_inds:
            current = mat.col(cols+1,0)
            temp=[val for val in current if isinstance(val,(int,float))]
            try:
                mn,mx = min(temp),max(temp)
            except:
                #All values are invalid
                temp=[len(str(val)) for val in current ]
                c[feats[cols]]=[min(temp),max(temp)]
            else:
                c[feats[cols]]=[mn,mx]

    #Complex dtype
    elif mat._cMat:
        try:
            for i in range(d1):
                temp=[]
                for rows in range(d0):
                    num = lis[rows][i]
                    temp.append(num.real)
                    temp.append(num.imag)
                c[feats[i]]=[min(temp),max(temp)]
        except AttributeError:
            raise TypeError(f"complex dtype matrix only allows complex numbers as its elements")

    #Float or int dtype
    else:
        try:
            for cols in range(d1):
                temp = [lis[rows][cols] for rows in range(d0)]
                c[feats[cols]]=[min(temp),max(temp)]
        except (TypeError,ValueError):
            typ = [int,float][mat._fMat]
            raise ValueError(f"{typ} dtype matrix can't have non-{typ} values")

    return c

def declareColdtypes(lis):
    from random import sample
    def is_float(data):
        try:
            if type(data).__name__ == "null":
                return False
            n = float(data)
            return True
        except:
            return False

    def is_int(data):
        try:
            if type(data).__name__ == "null":
                return False
            if "." in str(data):
                return False
            n = int(data)
            return True
        except:
            return False

    #Choose dtypes for columns           
    samples = sample(lis,30) if len(lis)>30 else lis
    dtyps = []
    
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

    return dtyps
