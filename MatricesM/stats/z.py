def z(mat,col=None,population=1,empty=None):
    """
    z-scores of the elements
    column:integer>=1 |None ; z-score of the desired column
    population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
    
    Give no arguments to get the whole scores in a matrix
    """
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
    d = [i for i in range(mat.dim[1]) if feats[i] in availablecols]
 
    scores._matrix=[[(mat.matrix[r][c]-m[feats[c]])/s[feats[c]] for c in d] for r in range(scores.dim[0])]   
    scores._Matrix__dim=[dims[0],len(d)]
    scores.features = availablecols
   
    return scores