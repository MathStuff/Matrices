def wheres(mat,conds,feats,inplace,lvl=1):

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
        #Use same level for all names
        if isinstance(lvl,int):
            for f in list(set(feats.get_level(lvl))):
                if f in conds:
                    conds = conds.replace(f,f"mat.level[{lvl}].name['{f}']")

        #Use different levels for each name 
        elif isinstance(lvl,dict):
            for name,level in lvl.items():
                if name in conds:
                    conds = conds.replace(name,f"mat.level[{level}].name['{name}']")

        #Apply the conditions and find out where it is True
        bool_matrix = eval(conds)
        mm = mat.matrix

        allinds = bool_matrix.find(mat.DEFAULT_BOOL[True],0)
        if allinds == None:
            raise ValueError("No data found")
        
        inds = [ind for ind,i in enumerate(bool_matrix.matrix) if all(i)]
        filtered = [mm[i][:] for i in inds]

        return (filtered,inds)
    else:
        mat._Matrix__use_value_based_comparison=True
        pass
        del mat._Matrix__use_value_based_comparison
        
