def concat(mat,matrix,axis,fill):
    #Assertions
    if matrix.dtype==complex and mat.dtype!=complex:
        raise TypeError("Can't concatenate complex valued matrix to real valued matrix")

    d0,d1 = mat.dim
    md0,md1 = matrix.dim
    newmat = matrix.copy

    #Fill null if needed
    if fill:
        from MatricesM.customs.objects import null   
        if axis==0:
            for i in range(0,d1-md1):
                newmat.add([null for _ in range(md0)],col=d1+i+1)
                md1 += 1
        elif axis==1:
            for i in range(0,d0-md0):
                newmat.add([null for _ in range(md1)],row=d0+i+1)
                md0 += 1
                
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
