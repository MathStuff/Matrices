def grouping(mat,col):
    from MatricesM.customs.objects import Group

    #Assert dataframe
    if not mat._dfMat:
        raise TypeError("Grouping is only available on dataframes")

    #Assert column names exist
    if isinstance(col,str):
        if not col in mat.features:
            raise NameError(f"'{col}' is not a column name")
    elif isinstance(col,list):
        for name in col:
            if not name in mat.features:
                raise NameError(f"'{name}' is not a column name")
            if col.count(name) != 1:
                raise IndexError(f"{name} can't appear in the given list more than once")
    elif col != None:
        raise TypeError("'column' parameter only accepts str|list of strings|None")
    
    #All possible groups
    #Use row labels
    if col == None:
        grp = []
        for ind in mat.index:
            if not ind in grp:
                grp.append(ind)

        if len(grp) == 1:
            return mat

        return Group([(group,mat.ind[group]) for group in grp],names=col)

    #Use given columns
    else:
        #Group by single column
        if len(col) == 1:
            grp = mat.uniques(col)

            if len(grp) == 1:
                return mat

            return Group([(group,mat[mat[col]==group]) for group in grp],names=col)

        #Group by multiple columns
        else:
            grp = []
            cut_matrix = mat.select(tuple(col))
            for ind in cut_matrix.matrix:
                if not ind in grp:
                    grp.append(ind)

            if len(grp) == 1:
                return mat

            table = []
            for group in grp:
                filtered = cut_matrix.copy
                for i,value in enumerate(group):
                    filtered = filtered[filtered[col[i]]==value]
                table.append(tuple([group,filtered]))
            
            return Group(table,names=col)