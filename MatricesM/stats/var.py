def var(mat,col,population,get,obj,dFrame):
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
        vs[k]=v**2
    
    #Return a matrix
    if get==2:
        cols = mat.d1 if col==None else 1
        return obj((cols,2),[[i,j] for i,j in vs.items()],features=["Column","Variance"],dtype=dFrame,coldtypes=[str,complex])
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