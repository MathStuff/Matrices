def _repr(mat,notes,dFrame):
    from shutil import get_terminal_size as gts
    
    old = None
    d0,d1 = mat.dim
    feats = mat.features
    ind_level = mat.index.level
    col_place_holder = mat.DISPLAY_OPTIONS["col_place_holder"]
    row_place_holder = mat.DISPLAY_OPTIONS["row_place_holder"]
    available = gts().columns - 4
    
    shuffled_col_inds = []
    usedcols = []
    used_col_amount = 0 

    upper = d1//2 + 1 if d1%2 else d1//2

    for ind in range(upper):
        shuffled_col_inds.append(ind)
        shuffled_col_inds.append(d1-ind-1)
    if d1%2:
        shuffled_col_inds.append(d1//2 + 1)

    rowlimit = min(d0,mat.ROW_LIMIT)
    halfrow = rowlimit//2
    if rowlimit%2:
        halfrow += 1

    #Get column tab lengths to decide which columns to print
    old_dfMat,old_fMat,old_cMat = mat._dfMat,mat._fMat,mat._cMat
    #Turn non-dataframe into dataframe
    if mat.dtype != dFrame:
        old = mat.copy
        mat = old.copy
        mat.dtype = dFrame
    #All rows can be printed
    if rowlimit==d0:
        string_bounds = mat._stringfy(mat.coldtypes,True)
    #Too many rows, use only the head and tail rows' tab lengths
    else:
        top_bounds = mat[:halfrow]._stringfy(mat.coldtypes,True)
        bottom_bounds = mat[d0-(rowlimit//2):]._stringfy(mat.coldtypes,True)
        string_bounds = [max(top_bounds[i],bottom_bounds[i]) for i in range(d1+ind_level)]

    if string_bounds == "Empty matrix":
        return string_bounds

    total_col_size = sum(string_bounds[:ind_level])+(ind_level-1)+1
    string_bounds = list(map(lambda a:a+2,string_bounds[ind_level:-1])) + [string_bounds[-1]]

    if (not isinstance(string_bounds,list)) or (len(feats)==0):
        return "Empty Matrix"

    if sum(string_bounds)+total_col_size>available:
    #Check how many columns will fit
        for num,i in enumerate(shuffled_col_inds):
            bound = string_bounds[i]
            extra = 5 if num!=d1-1 else 0
            new = total_col_size + bound + extra
            if new <= available:
                total_col_size += bound
                used_col_amount += 1
                usedcols.append(i)
            else:
                break
    else:
        used_col_amount = d1

    if used_col_amount == 0:
        return "\nWindow \ntoo \nsmall"

    #Check limits
    collimit = min(d1,used_col_amount)
    for i in [rowlimit,collimit]:
        if not isinstance(i,int):
            raise TypeError("ROW/COL limit can't be non-integer values")
        else:
            if i<1:
                return f"Can't display any rows/columns using limits for rows and columns : [{rowlimit},{collimit}]"
    
    if not isinstance(notes,str):
        raise TypeError(f"NOTES option can only be used with strings, not {type(notes).__name__}")

    #Not too many rows or columns
    if d0<=rowlimit and d1<=collimit:
        if old != None:
            return old._stringfy(coldtypes=mat.coldtypes[:]) + "\n\n" + notes
        return mat._stringfy(coldtypes=mat.coldtypes[:]) + "\n\n" + notes

    halfcol = collimit//2
    if collimit%2:
        halfcol += 1
    
    srted = sorted(usedcols)
    first = srted[:halfcol]
    second = srted[halfcol:]
    dec = mat.decimal if (old_dfMat or old_fMat or old_cMat) else 0
    #Too many rows
    if d0>rowlimit:
        #Too many columns
        if d1>collimit and collimit>1:
            #Divide matrix into 4 parts
            topLeft = mat[:halfrow,first].roundForm(mat.decimal,dec)
            topRight = mat[:halfrow,second].roundForm(mat.decimal,dec)
            bottomLeft = mat[d0-(rowlimit//2):,first].roundForm(mat.decimal,dec)
            bottomRight = mat[d0-(rowlimit//2):,second].roundForm(mat.decimal,dec)

            #Change dtypes to dFrames filled with strings
            for i in [topLeft,topRight,bottomLeft,bottomRight]:
                if i.dtype != dFrame:
                    i.dtype = dFrame

            #Add  ...  to represent missing column's existence
            topLeft.add([col_place_holder]*topLeft.d0,col=halfcol + 1,dtype=str,feature=col_place_holder)
            bottomLeft.add([col_place_holder]*bottomLeft.d0,col=halfcol + 1,dtype=str,feature=col_place_holder)
            
            #Concat left parts with rights, dots in the middle
            topLeft.concat(topRight,axis=1)
            bottomLeft.concat(bottomRight,axis=1)

            #Fix indices       
            if mat._dfMat:
                topLeft.index = mat.index[:halfrow]
                bottomLeft.index = mat.index[d0-(rowlimit//2):]
            else:
                bottomLeft.index = list(range(d0-(rowlimit//2),d0))

            #Concat bottom to top
            topLeft.concat(bottomLeft,axis=0)
            
            #Add dots as middle row
            topLeft.add([row_place_holder]*topLeft.d1,row=halfrow+1,index=row_place_holder)

            return topLeft._stringfy(coldtypes=topLeft.coldtypes) + "\n\n" + notes

        #Just too many rows
        else:
            end = 1 if collimit==1 else d1
            #Get needed parts
            top = mat[:halfrow,:end].roundForm(mat.decimal,dec)
            bottom = mat[d0-(rowlimit//2):,:end].roundForm(mat.decimal,dec)
            if d1>1 and end == 1:
                top.add([col_place_holder]*top.d0,col=2,dtype=str,feature=col_place_holder)
                bottom.add([col_place_holder]*bottom.d0,col=2,dtype=str,feature=col_place_holder)
            #Set new dtypes
            for i in [top,bottom]:
                if i.dtype != dFrame:
                    i.dtype = dFrame

            #Fix indices       
            if mat._dfMat:
                top.index = mat.index[:halfrow]
                bottom.index = mat.index[d0-(rowlimit//2):]
            else:
                bottom.index = list(range(d0-(rowlimit//2),d0))

            #Concat last items
            top.concat(bottom,axis=0)

            #Add middle part
            top.add([row_place_holder]*top.d1,row=halfrow+1,index=row_place_holder)

            return top._stringfy(coldtypes=top.coldtypes) + "\n\n" + notes
            
    #Just too many columns
    elif d1>collimit:
        #Single column can fit
        if first == second:
            left = mat[:,0].roundForm(mat.decimal,dec)
            if d1>1:
                left.add([col_place_holder]*d0,col=2,dtype=str,feature=col_place_holder)
            if not mat._dfMat:
                left.dtype = dFrame

        else:
            #Get needed parts
            left = mat[:,first].roundForm(mat.decimal,dec)
            right = mat[:,second].roundForm(mat.decimal,dec)
            #Set new dtypes
            for i in [left,right]:
                if i.dtype != dFrame:
                    i.dtype = dFrame

            #Add and concat rest of the stuff
            left.add([col_place_holder]*d0,col=halfcol + 1,dtype=str,feature=col_place_holder)
            left.concat(right,axis=1)

        return left._stringfy(coldtypes=left.coldtypes) + "\n\n" + notes
    #Should't go here
    else:
        raise ValueError("Something is wrong with the matrix, check dimensions and values")
