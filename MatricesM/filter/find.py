def find(mat,dims,element,start=1):
    class empty:
        def __init__(self):
            self.empty=True
        
    indeces=[]
    try:
        assert start==0 or start==1
        assert isinstance(element,int) or isinstance(element,float) or isinstance(element,complex) or isinstance(element,str)
        for row in range(dims[0]):
            while element in mat[row]:
                n=mat[row].index(element)
                indeces.append((row+start,n+start))
                mat[row][n]=empty
    except AssertionError:
        print("Invalid arguments")
    else:
        if len(indeces):
            return indeces
        return None
