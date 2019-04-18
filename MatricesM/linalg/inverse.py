def inverse(mat,ident):
    """
    Returns the inversed matrix
    """
    if not mat.isSquare or mat.isSingular:
        return None
    else:
        temp=mat.copy
        temp.concat(ident,"col")
        mat._inv=temp.rrechelon.subM(1,mat.dim[0],mat.dim[1]+1,mat.dim[1]*2)
        mat._Matrix__invCalc=1
        return mat._inv