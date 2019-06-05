def betterslice(oldslice,dim0):
    s,e,t = 0,dim0,1
    vs,ve,vt = oldslice.start,oldslice.stop,oldslice.step
    if vs!=None:
        if vs>0 and vs<dim0:
            s = vs
    if ve!=None:
        if ve>0 and ve<dim0:
            if ve<=vs:
                e = vs
            else:
                e = ve
    if vt!=None:
        if abs(vt)<=dim0:
            t = vt
        else:
            t = dim0
    return slice(s,e,t)

def getitem(mat,pos,obj):
    #Get 1 row
    if isinstance(pos,int):
        return obj(listed=[mat._matrix[pos]],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:])
    #Get multiple rows
    elif isinstance(pos,slice):
        return obj(listed=mat._matrix[pos],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:])
    #Get 1 column
    elif isinstance(pos,str):
        if pos not in mat.features:
            raise ValueError(f"{pos} is not in column names")
        return mat.col(mat.features.index(pos)+1)

    #Get certain parts of the matrix
    elif isinstance(pos,tuple):
        #Column names given
        if all([1 if isinstance(i,str) else 0 for i in pos]):
            colinds = [mat.features.index(i) for i in pos]
            temp = obj((mat.dim[0],len(pos)),fill=0,features=list(pos),decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[i] for i in colinds])
            for row in range(mat.dim[0]):
                c = 0
                for col in colinds:
                    temp._matrix[row][c] = mat._matrix[row][col]
                    c+=1
            return temp
        
        #Tuple given    
        if len(pos)==2:
            # (row_index,column_name)
            if isinstance(pos[1],str):
                pos = list(pos)
                pos[1] = mat.features.index(pos[1])
            # (row_index,tuple_of_column_names)
            elif isinstance(pos[1],tuple):
                if all([1 if isinstance(i,str) else 0 for i in pos[1]]):
                    colinds = [mat.features.index(i) for i in pos[1]]

                    if isinstance(pos[0],slice):
                        newslice = betterslice(pos[0],mat.dim[0])
                        rowrange = range(newslice.start,min(newslice.stop,mat.dim[0]),newslice.step)
                    if isinstance(pos[0],int):
                        rowrange = [pos[0]]
                    if isinstance(pos[0],obj):
                        rowrange = [i[0] for i in pos[0].find(1,0)]

                    temp = obj((len(rowrange),len(pos[1])),fill=0,features=list(pos[1]),decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[i] for i in colinds])
                    r = 0
                    for row in rowrange:
                        c = 0
                        for col in colinds:
                            temp._matrix[r][c] = mat._matrix[row][col]
                            c+=1
                        r+=1
                    return temp
                else:
                    raise ValueError(f"{pos[1]} has non-string values")
            
            t = mat.coldtypes[pos[1]]
            if type(t) != list:
                t = [t]
            # mat[ slice, slice ] 
            if isinstance(pos[0],slice) and isinstance(pos[1],slice):
                return obj(listed=[i[pos[1]] for i in mat._matrix[pos[0]]],features=mat.features[pos[1]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t)
            # mat[ slice, int ] 
            elif isinstance(pos[0],slice) and isinstance(pos[1],int):
                return obj(listed=[[i[pos[1]]] for i in mat._matrix[pos[0]]],features=[mat.features[pos[1]]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t)
            # mat[ int, slice ]
            elif isinstance(pos[0],int) and isinstance(pos[1],slice):
                return obj(listed=[mat._matrix[pos[0]][pos[1]]],features=mat.features[pos[1]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t)
            # mat[ int, int]
            elif isinstance(pos[0],int) and isinstance(pos[1],int):
                return mat._matrix[pos[0]][pos[1]]
            elif isinstance(pos[0],obj):
                temp = []
                if isinstance(pos[1],int):
                    pos[1] = slice(pos[1],pos[1]+1)

                for i in range(mat.dim[0]):
                    if pos[0]._matrix[i][0]==1:
                        temp.append(mat._matrix[i][pos[1]])

                return obj(listed=temp,features=mat.features[pos[1]],dtype=mat.dtype,decimal=mat.decimal,coldtypes=mat.coldtypes[pos[1]])
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #0-1 filled matrix given as indeces
    elif isinstance(pos,obj):
        temp = [mat._matrix[i] for i in range(mat.dim[0]) if pos._matrix[i][0]==1]
        return obj(listed=temp,features=mat.features,dtype=mat.dtype,decimal=mat.decimal,coldtypes=mat.coldtypes)

def setitem(mat,pos,item,obj):
    #Change rows
    #Lists should be given as [[1,2,...],[3,4,...],...]
    if isinstance(pos,slice):
        try:
            if isinstance(item,obj):
                item = item.matrix

            elif isinstance(item,list):
                for i in item:
                    if type(i)!=list:
                        raise TypeError(f"Given list contains non-list element: {i}")

            elif isinstance(item,(int,float,complex,str,type,tuple)):
                #Fix slice
                pos = betterslice(pos,mat.dim[0])
                #Fill a list filled with the desired value
                item = [[item for i in range(mat.dim[1])] for j in range(s,min(mat.dim[0],e),t)]

            mat._matrix[pos] = item 
        except:
            raise ValueError(f"Dimensions of the given list/obj can't work with {pos}")

    #Change a row
    #Lists should be given as [1,2,...]
    elif isinstance(pos,int):
        if pos not in range(mat.dim[0]):
            raise IndexError(f"{pos} index is out of range")

        if isinstance(item,obj):
            if item.dim[0] != 1:
                raise ValueError("Given matrix should have 1 row")
            item = item.matrix[0]

        elif isinstance(item,list):
            if len(item)!=mat.dim[1]: 
                raise AssertionError(f"Expected length of the list to be :{mat.dim[1]}, but got {len(item)}")
        
        #If given 'item' is not in a list or a matrix
        elif isinstance(item,(int,float,complex,str,type,tuple)):
            item = [item for j in range(mat.dim[1])]

        mat._matrix[pos] = item

    #Change a column
    elif isinstance(pos,str):
        if not pos in mat.features:
            raise ValueError(f"{pos} is not a column name")
        
        if isinstance(item,obj):
            if item.dim[1] == 1  ^ item.dim[0] == 1:
                raise ValueError("Given matrix should have 1 column or row")
            if item.dim[0] == 1:
                item = item.matrix[0]
            else:
                item = item.col(1,0)

        elif isinstance(item,list):
            if len(item)!=mat.dim[0]: 
                raise AssertionError(f"Expected length of the list to be :{mat.dim[0]}, but got {len(item)}")
        
        #If given 'item' is not in a list or a matrix
        elif isinstance(item,(int,float,complex,str,type,tuple)):
            item = [item for j in range(mat.dim[0])]

        ind = mat.features.index(pos)
        for i in range(mat.dim[0]):
            mat._matrix[i][ind] = item[i]

    #Change certain parts of the matrix
    elif isinstance(pos,tuple):
        #Change given columns
        if all([1 if isinstance(i,str) else 0 for i in pos]):
            if isinstance(item,list):
                for i in item:
                    if type(i)!=list:
                        raise TypeError(f"Given list contains non-list element: {i}")
                    elif len(i)!=mat.dim[0]:
                        raise IndexError(f"Expected {mat.dim[0]}x{len(pos)} dimensions, but got at least one {len(i)} length list")

            elif isinstance(item,obj):
                if item.dim[0] != mat.dim[0] or item.dim[1] != len(pos):
                    raise IndexError(f"Expected {mat.dim[0]}x{len(pos)} dimensions, but got {item.dim[0]}x{item.dim[1]}")
                item = item.matrix
            
            colrange = [mat.features.index(v) for v in pos]   
            
            #If given 'item' is not in a list or a matrix
            if isinstance(item,(int,float,complex,str,type,tuple)):
                item = [[item for i in range(len(colrange))] for j in range(mat.dim[0])]
            
            for r in range(mat.dim[0]):
                i = 0
                for c in colrange:
                    mat._matrix[r][c] = item[r][i]
                    i+=1
        #Tuple with row indices first, column indices/names second
        elif len(pos)==2:
            pos = list(pos)
            newpos = []
            ind = 0
            for p in pos:
                if type(p) == slice:
                    newpos.append(betterslice(p,mat.dim[0]))
                else:
                    newpos.append(p)
                ind += 1
            pos = newpos

            # (row_index,column_name)
            if isinstance(pos[1],str):
                pos[1] = mat.features.index(pos[1])

            # (row_index,tuple_of_column_names)
            elif isinstance(pos[1],tuple):
                #Assert second index contains column names
                if all([1 if isinstance(i,str) else 0 for i in pos[1]]):
                    if isinstance(item,list):
                        for i in item:
                            if type(i)!=list:
                                raise TypeError(f"Given list contains non-list element: {i}")
                    elif isinstance(item,obj):
                        item = item.matrix
                    #If given 'item' is not in a list or a matrix
                    elif isinstance(item,(int,float,complex,str,type,tuple)):
                        rowrange = range(1)
                        #Check row indices
                        if isinstance(pos[0],slice):
                            newslice = betterslice(pos[0],mat.dim[0])
                            rowrange = range(newslice.start,min(newslice.stop,mat.dim[0]),newslice.step)
                        
                        elif isinstance(pos[0],int):
                            rowrange = [pos[0]]
                        
                        elif isinstance(pos[0],obj):
                            rowrange = [i[0] for i in pos[0].find(1,0)]

                        else:
                            raise TypeError("Row indices should be either an integer, a slice or a boolean matrix")
                        
                        item = [[item for i in range(len(pos[1]))] for j in rowrange]
                else:
                    raise ValueError(f"{pos[1]} has non-string values")

                colinds = [mat.features.index(i) for i in pos[1]]
                r1=0
                for r in rowrange:
                    c1=0
                    for c in colinds:
                        mat._matrix[r][c] = item[r1][c1]
                        c1+=1
                    r1+=1
                return None

            #Get the list of items
            if isinstance(item,obj):
                item = item.matrix

            # mat[ slice, slice ]
            if isinstance(pos[0],slice) and isinstance(pos[1],slice):
                #Get indices
                rowrange = range(pos[0].start,min(pos[0].stop,mat.dim[0]),pos[0].step)
                colrange = range(pos[1].start,min(pos[1].stop,mat.dim[1]),pos[1].step)

                #If given 'item' is not in a list or a matrix
                if isinstance(item,(int,float,complex,str,type,tuple)):
                    item = [[item for i in colrange] for j in rowrange]

                row=0
                for r in rowrange:
                    col=0
                    for c in colrange:
                        mat._matrix[r][c] = item[row][col]
                        col+=1
                    row+=1
            # mat[ slice, int ] 
            elif isinstance(pos[0],slice) and isinstance(pos[1],int):
                #Get indices
                rowrange = range(pos[0].start,min(pos[0].stop,mat.dim[0]),pos[0].step)
                #If given 'item' is not in a list or a matrix
                if isinstance(item,(int,float,complex,str,type,tuple)):
                    item = [[item] for j in rowrange]

                row=0
                for r in rowrange:
                    mat._matrix[r][pos[1]] = item[row][0]
                    row+=1

            # mat[ int, slice ]
            elif isinstance(pos[0],int) and isinstance(pos[1],slice):
                #Get indices
                colrange = range(pos[1].start,min(pos[1].stop,mat.dim[1]),pos[1].step)
                #If given 'item' is not in a list or a matrix
                if isinstance(item,(int,float,complex,str,type,tuple)):
                    item = [[item for i in colrange]]

                col=0
                for c in colrange:
                    mat._matrix[pos[0]][c] = item[0][col]
                    col+=1

            # mat[ int, int]
            elif isinstance(pos[0],int) and isinstance(pos[1],int):
                mat._matrix[pos[0]][pos[1]] = item

            #0-1 filled matrix given as indeces
            elif isinstance(pos[0],obj):
                inds = [i[0] for i in pos[0].find(1,0)]
                #[bool_matrix,int]
                if isinstance(pos[1],int):
                    cols = [pos[1]]
                #[bool_matrix,tuple_of_column_names]
                elif isinstance(pos[1],tuple):
                    cols = [mat.features.index(i) for i in pos[1]]

                #Given item is list of lists   
                if isinstance(item,list):
                    for i in item:
                        if type(i)!=list:
                            raise TypeError(f"Given list contains non-list element: {i}")
                
                #Given item is a matrix
                elif isinstance(item,obj):
                    item = item.matrix

                #Given item should be repeated in a list
                elif isinstance(item,(int,float,complex,str,type,tuple)):
                    item = [[item for j in cols] for _ in range(len(inds))]
                r=0
                for row in inds:
                    c=0
                    for col in cols:
                        mat._matrix[row][col] = item[r][c]
                        c+=1
                    r+=1
            else:
                raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #0-1 filled matrix given as indeces
    elif isinstance(pos,obj):
        inds = [i[0] for i in pos.find(1,0)]
        if isinstance(item,list):
            for i in item:
                if type(i)!=list:
                    raise TypeError(f"Given list contains non-list element: {i}")

        elif isinstance(item,obj):
            item = item.matrix

        elif isinstance(item,(int,float,complex,str,type,tuple)):
            item = [item for j in range(mat.dim[1])]
        for row in inds:
            mat._matrix[row] = item
    else:
        raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")

    return mat

def delitem(mat,val,obj):
        #A string passed == delete a column
        if isinstance(val,str):
            #Assertion
            if not val in mat.features:
                raise ValueError(f"'{val}' isn't a column name")
            #Indices
            colind = mat.features.index(val)
            #Remove the desired column
            for i in range(mat.dim[0]):
                del mat.matrix[i][colind]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0],mat.dim[1]-1]
            del mat.features[colind]
            del mat.coldtypes[colind]

        #An integer passed == delete a row
        elif isinstance(val,int):
            #Assertion
            if not (val>=0 and val<mat.dim[0]):
                raise ValueError("Row index out of range")
            #Remove the desired row
            del mat.matrix[val]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0]-1,mat.dim[1]]

        #Slice object passed == delete 1 or more rows
        elif isinstance(val,slice):
            from math import ceil
            #Check how many rows will be deleted
            newslice = betterslice(val,mat.dim[0])
            s,e,t = newslice.start,newslice.stop,newslice.step
            #Remove rows
            mat._matrix = [mat._matrix[i] for i in range(mat.dim[0]) if not i in range(mat.dim[0])[val]]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0]-ceil((e-s)/t),mat.dim[1]]

        #Multiple arguments passed == delete 1 or more rows and columns
        elif isinstance(val,tuple):
            #Column names given == delete all rows of the given columns
            if all([1 if isinstance(i,str) else 0 for i in val]):
                #Indices
                colinds = [mat.features.index(i) for i in val if i in mat.features]
                #Remove columns
                for r in range(mat.dim[0]):
                    mat._matrix[r] = [mat._matrix[r][i] for i in range(mat.dim[1]) if not i in colinds]
                #Remove column names and dtypes        
                mat._Matrix__features = [mat.features[i] for i in range(mat.dim[1]) if not i in colinds]
                mat._Matrix__coldtypes = [mat.coldtypes[i] for i in range(mat.dim[1]) if not i in colinds]
                #Set new dimensions
                mat._Matrix__dim = [mat.dim[0],mat.dim[1]-len(colinds)]

            #Columns can't be deleted just for some rows
            else:
                if isinstance(val[0],slice):
                    if betterslice(val[0],mat.dim[0]) != slice(0,mat.dim[0],1):
                        raise TypeError("Rows or columns should be deleted entirely not at all. Use 'replace' method to change individual values in rows")
                    else:
                        if isinstance(val[1],slice):
                            cols = mat.features[val[1]]
                        for col in cols:
                            mat.__delitem__(col)
                else:
                    raise TypeError("Rows or columns should be deleted entirely not at all. Use 'replace' method to change individual values in rows")
                    
        #Boolean matrix given as indeces == remove 0 or more rows
        elif isinstance(val,obj):
            #Assertion
            if val.dim[0] != mat.dim[0]:
                raise ValueError("Dimensions don't match")
            #Remove rows and keep track of how many of them are deleted
            rowinds = [i[0] for i in val.find(1,0)]
            deleted = len(rowinds)
            mat._matrix = [mat._matrix[i] for i in range(mat.dim[0]) if i not in rowinds]
            #Set new dimensions
            mat._Matrix__dim = [mat.dim[0]-deleted,mat.dim[1]]