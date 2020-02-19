def _SVD(mat):
    """
    Singular value decomposition, Matrix = U@E@V.ht
    """

    transposed = mat.t
    
    #mat.t@mat@V = V@E**2 --> solve eigenvalue problem
    left_hand_side = transposed@mat
    E_and_V = left_hand_side.EIGENDEC
    E = E_and_V[1]**(0.5) #square root of diagonal matrix
    V = E_and_V[0] #Right singular vectors
    
    #mat@mat.t@U = U@E**2 --> solve eigenvalue problem
    left_hand_side = mat@transposed
    U = left_hand_side.eigenvecmat

    for diagonal in E.diags:
        if isinstance(diagonal,complex):
            E.dtype = complex
            break
        
    d0,d1 = mat.dim
    n,x = min(d0,d1),max(d0,d1)
    #Add zero rows if needed
    zeros = mat(dim=(x-n,d1),data=None,fill=0,index=[],features=[])
    E.concat(zeros,axis=0)

    return (U,E,V)