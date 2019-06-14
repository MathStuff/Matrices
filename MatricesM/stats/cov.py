def cov(mat,col1=None,col2=None,population=1,obj=None):
    #Change column names to indices
    for i in [col1,col2]:
        if isinstance(i,str):
            i=mat.features.index(i)+1
    #Assert types for columns
    if not (isinstance(col1,int) and isinstance(col2,int)) and (col1!=None and col2!=None):
        raise TypeError("col1 and col2 should be integers or column names or both None")
    #Assert population value
    if population not in [0,1]:
        raise ValueError("population should be 0 for samples, 1 for population")
    #Columns given
    if (col1!=None and col2!=None):
        if not (col1>=1 and col1<=mat.dim[1] and col2>=1 and col2<=mat.dim[1] ):
            raise ValueError("col1 and col2 are not in the valid range")

        c1,c2 = mat.col(col1,0),mat.col(col2,0)
        m1,m2 = mat.mean(col1,asDict=0),mat.mean(col2,asDict=0)
        try:
            s = sum([(c1[i]-m1)*(c2[i]-m2) for i in range(len(c1))])
        except TypeError:
            raise TypeError("Error getting covariance, replace invalid values first")
        return s/(len(c1)-1+population)
    #Covariance matrix
    else:
        #Dataframe's float or int value column indices and names
        validinds = [i for i in range(mat.dim[1]) if mat.coldtypes[i] in [float,int]]
        validfeats = [mat.features[i] for i in validinds]
        #Create the base
        covmat = obj(len(validfeats),fill=0)
        #Diagonals are variance values
        vrs = mat.var()
        for i in range(covmat.dim[0]):
            covmat[i,i] = vrs[validfeats[i]]
        #Calculation
        m = 0
        for i in validinds[:]:
            validinds.remove(i)
            n = m+1
            for j in validinds:
                c1,c2 = mat.col(m+1,0),mat.col(n+1,0)
                m1,m2 = mat.mean(validfeats[m],asDict=0),mat.mean(validfeats[n],asDict=0)
                val = sum([(c1[a]-m1)*(c2[a]-m2) for a in range(len(c1))])/(len(c1)-1+population)

                covmat._matrix[m][n] = val
                covmat._matrix[n][m] = val
                n+=1
            m+=1
        return covmat