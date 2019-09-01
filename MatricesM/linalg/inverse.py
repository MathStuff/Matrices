def inverse(mat,ident):
    if not mat.isSquare or mat.isSingular:
        return None
    else:
        temp=mat.copy
        temp.concat(ident)
        inv=temp.rrechelon[:,mat.dim[1]:]
        if mat._cMat:
            dt = complex
        else:
            dt = float
        inv._Matrix__dtype = dt
        inv._Matrix__features = mat.features[:]
        return inv