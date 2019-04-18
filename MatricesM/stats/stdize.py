def stdize(mat,col=None,inplace=True,zerobound=12):
    """
    Original matrix should be an FMatrix or there will be printing issues when "inplace" is used.
    Use name=name.floatForm to get better results
    
    Standardization to get mean of 0 and standard deviation of 1
    col : int>=1 ; column number
    inplace : boolean ; True to apply changes to matrix, False to return a new matrix
    zerobound : integer ; limit of the decimals after dot to round the sdev to be considered 0
    """
    if not inplace:
        if col==None:
            temp = mat.floatForm
            mean = list(mat.mean().values())
            sd = list(mat.sdev().values())
            
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
                
            for i in range(mat.dim[1]):
                m,s = mean[i],sd[i]
                for j in range(mat.dim[0]):
                    temp._matrix[j][i] = (temp._matrix[j][i]-m)/s
                    
            return temp
        
        elif isinstance(col,int):
            if not col>=1 and col<=mat.dim[1]:
                return None
            temp = mat.floatForm.col(col)
            mean = list(mat.mean(col).values())[0]
            sd = list(mat.sdev(col).values())[0]
            
            if round(sd,zerobound)==0:
                raise ZeroDivisionError("Standard deviation of 0")
            col-=1    
            for i in range(temp.dim[0]):
                temp._matrix[i][col] = (temp._matrix[i][col]-mean)/sd
                        
            return temp
        
        else:
            return None
 
    else:
        if col==None:
            mean = list(mat.mean(col).values())
            sd = list(mat.sdev(col).values())
            
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
                
            for i in range(mat.dim[1]):
                m,s = mean[i],sd[i]
                for j in range(mat.dim[0]):
                    mat._matrix[j][i] = (mat._matrix[j][i]-m)/s

        elif isinstance(col,int):
            if not col>=1 and col<=mat.dim[1]:
                return None
            mean = list(mat.mean(col).values())[0]
            sd = list(mat.sdev(col).values())[0]
            
            if round(sd,zerobound)==0:
                raise ZeroDivisionError("Standard deviation of 0")
            col-=1  
            for i in range(mat.dim[0]):
                mat._matrix[i][col] = (mat._matrix[i][col]-mean)/sd

        else:
            return None 