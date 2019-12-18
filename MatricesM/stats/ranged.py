def ranged(mat,col,get,obj,dFrame):
    from ..customs.objects import Label

    rang = mat._declareRange(mat._matrix)
    feats = mat.features.labels
    
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    col = feats.index(col)+1 if isinstance(col,(tuple,str)) else col

    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        name = feats[col-1]
        rang = {name:rang[name]}
    
    #Return a matrix
    if get==2:
        cols = list(rang.keys())
        return obj((len(cols),1),[[[i,j]] for i,j in rang.values()],features=["Range"],dtype=dFrame,coldtypes=[list],index=Label(cols,mat.features.names[:]))
    #Return a dictionary
    elif get==1:
        if col==None:
            return rang
        return {feats[col-1]:rang[feats[col-1]]}
    #Return a list
    else:  
        items=list(rang.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]