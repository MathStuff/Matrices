def normalize(mat,col=None,inplace=True,zerobound=12):
    """
    Normalizes the data to be valued between 0 and 1
    
    col : int>=1|str ; column number or column name
    inplace : boolean ; True to apply changes to matrix, False to return a new matrix
    zerobound : integer ; limit of the decimals after dot to round the max-min of the columns to be considered 0

    float dtype is recommended for better printing results
    """
    if not inplace:
        if col==None:
            temp = mat.copy
            r = list(mat.ranged().values())
            valid_col_indeces = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]

            for i in valid_col_indeces:
                mn,mx = r[i][0],r[i][1]
                
                if round(mx-mn,zerobound) == 0:
                    raise ZeroDivisionError("Max and min values are the same")
                    
                for j in range(mat.dim[0]):
                    temp._matrix[j][i] = (temp._matrix[j][i]-mn)/(mx-mn)
                    
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
            r = list(temp.ranged().values())[0]
            mn,mx = r[0],r[1]
            
            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")

            for i in range(temp.dim[0]):
                temp._matrix[i][0] = (temp._matrix[i][0]-mn)/(mx-mn)
                        
            return temp
        
    else:
        if col==None:
            r = list(mat.ranged().values())
            valid_col_indeces = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
            for i in valid_col_indeces:
                mn,mx = r[i][0],r[i][1]
                
                if round(mx-mn,zerobound) == 0:
                    raise ZeroDivisionError("Max and min values are the same")
                    
                for j in range(mat.dim[0]):
                    mat._matrix[j][i] = (mat._matrix[j][i]-mn)/(mx-mn)

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

            r = list(mat.ranged().values())[col-1]
            mn,mx = r[0],r[1]
            
            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")
            col-=1    
            for i in range(mat.dim[0]):
                mat._matrix[i][col] = (mat._matrix[i][col]-mn)/(mx-mn)
