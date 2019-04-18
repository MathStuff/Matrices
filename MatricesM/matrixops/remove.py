def remove(mat,r=None,c=None):
    """
    Deletes the given row or column
    Changes the matrix
    Give only 1 parameter, r for row, c for column. (Starts from 1)
    If no parameter name given, takes it as row
    """
    try:
        assert (r==None or c==None) and (r!=None or c!=None) 
        if c==None:
            del mat._matrix[r-1]
            r=1
            c=0
        elif r==None:
            for rows in range(mat.dim[0]):
                del mat._matrix[rows][c-1]
            r=0
            c=1
    except:
        print("Bad arguments")
    else:           
        if c!=None and len(mat.features)>0:
            del(mat.features[c-1])        
        mat._Matrix__dim=[mat.dim[0]-r,mat.dim[1]-c]