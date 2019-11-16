def freq(mat,col,get,obj,dFrame):
    from collections import Counter
    from MatricesM.errors.errors import MatrixError
    from MatricesM.customs.objects import Label

    #Get the parts needed
    #No argument given
    if col==None:
        temp=mat.t
        feats = mat.features.labels
        if mat.features.level == 1:
            feats = [row[0] for row in feats]
        r=mat.dim[1]
    #Column index or name given
    else:
        if isinstance(col,str):
            col=mat.features.index(col)+1
        if col != None:
            if col<=0 or col>mat.d1:
                raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
        temp=mat[:,col-1].t
        feats = mat.features.labels[col-1]
        if mat.features.level == 1:
            feats = feats[0]
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
        temp = []
        for feat,c in res.items():
            repeats = list(c.keys())
            temp.append(obj((len(repeats),1),
                        [i for i in c.values()],
                        features=["Frequency"],
                        dtype=dFrame,
                        coldtypes=[int],
                        index=Label(repeats,str(feat)[1:-1])))
        return tuple(temp)
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
    from MatricesM.customs.objects import Label

    colds = mat.coldtypes[:]
    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]
    #Column name given
    if isinstance(col,str):
        if not col in feats:
            raise NameError(f"{col} is not a column name")
        col = mat.features.index(col)
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
        return obj((len(cols),1),[i for i in counts.values()],features=["Valid_values"],dtype=dFrame,coldtypes=[int],index=Label(cols,["Column"]))
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
