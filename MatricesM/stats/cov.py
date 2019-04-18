def cov(mat,col1=None,col2=None,population=1):
    """
    Covariance of two columns
    col1,col2: integers>=1  ; column numbers
    population: 0 or 1 ; 0 for samples, 1 for population
    """
    if not ( isinstance(col1,int) and isinstance(col2,int) ):
        raise TypeError("col1 and col2 should be integers")
        
    if population not in [0,1]:
        raise ValueError("population should be 0 for samples, 1 for population")
    
    if not ( col1>=1 and col1<=mat.dim[1] and col2>=1 and col2<=mat.dim[1] ):
        raise ValueError("col1 and col2 are not in the valid range")

    c1,c2 = mat.col(col1,0),mat.col(col2,0)
    m1,m2 = mat.mean(col1,asDict=0),mat.mean(col2,asDict=0)
    s = sum([(c1[i]-m1)*(c2[i]-m2) for i in range(len(c1))])
    
    return s/(len(c1)-1+population)