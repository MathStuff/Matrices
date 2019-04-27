def perma(mat):
    """
    Permanent of the matrix
    """
    if not mat.isSquare:
        return None
    
    if mat.isIdentity:
        return 1
    
    if mat.dim[0]==2:
        m = mat._matrix
        return m[0][0]*m[1][1] + m[1][0]*m[0][1]
    
    if mat.dim[0]==3:
        m = mat._matrix
        return (m[0][0]*m[1][1]*m[2][2] + 
                m[0][1]*m[1][2]*m[2][0] +
                m[0][2]*m[1][0]*m[2][1] +
                m[0][2]*m[1][1]*m[2][0] +
                m[0][1]*m[1][0]*m[2][2] +
                m[0][0]*m[1][2]*m[2][1]
                )
    total=0
    for i in range(mat.dim[0]):
        temp = mat.copy
        temp.remove(col=1)
        temp.remove(row=i+1)

        co = mat.matrix[i][0]

        total += co*perma(temp)
        
    return total