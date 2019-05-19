def rrechelon(mat,copy,obj):
    """
    Returns reduced row echelon form of the matrix
    """
    from MatricesM.C_funcs.linalg import Crrechelon
    return Crrechelon(copy,obj,mat._cMat,mat.dim)
