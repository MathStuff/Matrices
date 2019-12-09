def z(mat,col=None,population=1,obj=None):
    from ..customs.objects import Label

    if isinstance(col,str):
        col=mat.features.index(col)+1
        
    if population not in [0,1]:
        raise ValueError("population should be 0 for samples, 1 for population")
        
    if col==None:
        dims=mat.dim
        
    elif isinstance(col,int) and col>=1 and col<=mat.dim[1]:
        dims=[mat.dim[0],1]
    
    else:
        if col!=None and not isinstance(col,int):
            raise TypeError("column parameter should be either an integer or None type")
        raise ValueError("column value is out of range")
        
    m = mat.mean(col)
    s = mat.sdev(col,population=population)

    if m == None or s == None:
        raise ValueError("Can't get mean and standard deviation")
        
    feats = mat.features
    labels = feats.labels if feats.level != 1 else [label[0] for label in feats.labels]
    availablecols = list(m.keys())
    all_inds = [i for i in range(mat.dim[1]) if labels[i] in availablecols]
    
    mm = mat.matrix
    l = len(all_inds)
    defnull = mat.DEFAULT_NULL
    scores = []

    for i in range(mat.dim[0]):
        j=0 #Index
        row = mm[i]
        vals = []
        while True:
            try:
                while j<l:
                    ind = all_inds[j]
                    name = labels[ind]
                    vals.append((row[ind]-m[name])/s[name])
                    j+=1
            except:#Value was invalid
                vals.append(defnull)
                j+=1
                continue
            else:
                scores.append(vals)
                break  

    return obj(dim=[dims[0],l],data=scores,features=Label(availablecols,feats.names))