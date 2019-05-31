def normalize(mat,col=None,inplace=True,zerobound=12):
    if isinstance(col,str):
        col=mat.features.index(col)+1
        
    if not inplace:
        if col==None:
            temp = mat.copy
            r = mat.ranged()
            valid_col_indeces = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
            for i in valid_col_indeces:
                mn,mx = r[mat.features[i]][0],r[mat.features[i]][1]
                
                if round(mx-mn,zerobound) == 0:
                    raise ZeroDivisionError("Max and min values are the same")

                j=0 #Index
                while True:#Loop through the column
                    try:
                        while j<mat.dim[0]:
                            temp._matrix[j][i] = (temp._matrix[j][i]-mn)/(mx-mn)
                            j+=1
                    except:#Value was invalid
                        j+=1
                        continue
                    else:
                        break
    
            return temp
        
        else:
            if isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't normalize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            temp = mat.col(col)
            r = mat.ranged(col,asDict=False)
            mn,mx = r[0],r[1]

            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")

            i=0 #Index
            while True:#Loop through the column
                try:
                    while i<mat.dim[0]:
                        temp._matrix[i][0] = (temp._matrix[i][0]-mn)/(mx-mn)
                        i+=1
                except:#Value was invalid
                    i+=1
                    continue
                else:
                    break

            return temp
        
    else:
        if col==None:
            r = mat.ranged()
            valid_col_indeces = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
            for i in valid_col_indeces:
                mn,mx = r[mat.features[i]][0],r[mat.features[i]][1]
                
                if round(mx-mn,zerobound) == 0:
                    raise ZeroDivisionError("Max and min values are the same")
                
                j=0 #Index
                while True:#Loop through the column
                    try:
                        while j<mat.dim[0]:
                            mat._matrix[j][i] = (mat._matrix[j][i]-mn)/(mx-mn)
                            j+=1
                    except:#Value was invalid
                        j+=1
                        continue
                    else:
                        break
                        
        else:
            if isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't normalize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            r = mat.ranged(col,asDict=False)
            mn,mx = r[0],r[1]
            
            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")
            col-=1 
            j=0 #Index
            while True:#Loop through the column
                try:
                    while j<mat.dim[0]:
                        temp._matrix[j][col] = (temp._matrix[j][col]-mn)/(mx-mn)
                        j+=1
                except:#Value was invalid
                    j+=1
                    continue
                else:
                    break
                    