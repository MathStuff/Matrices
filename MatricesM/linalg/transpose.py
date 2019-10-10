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

    old_f = mat.features[:] if mat._dfMat else None
    old_i = mat.index.labels[:] if mat._dfMat else []
    return obj((d1,d0),transposed,dtype=mat.dtype,features=old_i,index=old_f,implicit=True)
