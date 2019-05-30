def applyop(mat,e,cols,conds,feats=None):
    #If no expression is given, raise an exception
    if e == None:
        raise ValueError("Expression parameter can't be left as None")
    
    #Get arguments into tuples if they are given as strings 
    if type(e) not in [tuple,list]:
        e = (e,)
    if type(cols) not in [tuple,list]:
        cols = (cols,)
        
    #If no column names given, assume all columns
    if cols == (None,) or cols == None:
        cols = feats

    #Matrix and dimension base
    [filtered,inds] = (mat._matrix,list(range(mat.dim[0])))

    #Split the given operators and duplicate if necessary
    ops = [op.split(" ") for op in e]
    
    if len(ops)==1 and len(ops) != len(cols):
        ops = ops*len(cols)
    elif len(ops) != len(cols):
        raise ValueError("Bad amount of expressions for the given columns")

    #Get indeces of which columns to operate on
    featinds = [feats.index(i) for i in cols]

    #Get indeces which rows to operate on
    if conds != None:
        from MatricesM.filter.where import wheres
        inds = wheres(mat,conds,feats)[1]
        
    #Execute the operations
    for i in inds:
        for j in range(len(featinds)):
            for op in ops[j]:
                ind = featinds[j]
                exec(f"filtered[i][ind]=eval('filtered[i][ind]'+op)")
    
    return mat




