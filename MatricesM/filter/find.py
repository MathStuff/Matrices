def find(mat,dims,element,start=1):
    """
    element: Real number
    start: 0 or 1. Index to start from 
    Returns the indeces of the given elements, multiple occurances are returned in a list
    """
    indeces=[]
    try:
        assert start==0 or start==1
        assert isinstance(element,int) or isinstance(element,float) or isinstance(element,complex) or isinstance(element,str)
        for row in range(dims[0]):
            while element in mat[row]:
                n=mat[row].index(element)
                indeces.append((row+start,n+start))
                mat[row][n]=""
    except AssertionError:
        print("Invalid arguments")
    else:
        if len(indeces):
            return indeces
        return None
