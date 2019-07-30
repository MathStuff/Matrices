def add(mat,lis,row,col,feature,dtype,index,fill):
    from MatricesM.customs.objects import null

    r,c = 0,0
    d0,d1 = mat.dim
    assert isinstance(lis,(list,tuple)) , "'lis' parameter only accepts tuples or lists"
    length = len(lis)

    if (row==None) ^ (col==None):
        #Insert a row
        if col==None:
            r+=1
            if fill:
                for rest in range(d1-length):
                    lis.append(null)
                length = len(lis)

            if length!=d1:
                raise ValueError(f"Given list's length doesn't match the dimensions; expected {d1} elements, got {length} instead")

            if row>0 and isinstance(row,int):
                mat._matrix.insert(row-1,list(lis))
                if mat._dfMat:
                    mat._Matrix__index.insert(row-1,index)
            else:
                raise ValueError(f"'row' should be an integer higher than 0")

        #Insert a column
        elif row==None:
            c+=1
            if fill:
                for rest in range(d0-length):
                    lis.append(null)
                length = len(lis)
                
            if length!=d0:
                raise ValueError(f"Given list's length doesn't match the dimensions; expected {d0} elements, got {length} instead")

            if col>0 and isinstance(col,int):
                col -= 1
                for i in range(mat.d0):
                    mat._matrix[i].insert(col,lis[i])
            else:
                raise ValueError(f"'col' should be an integer higher than 0")

            #Pick first elements type as column dtype as default
            if dtype==None:
                dtype=type(lis[0])

            if feature == None:
                feature = f"col_{col + 1}"
            #Prevent repetation of the column names
            if feature in mat.features:
                feature = "_"+feature

            #Store column name and dtype
            mat.features.insert(col,feature)
            mat.coldtypes.insert(col,dtype)
            
    else:
        raise TypeError("Either one of 'row' and 'col' parameters should have a value passed")

    mat._Matrix__dim = [d0+r,d1+c]
