def concat(mat,matrix,axis,fill,obj):

    d0,d1 = mat.dim
    #Type check of given matrix
    if not isinstance(matrix,obj):
        raise TypeError(f"Can't concatenate type '{type(matrix).__name__}' to self")

    #Empty matrix
    if [d0,d1] == [0,0]:
        return mat

    #Assertions
    if matrix.dtype==complex and not (mat.dtype.__name__ in ['complex','dataframe']):
        raise TypeError("Can't concatenate complex valued matrix to real valued matrix")

    md0,md1 = matrix.dim
    newmat = matrix.copy

    #Fill null if needed
    if fill:
        nullobj = mat.DEFAULT_NULL   
        if axis==0:
            #Given matrix is smaller
            for i in range(0,d1-md1):
                newmat.add([nullobj for _ in range(md0)],col=d1+i+1)
                md1 += 1
            #Given matrix is bigger
            for i in range(0,md1-d1):
                mat.add([nullobj for _ in range(d0)],col=md1+i+1)
                d1 += 1

        elif axis==1:
            #Given matrix is smaller
            for i in range(0,d0-md0):
                newmat.add([nullobj for _ in range(md1)],row=d0+i+1)
                md0 += 1
            #Given matrix is bigger
            for i in range(0,md0-d0):
                mat.add([nullobj for _ in range(d1)],row=md0+i+1)
                d0 += 1
           
    if axis==0:
        assert d1==md1 , "Dimensions don't match for concatenation"
    elif axis==1:
        assert d0==md0 , "Dimensions don't match for concatenation"
    
    #Concat
    if axis==0:
        new = newmat.matrix
        for rows in range(md0):
            mat._matrix.append(new[rows])

    elif axis==1:
        new = newmat.matrix
        for rows in range(md0):
            mat._matrix[rows]+=new[rows]
    else:
        return None    

    #Update attributes
    mat._Matrix__dim=mat._declareDim()
    if axis==1:
        newfeats = []
        for name in newmat.features:
            while name in mat.features:
                name = "_"+name
            newfeats.append(name)

        mat._Matrix__features = mat.features + newfeats
        mat._Matrix__coldtypes = mat.coldtypes + [i for i in newmat.coldtypes]
    else:
        if mat._dfMat:
            newinds = [ind for ind in newmat.index] if newmat._dfMat else ["" for _ in range(md0)]
            mat._Matrix__index = mat.index + newinds
