def nilpotency(mat,limit=50):
    """
    Value of k for (A@A@A@...@A) == 0 where the matrix is multipled by itself k times, k in (0,inf) interval
    limit : integer | upper bound to stop iterations
    """
    if not mat.isSquare or mat._cMat or mat.isPositive:
        return None
    
    from math import inf,nan
    
    lim = limit
    zeroM = mat.copy
    zeroM._matrix = [[0 for i in range(zeroM.dim[0])] for j in range(zeroM.dim[0]) ]
    temp = mat.copy
    
    for i in range(2,lim+2):
        temp = temp@temp
        
        if temp.roundForm(8).matrix == zeroM.matrix:
            return i
        
        lis = [temp.matrix[i][j] for i in range(temp.dim[0]) for j in range(temp.dim[1])]
        if (inf in lis) or (nan in lis):
            print("Some elements converged to inf")
            return None