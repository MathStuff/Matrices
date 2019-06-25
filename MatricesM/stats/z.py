def z(mat,col=None,population=1,empty=None):
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
        
    scores = empty
    m = mat.mean(col)
    s = mat.sdev(col,population=population)

    if m == None or s == None:
        raise ValueError("Can't get mean and standard deviation")
        
    feats = mat.features
    availablecols = list(m.keys())
    all_inds = [i for i in range(mat.dim[1]) if feats[i] in availablecols]
    mm = mat.matrix
    l = len(all_inds)
    for i in range(mat.dim[0]):
        j=0 #Index
        while True:#Loop through the column
            try:
                while j<l:
                    ind = all_inds[j]
                    scores._matrix[i][ind] = (mm[i][ind]-m[feats[ind]])/s[feats[ind]]
                    j+=1
            except:#Value was invalid
                j+=1
                continue
            else:
                break  

    scores._Matrix__dim = [dims[0],l]
    scores._Matrix__features = availablecols
    return scores