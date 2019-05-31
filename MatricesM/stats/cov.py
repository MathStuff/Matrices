def cov(mat,col1=None,col2=None,population=1):
    for i in [col1,col2]:
        if isinstance(i,str):
            i=mat.features.index(i)+1
    
    if not ( isinstance(col1,int) and isinstance(col2,int) ):
        raise TypeError("col1 and col2 should be integers or column names")
        
    if population not in [0,1]:
        raise ValueError("population should be 0 for samples, 1 for population")
    
    if not ( col1>=1 and col1<=mat.dim[1] and col2>=1 and col2<=mat.dim[1] ):
        raise ValueError("col1 and col2 are not in the valid range")

    c1,c2 = mat.col(col1,0),mat.col(col2,0)
    m1,m2 = mat.mean(col1,asDict=0),mat.mean(col2,asDict=0)
    try:
        s = sum([(c1[i]-m1)*(c2[i]-m2) for i in range(len(c1))])
    except TypeError:
        raise TypeError("Error getting covariance, replace invalid values first")
    return s/(len(c1)-1+population)