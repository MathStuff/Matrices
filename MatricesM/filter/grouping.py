def grouping(mat,col,dFrame,lvl):
    from ..customs.objects import Group,Label

    feats = mat.features.get_level(lvl)
    #Assert dataframe
    if not mat._dfMat:
        raise TypeError("Grouping is only available on dataframes")

    #Assert column names exist
    if isinstance(col,str):
        if not col in feats:
            raise NameError(f"'{col}' is not a column name")
        col = [col]
    elif isinstance(col,list):
        for name in col:
            if not name in feats:
                raise NameError(f"'{name}' is not a column name")
            if col.count(name) != 1:
                raise IndexError(f"{name} can't appear in the given list more than once")
    elif col != None:
        raise TypeError("'column' parameter only accepts str|list of strings|None")
    
    #All possible groups
    #Use row labels
    if col == None:
        grp = []
        for ind in mat.index.labels:
            if not ind in grp:
                grp.append(ind)

        if len(grp) == 1:
            return mat

        return Group([(group,mat.ind[group]) for group in grp],names=col)

    #Use given columns
    else:
        #Group by single column
        if len(col) == 1:
            grp = mat.uniques(col[0])

            if len(grp) == 1:
                return mat

            return Group([(group,mat[mat[col[0]]==group]) for group in grp],names=col)

        #Group by multiple columns
        else:
            grp = []
            for ind in mat.select(tuple(col)).matrix:
                if not ind in grp:
                    grp.append(ind)

            if len(grp) == 1:
                return mat
            
            #Get each row's group
            tables = [tuple([group,[]]) for group in grp]
            #Column indices by names
            columnindices = [feats.index(name) for name in col]

            #Row labels for groups
            index_column = mat.index[:]
            groups_indices = [tuple([group,[]]) for group in grp]

            for i,row in enumerate(mat.matrix):
                #Get needed columns of the row
                grp_ind = grp.index([row[i] for i in columnindices])
                #Add row to its group,store row's index
                tables[grp_ind][1].append(row)
                groups_indices[grp_ind][1].append(index_column[i])

            table = []
            cdtyps = mat.coldtypes
            indname = mat.index.names
            for i,group in enumerate(tables):
                table.append((group[0],dFrame(group[1],features=feats[:],
                                              coldtypes=cdtyps[:],
                                              index=Label(groups_indices[i][1],indname),
                                              )))
            return Group(table,names=col)