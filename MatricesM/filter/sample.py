def samples(mat,size,conds,obj):
    from random import sample
    from MatricesM.customs.objects import Label

    if size > mat.d0:
        raise ValueError("Sample size is too big")

    filtered = mat.where(conds) if conds != None else mat  

    i = filtered.index.labels
    mm = filtered.matrix
    sample_inds = sample(list(range(filtered.d0)),size)

    indices = Label([i[row] for row in sample_inds],mat.index.names) if mat._dfMat else Label()
    return obj(data=[mm[row][:] for row in sample_inds],decimal=mat.decimal,
               dtype=mat.dtype,features=mat.features[:],coldtypes=mat.coldtypes[:],
               index=indices)