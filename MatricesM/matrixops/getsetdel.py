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

def getitem(mat,pos,obj,useindex,returninds=False):
    from MatricesM.validations.validate import consistentlist,sublist,rangedlist

    mat.use_row_index_to_get_item = 0 #Reset ind
    d0,d1 = mat.dim

    #Get 1 row
    if isinstance(pos,int):
        if useindex:
            ind = mat.index
            mm = mat.matrix
            rowinds = [i for i in range(d0) if ind[i]==pos]
            lastinds = [pos for i in rowinds]
            if returninds:
                return (rowinds,None)
            return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds,indexname=mat.indexname)
        
        if returninds:
            return (pos,None)
        
        return obj(listed=[mat._matrix[pos]],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[mat.index[pos]],indexname=mat.indexname)

    #Get multiple rows
    elif isinstance(pos,slice):
        if useindex:
            indices = mat.index
            start = pos.start if pos.start != None else 0
            end = pos.stop if pos.stop != None else d1
            rowrange,mm = [],mat.matrix
            for i in range(d0):
                try:
                    if indices[i]>=start:
                        if indices[i]>=end:
                            break
                        rowrange.append(i)
                except:
                    continue
            if returninds:
                return (rowrange,None)        
            lastinds = [indices[i] for i in rowrange]
            lastmatrix = [mm[i] for i in rowrange]
            
            return obj(listed=lastmatrix,features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=lastinds,indexname=mat.indexname)
        
        if returninds:
            return (range(d0)[pos],None)
        
        return obj(listed=mat._matrix[pos],features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=mat.index[pos],indexname=mat.indexname)
    
    #Get 1 column or use a specific row index
    elif isinstance(pos,str):
        if useindex:
            index = mat.index
            if not pos in index:
                raise ValueError(f"{pos} is not a row index")
            else:
                mm = mat.matrix
                rowinds = [i for i in range(d0) if index[i]==pos]
                if returninds:
                    return (rowinds,None)
                return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                           dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[pos for _ in range(len(rowinds))],
                           indexname=mat.indexname)

        if not (pos in mat.features):
            if returninds:
                return (None,range(d0))
            raise ValueError(f"{pos} is not in column names")
        else:
            pos = mat.features.index(pos)

        if returninds:
            return (None,pos)

        mat =  obj(dim=[d0,1],listed=[[i[pos]] for i in mat._matrix],features=[mat.features[pos]],
                   decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[pos]],index=mat.index[:],
                   indexname=mat.indexname,implicit=True)
        mat.NOTES = f"n:{d0},type:{mat.coldtypes[0].__name__},invalid:{d0-mat.count(get=0)}\n\n"
        return mat

    #Get rows from given indices
    elif isinstance(pos,list):
        if useindex:
            indices = mat.index
            #######Assertion
            sublist(pos,indices,"list of indices","indices",throw=True)
            #######
            mm = mat.matrix
            rowinds = [i for i in range(d0) if indices[i] in pos]
            if returninds:
                return rowinds
            return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                        dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[indices[a] for a in rowinds],
                        indexname=mat.indexname)

        #######Assertion
        consistentlist(pos,int,"indices",throw=True)
        rangedlist(pos,lambda a:(a<d0) and (a>=0),"indices",f"[0,{d0})",throw=True)
        #######
        if returninds:
            return (pos,None)
        mm = mat.matrix
        i = mat.index
        inds = [i[index] for index in pos] if mat._dfMat else []
        
        return obj(listed=[mm[i][:] for i in pos],features=mat.features,coldtypes=mat.coldtypes,dtype=mat.dtype,decimal=mat.decimal,index=inds,indexname=mat.indexname)

    #Get certain parts of the matrix
    elif isinstance(pos,tuple):
        pos = list(pos)
        #Column names or row indices given
        if consistentlist(pos,str):
            #Use as row indices
            if useindex:
                indices = mat.index
                rowinds = [i for i in range(d0) if indices[i] in pos]
                if returninds:
                    return (rowinds,None)
                return obj(listed=[mm[i][:] for i in rowinds],features=mat.features[:],decimal=mat.decimal,
                           dtype=mat.dtype,coldtypes=mat.coldtypes[:],index=[indices[a] for a in rowinds],
                           indexname=mat.indexname)

            #Use as column names
            colinds = [mat.features.index(i) for i in pos]
            if returninds:
                return (None,colinds)

            temp = obj((d0,len(pos)),fill=0,features=list(pos),decimal=mat.decimal,dtype=mat.dtype,coldtypes=[mat.coldtypes[i] for i in colinds],index=mat.index[:],indexname=mat.indexname)
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
                if useindex:
                    indices = mat.index
                    start = pos[0].start if pos[0].start != None else 0
                    end = pos[0].stop if pos[0].stop != None else mat.d1
                    rowrange = []
                    for i in range(mat.d0):
                        try:
                            if indices[i]>=start:
                                if indices[i]>=end:
                                    break
                                rowrange.append(i)
                        except:
                            continue
                else:
                    newslice = betterslice(pos[0],d0)
                    rowrange = range(newslice.start,min(newslice.stop,d0),newslice.step)
            # Matrix[int,column_index]
            elif isinstance(pos[0],int):
                if useindex:
                    indices = mat.index
                    rowrange = [i for i in range(mat.d0) if indices[i]==pos[0]]
                else:
                    rowrange = [pos[0]]
            # Matrix[list,column_index]
            elif isinstance(pos[0],list):
                if useindex:
                    indices = mat.index
                    #######Assertion
                    sublist(pos[0],indices,"list of indices","indices",throw=True)
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
                if useindex:
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
                indices = [inds[row] for row in rowrange] if mat._dfMat else []
                temp = []
                mm = mat.matrix
                r=0
                rowrange = list(set(rowrange))

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
                            indexname=mat.indexname)

            t = mat.coldtypes[pos[1]]
            mm = mat.matrix
            inds = mat.index
            rowrange = list(set(rowrange))
            lastinds = [inds[i] for i in rowrange] if mat._dfMat else []

            if type(t) != list:
                t = [t]

            if returninds:
                if isinstance(pos[1],slice):
                    return (rowrange,range(d1)[pos[1]])
                return (rowrange,pos[1])

            if isinstance(pos[0],int) and isinstance(pos[1],int):
                return mat._matrix[rowrange[0]][pos[1]]
                
            elif isinstance(pos[1],int):
                return obj(listed=[[mm[i][pos[1]]] for i in rowrange],features=[mat.features[pos[1]]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t,index=lastinds,indexname=mat.indexname)
            
            elif isinstance(pos[1],slice):
                return obj(listed=[mm[i][pos[1]] for i in rowrange],features=mat.features[pos[1]],decimal=mat.decimal,dtype=mat.dtype,coldtypes=t,index=lastinds,indexname=mat.indexname)
            
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

                return obj(listed=temp,features=mat.features[pos[1]],dtype=mat.dtype,decimal=mat.decimal,coldtypes=mat.coldtypes[pos[1]],index=lastinds,indexname=mat.indexname)
        else:
            raise IndexError(f"{pos} can't be used as indices")

    #0-1 filled matrix given as indeces
    elif isinstance(pos,obj):
        if useindex:
            return None
        rowrange = [i for i in range(mat.d0) if pos._matrix[i][0]==1]
        rowrange = list(set(rowrange))

        if returninds:
            return (rowrange,None)

        mm = mat.matrix
        temp = [mm[i] for i in rowrange]
        indices = mat.index
        return obj(listed=temp,features=mat.features,dtype=mat.dtype,decimal=mat.decimal,coldtypes=mat.coldtypes,index=[indices[i] for i in rowrange],indexname=mat.indexname)

def setitem(mat,pos,item,obj,useindex):
    from MatricesM.errors.errors import DimensionError
    from MatricesM.validations.validate import consistentlist,exactdimension

    mat.use_row_index_to_get_item = 0 #Reset ind
    d0,d1 = mat.dim

    def fix_given_item(item,rowrange:list,colrange:list,axis:[0,1]=0):
        rl,cl = len(rowrange),len(colrange)
        #List given
        if isinstance(item,list):
            #Lists of lists given
            if consistentlist(item,list):
                #No changes needed  
                exactdimension(item,rl,cl,throw=True)
            #List of values given 
            elif len(item)==cl:
                if axis:
                    item = [[item[i] for _ in rowrange] for i in colrange]
                else:
                    item = [item[:] for _ in rowrange]
            else:
                raise DimensionError(f"Given list's length should be {cl}")
                
        #Matrix given
        elif isinstance(item,obj):
            if item.dim[1] != cl  or item.dim[0] != rl:
                raise DimensionError(f"Given matrix's dimensions should be {rl}x{cl}")
            item = item.matrix

        #Single value given
        else:
            if axis:
                item = [[item for j in colrange] for i in rowrange]
            else:
                item = [[item for j in rowrange] for i in colrange]
        return item
    
    rowrange,colrange = getitem(mat,pos,None,useindex,returninds=True)
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
        if not (pos in mat.features) and not useindex:
            new_col = 1
        if not new_col:
            if useindex:#Change rows with given index
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
                    mat._matrix[r][c] = item[j][i]
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
                        mat._matrix[r][c] = item[j][i]
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
        item = fix_given_item(item,rows,cols)
        ###############################
        i = 0
        for row in rows:
            mat._matrix[row] = item[i][:]
            i+=1
        
    else:
        raise AssertionError(f"item: {item} can't be set to index: {pos}.\n\tUse ._matrix property to change individual elements")

    return mat

def delitem(mat,pos,obj,useind):
    from MatricesM.validations.validate import consistentlist

    mat.use_row_index_to_get_item = 0 #Reset ind
    d0,d1 = mat.dim

    rowrange,colrange = getitem(mat,pos,None,useind,returninds=True)
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
        mat._Matrix__index = []
    
    #Rows deleted
    elif allcols:
        if mat._dfMat:
            for row in rows:
                del mat._matrix[row]
                del mat.index[row]

        for row in rows:
            del mat._matrix[row]

        mat._Matrix__dim = [d0-len(rows),d1]

    #Columns deleted
    elif allrows:
        for col in cols:
            del mat._Matrix__coldtypes[col]
            del mat._Matrix__features[col]
            for row in rows:
                del mat._matrix[row][col]
                
        mat._Matrix__dim = [d0,d1-len(cols)]
    
    #Can't delete smaller parts 
    else:
        raise ValueError(f"Can't delete parts of the matrix that aren't complete columns or rows")