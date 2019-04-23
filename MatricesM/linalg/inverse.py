def inverse(mat,ident):
    """
    Returns the inversed matrix
    """
    if not mat.isSquare or mat.isSingular:
        return None
    else:
        temp=mat.copy
        temp.concat(ident,"col")
        mat._inv=temp.rrechelon[:,mat.dim[1]:]
        return mat._inv