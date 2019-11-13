def _combine(mat,cols,foo,feat,dt,inplace,lvl,dframe):
    
    from MatricesM.validations.validate import consistentlist

    if not isinstance(cols,(tuple,list)):
        raise TypeError("Column names should be given in a tuple/list")
    
    d0,d1 = mat.dim
    all_names = mat.features
    mm = mat.matrix

    #Get column indices
    #Column names in the same level given as strings
    if consistentlist(cols,str):
        level = all_names.get_level(lvl)
        colinds = [level.index(col) for col in cols]

    #Column names given in tuples, no need to check level
    elif consistentlist(cols,tuple):
        labels = all_names.labels
        colinds = [labels.index(name) for name in cols]

    else:
        raise TypeError("Column names should all be given in tuples or as strings")
    
    #Filter the matrix
    filtered_matrix = mat[:,list(colinds)]
    filtered_mm = filtered_matrix.matrix

    #Create the matrix to concatenate
    col_matrix = dframe(dim=(d0,1),fill=mat.DEFAULT_NULL,features=[feat],coldtypes=[dt])

    #Apply given function
    for i,row in enumerate(filtered_mm):
        try:
            val = foo(*tuple(row))
        except:
            val = mat.DEFAULT_NULL

        col_matrix._matrix[i] = [val]
    
    if inplace:
        mat.concat(col_matrix,axis=1)
        return mat

    return col_matrix
