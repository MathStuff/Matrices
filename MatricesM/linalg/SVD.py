def _SVD(mat):
    """
    Singular value decomposition, Matrix = U@E@V.ht
    """
    transposed = mat.t
    
    #mat.t@mat@V = V@E**2 --> solve eigenvalue problem
    left_hand_side = transposed@mat
    E_and_V = left_hand_side.EIGENDEC
    E = E_and_V[1]**(0.5) #square root of diagonal matrix
    V = E_and_V[0].ht #hermitian transpose of the eigenvector matrix
    
    #mat@mat.t@U = U@E**2 --> solve eigenvalue problem
    left_hand_side = mat@transposed
    U = left_hand_side.eigenvecmat

    for diagonal in E.diags:
        if isinstance(diagonal,complex):
            E.dtype = complex
            break

    return (U,E,V)