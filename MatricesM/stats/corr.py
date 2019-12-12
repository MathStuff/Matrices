def _corr(mat,col1,col2,population,temp,method,Labelobj):
    for i in [col1,col2]:
        if isinstance(i,str):
            i=mat.features.index(i)+1
    
    if not (( isinstance(col1,int) and isinstance(col2,int) ) or (col1==None and col2==None)):
        raise TypeError("'col1' and 'col2' should be integers | both None | column names")
        
    if not population in [0,1]:
        raise ValueError("'population' should be 0 for samples, 1 for population")
    
    if not method in ["pearson","kendall","spearman"]:
        raise ValueError("'method' should be one of : pearson, kendall, spearman")

    if col1!=None and col2!=None:
        if not (col1>=1 and col1<=mat.dim[1] and col2>=1 and col2<=mat.dim[1]):
            raise ValueError("'col1' and 'col2' are not in the valid range")
    
    if col1==None and col2==None:
        if mat._dfMat:
            dts = mat.coldtypes
            j=0
            for i in range(len(dts)):
                if not dts[i] in [float,int]:
                    temp.remove(row=i+1-j,col=i+1-j)
                    j+=1

        feats,tfeats = mat.features.labels,temp.features.labels
        if mat.features.level == 1:
            feats,tfeats = [row[0] for row in feats],[row[0] for row in tfeats]

        availablecols = [i for i in range(mat.dim[1]) if feats[i] in tfeats]
        availablefeats = [feats[i] for i in availablecols]
        
        d0 = mat.d0
        m = 0
        #Pearson correlation coefficients
        if method == "pearson":
            sd = mat.sdev(population=population)
            for i in availablecols[:]:
                availablecols.remove(i)
                n = m+1
                for j in availablecols:
                    cv = mat.cov(i+1,j+1,population=population)
                    s = sd[feats[i]]*sd[feats[j]]
                    if s == 0:
                        raise ZeroDivisionError("Standard deviation of 0")
                    val =  cv/s
                    temp._matrix[m][n] = val
                    temp._matrix[n][m] = val
                    n+=1
                m+=1
        #Spearman correlation coefficients
        elif method == "spearman":
            ranks = mat.ranked(get=2)
            den = d0*(d0**2 - 1)
            for i in availablecols[:]:
                availablecols.remove(i)
                n = m+1
                for j in availablecols:
                    p = 1-((6*((ranks[i]["Rank"]-ranks[j]["Rank"])**2).sum(get=0))/den)
                    temp._matrix[m][n] = p
                    temp._matrix[n][m] = p
                    n+=1
                m+=1
        #Kendall rank correlation coefficients
        else:
            return None
            for i in availablecols[:]:
                availablecols.remove(i)
                n = m+1
                for j in availablecols:
                    table = mat.col(i+1).concat(mat.col(j+1),returnmat=True).sortBy(availablefeats[i],returnmat=True).ranked(availablefeats[j],get=0)
                    C = [[1 if num>table[i] else 0 for num in table[i+1:]].count(1) for i in range(d0)]
                    D = [d0-C[i]-1 for i in range(d0)]

                    Csum,Dsum = sum(C),sum(D)
                    t = (Csum-Dsum)/(Csum+Dsum)
                    temp._matrix[m][n] = t
                    temp._matrix[n][m] = t
                    n+=1
                m+=1

        temp.index = Labelobj(availablefeats,mat.features.names[:])
        return temp
    
    else:
        if method == "pearson":
            sd = mat.sdev(population=population,get=0)
            if 0 in sd:
                raise ZeroDivisionError("Standard deviation of 0")
            return mat.cov(col1,col2,population=population)/(sd[col1-1]*sd[col2-1])

        elif method == "spearman":
            return 1-((6*((mat.ranked(col1,get=2)["Rank"]-mat.ranked(col2,get=2)["Rank"])**2).sum(get=0))/d0*(d0**2 - 1))
        
        else:
            return None