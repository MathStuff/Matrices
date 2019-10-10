def betterslice(oldslice,dim):
    s,e,t = 0,dim,1
    vs,ve,vt = oldslice.start,oldslice.stop,oldslice.step
    if vs!=None:
        if vs>0 and vs<dim:
            s = vs
        elif vs<0 and abs(vs)-1<dim:
            return slice(vs,ve,t)
    if ve!=None:
        if ve>0 and ve<dim:
            if ve<=s:
                e = s
            else:
                e = ve
        elif ve<0 and abs(ve)-1<dim:
            e = dim+ve
    if vt!=None:
        if abs(vt)<=dim:
            t = vt
        else:
            t = dim
    return slice(s,e,t)

def getitem(mat,pos,obj,uselabel,returninds=False,rowlevel=1):
    from MatricesM.validations.validate import consistentlist,sublist,rangedlist
    from MatricesM.errors.errors import MatrixError
    from MatricesM.customs.objects import Label

    d0,d1 = mat.dim

    #Get 1 row
    if isinstance(pos,int):
        if uselabel:
            indices = mat.index
            indices_labels = indices.labels

            filtered_labels = indices.get_level(rowlevel)

            mm = mat.matrix
            rowinds = [i for i in range(d0) if filtered_labels[i]==pos]
            lastinds = Label([pos for i in rowinds],indices.names)
            if returninds:
                return (rowinds,None)
            return obj(data=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds)
        
        if returninds:
            return (pos,None)

        inds = mat.index
        lastinds = inds if inds in [[],None,Label()] else inds[pos]
        return obj(data=[mat._matrix[pos]],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds)

    #Get multiple rows
    elif isinstance(pos,slice):
        if uselabel:
            indices = mat.index
            indices_labels = indices.labels

            filtered_labels = indices.get_level(rowlevel)

            start = filtered_labels.index(pos.start) if pos.start != None else None
            end = filtered_labels.index(pos.stop) if pos.stop != None else None

            first_item = filtered_labels[start] if start != None else None
            last_item = filtered_labels[end] if end != None else None

            no_end = True if end == None else False

            start = start if start != None else 0
            end = end if end != None else d0

            first_found = False if first_item != None else True

            rowrange,mm = [],mat.matrix
            for i in range(start,end):
                try:
                    val = filtered_labels[i]

                    if val==last_item and no_end:
                        break
                    if not first_found:
                        first_found = bool(val==first_item)

                    if first_found:
                        rowrange.append(i)
                        
                except:
                    continue

            if returninds:
                return (rowrange,None)        
            lastinds = Label([indices_labels[i] for i in rowrange],indices.names)
            lastmatrix = [mm[i] for i in rowrange]

            return obj(data=lastmatrix,features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds)
        
        if returninds:
            return (range(d0)[pos],None)

        inds = mat.index
        lastinds = inds if inds in [[],None,Label()] else inds[pos]
        return obj(data=mat._matrix[pos],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds)
    
    #Get 1 column or use a specific row index
    elif isinstance(pos,str):
        if uselabel:
            indices = mat.index
            indices_labels = indices.labels

            filtered_labels = indices.get_level(rowlevel)

            mm = mat.matrix

            rowinds = [i for i in range(d0) if filtered_labels[i]==pos]
            lastinds = Label([indices_labels[i] for i in rowinds],indices.names)

            if returninds:
                return (rowinds,None)
            return obj(data=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                        dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds)                        

        if not (pos in mat.features):
            if returninds:
                return (None,range(d0))
            raise MatrixError(f"{pos} is not in column names")
        else:
            pos = mat.features.index(pos)

        if returninds:
            return (None,pos)

        inds = mat.index
        lastinds = inds[:]

        mat =  obj(dim=[d0,1],data=[[i[pos]] for i in mat._matrix],features=[mat.features[pos]],
                   decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[pos]],index=lastinds,
                   implicit=True)

        mat.NOTES = f"n:{d0},type:{mat.coldtypes[0].__name__},invalid:{d0-mat.count(get=0)}\n\n"
        return mat

    #Get rows from given indices
    elif isinstance(pos,list):
        if uselabel:
            indices = mat.index
            indices_labels = indices.labels

            filtered_labels = indices.get_level(rowlevel)

            #######Assertion
            #sublist(pos,indices,"list of indices","indices",throw=True)
            #######
            mm = mat.matrix
            
            rowinds = [i for i in range(d0) if filtered_labels[i] in pos]
            lastinds = Label([indices_labels[i] for i in rowinds],indices.names)

            if returninds:
                return rowinds
            return obj(data=[mm[i][:] for i in rowinds],
                       features=mat.features[:],
                       decimal=mat.decimal,
                       dtype=mat.dtype,
                       coldtypes=mat.coldtypes[:],
                       index=lastinds)

        #######Assertion
        consistentlist(pos,int,"indices",throw=True)
        rangedlist(pos,lambda a:(a<d0) and (a>=0),"indices",f"[0,{d0})",throw=True)
        #######
        if returninds:
            return (pos,None)
        mm = mat.matrix
        i = mat.index.labels
        inds = Label([i[index] for index in pos],mat.index.names) if mat._dfMat else Label()

        return obj(data=[mm[i][:] for i in pos],features=mat.features,coldtypes=mat.coldtypes,dtype=mat.dtype,decimal=mat.decimal,index=inds)

    #Get certain parts of the matrix
    elif isinstance(pos,tuple):
        pos = list(pos)
        #Column names or row indices given
        if consistentlist(pos,str):
            #Use as row labels
            if uselabel:
                indices = mat.index
                indices_labels = indices.labels

                filtered_labels = indices.get_level(rowlevel)
                
                rowinds = [i for i in range(d0) if filtered_labels[i] in pos]
                lastinds = Label([indices_labels[i] for i in rowinds],indices.names) if mat._dfMat else Label()
                
                if returninds:
                    return (rowinds,None)
                mm = mat.matrix
                return obj(data=[mm[i][:] for i in rowinds],
                           features=mat.features[:],
                           decimal=mat.decimal,
                           dtype=mat.dtype,
                           coldtypes=mat.coldtypes[:],
                           index=lastinds)

            #Use as column names
            colinds = [mat.features.index(i) for i in pos]
            if returninds:
                return (None,colinds)

            inds = mat.index
            lastinds = Label() if inds in [[],None,Label()] else inds[:]
            
            temp = obj((d0,len(pos)),
                        fill=0,
                        features=list(pos),
                        decimal=mat.decimal,
                        dtype=mat.dtype,
                        coldtypes=[mat.coldtypes[i] for i in colinds],
                        index=lastinds)
            
            mm = mat.matrix
            for row in range(d0):
                c = 0
                for col in colinds:
                    temp._matrix[row][c] = mm[row][col]
                    c+=1
            return temp
        
        #Tuple given    
        if len(pos)==2:
            pos = list(pos)
            # Matrix[slice,column_index]
            if isinstance(pos[0],slice):
                if uselabel:
                    indices = mat.index
                    indices_labels = indices.labels

                    filtered_labels = indices.get_level(rowlevel)

                    start = filtered_labels.index(pos[0].start) if pos[0].start != None else None
                    end = filtered_labels.index(pos[0].stop) if pos[0].stop != None else None

                    first_item = filtered_labels[start] if start != None else None
                    last_item = filtered_labels[end] if end != None else None

                    no_end = True if end == None else False

                    start = start if start != None else 0
                    end = end if end != None else d0

                    first_found = False if first_item != None else True

                    rowrange,mm = [],mat.matrix
                    for i in range(start,end):
                        try:
                            val = filtered_labels[i]

                            if val==last_item and no_end:
                                break
                            if not first_found:
                                first_found = bool(val==first_item)

                            if first_found:
                                rowrange.append(i)
                                
                        except:
                            continue     

                else:
                    newslice = betterslice(pos[0],d0)
                    rowrange = list(range(newslice.start,newslice.stop,newslice.step))

            # Matrix[int,column_index]
            elif isinstance(pos[0],int):
                if uselabel:
                    indices = mat.index.get_level(rowlevel)
                    rowrange = [i for i in range(mat.d0) if indices[i]==pos[0]]
                else:
                    rowrange = [pos[0]]

            # Matrix[list,column_index]
            elif isinstance(pos[0],list):
                if uselabel:
                    indices = mat.index.get_level(rowlevel)
                    #######Assertion
                    #sublist(pos[0],indices,"list of indices","indices",throw=True)
                    #######
                    rowrange = [i for i in range(d0) if indices[i] in pos[0]]
                else:
                    #######Assertion
                    consistentlist(pos[0],int,"indices",throw=True)
                    rangedlist(pos[0],lambda a:(a<d0) and (a>=0),"indices",f"[0,{d0})",throw=True)
                    #######
                    rowrange = pos[0]

            # Matrix(Matrix,column_index]
            elif isinstance(pos[0],obj):
                if uselabel:
                    return None
                rowrange = [i[0] for i in pos[0].find(1,0)]
            else:
                raise TypeError(f"{pos[0]} can't be used as row index")
        
            #########################
            
            # Matrix[row_index,str]
            if isinstance(pos[1],str):
                pos[1] = mat.features.index(pos[1])

            # Matrix[row_index,slice]
            elif isinstance(pos[1],slice):
                default_st = pos[1].start if pos[1].start!=None else 0
                default_en = pos[1].stop if pos[1].stop!=None else d1
                start = mat.features.index(pos[1].start) if isinstance(pos[1].start,str) else default_st
                end = mat.features.index(pos[1].stop) if isinstance(pos[1].stop,str) else default_en
                pos[1] = betterslice(slice(start,end),d1)

            # Matrix[row_index,Tuple(str)]
            elif isinstance(pos[1],(tuple,list)):
                #######Assertion
                consistentlist(pos[1],(int,str),"indices",throw=True)
                colinds = [mat.features.index(i) if isinstance(i,str) else i for i in pos[1]]
                rangedlist(colinds,lambda a:(a<d1) and (a>=0),"indices",f"[0,{d1})",throw=True)
                #######
                inds = mat.index
                labels = inds.labels
                indices = Label([labels[i] for i in rowrange],inds.names) if mat._dfMat else Label()

                temp = []
                mm = mat.matrix
                r=0

                if returninds:
                    return (rowrange,colinds)

                for row in rowrange:
                    temp.append([])
                    for col in colinds:
                        temp[r].append(mm[row][col])
                    r+=1

                return obj((len(rowrange),len(colinds)),temp,
                            features=[mat.features[i] for i in colinds],
                            decimal=mat.decimal,dtype=mat.dtype,
                            coldtypes=[mat.coldtypes[i] for i in colinds],
                            index=indices,
                            )

            t = mat.coldtypes[pos[1]]
            mm = mat.matrix
            inds = mat.index
            labels = inds.labels
            lastinds = Label([labels[i] for i in rowrange],inds.names) if mat._dfMat else Label()

            if type(t) != list:
                t = [t]

            if returninds:
                if isinstance(pos[1],slice):
                    return (rowrange,range(d1)[pos[1]])
                return (rowrange,pos[1])

            if isinstance(pos[0],int) and isinstance(pos[1],int):
                return mat._matrix[rowrange[0]][pos[1]]
                
            elif isinstance(pos[1],int):
                return obj(data=[[mm[i][pos[1]]] for i in rowrange],
                           features=[mat.features[pos[1]]],
                           decimal=mat.decimal,
                           dtype=mat.dtype,
                           coldtypes=t,
                           index=lastinds)
            
            elif isinstance(pos[1],slice):
                return obj(data=[mm[i][pos[1]] for i in rowrange],
                           features=mat.features[pos[1]],
                           decimal=mat.decimal,
                           dtype=mat.dtype,
                           coldtypes=t,
                           index=lastinds)
            
            # Matrix[Matrix,column_index]
            elif isinstance(pos[0],obj):
                temp = []
                if isinstance(pos[1],int): #Force slice
                    if pos[1]>=d1 or pos[1]<0:
                        raise IndexError(f"{pos[1]} can't be used as column index")
                    pos[1] = slice(pos[1],pos[1]+1)

                mm = mat.matrix

                for i in rowrange:
                    temp.append(mm[i][pos[1]])

                return obj(data=temp,
                           features=mat.features[pos[1]],
                           dtype=mat.dtype,
                           decimal=mat.decimal,
                           coldtypes=mat.coldtypes[pos[1]],
                           index=lastinds)
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #0-1 filled matrix given as indeces
    elif isinstance(pos,obj):
        if uselabel:
            return None
        rowrange = [i for i in range(mat.d0) if pos._matrix[i][0]==1]

        if returninds:
            return (rowrange,None)

        mm = mat.matrix
        temp = [mm[i] for i in rowrange]

        inds = mat.index
        labels = inds.labels
        lastinds = Label([labels[i] for i in rowrange],inds.names) if mat._dfMat else Label()

        return obj(data=temp,
                   features=mat.features,
                   dtype=mat.dtype,
                   decimal=mat.decimal,
                   coldtypes=mat.coldtypes,
                   index=lastinds)

