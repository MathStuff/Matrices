def samples(mat,size,conds):
    if conds!=None:
        filtered=mat.where(conds).matrix
    else:
        filtered=mat._matrix

    if size>=len(filtered):
        raise ValueError("Sample size is bigger than the population")

    from random import sample
    return sample(filtered,size)