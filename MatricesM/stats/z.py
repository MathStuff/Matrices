def z(mat,row=None,col=None,population=1,empty=None):
    """
    z-scores of the elements
    row:integer>=1 |None ; z-score of the desired row
    column:integer>=1 |None ; z-score of the desired column
    population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
    
    Give no arguments to get the whole scores in a matrix
    """
    if population not in [0,1]:
        raise ValueError("population should be 0 for samples, 1 for population")
        
    if col==None and ( (isinstance(row,int) and row>=1 and row<=mat.dim[1]) or row==None ):
        dims=mat.dim
        feats=mat.features
        sub=mat.copy
        
    elif isinstance(col,int) and col>=1 and col<=mat.dim[1] and row==None:
        dims=[mat.dim[0],1]
        feats=mat.features[col-1]
        sub=mat[:,col-1]
        col=1
        
    elif (isinstance(col,int) and col>=1 and col<=mat.dim[1]) and (isinstance(row,int) and row>=1 and row<=mat.dim[0]):
        return (mat.matrix[row-1][col-1]-mat.mean(col,asDict=0))/mat.sdev(col,asDict=0)
    
    else:
        if (col!=None and row!=None) and not ( isinstance(row,int) and isinstance(col,int) ):
            raise TypeError("row and column parameters should be either integers or None types")
        raise ValueError("row and/or column value(s) are out of range")
        
    scores = empty
    m = sub.mean(asDict=0)
    s = sub.sdev(population=population,asDict=0)
    
    #Put single values in a list for calculation's favor
    if not isinstance(m,list):
        m = [m]
    if not isinstance(s,list):
        s = [s]

    scores._matrix=[[(sub.matrix[r][c]-m[c])/s[c] for c in range(scores.dim[1])] for r in range(scores.dim[0])]   

    if row!=None and col==None:
        return scores[row-1:,:]    
    return scores