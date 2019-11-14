def declareDim(mat):
    nullobj = mat.DEFAULT_NULL

    m = mat._matrix
    if m in [None,[],{},[[]]]:
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
                m[i] += [nullobj for _ in range(col_length-row_length)]

        return [rows,col_length]
    
def declareRange(mat,lis,df):
    nullobj = mat.DEFAULT_NULL
    c={}
    d0,d1 = mat.dim
    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]
        
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
                c[feats[cols]]=[nullobj,nullobj]
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

def declareColdtypes(lis,nullname="null"):
    from random import sample
    import re
    
    def is_float(data):
        try:
            if type(data).__name__ == nullname:
                return False
            n = float(data)
            return True
        except:
            return False

    def is_int(data):
        try:
            if type(data).__name__ == nullname:
                return False
            if "." in str(data):
                return False
            n = int(data)
            return True
        except:
            return False

    def is_complex(data):
        pattern=r"\-?[0-9]+(?:\.?[0-9]*)[-+][0-9]+(?:\.?[0-9]*)j"
        if re.findall(pattern,str(data)):
            return True
        return False

    #Choose dtypes for columns           
    samples = sample(lis,30) if len(lis)>30 else lis
    dtyps = []
    
    ints = [[is_int(d) for d in row] for row in samples]
    floats = [[is_float(d) for d in row] for row in samples]
    complexs = [[is_complex(d) for d in row] for row in samples]

    for i in range(len(samples[0])):
        i_c,f_c,c_c = 0,0,0
        for j in range(len(samples)):
            if (ints[j][i] and floats[j][i]): #Can be used as int
                i_c += 1
            if (ints[j][i] or floats[j][i]): #Can be used as float
                f_c += 1
            if complexs[j][i]: #Can be used as complex
                c_c += 1

        #Decide the dtype for the column
        if (i_c >= f_c) and (i_c>=1): #int over float
            dtyps.append(int)
        elif (i_c < f_c) and (f_c>=1): #float over int
            dtyps.append(float)
        elif (c_c > 0): #complex over str
            dtyps.append(complex)
        else: #Nothing worked, use str
            dtyps.append(str)

    return dtyps
