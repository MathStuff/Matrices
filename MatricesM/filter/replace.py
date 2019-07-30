def _replace(mat,old,new,col,cond,obj):
    #Assert parameters
    if not isinstance(col,(str,tuple,list)) and col!=None:
        raise TypeError("column parameter only accepts str|tuple|list|None")
    if not isinstance(cond,obj) and cond!=None:
        raise TypeError("conditions should be a boolean matrix or None")
    if isinstance(col,str):
        col = (col,)
    #(bool_mat,value,columns,bool_mat)
    if isinstance(old,obj):
        if cond != None:
            rowinds = [i[0] for i in (cond & old).find(1,0)]
        else:
            rowinds = [i[0] for i in old.find(1,0)]
        colinds = [mat.features.index(c) for c in col]
        for r in rowinds:
            for c in colinds:
                mat._matrix[r][c] = new
    else:
        try:
            r1 = list(set([i[0] for feat in col for i in mat.col(feat).find(old,0)]))
        except:
            raise ValueError("No data found to be replaced in given columns")
        else:
            if cond!=None:
                r2 = [i[0] for i in cond.find(1,0)]
                rowinds = [i for i in r1 if i in r2]
            else:
                rowinds = r1

            colinds = [mat.features.index(c) for c in col]
            for r in rowinds:
                for c in colinds:
                    mat._matrix[r][c] = new