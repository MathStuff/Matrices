def QR(mat,obj):
    from MatricesM.matrix import dataframe

    if mat.isSquare:
        if mat.isSingular:
            return (None,None)
    
    def _projection(vec1,vec2):
        """
        Projection vector of vec2 over vec1
        """
        return [(sum([vec1[a]*vec2[a] for a in range(len(vec1))])/sum([a*a for a in vec1]))*c for c in vec1]

    #Gram-Schmitt to get orthogonal set of the matrix
    U=[]
    
    for b in range(1,min(mat.dim)+1):
        u=mat.col(b,0)
        
        for i in range(1,b):
            #Projection vector
            p=_projection(U[i-1],mat.col(b,0))
            #Keep subtracting the other vectors' projections from itmat
            u=[u[i]-p[i] for i in range(len(u))]
            
        U.append(u.copy())
    if mat.dtype in [float,int,dataframe]:
        dt = float
    else:
        dt = complex
    matU = obj((len(U),len(U[0])),U,dtype=dt,implicit=True).t
    #Orthonormalize by diving the columns by their norms
    Q = matU/[sum([a*a for a in U[i]])**(1/2) for i in range(len(U))]
    #Get the upper-triangular part
    R = Q.t@mat

    return (Q,R)