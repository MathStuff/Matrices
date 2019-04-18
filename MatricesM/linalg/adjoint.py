def adjoint(mat):
    if not mat.isSquare:
        return None
    else:
        adjL=[[mat.minor(rows+1,cols+1).det*((-1)**(rows+cols)) for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        adjM = mat.floatForm
        adjM._matrix = adjL
        
        mat._adj=adjM.t
        mat._Matrix__adjCalc=1
        
        return mat._adj