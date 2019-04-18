def QR(mat):
        """
        Decompose the matrix into Q and R where Q is a orthogonal matrix and R is a upper triangular matrix
        """
        if mat._cMat:
            return (None,None)
        
        if mat.isSquare:
            if mat.isSingular:
                return (None,None)
         
        if mat.dim[0]>mat.dim[1]:
            return (None,None)
        
        def _projection(vec1,vec2):
            """
            Projection vector of vec2 over vec1
            """
            return [(sum([vec1[a]*vec2[a] for a in range(len(vec1))])/sum([a*a for a in vec1]))*c for c in vec1]

        #Gram-Schmitt to get orthogonal set of the matrix
        U=[mat.col(1,0)]
        
        for b in range(2,min(mat.dim)+1):
            u=mat.col(b,0)
            
            for i in range(1,b):
                #Projection vector
                p=_projection(U[i-1],mat.col(b,0))
                #Keep subtracting the other vectors' projections from itmat
                u=[u[i]-p[i] for i in range(len(u))]
                
            U.append(u.copy())
        
        matU = mat.floatForm
        matU.setMatrix(min(mat.dim),None,U)
        matU = matU.t
        #Orthonormalize by diving the columns by their norms
        Q = matU/[sum([a*a for a in U[i]])**(1/2) for i in range(len(U))]
        #Get the upper-triangular part
        R = (Q.t@mat).roundForm(8)
        return (Q,R)