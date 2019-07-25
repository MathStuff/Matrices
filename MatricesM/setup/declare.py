def declareDim(mat):
    m = mat._matrix
    if m == None:
        mat._matrix = []
        return [0,0]
    rows= len(m)
    cols = len(m[0])
    for i in range(rows):
        if cols != len(m[i]):
            raise IndexError("Matrix has different length rows")

    return [rows,cols]
    
def declareRange(mat,lis):
    c={}
    #Dataframe
    if mat._dfMat:
        valid_feats_inds = [t for t in range(mat.d1) if mat.coldtypes[t] in [float,int]]
        for cols in valid_feats_inds:
            current = mat.col(cols+1,0)
            temp=[val for val in current if isinstance(val,(int,float))]
            try:
                mn,mx = min(temp),max(temp)
            except:
                #All values are invalid
                temp=[len(str(val)) for val in current ]
                c[mat.features[cols]]=[min(temp),max(temp)]
            else:
                c[mat.features[cols]]=[mn,mx]

    #Complex dtype
    elif mat._cMat:
        try:
            for i in range(mat.dim[1]):
                temp=[]
                for rows in range(mat.dim[0]):
                    temp.append(lis[rows][i].real)
                    temp.append(lis[rows][i].imag)
                c[mat.features[i]]=[min(temp),max(temp)]
        except AttributeError:
            raise TypeError(f"complex dtype matrix only allows complex numbers as its elements")

    #Float or int dtype
    else:
        try:
            for cols in range(mat.dim[1]):
                temp=mat.col(cols+1,0)
                c[mat.features[cols]]=[min(temp),max(temp)]
        except (TypeError,ValueError):
            typ = [int,float][mat._fMat]
            raise ValueError(f"{typ} dtype matrix can't have non-{typ} values")

    return c
