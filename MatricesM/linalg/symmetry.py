def symDecomp(mat,obj):
    """
    Decompose the matrix into a symmetrical and an antisymmetrical matrix
    """
    if not mat.isSquare or mat._cMat:
        return (None,None)
    
    else:
        m = mat.matrix
        anti = obj
        for i in range(0,mat.dim[0]-1):
            for j in range(i+1,mat.dim[1]):
                avg = (m[i][j]+m[j][i])/2
                anti.matrix[i][j] = m[i][j]-avg
                anti.matrix[j][i] = m[j][i]-avg
        sym = mat-anti
        return (sym,anti)