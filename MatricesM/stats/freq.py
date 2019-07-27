def freq(mat,col,get,obj,dFrame):
    from collections import Counter
    from MatricesM.errors.errors import MatrixError

    #Get the parts needed
    #No argument given
    if col==None:
        temp=mat.t
        feats=mat.features[:]
        r=mat.dim[1]
    #Column index or name given
    else:
        if isinstance(col,str):
            col=mat.features.index(col)+1
        if col != None:
            if col<=0 or col>mat.d1:
                raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        temp=mat[:,col-1].t
        feats=mat.features[col-1]
        r=1

    res={}

    #Iterate over the transposed rows
    for rows in range(r):
        a=dict(Counter(temp.matrix[rows]))

        #Add to dictionary
        if col!=None:
            res[feats]=a
        else:
            res[feats[rows]]=a

    #Return matrices
    if get==2:
        return tuple(obj((len(list(c.keys())),1),[i for i in c.values()],features=["Frequencies"],dtype=dFrame,coldtypes=[int],index=list(c.keys()),indexname=feat) for feat,c in res.items())
    #Return a dictionary
    elif get==1:
        return res
    #Return a list
    else:
        items=list(res.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]

def _count(mat,col,get,obj,dFrame):
    colds = mat.coldtypes[:]
    feats = mat.features[:]

    #Column name given
    if isinstance(col,str):
        if not col in feats:
            raise NameError(f"{col} is not a column name")
        col = feats.index(col)
        colrange = [col]
    #Column number given
    elif isinstance(col,int):
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        colrange = [col-1]
    #None given
    else:
        colrange = range(mat.d1)

    counts = {feats[i]:len([1 for k in mat.col(i+1,0) if type(k) == colds[i]]) for i in colrange}
    
    #Return a matrix
    if get == 2:
        cols = list(counts.keys())
        return obj((len(cols),1),[i for i in counts.values()],features=["Valid_values"],dtype=dFrame,coldtypes=[int],index=cols,indexname="Column")
    #Return a dictionary
    elif get == 1:
        return counts
    #Return a list
    else:
        items=list(counts.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]
