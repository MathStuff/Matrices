def transpose(mat,hermitian=False,obj=None):
    if mat.isIdentity:
        return mat
    
    temp=mat._matrix
    d0,d1=mat.dim[0],mat.dim[1]
    if hermitian:
        transposed=[[temp[cols][rows].conjugate() for cols in range(d0)] for rows in range(d1)]
    else:
        transposed=[[temp[cols][rows] for cols in range(d0)] for rows in range(d1)]
    
    return obj((d1,d0),transposed,dtype=mat.dtype)
