def var(mat,col,population,get,obj,dFrame):
    from MatricesM.customs.objects import null
    
    if isinstance(col,str):
        col=mat.features.index(col)+1
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
            vs[k]=null
    #Return a matrix
    if get==2:
        cols = list(vs.keys())
        return obj((len(cols),1),[i for i in vs.values()],features=["Variance"],dtype=dFrame,coldtypes=[complex],index=cols,indexname="Column")
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