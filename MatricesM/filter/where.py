def wheres(mat,conds,feats,inplace):
    if inplace:
        #Replace comparison operators with proper symbols
        if " and " in conds:
            conds = conds.replace(" and ","&")
        if " or " in conds:
            conds = conds.replace(" or ","|")

        #Replace feature names with column matrices
        for f in feats:
            if f in conds:
                conds = conds.replace(f,f"mat.col({feats.index(f)+1})")

        #Apply the conditions and find out where it is True
        allinds = eval(conds).find(1,0)
        if allinds == None:
            raise ValueError("No data found")
            
        inds = [i[0] for i in eval(conds).find(1,0)]
        filtered = [mat.matrix[i][:] for i in inds]
        return (filtered,inds)
    else:
        pass
