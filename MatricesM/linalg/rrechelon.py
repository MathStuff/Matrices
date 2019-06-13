def rrechelon(mat,copy,obj,rrechelon):
    from MatricesM.matrix import dataframe
    from MatricesM.C_funcs.linalg import Crrechelon
    
    res = Crrechelon(copy,mat._cMat,mat.dim,rrechelon)
    if mat.dtype in [float,int,dataframe]:
        dt = float
    else:
        dt = complex
    return (obj(mat.dim[:],res[0],dtype=dt,implicit=True),res[1])
