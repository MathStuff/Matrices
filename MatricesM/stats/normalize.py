def normalize(mat,col=None,inplace=True,zerobound=12,dec=True,ret=False):
    
    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    col = feats.index(col)+1 if isinstance(col,(tuple,str)) else col
    
    if not inplace:
        if col==None:
            temp = mat.copy
            r = mat.ranged()

            valid_col_indices = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
            
            feats = mat.features.labels
            if mat.features.level == 1:
                feats = [row[0] for row in feats]

            for i in valid_col_indices:
                current_range = r[feats[i]]
                mn,mx = current_range[0],current_range[1]
                
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
            
            if dec:
                #Re-declare column dtypes
                temp.fix_coldtypes(valid_col_indices)

            return temp
        
        else:
            if isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't normalize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            temp = mat.copy
            r = mat.ranged(col,get=0)
            mn,mx = r[0],r[1]

            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")
            
            col -= 1
            i = 0 #Index
            while True:#Loop through the column
                try:
                    while i<mat.dim[0]:
                        temp._matrix[i][col] = (temp._matrix[i][col]-mn)/(mx-mn)
                        i+=1
                except:#Value was invalid
                    i+=1
                    continue
                else:
                    break

            if dec:
                #Re-declare column dtypes
                temp.fix_coldtypes(col)
            
            return temp
        
    else:
        if col==None:
            r = mat.ranged()
            valid_col_indices = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]

            feats = mat.features.labels
            if mat.features.level == 1:
                feats = [row[0] for row in feats]

            for i in valid_col_indices:
                current_range = r[feats[i]]
                mn,mx = current_range[0],current_range[1]
                
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

            r = mat.ranged(col,get=0)
            mn,mx = r[0],r[1]
            col-=1 
            valid_col_indices = col

            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")

            j=0 #Index
            while True:#Loop through the column
                try:
                    while j<mat.dim[0]:
                        mat._matrix[j][col] = (mat._matrix[j][col]-mn)/(mx-mn)
                        j+=1
                except:#Value was invalid
                    j+=1
                    continue
                else:
                    break

        if dec:
            #Re-declare column dtypes
            mat.fix_coldtypes(valid_col_indices)

        if ret:
            return mat