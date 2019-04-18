def transpose(mat,hermitian=False):
    try:
        if mat._isIdentity:
            return mat
        
        temp=mat.matrix
        d0,d1=mat.dim[0],mat.dim[1]
        if hermitian:
            transposed=[[temp[cols][rows].conjugate() for cols in range(d0)] for rows in range(d1)]
        else:
            transposed=[[temp[cols][rows] for cols in range(d0)] for rows in range(d1)]
        
    except Exception as err:
        print(err)
    else:
        t = mat.copy
        t.setMatrix((d1,d0),None,transposed)
        return t
