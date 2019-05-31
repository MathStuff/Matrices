def var(mat,col=None,population=1,asDict=True):
    if isinstance(col,str):
        col=mat.features.index(col)+1
    s=mat.sdev(col,population)
    if s == None:
        raise ValueError("Can't get standard deviations")
    vs={}
    for k,v in s.items():
        vs[k]=v**2
    if asDict:
        return vs
        
    items=list(vs.values())
    if len(items)==1:
        return items[0]
    
    if col==None:
        return items
    return items[col-1]