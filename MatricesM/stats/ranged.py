def ranged(mat,col=None,asDict=True):
    if isinstance(col,str):
        col=mat.features.index(col)+1
    mat._inRange=mat._declareRange(mat._matrix)
    if asDict:
        if col==None:
            return mat._inRange
        return {mat.features[col-1]:mat._inRange[mat.features[col-1]]}
                
    items=list(mat._inRange.values())
    if len(items)==1:
        return items[0]
    
    if col==None:
        return items
    return items[col-1]