def transpose(mat,hermitian=False,obj=None,labelobj=None):
    from ..customs.objects import Label
    
    if mat.isIdentity:
        return mat
    
    temp=mat._matrix
    d0,d1=mat.dim
    if hermitian:
        transposed=[[temp[cols][rows].conjugate() for cols in range(d0)] for rows in range(d1)]
    else:
        from ..C_funcs.linalg import Ctranspose
        transposed = Ctranspose(d0,d1,temp)

    inds = mat.features[:] if mat._dfMat else None
    feats = Label([tuple([str(label) for label in row]) for row in mat.index.labels[:]],mat.index.names) if mat._dfMat else None

    return obj((d1,d0),transposed,dtype=mat.dtype,features=feats,index=inds,implicit=True)
