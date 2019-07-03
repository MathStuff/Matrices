def add(mat,lis=[],row=None,col=None,feature="Col",dtype=None):

    r,c = 0,0
    assert isinstance(lis,(list,tuple)) , "'lis' parameter only accepts tuples or lists"
    length = len(lis)

    if (row==None) ^ (col==None):
        #Insert a row
        if col==None:
            r+=1
            if length!=mat.dim[1]:
                raise ValueError(f"Given list's length doesn't match the dimensions; expected {mat.dim[1]} elements, got {length} instead")

            if row>0 and isinstance(row,int):
                mat._matrix.insert(row-1,list(lis))

            else:
                raise ValueError(f"'row' should be an integer higher than 0")

        #Insert a column
        elif row==None:
            c+=1
            if length!=mat.dim[0]:
                raise ValueError(f"Given list's length doesn't match the dimensions; expected {mat.dim[0]} elements, got {length} instead")

            if col>0 and isinstance(col,int):
                col -= 1
                for i in range(mat.d0):
                    mat._matrix[i].insert(col,lis[i])
            else:
                raise ValueError(f"'col' should be an integer higher than 0")

            #Pick first elements type as column dtype as default
            if dtype==None:
                dtype=type(lis[0])

            #Prevent repetation of the column names
            if feature in mat.features:
                feature = "_"+feature

            #Store column name and dtype
            mat.features.insert(col,feature)
            mat.coldtypes.insert(col,dtype)
            
    else:
        raise TypeError("Either one of 'row' and 'col' parameters should have a value passed")

    mat._Matrix__dim = [mat.dim[0]+r,mat.dim[1]+c]
