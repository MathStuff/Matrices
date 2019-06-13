def LU(mat,z,copy,obj):
    from MatricesM.matrix import dataframe
    
    if not mat.isSquare:
        return (None,None,None)

    from MatricesM.C_funcs.linalg import CLU
    calcs = CLU(mat.dim,z,copy,mat._cMat)
    if mat.dtype in [float,int,dataframe]:
        dt = float
    else:
        dt = complex
    return (obj(mat.dim,calcs[0],dtype=dt,implicit=True),calcs[1],obj(mat.dim,calcs[2],dtype=dt,implicit=True))