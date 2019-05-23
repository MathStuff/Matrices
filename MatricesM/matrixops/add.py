def add(mat,lis=[],row=None,col=None,feature="Col",dtype=None):
    """
    Add a row or a column of numbers
    lis: list of numbers desired to be added to the matrix
    row: natural number
    col: natural number 
    row>=1 and col>=1

    feature: new column's name
    dtype: type of data the new column will hold, doesn't work if a row is inserted

    To append a row, only give the list of numbers, no other arguments
    To append a column, you need to use col = self.dim[1]
    """
    try:
        if row==None or col==None:
            if row==None and col==None:
                """Append a row """
                if mat.dim[0]>0:
                    if mat.dim[1]>0:
                        assert len(lis)==mat.dim[1]
                mat._matrix.append(lis)
                
            elif col==None and row>0:
                """Insert a row"""
                if len(lis)!=mat.dim[1] and mat.dim[1]>0:
                    raise Exception()
                if row<=mat.dim[0]:
                    mat._matrix.insert(row-1,lis)

                elif row-1==mat.dim[0]:
                    mat._matrix.append(lis)
                else:
                    print("Bad arguments")
                    return None
            elif row==None and col>0:
                if len(lis)!=mat.dim[0] and mat.dim[0]>0:
                    raise Exception()
                if col<=mat.dim[1]:
                    """Insert a column"""
                    i=0
                    for rows in mat._matrix:
                        rows.insert(col-1,lis[i])
                        i+=1
                elif col-1==mat.dim[1]:
                    """Append a column"""
                    i=0
                    for rows in mat._matrix:
                        rows.append(lis[i])
                        i+=1
                else:
                    print("Bad arguments")
                    return None
            else:
                return None
        else:
            return None
    except Exception as err:
        print("Bad arguments in add method:\n\t",err)
        return None
    else:
        if col!=None and mat.features!=[]:
            if dtype==None:
                dtype=type(lis[0])
            mat.features.insert(col-1,feature)
            mat.coldtypes.insert(col-1,dtype)
        if row == None:
            row = 0
            col = 1
        if col == None:
            row = 1
            col = 0
        mat._Matrix__dim = [mat.dim[0]+row,mat.dim[1]+col]
