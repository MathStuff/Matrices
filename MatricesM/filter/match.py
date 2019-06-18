def _match(mat,reg,cols=None,retrow=None,obj=None):
    import re
    #Choose all columns if None given
    if cols == None:
        cols = [i for i in mat.features]
    #Column number given, change it to column name
    if isinstance(cols,int):
        if cols>mat.dim[1] or cols<1:
            raise IndexError(f"{cols} can't be used as column number. Should be in the range from 1 to column amount")
        cols = mat.features[cols-1]

    #Search all columns
    if isinstance(cols,(list,tuple)):
        m = mat.matrix
        feats = mat.features
        #Assert list
        cols = list(cols)
        #Replace non string values with strings
        for i in range(len(cols)):
            j = cols[i]
            #Column name not given
            if not isinstance(j,str):
                #Column number given
                if isinstance(j,int):
                    cols[i] = feats[j-1]
                else:
                    raise TypeError(f"{j} can't be used as column number/name")
            #Column doesn't exist
            elif not j in feats:
                raise NameError(f"{j} isn't a column name")

        #Return a dictionary
        if not retrow:
            results = {i:[] for i in cols}
            for i in range(mat.dim[0]):
                for j in range(mat.dim[1]):
                    match = re.findall(reg,str(m[i][j]))
                    if len(match)>0:
                        results[feats[j]].append((i,match))
            return results
        
        #Return rows in a matrix
        temp = []
        for i in range(mat.dim[0]):
            for j in range(mat.dim[1]):
                match = re.findall(reg,str(m[i][j]))
                if len(match)>0:
                    temp.append(m[i])
        return obj(listed=temp,features=feats,dtype=mat.dtype,coldtypes=mat.coldtypes,decimal=mat.decimal)

    #Search given column
    elif isinstance(cols,str):
        #Return a column matrix
        if not retrow:
            results = []
            col = mat.col(cols,0)
            for i in range(mat.dim[0]):
                match = re.findall(reg,str(col[i]))
                if len(match)>0:
                    results.append([(i,match)])
            return obj(listed=results,features=[cols],dtype=mat.dtype,coldtypes=[tuple])
        
        #Return rows in a matrix
        temp = []
        col = mat.col(cols,0)
        m = mat.matrix
        for i in range(mat.dim[0]):
            match = re.findall(reg,str(col[i]))
            if len(match)>0:
                temp.append(m[i])

        return obj(listed=temp,features=mat.features,dtype=mat.dtype,coldtypes=mat.coldtypes,decimal=mat.decimal)
        












