def wheres(mat,conds,feats):
    if "and" in conds:
        conds = conds.replace("and","&")
    if "or" in conds:
        conds = conds.replace("or","|")

    for f in feats:
        if f in conds:
            conds = conds.replace(f,f"mat.col({feats.index(f)+1})")

    inds = [i[0] for i in eval(conds).find(1,0)]
    if inds == None:
        raise ValueError("No data found")
    filtered = [mat.matrix[i][:] for i in inds]
    return filtered

