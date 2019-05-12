def remove(mat,m,n,r=None,c=None):
    """
    Deletes the given row or column
    Changes the matrix
    r : row number (>=1) int
    c : column number (>=1) int
    """
    if r!=None:
        del mat._matrix[r-1]
        m-=1

    if c!=None:
        for rows in range(m):
            del mat._matrix[rows][c-1]
        del mat._Matrix__features[c-1]
        del mat._Matrix__coldtypes[c-1]
        n-=1
    mat._Matrix__dim=[m,n]