def setitem(mat,pos,item,obj,uselabel,rowlevel=1):
    from MatricesM.errors.errors import DimensionError
    from MatricesM.validations.validate import consistentlist,exactdimension

    d0,d1 = mat.dim

    def fix_given_item(item,rowrange:list,colrange:list,axis:[0,1]=0):
        rl,cl = len(rowrange),len(colrange)
        lislen = [cl,rl][axis]
        #List given
        if isinstance(item,list):
            #Lists of lists given
            if consistentlist(item,list):
                #No changes needed  
                exactdimension(item,rl,cl,throw=True)
            #List of values given 
            elif len(item)==lislen:
                if axis:
                    item = [[item[i] for _ in colrange] for i in rowrange]
                else:
                    item = [item[:] for _ in rowrange]
            else:
                raise DimensionError(f"Given list's length should be {lislen}")
                
        #Matrix given
        elif isinstance(item,obj):
            if (item.dim[1] != cl) or (item.dim[0] != rl):
                raise DimensionError(f"Given matrix's dimensions should be {rl}x{cl}")
            item = item.matrix

        #Single value given
        else:
            item = [[item for j in colrange] for i in rowrange]
        return item
    
    rowrange,colrange = getitem(mat,pos,obj,uselabel,returninds=True)
    rowrange = rowrange if isinstance(rowrange,(list,range)) else [rowrange]
    colrange = colrange if isinstance(colrange,(list,range)) else [colrange]
    rows = rowrange if rowrange!=[None] else range(d0)
    cols = colrange if colrange!=[None] else range(d1)
    
    #Slice or list of row indices
    if isinstance(pos,(slice,list,int)):
        #####Fix item's dimensions#####
        item = fix_given_item(item,rows,cols)
        ###############################
        r = 0
        for row in rows:
            mat._matrix[row] = item[r][:]
            r+=1 

    #Change a column, add a column or change a column's values of given row indices
    elif isinstance(pos,str):
        new_col = 0
        if not (pos in mat.features) and not uselabel:
            new_col = 1
        if not new_col:
            if uselabel:#Change rows with given index
                #####Fix item's dimensions#####
                item = fix_given_item(item,rows,cols)
                ###############################
                r = 0
                for i in rows:
                    mat._matrix[i] = item[r][:]
                    r+=1
            else:#Change a column
                #####Fix item's dimensions#####
                item = fix_given_item(item,rows,cols,1)
                ###############################
                ind = mat.features.index(pos)
                for i in rows:
                    mat._matrix[i][ind] = item[i][0]
        else:
            #####Fix item's dimensions#####
            item = fix_given_item(item,rows,[None],1)
            ###############################
            for i in rows:
                mat._matrix[i].append(item[i][0])
            mat._Matrix__features.append(pos)
            mat._Matrix__coldtypes.append(type(item[i][0]))
            mat._Matrix__dim = [d0,d1+1]


    #Change certain parts of the matrix
    elif isinstance(pos,tuple):
        #Change given columns
        if consistentlist(pos,str):
            #####Fix item's dimensions#####
            item = fix_given_item(item,rows,cols,1)
            ###############################
            i = 0
            for r in rows:
                j = 0
                for c in cols:
                    mat._matrix[r][c] = item[i][j]
                    j+=1
                i+=1

        #Tuple with row indices first, column indices/names second
        elif len(pos)==2:
            #Assert second index contains column name
            if consistentlist(pos[1],str):
                #####Fix item's dimensions#####
                item = fix_given_item(item,rows,cols,1)
                ###############################
                i = 0
                for r in rows:
                    j = 0
                    for c in cols:
                        mat._matrix[r][c] = item[i][j]
                        j+=1
                    i+=1

            #Matrix[ slice|int, slice|int ] | Matrix[ Matrix,col_index ]
            elif (isinstance(pos[0],(slice,int)) and isinstance(pos[1],(slice,int))) or isinstance(pos[0],obj):
                #####Fix item's dimensions#####
                item = fix_given_item(item,rows,cols)
                ###############################
                i = 0
                for r in rows:
                    j = 0
                    for c in cols:
                        mat._matrix[r][c] = item[i][j]
                        j+=1
                    i+=1

            else:
                raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #Matrix[ Matrix ]
    elif isinstance(pos,obj):
        #####Fix item's dimensions#####
        rows = rows if len(rows)!=0 else list(range(d0))
        item = fix_given_item(item,rows,cols)
        ###############################
        i = 0
        for row in rows:
            mat._matrix[row] = item[i][:]
            i+=1
        
    else:
        raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")

    return mat

