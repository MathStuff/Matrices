def stdize(mat,col=None,inplace=True,zerobound=12):
    """
    Standardization to get mean of 0 and standard deviation of 1

    col : int>=1|str ; column number or column name
    inplace : boolean ; True to apply changes to matrix, False to return a new matrix
    zerobound : integer ; limit of the decimals after dot to round the sdev to be considered 0
    
    float dtype is recommended for better printing results
    """
    if not inplace:
        if col==None:
            temp = mat.copy
            mean = list(mat.mean().values())
            sd = list(mat.sdev().values())
            
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
            
            valid_col_indeces = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]

            statind = 0
            for i in valid_col_indeces:
                m,s = mean[statind],sd[statind]

                for j in range(mat.dim[0]):
                    temp._matrix[j][i] = (temp._matrix[j][i]-m)/s

                statind += 1

            return temp
        
        else:
            if isinstance(col,str):
                if col not in mat.features:
                    raise ValueError("No column named {name}".format(name=col))
                else:
                    col = mat.features.index(col)+1
            elif isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")
            else:
                raise TypeError("col parameter only accepts column number as an integer or column name as a string")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't normalize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            temp = mat.col(col)
            mean = list(mat.mean(col).values())[0]
            sd = list(mat.sdev(col).values())[0]
            
            if round(sd,zerobound)==0:
                raise ZeroDivisionError("Standard deviation of 0")
            col-=1    
            for i in range(temp.dim[0]):
                temp._matrix[i][col] = (temp._matrix[i][col]-mean)/sd
                        
            return temp

    else:
        if col==None:
            mean = list(mat.mean(col).values())
            sd = list(mat.sdev(col).values())
            
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
            
            valid_col_indeces = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
            
            statind = 0
            for i in valid_col_indeces:
                m,s = mean[statind],sd[statind]
                for j in range(mat.dim[0]):
                    mat._matrix[j][i] = (mat._matrix[j][i]-m)/s
                statind += 1

        else:
            if isinstance(col,str):
                if col not in mat.features:
                    raise ValueError("No column named {name}".format(name=col))
                else:
                    col = mat.features.index(col)+1

            elif isinstance(col,int):
                if not col>=1 and col<=mat.dim[1]:
                    raise IndexError("Not a valid column number")

            else:
                raise TypeError("col parameter only accepts column number as an integer or column name as a string")

            if not mat.coldtypes[col-1] in [float,int]:
                raise TypeError("Can't standardize column of type {typename}".format(typename=mat.coldtypes[col-1]))

            mean = list(mat.mean(col).values())[0]
            sd = list(mat.sdev(col).values())[0]
            
            if round(sd,zerobound)==0:
                raise ZeroDivisionError("Standard deviation of 0")

            col-=1  
            for i in range(mat.dim[0]):
                mat._matrix[i][col] = (mat._matrix[i][col]-mean)/sd
