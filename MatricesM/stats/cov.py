def cov(mat,col1,col2,population,obj,dFrame):
    #Change column names to indices
    if isinstance(col1,str):
        col1=mat.features.index(col1)+1
    if isinstance(col2,str):
        col2=mat.features.index(col2)+1
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
        m1,m2 = mat.mean(col1,get=0),mat.mean(col2,get=0)
        try:
            s = sum([(c1[i]-m1)*(c2[i]-m2) for i in range(len(c1))])
        except TypeError:
            raise TypeError("Error getting covariance, replace invalid values first")
        return s/(len(c1)-1+population)
    #Covariance matrix
    else:
        d0,d1 = mat.dim
        colds,feats = mat.coldtypes,mat.features.labels
        if mat.features.level == 1:
            feats = [row[0] for row in feats]
        #Dataframe's float or int value column indices and names
        validinds = [i for i in range(d1) if colds[i] in [float,int]]
        validfeats = [feats[i] for i in validinds]
        #Create the base
        covmat = obj(len(validfeats),fill=0)
        #Diagonals are variance values
        vrs = mat.var()
        for i in range(covmat.dim[0]):
            covmat[i,i] = vrs[validfeats[i]]
        #Calculation
        m = 0
        means = mat.mean()
        for i in validinds[:]:
            validinds.remove(i)
            n = m+1
            c1,m1 = mat.col(i+1,0),means[validfeats[i]]
            for j in validinds:
                c2 = mat.col(j+1,0)
                m2 = means[validfeats[j]]
                val = sum([(c1[a]-m1)*(c2[a]-m2) for a in range(d0)])/(d0-1+population)
                covmat._matrix[m][n] = val
                covmat._matrix[n][m] = val
                n+=1
            m+=1
        covmat.index = validfeats
        covmat.features = validfeats
        covmat.dtype = dFrame
        return covmat