def _repr(mat,notes,dFrame):
    from shutil import get_terminal_size as gts
    
    d0,d1 = mat.dim
    feats = mat.features
    used_col_amount = 1 if mat._dfMat else 0
    cmat = 4 if mat._cMat else 0

    string_bounds = mat._stringfy(mat.coldtypes,True)
    if (not isinstance(string_bounds,list)) or (len(feats)==0):
        return "Empty Matrix"
    string_bounds = string_bounds[:1] + list(map(lambda a:a+2+cmat,string_bounds[1:]))
    terminal_col_size = gts().columns - max([len(feat) for feat in feats]) - 8 - string_bounds[0]

    shuffled_col_inds = [0]
    upper = d1//2+1 if d1%2 else d1//2
    for ind in range(1,upper):
        shuffled_col_inds.append(ind)
        shuffled_col_inds.append(-ind)
    if not d1%2:
        shuffled_col_inds.append(d1//2)
    
    total = 0
    for i in shuffled_col_inds:
        bound = string_bounds[i]
        new = total+bound
        if new < terminal_col_size:
            total += bound
            used_col_amount += 1
        else:
            break

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
    if mat.dim[0]<=rowlimit and mat.dim[1]<=collimit:
        return mat._stringfy(coldtypes=mat.coldtypes[:]) + "\n\n" + notes

    halfrow = rowlimit//2
    halfcol = collimit//2
    if collimit%2 != 0:
        halfcol = collimit//2 + 1
    if rowlimit%2 != 0:
        halfrow = rowlimit//2 + 1

    #Too many rows
    if mat.dim[0]>rowlimit:
        #Too many columns
        if mat.dim[1]>collimit:
            #Divide matrix into 4 parts
            topLeft = mat[:halfrow,:halfcol].roundForm(mat.decimal)
            topRight = mat[:halfrow,-(collimit//2):].roundForm(mat.decimal)
            bottomLeft = mat[mat.d0-(rowlimit//2):,:halfcol].roundForm(mat.decimal)
            bottomRight = mat[mat.d0-(rowlimit//2):,-(collimit//2):].roundForm(mat.decimal)

            #Change dtypes to dFrames filled with strings
            for i in [topLeft,topRight,bottomLeft,bottomRight]:
                if i.dtype != dFrame:
                    i.dtype = dFrame
            topLeft.coldtypes = [str]*(halfcol)
            topRight.coldtypes = [str]*(collimit//2)
            bottomLeft.coldtypes = [str]*(halfcol)
            bottomRight.coldtypes = [str]*(collimit//2)

            #Add  ...  to represent missing column's existence
            topLeft.add([" ..."]*(halfrow),col=halfcol + 1,dtype=str,feature="")
            bottomLeft.add([" ..."]*(rowlimit//2),col=halfcol + 1,dtype=str,feature="")
            
            #Concat left part with right, dots in the middle
            topLeft.concat(topRight,concat_as="col")
            bottomLeft.concat(bottomRight,concat_as="col")
            topLeft.concat(bottomLeft,concat_as="row")
            
            #Add dots as middle row and spaces below and above it
            topLeft.add([""]*(collimit+1),row=halfrow+1)
            topLeft.add([" ..."]*(collimit+1),row=halfrow+1)
            topLeft.add([""]*(collimit+1),row=halfrow+1)
            return topLeft._stringfy(coldtypes=topLeft.coldtypes) + "\n\n" + notes

        #Just too many rows
        else:
            #Get needed parts
            top = mat[:halfrow,:].roundForm(mat.decimal)
            bottom = mat[mat.d0-(rowlimit//2):,:].roundForm(mat.decimal)
            #Set new dtypes
            for i in [top,bottom]:
                if i.dtype != dFrame:
                    i.dtype = dFrame
                i.coldtypes = [str]*(collimit)
            #Concat last items
            top.concat(bottom,concat_as="row")
            #Add middle part
            top.add([""]*mat.dim[1],row=halfrow+1)
            top.add([" ..."]*mat.dim[1],row=halfrow+1)
            top.add([""]*mat.dim[1],row=halfrow+1)

            return top._stringfy(coldtypes=top.coldtypes) + "\n\n" + notes
            
    #Just too many columns
    elif mat.dim[1]>collimit:
        #Get needed parts
        left = mat[:,:halfcol].roundForm(mat.decimal)
        right = mat[:,-(collimit//2):].roundForm(mat.decimal)
        #Set new dtypes
        for i in [left,right]:
            if i.dtype != dFrame:
                i.dtype = dFrame
        left.coldtypes = [str]*(halfcol)
        right.coldtypes = [str]*(collimit//2)
        #Add and concat rest of the stuff
        left.add([" ..."]*mat.dim[0],col=halfcol + 1,dtype=str,feature="")
        left.concat(right,concat_as="col")

        return left._stringfy(coldtypes=left.coldtypes) + "\n\n" + notes
    #Should't go here
    else:
        raise ValueError("Something is wrong with the matrix, check dimensions and values")