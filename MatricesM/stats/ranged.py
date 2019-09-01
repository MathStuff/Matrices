def ranged(mat,col,get,obj,dFrame):

    feats = mat.features
    rang = mat._declareRange(mat._matrix)

    if isinstance(col,str):
        col = feats.index(col)+1
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        name = feats[col-1]
        rang =  {name:rang[name]}
    
    #Return a matrix
    if get==2:
        cols = list(rang.keys())
        return obj((len(cols),1),[[[i,j]] for i,j in rang.values()],features=["Range"],dtype=dFrame,coldtypes=[list],index=cols,indexname="Column")
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