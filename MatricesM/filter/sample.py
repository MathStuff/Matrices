def samples(mat,size,conds,obj):
    from random import sample

    if size > mat.d0:
        raise ValueError("Sample size is too big")

    filtered = mat.where(conds) if conds != None else mat  

    i = filtered.index
    mm = filtered.matrix
    sample_inds = sample(list(range(filtered.d0)),size)

    indices = [i[row] for row in sample_inds] if mat._dfMat else []
    return obj(listed=[mm[row][:] for row in sample_inds],decimal=mat.decimal,
               dtype=mat.dtype,features=mat.features[:],coldtypes=mat.coldtypes[:],
               index=indices,indexname=mat.indexname)