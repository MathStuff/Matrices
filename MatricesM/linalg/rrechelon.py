def rrechelon(mat):
    """
    Returns reduced row echelon form of the matrix
    """
    temp=mat.copy
    i=0
    zeros=[0]*mat.dim[1]
    if mat._cMat:
        zeros=[0j]*mat.dim[1]
    while i <min(mat.dim):
        #Find any zero-filled rows and make sure they are on the last row
        if zeros in temp.matrix:
            del(temp.matrix[temp.matrix.index(zeros)])
            temp.matrix.append(zeros)
            
        #Swap rows if diagonal is 0       
        if temp[i][i]==0:
            try:
                i2=i
                old=temp[i][:]
                while temp[i2][i]==0 and i2<mat.dim[0]:
                    i2+=1
                temp[i]=temp[i2][:]
                temp[i2]=old[:]
            except:
                break
            
        #Do the calculations to reduce rows
        temp[i]=[temp[i][j]/temp[i][i] for j in range(mat.dim[1])]
        if mat._cMat:
            temp._matrix=[[complex(round((temp[k][m]-temp[i][m]*temp[k][i]).real,12),round((temp[k][m]-temp[i][m]*temp[k][i]).imag,12)) for m in range(mat.dim[1])] if k!=i else temp[i] for k in range(mat.dim[0])]
        else:    
            temp._matrix=[[round(temp[k][m]-temp[i][m]*temp[k][i],12) for m in range(mat.dim[1])] if k!=i else temp[i] for k in range(mat.dim[0])]
        i+=1

    #Fix -0.0 issue
    if mat._cMat:
        boundary=1e-10
        for i in range(mat.dim[0]):
            for j in range(mat.dim[1]):
                num=temp[i][j]
                if isinstance(num,complex):
                    if num.real<boundary and num.real>-boundary:
                        num=complex(0,num.imag)
                    if num.imag<boundary and num.imag>-boundary:
                        num=complex(num.real,0)
                else:
                    if str(num)=="-0.0":
                        num=0
                
                temp[i][j]=num
    else:
        boundary=1e-10
        temp._matrix=[[temp[i][j] if not (temp[i][j]<boundary and temp[i][j]>-boundary) else 0 for j in range(temp.dim[1])] for i in range(temp.dim[0])]

    z = temp.matrix.count(zeros)
    r = mat.floatForm
    r._matrix = temp.matrix
    return (r,mat.dim[0]-z)
