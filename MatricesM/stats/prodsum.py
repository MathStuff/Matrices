def _prodsum(mat,col,get,obj,dFrame,isSum):
    def p(lis):
        prd=1
        for i in lis:
            prd*=i
        return prd

    if isinstance(col,str):
        col = feats.index(col)
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")

    colds = mat.coldtypes[:]
    feats = mat.features[:]

    if isSum:
        p = sum
    vals = {feats[i]:p(mat.col(i+1,0)) for i in [j for j in range(mat.dim[1]) if colds[j] in [int,float,complex]]}
    
    #Return a matrix
    if get == 2:
        cols = mat.d1 if col==None else 1
        return obj((cols,2),[[i,j] for i,j in vals.items()],features=["Column",["Product","Sum"][isSum]],dtype=dFrame,coldtypes=[str,complex],index=None)
    #Return a dictionary
    elif get == 1:
        return vals
    #Return a list
    else:
        items=list(vals.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]
