def applyop(mat,e,cols,conds,feats,apply_method,obj):

    if type(cols) not in [tuple,list]:
        cols = (cols,)
        
    #If no column names given, assume all columns
    if cols == (None,) or cols == None:
        cols = feats

    #Get indeces which rows to operate on
    if conds != None:
        if isinstance(conds,str):
            from MatricesM.filter.where import wheres
            inds = wheres(mat,conds,feats,True)[1]
        elif isinstance(conds,obj):
            if conds.d1 != 1:
                raise ValueError("Given matrix should be a column matrix")
            inds = conds.find(1,0,True)
        else:
            raise TypeError(f"'{type(conds).__name__}' can't be used to get row indices")
    else:
        inds = list(range(mat.dim[0]))

    #Matrix and dimension base
    filtered = mat._matrix
    #Get indeces of which columns to operate on
    featinds = [feats.index(i) for i in cols]

    if apply_method:
        #If no expression is given, raise an exception
        if e == None:
            raise ValueError("Expression parameter can't be left as None")
        
        #Get arguments into tuples if they are given as strings 
        if type(e) not in [tuple,list]:
            e = (e,)

        #Split the given operators and duplicate if necessary
        ops = [op.split(" ") for op in e]
        
        if len(ops)==1 and len(ops) != len(cols):
            ops = ops*len(cols)
        elif len(ops) != len(cols):
            raise ValueError("Bad amount of expressions for the given columns")

        #Execute the operations
        for i in inds:
            for j in range(len(featinds)):
                for op in ops[j]:
                    try:
                        ind = featinds[j]
                        exec(f"filtered[i][ind]=eval('filtered[i][ind]'+op)")
                    except:
                        continue
        
        return mat

    else:
        if not type(e).__name__ in ['function','builtin_function_or_method','type']:
            raise TypeError(f"'{type(e).__name__}' type can't be used as a function")

        #Execute the operations
        for i in inds:
            for j in featinds:
                try:
                    filtered[i][j] = e(filtered[i][j])
                except:
                    continue
        return mat