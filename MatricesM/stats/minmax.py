def _minmax(mat,col,dic,ismax):
    if col==None:
        feats = mat.features[:]
        ranges = mat.ranged(asDict=False)
        if not isinstance(ranges[0],list):
            ranges = [ranges]
        m = {feats[i]:ranges[i][ismax] for i in range(len(ranges))}
    else:
        if isinstance(col,str):
            col = mat.features.index(col)+1
        name = mat.features[col-1]
        m = {name:mat.ranged(name,asDict=False)[ismax]}
    
    if dic:
        return m
    if col != None:
        return list(m.values())[0]
    return list(m.values())