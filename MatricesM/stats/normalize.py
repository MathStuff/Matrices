def normalize(mat,col=None,inplace=True,zerobound=12):
    """
    Original matrix should be an FMatrix or there will be printing issues when "inplace" is used.
    Use name=name.floatForm to get better results
     
    Normalizes the data to be valued between 0 and 1
    col : int>=1 ; column number
    inplace : boolean ; True to apply changes to matrix, False to return a new matrix
    zerobound : integer ; limit of the decimals after dot to round the max-min of the columns to be considered 0
    """
    if not inplace:
        if col==None:
            temp = mat.floatForm
            r = list(mat.ranged().values())
            
            for i in range(mat.dim[1]):
                mn,mx = r[i][0],r[i][1]
                
                if round(mx-mn,zerobound) == 0:
                    raise ZeroDivisionError("Max and min values are the same")
                    
                for j in range(mat.dim[0]):
                    temp._matrix[j][i] = (temp._matrix[j][i]-mn)/(mx-mn)
                    
            return temp
        
        elif isinstance(col,int):
            if not col>=1 and col<=mat.dim[1]:
                return None
            
            temp = mat.floatForm.col(col)
            r = list(temp.ranged().values())[0]
            mn,mx = r[0],r[1]
            
            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")
            col-=1    
            for i in range(temp.dim[0]):
                temp._matrix[i][col] = (temp._matrix[i][col]-mn)/(mx-mn)
                        
            return temp
        
        else:
            return None
        
    else:
        if col==None:
            r = list(mat.ranged().values())
            
            for i in range(mat.dim[1]):
                mn,mx = r[i][0],r[i][1]
                
                if round(mx-mn,zerobound) == 0:
                    raise ZeroDivisionError("Max and min values are the same")
                    
                for j in range(mat.dim[0]):
                    mat._matrix[j][i] = (mat._matrix[j][i]-mn)/(mx-mn)

        elif isinstance(col,int):
            if not col>=1 and col<=mat.dim[1]:
                return None
            
            r = mat.ranged(col)
            mn,mx = r[0],r[1]
            
            if round(mx-mn,zerobound) == 0:
                raise ZeroDivisionError("Max and min values are the same")
            col-=1    
            for i in range(mat.dim[0]):
                mat._matrix[i][col] = (mat._matrix[i][col]-mn)/(mx-mn)

        else:
            return None    