def delitem(mat,pos,obj,useind,rowlevel=1):
    from MatricesM.validations.validate import consistentlist
    from MatricesM.customs.objects import Label

    d0,d1 = mat.dim

    rowrange,colrange = getitem(mat,pos,obj,useind,returninds=True)
    rowrange = rowrange if isinstance(rowrange,(list,range)) else [rowrange]
    colrange = colrange if isinstance(colrange,(list,range)) else [colrange]
    rows = rowrange if rowrange!=[None] else range(d0)
    cols = colrange if colrange!=[None] else range(d1)

    allrows = bool(rows in [range(d0),list(range(d0))])
    allcols = bool(cols in [range(d1),list(range(d1))])

    #All values deleted
    if allrows and allcols:
        mat._Matrix__dim = [0,0]
        mat._matrix = []
        mat._Matrix__coldtypes = []
        mat._Matrix__features = []
        mat._Matrix__index = Label()
    
    #Rows deleted
    elif allcols:
        rows = sorted(rows)
        i = 0
        if mat._dfMat:
            for row in rows:
                del mat._matrix[row-i]
                del mat._Matrix__index[row-i]
                i+=1
        else:
            for row in rows:
                del mat._matrix[row-i]
                i+=1

        mat._Matrix__dim = [d0-i,d1]

    #Columns deleted
    elif allrows:
        rows = sorted(rows)
        cols = sorted(cols)
        j = 0
        for col in cols:
            del mat._Matrix__features[col-j]
            del mat._Matrix__coldtypes[col-j]
            for row in rows:
                del mat._matrix[row][col-j]
            j+=1

        mat._Matrix__dim = [d0,d1-j]
    
    #Can't delete smaller parts 
    else:
        raise ValueError(f"Can't delete parts of the matrix that aren't complete columns or rows")
