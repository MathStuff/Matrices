
def _eigenvals(mat,roundto):
    """
    Returns the eigenvalues using QR algorithm
    """

    assert mat.isSquare and mat.d0>=2, "Can't find eigenvalues for non-square matrices"
    if mat.d0==2:
        d=mat.det
        tr=mat.matrix[0][0]+mat.matrix[1][1]
        return list(set([(tr+(tr**2 - 4*d)**(1/2))/2,(tr-(tr**2 - 4*d)**(1/2))/2]))

    eigens = []
    q=mat.Q
    a1=q.t@mat@q
    for i in range(mat.QR_ITERS):#Iterations start
        qq=a1.Q
        a1=qq.t@a1@qq
    #Determine which values are real and which are complex eigenvalues
    if mat.isSymmetric:#Symmetrical matrices always have real eigenvalues
        return a1.diags

    #Wheter or not dimensions are odd
    isOdd=(a1.d0%2)
    precision = mat.PRECISION
    #Decide wheter or not to skip the bottom right 2x2 matrix
    if a1._cMat: 
        neighbor = a1[-1,-2]
        if round(neighbor.real,precision)==0 and round(neighbor.imag,precision):
            eigens.append(a1[-1,-1])
    else:
        if round(a1[-1,-2],precision)==0:
            eigens.append(a1[-1,-1])

    #Create rest of the eigenvalues from 2x2 matrices
    ind=0
    while ind<a1.d0-1:
        mat = a1[ind:ind+2,ind:ind+2]
        ind+=1+isOdd

        #Decide wheter or not to skip the top right corner 2x2 matrix
        done=0
        if a1._cMat:
            if round(mat[1,0].real,precision)==0 and round(mat[1,0].imag,precision):
                eigens.append(mat[0,0])
                ind-=isOdd
                done=1

        elif round(mat[1,0],precision)==0:
            eigens.append(mat[0,0])
            ind-=isOdd
            done=1

        #2x2 matrices in the middle
        if not done:
            ind+=1-isOdd
            r = mat.trace/2
            v = (mat.det - r**2)**(1/2)
            
            r = complex(complex(roundto(r.real,precision,True)),complex(roundto(r.imag,precision,True)))
            v = complex(complex(roundto(v.real,precision,True)),complex(roundto(v.imag,precision,True)))               
            
            c1 = complex(r,v)
            c2 = complex(r,v*(-1))
            
            if c1.imag==0:
                c1 = c1.real
            if c2.imag==0:
                c2 = c2.real
            
            eigens.append(c1)
            eigens.append(c2)

    return eigens

def _eigenvecs(mat,iters,alpha,ident,obj):
    """
    Returns the eigenvectors, eigenvector matrix and diagonal matrix
    """
    eigens = mat.eigenvalues or mat.diags
    if eigens in [None,[]]:
        return None
    
    d0,d1 = mat.dim[:]
    ones = obj(dim=(mat.d0,1),fill=1)
    vectors = []
    
    for eig in eigens:
        i = 0
        c = None
        x = ones.copy
        eigen = eig*alpha
        identity = ident(d0)*(eigen)
        
        while i<iters:
            try:
                y = ((mat - identity).inv)@x
            except:#Guess converged
                break
            else:
                c = (y.t@x).matrix[0][0]/(x.t@x).matrix[0][0]
                if c == 0:
                    c = None

                m = (y**2).sum("col_1",get=0)**(0.5)
                if m == 0:
                    break

                x = y/m
                i += 1

        guess = (1/c)+eig if c != None else eig
        vectors.append((f"{i} iters for {eig}",guess,x))

    ########################################################
    eigenmat = vectors[0][2].copy
    dtype_changed = False

    for i in range(1,len(vectors)):
        colvec = vectors[i][2]

        if colvec.dtype == complex and not dtype_changed:
            eigenmat.dtype = complex
            dtype_changed == True

        eigenmat.concat(colvec,axis=1)

    ########################################################
    diagmat = obj(dim=len(vectors),fill=0,dtype=float)
    dtype_changed = False

    for i in range(len(vectors)):
        eigvalue = vectors[i][1]
        if isinstance(eigvalue,complex) and not dtype_changed:
            diagmat.dtype = complex
            dtype_changed = True

        diagmat._matrix[i][i] = eigvalue

    ########################################################

    return (vectors,eigenmat,diagmat)