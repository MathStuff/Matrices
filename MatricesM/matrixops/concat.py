def concat(mat,matrix,concat_as="row"):
    """
    Concatenate matrices row or columns vice
    matrix:matrix to concatenate to self
    concat_as:"row" to concat b matrix as rows, "col" to add b matrix as columns
    Note: This method concatenates the matrix to self
    """
    try:
        if concat_as=="row":
            assert matrix.dim[1]==mat.dim[1]
        elif concat_as=="col":
            assert matrix.dim[0]==mat.dim[0]
        if matrix.dtype==complex and mat.dtype!=complex:
            raise TypeError

    except AssertionError:
        raise AssertionError("Dimensions don't match for concatenation")
    except TypeError:
        raise TypeError("Can't concatenate complex valued matrix to real valued matrix")
    else:
        if concat_as=="row":
            for rows in range(matrix.dim[0]):
                mat._matrix.append(matrix.matrix[rows])

        elif concat_as=="col":
            for rows in range(matrix.dim[0]):
                mat._matrix[rows]+=matrix.matrix[rows]
        else:
            return None    

        mat._Matrix__dim=mat._declareDim()
        if concat_as=="col":
            mat._Matrix__features = mat.features + [i if i not in mat.features else "_"+i for i in matrix.features]
            mat._Matrix__coldtypes = mat.coldtypes + [i for i in matrix.coldtypes]
