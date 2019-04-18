def sdev(mat,col=None,population=1,asDict=True):
    """
    Standard deviation of the columns
    col:integer>=1
    population: 1 for σ, 0 for s value (default 1)
    asDict: True|False ; Wheter or not to return a dictionary with features as keys standard deviations as values, if set to False:
        1) If there is only 1 column returns the value as it is
        2) If there are multiple columns returns the values in order in a list
    """
    try:
        assert mat.dim[0]>1
        assert population in [0,1]
        if col==None:
            sd={}
            avgs=mat.mean()
            for i in range(mat.dim[1]):
                e=sum([(mat._matrix[j][i]-avgs[mat.features[i]])**2 for j in range(mat.dim[0])])
                sd[mat.features[i]]=(e/(mat.dim[0]-1+population))**(1/2)
                
        else:
            try:
                assert col>0 and col<=mat.dim[1]
            except AssertionError:
                print("Col parameter is not valid")
            else:
                sd={}
                a=list(mat.mean(col).values())[0]
    
                e=sum([(mat.matrix[i][col-1]-a)**2 for i in range(mat.dim[0])])
                sd[mat.features[col-1]] = (e/(mat.dim[0]-1+population))**(1/2)
    except:
        print("Can't get standard deviation")
        
    else: 
        if asDict:
            return sd
        
        items=list(sd.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]