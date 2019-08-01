def joins(mat,cols,method,other,conds,null,obj):
    #######Type checks start#######
    #Matrix assertion
    if not isinstance(other,obj):
        raise TypeError("'JOIN' only accepts Matrix objects")

    #dataframe check
    assert mat.dtype.__name__ == "dataframe" \
    and other.dtype.__name__ == "dataframe" , "'join' method only works with dataframes"
    
    d0,d1 = mat.dim
    md0,md1 = other.dim
    feats,mfeats = mat.features[:],other.features[:]

    #Method name check
    methods = ['INNER','LEFT','LEFT-EX','RIGHT','RIGHT-EX','FULL','FULL-EX','CROSS']
    if not method in methods:
        raise ValueError(f"{method} is not a join method.")

    #If no condition given, its same as 'CROSS' join method
    if conds == None:
        method = 'CROSS'
    elif isinstance(conds,str):
        groups = mat.where(conds,inplace=False)
        pass

    else:
        raise TypeError("'ON' can only work with strings or None")

    #Selected columns check
    if isinstance(cols,(tuple,list)):
        for col in cols:
            if not isinstance(col,obj):
                raise TypeError("'SELECT' only accepts column matrices")
            else:
                assert col.d1 == 1 , "'SELECT' only accepts column boolean matrices"
                assert col.d0 == d0, f"'SELECT' should have matrices with {d0} rows, not {conds.d0}"

    elif cols == "*":
        other = other.copy
        #Get new columns from the passed matrix
        for name in mfeats:
            if name in feats:
                del other[name]

        #Repeat rows in self and add new columns to each row
        self_matrix,other_matrix = mat._matrix,other._matrix

        #Cross-join
        if method == "CROSS":
            inds = [index for _ in range(md0) for index in mat.index[:]]
            temp = [row+other_matrix[repeat] for repeat in range(md0) for row in self_matrix]
            return obj([d0*md0,d1+other.d1],temp,features=feats+other.features,
                       index=inds,indexname=mat.indexname,dtype=mat.dtype,coldtypes=mat.coldtypes+other.coldtypes,
                       implicit=True)
        
        elif method == "INNER":
            pass
        
    else:   
        raise TypeError("'SELECT' only accepts tuple/list of column matrices or '*'")

    
    #######Type checks end#######
    #Start joining
    pass