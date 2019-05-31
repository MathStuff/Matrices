def mean(mat,col=None,asDict=True):
    try:    
        if isinstance(col,str):
            col=mat.features.index(col)+1
        assert (isinstance(col,int) and col>=1 and col<=mat.dim[1]) or col==None
        
        avg={}
        feats=mat.features[:]
        inds = []
        if mat._dfMat:
            dts = mat.coldtypes
            if col==None:
                for i in range(len(dts)):
                    if dts[i] == str:
                        continue
                    else:
                        inds.append(i)
            else:
                if dts[col-1] == str:
                    raise TypeError(f"Can't use str dtype (column{col}) to calculate the mean")
                else:
                    inds = [col-1]
        else:
            if col==None:
                inds = range(0,mat.dim[1])
            else:
                inds = [col-1]  
                
        for c in inds:
            t=0 #Total
            i=0 #Index
            vals=0 #How many valid elements were in the column
            while True:#Loop through the column
                try:
                    while i<mat.dim[0]:
                        t+=mat.matrix[i][c]
                        i+=1
                        vals+=1
                except:#Value was invalid
                    i+=1
                    continue
                else:
                    if vals!=0:
                        avg[feats[c]]=t/vals
                    else:#No valid values found
                        avg[feats[c]]=None
                    break
            
   
    except AssertionError:
        print("Col parameter should be in range [1,amount of columns]")
    except Exception as err:
        print("Error in 'mean':\n\t",err)
        return None
    
    else:
        if asDict:
            return avg
        
        items=list(avg.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]
