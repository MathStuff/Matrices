def find(mat,dims,element,start,rowind):
    assert isinstance(start,int), "Starting index have to be an integer"
    
    indices=[]
    d0,d1 = dims

    for i in range(d0):
        mm = mat[i]
        for j in range(d1):
            if mm[j] == element:
                indices.append((i+start,j+start))

    if len(indices):
        if rowind:
            return list(set([i[0] for i in indices]))
        return indices
