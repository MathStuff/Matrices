def _minmax(mat,col,get,ismax,obj,dFrame):
    from ..customs.objects import Label
    
    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    col = feats.index(col)+1 if isinstance(col,(tuple,str)) else col

    if col==None:
        ranges = mat.ranged(get=0)
        if not isinstance(ranges[0],list):
            ranges = [ranges]
        m = {feats[i]:ranges[i][ismax] for i in range(len(ranges))}
    else:
        if col != None:
            if col<=0 or col>mat.d1:
                raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        name = feats[col-1]
        m = {name:mat.ranged(name,get=0)[ismax]}
    
    #Return a matrix
    if get==2:
        cols = list(m.keys())
        return obj((len(cols),1),[i for i in m.values()],features=[["Minimum","Maximum"][ismax]],dtype=dFrame,coldtypes=[float],index=Label(cols,mat.features.names[:]))
    #Return a dictionary
    elif get==1:
        return m
    #Return a list
    else:
        if col != None:
            return list(m.values())[0]
        return list(m.values())