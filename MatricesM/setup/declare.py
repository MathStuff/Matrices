def declareDim(mat):
    """
    Set new dimension 
    """
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
    """
    Finds and returns the range of the elements in a given list
    """
    c={}
    if mat._dfMat:
        valid_feats_inds = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
        for cols in valid_feats_inds:
            current = mat.col(cols+1,0)
            temp=[val for val in current if isinstance(val,(int,float))]
            c[mat.features[cols]]=[min(temp),max(temp)]
    elif mat._cMat:
        for i in range(mat.dim[1]):
            temp=[]
            for rows in range(mat.dim[0]):
                temp.append(lis[rows][i].real)
                temp.append(lis[rows][i].imag)
            c[mat.features[i]]=[min(temp),max(temp)]
    else:
        for cols in range(mat.dim[1]):
            temp=mat.col(cols+1,0)
            c[mat.features[cols]]=[min(temp),max(temp)]
    return c
