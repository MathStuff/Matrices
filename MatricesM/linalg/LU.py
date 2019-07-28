def LU(mat,z,copy,obj):    
    if not mat.isSquare:
        return (None,None,None)

    from MatricesM.C_funcs.linalg import CLU
    calcs = CLU(mat.dim,z,copy,mat._cMat)
    if mat._cMat:
        dt = complex
    else:
        dt = float
    return (obj(mat.dim,calcs[0],dtype=dt,implicit=True),calcs[1],obj(mat.dim,calcs[2],dtype=dt,implicit=True))