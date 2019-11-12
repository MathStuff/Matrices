def _replace(mat,old,new,col,cond,obj,lvl):
    names = mat.features.get_level(lvl)
    #Handle arguments
    if not isinstance(cond,obj) and cond!=None:
        raise TypeError("conditions should be a boolean matrix or None")

    temp = []
    if isinstance(col,(tuple,list)):
        for i in col:
            if isinstance(i,int):
                temp.append(names[i-1])
            elif isinstance(i,str):
                temp.append(i)
            else:
                raise TypeError(f"{i} can't be used as column name or number")
        col = temp

    elif isinstance(col,str):
        if not col in names:
            raise ValueError(f"{col} isn't a column name")
        col = (col,)

    elif col in [None,(None,),[]]:
        col = names[:]

    else:
        raise TypeError("column parameter only accepts str|tuple|list|None")

    #(bool_mat,value,columns,bool_mat)
    if isinstance(old,obj):
        if cond != None:
            rowinds = [i[0] for i in (cond & old).find(1,0)]
        else:
            rowinds = [i[0] for i in old.find(1,0)]
        colinds = [names.index(c) for c in col]
        for r in rowinds:
            for c in colinds:
                mat._matrix[r][c] = new
    else:
        try:
            indices = []
            for feat in col:
                try:
                    for i in mat.col(feat,namelevel=lvl).find(old,0):
                        indices.append([i[0],names.index(feat)])
                except:
                    continue #No data was found on given column

            if indices == []:
                raise Exception #Nothing was found
        except:
            raise ValueError("No data found to be replaced in given columns")
        else:
            if cond!=None:
                filtered = [i for i in cond.find(1,0,True)]
                indices = [i for i in r1 if i[0] in filtered]

            for r,c in indices:
                mat._matrix[r][c] = new