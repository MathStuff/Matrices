def joins(mat,table,conds,method,obj):
    methods = ["inner","left","left-ex","right","right-ex","full","full-ex"]

    if not method in methods:
        raise ValueError(f"{method} is not a join method. Available methods:\n\t{", ".join(methods)}")
    if not isinstance(table,obj):
        raise TypeError(f"Can't use type {type(table).__name__} as a Matrix")

    temp_mat,temp_ind = [],[]
    mm = mat.where(conds).matrix
    other_mm = other.where(conds).matrix
    inds = mat.index

    if method == "inner":
        for i,row in enumerate(mm):
            if row in other_mm:
                temp_mat.append(row[:])
                temp_ind.append(inds[i])

    elif method == "left":
        for i,row in enumerate(other_mm):
            if row in other_mm:
                temp_mat.append(row[:])
                temp_ind.append(inds[i])
    