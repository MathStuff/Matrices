def symDecomp(mat):
    """
    Decompose the matrix into a symmetrical and an antisymmetrical matrix
    """
    if not mat.isSquare or mat._cMat:
        return (None,None)
    
    else:
        m = mat.matrix
        anti = mat.floatForm
        anti._matrix = [[0 for i in range(mat.dim[0])] for j in range(mat.dim[0])]
        for i in range(0,mat.dim[0]-1):
            for j in range(i+1,mat.dim[1]):
                avg = (m[i][j]+m[j][i])/2
                anti.matrix[i][j] = m[i][j]-avg
                anti.matrix[j][i] = m[j][i]-avg
        sym = mat-anti
        return (sym,anti)