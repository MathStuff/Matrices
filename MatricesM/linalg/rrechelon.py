def rrechelon(mat,copy,obj,rrechelon):
    from ..C_funcs.linalg import Crrechelon
    
    res = Crrechelon(copy,mat._cMat,mat.dim,rrechelon)
        
    if mat._cMat:
        dt = complex
    else:
        dt = float

    return (obj(mat.dim[:],res[0],dtype=dt,implicit=True),res[1])
