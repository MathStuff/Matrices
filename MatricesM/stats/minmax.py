def _minmax(mat,col,get,ismax,obj,dFrame):

    if col==None:
        feats = mat.features[:]
        ranges = mat.ranged(get=0)
        if not isinstance(ranges[0],list):
            ranges = [ranges]
        m = {feats[i]:ranges[i][ismax] for i in range(len(ranges))}
    else:
        if isinstance(col,str):
            col = mat.features.index(col)+1
        if col != None:
            if col<=0 or col>mat.d1:
                raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        name = mat.features[col-1]
        m = {name:mat.ranged(name,get=0)[ismax]}
    
    #Return a matrix
    if get==2:
        cols = mat.d1 if col==None else 1
        return obj((cols,2),[[i,j] for i,j in m.items()],features=["Column",["Minimum","Maximum"][ismax]],dtype=dFrame,coldtypes=[str,float],index=None)
    #Return a dictionary
    elif get==1:
        return m
    #Return a list
    else:
        if col != None:
            return list(m.values())[0]
        return list(m.values())