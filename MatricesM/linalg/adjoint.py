def adjoint(mat):
    if not mat.isSquare:
        return None
    else:
        adjM=[[mat.minor(cols+1,rows+1)*((-1)**(rows+cols)) for cols in range(mat.dim[0])] for rows in range(mat.dim[0])]
        
        return adjM