def var(mat,col,population,get,obj,dFrame):
    from ..customs.objects import Label
    nullobj = mat.DEFAULT_NULL
    
    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    col = feats.index(col)+1 if isinstance(col,(tuple,str)) else col

    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")

    s=mat.sdev(col,population)
    if s == None:
        raise ValueError("Can't get standard deviations")
    vs={}
    for k,v in s.items():
        try:
            vs[k]=v**2
        except:
            vs[k]=nullobj
    #Return a matrix
    if get==2:
        cols = list(vs.keys())
        v = [i for i in vs.values()]
        cdtypes = [complex] if any([1 if isinstance(val,complex) else 0 for val in v]) else [float]
        return obj((len(cols),1),v,features=["Variance"],dtype=dFrame,coldtypes=cdtypes,index=Label(cols,mat.features.names[:]))
    #Return a dictionary
    elif get==1:
        return vs
    else:
        items=list(vs.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]