def concat(mat,matrix,axis):
    try:
        if axis==0:
            assert matrix.dim[1]==mat.dim[1]
        elif axis==1:
            assert matrix.dim[0]==mat.dim[0]
        if matrix.dtype==complex and mat.dtype!=complex:
            raise TypeError

    except AssertionError:
        raise AssertionError("Dimensions don't match for concatenation")
    except TypeError:
        raise TypeError("Can't concatenate complex valued matrix to real valued matrix")
    else:
        if axis==0:
            for rows in range(matrix.dim[0]):
                mat._matrix.append(matrix.matrix[rows])

        elif axis==1:
            for rows in range(matrix.dim[0]):
                mat._matrix[rows]+=matrix.matrix[rows]
        else:
            return None    

        mat._Matrix__dim=mat._declareDim()
        if axis==1:
            mat._Matrix__features = mat.features + [i if i not in mat.features else "_"+i for i in matrix.features]
            mat._Matrix__coldtypes = mat.coldtypes + [i for i in matrix.coldtypes]
        else:
            if mat._dfMat:
                mat._Matrix__index = mat.index + [ind for ind in matrix.index]
