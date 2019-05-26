def rrechelon(mat,copy,obj):
    """
    Returns reduced row echelon form of the matrix
    """
    from MatricesM.C_funcs.linalg import Crrechelon
    res = Crrechelon(copy,mat._cMat,mat.dim)
    if mat.dtype in ["float","integer","dataframe"]:
        dt = "float"
    else:
        dt = "complex"
    return (obj(mat.dim[:],res[0],dtype=dt,implicit=True),res[1])
