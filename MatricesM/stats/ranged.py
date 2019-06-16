def ranged(mat,col=None,asDict=True):
    if isinstance(col,str):
        col = mat.features.index(col)+1
    rang = mat._declareRange(mat._matrix)
    
    if asDict:
        if col==None:
            return rang
        return {mat.features[col-1]:rang[mat.features[col-1]]}
                
    items=list(rang.values())
    if len(items)==1:
        return items[0]
    
    if col==None:
        return items
    return items[col-1]