def QR(mat,obj):
    if mat.isSquare:
        if mat.isSingular:
            return (None,None)
    
    def dotprodsum(vec1,vec2):
        """
        Sum of the coordinates from a dot product of two vectors of same size
        """
        total = 0
        for i,val in enumerate(vec1):
            total += vec2[i]*val
        return total

    def normsq(vec):
        """
        Norm of a vector squared
        """
        total = 0
        for val in vec:
            total += val*val
        return total

    def _projection(vec1,vec2):
        """
        Projection vector of vec2 over vec1
        """
        
        val = dotprodsum(vec1,vec2)/normsq(vec1)
        return [i*val for i in vec1]

    #Gram-Schmitt to get orthogonal set of the matrix
    U=[]
    mm = mat.matrix
    d0,d1 = mat.dim
    min_dim = min(d0,d1)

    for b in range(min_dim):
        u=[row[b] for row in mm]
        copy = u[:]

        for i in range(b):
            #Projection vector
            p=_projection(U[i],copy)
            #Keep subtracting the other vectors' projections from it
            u=[u[j]-p[j] for j in range(d0)]
            
        U.append(u.copy())
        
    if mat._cMat:
        dt = complex
    else:
        dt = float

    matU = obj((min_dim,d0),U,dtype=dt,implicit=True).t
    #Norms
    norms = [normsq(U[i])**(0.5) for i in range(min_dim)]

    #Orthonormalize by diving the columns by their norms
    Q = matU/norms
    #Get the upper-triangular part
    R = Q.t@mat

    return (Q,R)