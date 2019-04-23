def LU(mat,z,copy,obj):
    """
    Returns L and U matrices of the matrix
    ***KNOWN ISSUE:Doesn't always work if determinant is 0 | linear system is inconsistant***
    ***STILL NEEDS CLEAN UP***
    """
    if not mat.isSquare:
        return (None,None,None)
    temp = copy
    rowC = 0
    prod = 1
    dia = []
    i = 0
    L = z
    
    while i <min(mat.dim):
        #Swap lines if diagonal has 0, stop when you find a non zero in the column
        if temp[i][i]==0:
            try:
                i2=i
                old=temp[i][:]
                while temp[i2][i]==0 and i2<min(mat.dim):
                    rowC+=1
                    i2+=1
                temp[i]=temp[i2][:]
                temp[i2]=old[:]
            except:
                #print("Determinant is 0, can't get lower/upper triangular matrices")
                return [None,0,None]
            
        #Loop through the ith column find the coefficients to multiply the diagonal element with
        #to make the elements under [i][i] all zeros
        if mat._cMat:
            rowMulti=[complex(round((temp[j][i]/temp[i][i]).real,8),round((temp[j][i]/temp[i][i]).real,8)) for j in range(i+1,mat.dim[0])]
        else:
            rowMulti=[round(temp[j][i]/temp[i][i],8) for j in range(i+1,mat.dim[0])]
        #Loop to substitute ith row times the coefficient found from the i+n th row (n>0 & n<rows)
        k0=0
        for k in range(i+1,mat.dim[0]):

            temp[k]=[temp[k][m]-(rowMulti[k0]*temp[i][m]) for m in range(mat.dim[1])]
            #Lower triangular matrix
            L.matrix[k][i]=rowMulti[k0]
            k0+=1   
        #Get the diagonal for determinant calculation
        dia.append(temp[i][i])
        i+=1

    for element in dia:
        prod*=element
            
    return (obj(mat.dim,temp,dtype=mat.dtype),((-1)**(rowC))*prod,L)