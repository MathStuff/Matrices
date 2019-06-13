def inverse(mat,ident):
    """
    Returns the inversed matrix
    """
    from MatricesM.matrix import dataframe
    if not mat.isSquare or mat.isSingular:
        return None
    else:
        temp=mat.copy
        temp.concat(ident,"col")
        mat._inv=temp.rrechelon[:,mat.dim[1]:]
        if mat.dtype in [float,int,dataframe]:
            dt = float
        else:
            dt = complex
        mat._inv.dtype = dt
        mat._inv.features = mat.features[:]
        return mat._inv