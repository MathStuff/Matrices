def rrechelon(mat,copy,obj):
    """
    Returns reduced row echelon form of the matrix
    """
    from MatricesM.C_funcs.linalg import Crrechelon
    res = Crrechelon(copy,mat._cMat,mat.dim)
    return (obj(mat.dim[:],res[0],dtype=mat.dtype,implicit=True),res[1])
