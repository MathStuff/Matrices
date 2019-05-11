def mean(mat,col=None,asDict=True):
    """
    col:integer|None ; column number
    Mean of the columns
    asDict: True|False ; Wheter or not to return a dictionary with features as keys means as values, if set to False:
        1) If there is only 1 column returns the value as it is
        2) If there are multiple columns returns the values in order in a list
    """
    try:
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
            t=sum([mat.matrix[r][c] for r in range(mat.dim[0])])
            avg[feats[c]]=t/mat.dim[0]
   
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
