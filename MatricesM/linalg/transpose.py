def transpose(mat,hermitian=False,obj=None):
    if mat.isIdentity:
        return mat
    
    temp=mat._matrix
    d0,d1=mat.dim[0],mat.dim[1]
    if hermitian:
        transposed=[[temp[cols][rows].conjugate() for cols in range(d0)] for rows in range(d1)]
    else:
        from MatricesM.C_funcs.linalg import Ctranspose
        transposed = Ctranspose(d0,d1,temp)
    
    return obj((d1,d0),transposed,dtype=mat.dtype,implicit=True)
