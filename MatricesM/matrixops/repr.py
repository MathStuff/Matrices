def _repr(mat):
    from MatricesM.matrix import dataframe
    rowlimit,collimit = min(mat.dim[0],mat.ROW_LIMIT),min(mat.dim[1],mat.COL_LIMIT)
    for i in [rowlimit,collimit]:
        if not isinstance(i,int):
            raise TypeError("ROW/COL limit can't be non-integer values")
        else:
            if i<1:
                return f"Can't display any rows/columns using limits for rows and columns : [{rowlimit},{collimit}]"
                
    #Not too many rows or columns
    if mat.dim[0]<=rowlimit and mat.dim[1]<=collimit:
        return mat._stringfy(coldtypes=mat.coldtypes[:])

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
            bottomLeft = mat[-(rowlimit//2):,:halfcol].roundForm(mat.decimal)
            bottomRight = mat[-(rowlimit//2):,-(collimit//2):].roundForm(mat.decimal)

            #Change dtypes to dataframes filled with strings
            for i in [topLeft,topRight,bottomLeft,bottomRight]:
                if i.dtype != dataframe:
                    i.dtype = dataframe
            topLeft.coldtypes = [str]*(halfcol)
            topRight.coldtypes = [str]*(collimit//2)
            bottomLeft.coldtypes = [str]*(halfcol)
            bottomRight.coldtypes = [str]*(collimit//2)

            #Add . . . to represent missing column's existence
            topLeft.add([". . ."]*(halfrow),col=halfcol + 1,dtype=str,feature="")
            bottomLeft.add([". . ."]*(rowlimit//2),col=halfcol + 1,dtype=str,feature="")
            
            #Concat left part with right, dots in the middle
            topLeft.concat(topRight,concat_as="col")
            bottomLeft.concat(bottomRight,concat_as="col")
            topLeft.concat(bottomLeft,concat_as="row")
            
            #Add dots as middle row and spaces below and above it
            topLeft.add([""]*(collimit+1),row=halfrow+1)
            topLeft.add([". . ."]*(collimit+1),row=halfrow+1)
            topLeft.add([""]*(collimit+1),row=halfrow+1)
            return topLeft._stringfy(coldtypes=topLeft.coldtypes)

        #Just too many rows
        else:
            #Get needed parts
            top = mat[:halfrow,:].roundForm(mat.decimal)
            bottom = mat[-(rowlimit//2):,:].roundForm(mat.decimal)
            #Set new dtypes
            for i in [top,bottom]:
                if i.dtype != dataframe:
                    i.dtype = dataframe
                i.coldtypes = [str]*(collimit)
            #Concat last items
            top.concat(bottom,concat_as="row")
            #Add middle part
            top.add([""]*mat.dim[1],row=halfrow+1)
            top.add([". . ."]*mat.dim[1],row=halfrow+1)
            top.add([""]*mat.dim[1],row=halfrow+1)

            return top._stringfy(coldtypes=top.coldtypes)
            
    #Just too many columns
    elif mat.dim[1]>collimit:
        #Get needed parts
        left = mat[:,:halfcol].roundForm(mat.decimal)
        right = mat[:,-(collimit//2):].roundForm(mat.decimal)
        #Set new dtypes
        for i in [left,right]:
            if i.dtype != dataframe:
                i.dtype = dataframe
        left.coldtypes = [str]*(halfcol)
        right.coldtypes = [str]*(collimit//2)
        #Add and concat rest of the stuff
        left.add([". . ."]*mat.dim[0],col=halfcol + 1,dtype=str,feature="")
        left.concat(right,concat_as="col")

        return left._stringfy(coldtypes=left.coldtypes)
    #Should't go here
    else:
        raise ValueError("Something is wrong with the matrix, check dimensions and values")