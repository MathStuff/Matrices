def wheres(mat,conds,feats,inplace):
    #Replace comparison operators with proper symbols
    if " and " in conds:
        conds = conds.replace(" and ","&")
    if " or " in conds:
        conds = conds.replace(" or ","|")
    if ' is ' in conds:
        conds = conds.replace(" is ","==")
    if " = " in conds:
        conds = conds.replace(" = ","==")

    if inplace:
        #Replace feature names with column matrices
        for f in feats:
            if f in conds:
                conds = conds.replace(f,f"mat['{f}']")

        #Apply the conditions and find out where it is True
        allinds = eval(conds).find(1,0)
        if allinds == None:
            raise ValueError("No data found")
            
        inds = [i[0] for i in eval(conds).find(1,0)]
        filtered = [mat.matrix[i][:] for i in inds]
        return (filtered,inds)
    else:
        mat._Matrix__use_value_based_comparison=True

        del mat._Matrix__use_value_based_comparison
        
