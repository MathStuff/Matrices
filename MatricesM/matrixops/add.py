def add(mat,lis,row,col,feature,dtype,index,fill):
    nullobj = mat.DEFAULT_NULL

    r,c = 0,0
    d0,d1 = mat.dim
    assert isinstance(lis,(list,tuple)) , "'lis' parameter only accepts tuples or lists"
    length = len(lis)

    if (row==None) ^ (col==None):
        #Insert a row
        if col==None:
            #Empty matrix
            if [d0,d1] == [0,0]:
                inds = index if isinstance(index,(Label,list)) else [index]
                mat.__init__([1,length],lis,dtype=mat.dtype,index=inds)
                return mat

            r+=1
            if fill:
                #Given list is shorter
                for rest in range(0,d1-length):
                    lis.append(nullobj)
                length = len(lis)

                #Given list is longer
                for rest in range(0,length-d1):
                    mat.add([nullobj for _ in range(d0)],col=d1+rest+1)
                    d1 += 1

            if length!=d1:
                raise ValueError(f"Given list's length doesn't match the dimensions; expected {d1} elements, got {length} instead")

            if row>0 and isinstance(row,int):
                mat._matrix.insert(row-1,list(lis))
                if mat._dfMat:
                    mat.index.insert(row-1,index)
            else:
                raise ValueError(f"'row' should be an integer higher than 0")

        #Insert a column
        elif row==None:
            #Empty matrix
            if [d0,d1] == [0,0]:
                feat = [feature] if isinstance(feature,str) else []
                mat.__init__([length,1],lis,dtype=mat.dtype,coldtypes=[dtype],features=feat)
                return mat
            
            c+=1   
            if fill:
                #Given list is shorter
                for rest in range(0,d0-length):
                    lis.append(nullobj)
                length = len(lis)

                #Given list is longer
                for rest in range(0,length-d0):
                    mat.add([nullobj for _ in range(d1)],row=d0+rest+1)
                    d0 += 1
                
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
                from MatricesM.setup.declare import declareColdtypes
                dtype=declareColdtypes([[row] for row in lis],mat.DEFAULT_NULL.__name__)[0]

            if feature == None:
                feature = f"col_{col + 1}"
            #Prevent repetation of the column names
            while feature in mat.features.get_level(1):
                feature = "_"+feature

            #Store column name and dtype
            mat.features.insert(col,feature)
            mat.coldtypes.insert(col,dtype)
            
    else:
        raise TypeError("Either one of 'row' and 'col' parameters should have a value passed")

    mat._Matrix__dim = [d0+r,d1+c]
