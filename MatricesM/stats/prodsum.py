def _prodsum(mat,col,get,obj,dFrame,isSum,inf_limit):
    import math

    def sums(lis,limit,length):
        i = 0
        total=0
        try:
            while i<length:
                num = lis[i]
                if isinstance(num,valid_types):
                    total+=num
                i+=1
        except OverflowError:
            return math.inf
        except:
            return math.nan
        else:
            if abs(total) > limit:
                return math.inf
            return total

    def prod(lis,limit,length):
        i = 0
        prd=1
        try:
            while i<length:
                num = lis[i]
                if isinstance(num,valid_types):
                    prd*=num
                i+=1
        except OverflowError:
            return math.inf
        except:
            return math.nan
        else:
            if abs(prd) > limit:
                return math.inf
            return prd


    if isinstance(col,str):
        col = feats.index(col)
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")

    colds = mat.coldtypes[:]
    feats = mat.features[:]
    valid_types = (int,float,complex)
    d0,d1 = mat.dim

    if isSum:
        func = sums
    else:
        func = prod
        
    vals = {feats[i]:func(mat.col(i+1,0),inf_limit,d0) for i in [j for j in range(mat.dim[1]) if colds[j] in valid_types]}
    
    #Return a matrix
    if get == 2:
        cols = list(vals.keys())
        return obj((len(cols),1),[i for i in vals.values()],features=[["Product","Sum"][isSum]],dtype=dFrame,coldtypes=[complex],index=cols,indexname="Column")
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
