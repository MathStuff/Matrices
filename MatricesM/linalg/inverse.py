def inverse(mat,ident):
    """
    Returns the inversed matrix
    """
    from MatricesM.matrix import dataframe
    if not mat.isSquare or mat.isSingular:
        return None
    else:
        temp=mat.copy
        temp.concat(ident)
        inv=temp.rrechelon[:,mat.dim[1]:]
        if mat.dtype in [float,int,dataframe]:
            dt = float
        else:
            dt = complex
        inv._Matrix__dtype = dt
        inv._Matrix__features = mat.features[:]
        return inv