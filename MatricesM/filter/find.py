def find(mat,dims,element,start,rowind):
    class empty:
        pass
        
    indices=[]
    try:
        assert start==0 or start==1
        assert isinstance(element,int) or isinstance(element,float) or isinstance(element,complex) or isinstance(element,str)
        for row in range(dims[0]):
            while element in mat[row]:
                n=mat[row].index(element)
                indices.append((row+start,n+start))
                mat[row][n]=empty
    except AssertionError:
        print("Invalid arguments")
    else:
        if len(indices):
            if rowind:
                return list(set([i[0] for i in indices]))
            return indices
        return None
