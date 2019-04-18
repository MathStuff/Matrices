def ranged(mat,col=None,asDict=True):
    """
    col:integer|None ; column number
    Range of the columns
    asDict: True|False ; Wheter or not to return a dictionary with features as keys ranges as lists, if set to False:
        1) If there is only 1 column returns the list as it is
        2) If there are multiple columns returns the lists in order in a list        
    """
    mat._inRange=mat._declareRange(mat._matrix)
    if asDict:
        if col==None:
            return mat._inRange
        return {mat.features[col-1]:mat._inRange[mat.features[col-1]]}
                
    items=list(mat._inRange.values())
    if len(items)==1:
        return items[0]
    
    if col==None:
        return items
    return items[col-1]