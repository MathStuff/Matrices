def _repr(mat,notes,dFrame):
    from shutil import get_terminal_size as gts
    
    d0,d1 = mat.dim
    feats = mat.features
    available = gts().columns - 1
    
    shuffled_col_inds = []
    usedcols = []
    used_col_amount = 0 

    upper = d1//2 + 1 if d1%2 else d1//2
    cmat = 4 if mat._cMat else 0

    for ind in range(1,d1):
        shuffled_col_inds.append(ind)
        shuffled_col_inds.append(d1-ind)
    if not d1%2:
        shuffled_col_inds.append(d1//2 + 1)

    string_bounds = mat._stringfy(mat.coldtypes,True)
    string_bounds = [string_bounds[0]+1] + list(map(lambda a:a+cmat+2,string_bounds[1:]))
    total_col_size = string_bounds[0]

    if (not isinstance(string_bounds,list)) or (len(feats)==0):
        return "Empty Matrix"

    if sum(string_bounds)>available:
    #Check how many columns will fit
        for i in shuffled_col_inds:
            bound = string_bounds[i]
            new = total_col_size + bound + 5
            if new <= available:
                total_col_size += bound
                used_col_amount += 1
                usedcols.append(i-1)
            else:
                break
    else:
        used_col_amount = d1

    if used_col_amount == 0:
        return "\nWindow \ntoo \nsmall"

    #Check limits
    rowlimit,collimit = min(d0,mat.ROW_LIMIT),min(d1,mat.COL_LIMIT,used_col_amount)
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
        return mat._stringfy(coldtypes=mat.coldtypes[:]) + "\n\n" + notes

    halfrow = rowlimit//2
    if rowlimit%2 != 0:
        halfrow = rowlimit//2 + 1

    halfcol = collimit//2
    if collimit%2 != 0:
        halfcol = collimit//2 + 1
    
    srted = sorted(usedcols)
    first = srted[:halfcol]
    second = srted[-(collimit//2):]
    #Too many rows
    if d0>rowlimit:
        #Too many columns
        if d1>collimit and collimit>1:
            #Divide matrix into 4 parts
            topLeft = mat[:halfrow,first].roundForm(mat.decimal)
            topRight = mat[:halfrow,second].roundForm(mat.decimal)
            bottomLeft = mat[mat.d0-(rowlimit//2):,first].roundForm(mat.decimal)
            bottomRight = mat[mat.d0-(rowlimit//2):,second].roundForm(mat.decimal)

            #Change dtypes to dFrames filled with strings
            for i in [topLeft,topRight,bottomLeft,bottomRight]:
                if i.dtype != dFrame:
                    i.dtype = dFrame

            #Add  ...  to represent missing column's existence
            topLeft.add(["..."]*(halfrow),col=halfcol + 1,dtype=str,feature="")
            bottomLeft.add(["..."]*(rowlimit//2),col=halfcol + 1,dtype=str,feature="")
            
            #Concat left part with right, dots in the middle
            topLeft.concat(topRight,axis=1)
            bottomLeft.concat(bottomRight,axis=1)
            topLeft.concat(bottomLeft,axis=0)
            
            #Add dots as middle row
            topLeft.add(["..."]*(collimit+1),row=halfrow+1,index="...")

            return topLeft._stringfy(coldtypes=topLeft.coldtypes) + "\n\n" + notes

        #Just too many rows
        else:
            end = 1 if collimit==1 else d1
            #Get needed parts
            top = mat[:halfrow,:end].roundForm(mat.decimal)
            bottom = mat[mat.d0-(rowlimit//2):,:end].roundForm(mat.decimal)
            if d1>1 and end == 1:
                top.add(["..."]*(halfrow),col=2,dtype=str,feature="")
                bottom.add(["..."]*(rowlimit//2),col=2,dtype=str,feature="")
                end = 2
            #Set new dtypes
            for i in [top,bottom]:
                if i.dtype != dFrame:
                    i.dtype = dFrame

            #Concat last items
            top.concat(bottom,axis=0)

            #Add middle part
            top.add(["..."]*end,row=halfrow+1,index="...")

            return top._stringfy(coldtypes=top.coldtypes) + "\n\n" + notes
            
    #Just too many columns
    elif d1>collimit:
        #Single column can fit
        if first == second:
            left = mat[:,0].roundForm(mat.decimal)
            if d1>1:
                left.add(["..."]*d0,col=2,dtype=str,feature="")
            if not mat._dfMat:
                left.dtype = dFrame

        else:
            #Get needed parts
            left = mat[:,first].roundForm(mat.decimal)
            right = mat[:,second].roundForm(mat.decimal)
            
            #Set new dtypes
            for i in [left,right]:
                if i.dtype != dFrame:
                    i.dtype = dFrame

            #Add and concat rest of the stuff
            left.add(["..."]*d0,col=halfcol + 1,dtype=str,feature="")
            left.concat(right,axis=1)

        return left._stringfy(coldtypes=left.coldtypes) + "\n\n" + notes
    #Should't go here
    else:
        raise ValueError("Something is wrong with the matrix, check dimensions and values")