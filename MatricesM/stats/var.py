def var(mat,col=None,population=1,asDict=True):
    """
    Variance in the columns
    col:integer>=1 |None ; Number of the column, None to get all columns 
    population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
    asDict: True|False ; Wheter or not to return a dictionary with features as keys variance as values, if set to False:
        1) If there is only 1 column returns the value as it is
        2) If there are multiple columns returns the values in order in a list
    """
    s=mat.sdev(col,population)
    vs={}
    for k,v in s.items():
        vs[k]=v**2
    if asDict:
        return vs
        
    items=list(vs.values())
    if len(items)==1:
        return items[0]
    
    if col==None:
        return items
    return items[col-1]