def stdize(mat,col=None,inplace=True,zerobound=12,dec=True,ret=False):

    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    col = feats.index(col)+1 if isinstance(col,(tuple,str)) else col
    
    if not inplace:
        if col==None:
            temp = mat.copy
            mean = list(mat.mean().values())
            sd = list(mat.sdev().values())
            
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
            
            valid_col_indices = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]

            statind = 0
            for i in valid_col_indices:
                m,s = mean[statind],sd[statind]
                j=0 #Index
                while True:#Loop through the column
                    try:
                        while j<mat.dim[0]:
                            temp._matrix[j][i] = (temp._matrix[j][i]-m)/s
                            j+=1
                    except:#Value was invalid
                        j+=1
                        continue
                    else:
                        break
                statind += 1
            
            #Re-declare column dtypes
            if dec:
                temp.fix_coldtypes(valid_col_indices)
            
            return temp
        
        else:
            if isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't normalize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            temp = mat.copy
            mean = mat.mean(col,0)
            sd = mat.sdev(col,get=0)
            col -= 1
            if round(sd,zerobound)==0:
                raise ZeroDivisionError("Standard deviation of 0")

            j=0 #Index
            while True:#Loop through the column
                try:
                    while j<mat.dim[0]:
                        temp._matrix[j][col] = (temp._matrix[j][col]-mean)/sd
                        j+=1
                except:#Value was invalid
                    j+=1
                    continue
                else:
                    break  

            #Re-declare column dtypes
            if dec:
                temp.fix_coldtypes(col)
                  
            return temp

    else:
        if col==None:
            mean = list(mat.mean(col).values())
            sd = list(mat.sdev(col).values())
            
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
            
            valid_col_indices = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
            
            statind = 0
            for i in valid_col_indices:
                m,s = mean[statind],sd[statind]
                j=0 #Index
                while True:#Loop through the column
                    try:
                        while j<mat.dim[0]:
                            mat._matrix[j][i] = (mat._matrix[j][i]-m)/s
                            j+=1
                    except:#Value was invalid
                        j+=1
                        continue
                    else:
                        break  
                statind += 1

        else:
            if isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't standardize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            mean = mat.mean(col,0)
            sd = mat.sdev(col,get=0)

            col-=1
            valid_col_indices = 0

            if round(sd,zerobound)==0:
                raise ZeroDivisionError("Standard deviation of 0")
            
            j=0 #Index
            while True:#Loop through the column
                try:
                    while j<mat.dim[0]:
                        mat._matrix[j][col] = (mat._matrix[j][col]-mean)/sd
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
