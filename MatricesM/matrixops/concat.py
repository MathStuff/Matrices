def concat(mat,matrix,concat_as="row"):
    """
    Concatenate matrices row or columns vice
    b:matrix to concatenate to self
    concat_as:"row" to concat b matrix as rows, "col" to add b matrix as columns
    Note: This method concatenates the matrix to self
    """
    try:
        if concat_as=="row":
            assert matrix.dim[1]==mat.dim[1]
        elif concat_as=="col":
            assert matrix.dim[0]==mat.dim[0]
        b=matrix.copy
    except AssertionError:
        print("Bad dimensions at concat")
    else:
        if concat_as=="row":
            for rows in b.matrix:
                mat._matrix.append(rows)

        else:
            i=0
            for rows in mat._matrix:
                for cols in range(b.dim[1]):
                    rows.append(b[i][cols])
                i+=1
                  
        mat._Matrix__dim=mat._declareDim()
        if concat_as=="col":
            mat.features = mat.features+matrix.features
