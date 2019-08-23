def mean(mat,col,get,obj,dFrame):   
    from MatricesM.customs.objects import null

    if isinstance(col,str):
        col=mat.features.index(col)+1
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        col -= 1

    avg={}
    feats=mat.features[:]
    inds = []
    mm = mat.matrix

    if mat._dfMat:
        dts = mat.coldtypes
        if col==None:
            for i in range(len(dts)):
                if dts[i] not in [int,float,complex]:
                    continue
                else:
                    inds.append(i)
        else:
            if dts[col] not in [int,float,complex]:
                raise TypeError(f"Can't use {dts[col]} dtype (column{col+1}) to calculate the mean")
            else:
                inds = [col]
    else:
        if col==None:
            inds = range(0,mat.dim[1])
        else:
            inds = [col]  
            
    for c in inds:
        t=0 #Total
        i=0 #Index
        vals=0 #How many valid elements were in the column
        while True:#Loop through the column
            try:
                while i<mat.dim[0]:
                    t+=mm[i][c]
                    i+=1
                    vals+=1
            except:#Value was invalid
                i+=1
                continue
            else:
                if vals!=0:
                    avg[feats[c]]=t/vals
                else:#No valid values found
                    avg[feats[c]]=null
                break
    #Return a matrix
    if get == 2:
        cols = list(avg.keys())
        means = [i for i in avg.values()]
        cdtypes = [complex] if any([1 if isinstance(val,complex) else 0 for val in means]) else [float]
        return obj((len(cols),1),means,features=["Mean"],dtype=dFrame,coldtypes=cdtypes,index=cols,indexname="Column")
    #Return a dictionary
    elif get == 1:
        return avg

    #Return a list
    else:
        items=list(avg.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col]
