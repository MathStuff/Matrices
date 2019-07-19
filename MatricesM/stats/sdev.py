def sdev(mat,col,population,get,obj,dFrame):

    if isinstance(col,str):
        col=mat.features.index(col)+1
        
    if mat.dim[0]<=1:
        raise ValueError("Not enough rows")
    if not population in [0,1]:
        raise ValueError("'population' should be either 0 or 1")
    if col==None:
        sd={}
        avgs=mat.mean()
        feats = list(avgs.keys())
        d = [i for i in range(mat.dim[1]) if mat.features[i] in feats]
        fi = 0
        for i in d:
            t=0 #Total
            ind=0 #Index
            vals=0 #How many valid elements were in the column
            while True:#Loop through the column
                try:
                    while ind<mat.dim[0]:
                        t+=(mat._matrix[ind][i]-avgs[feats[fi]])**2
                        ind+=1
                        vals+=1
                except:#Value was invalid
                    ind+=1
                    continue
                else:
                    if vals!=0 and not (vals==1 and population==0):
                        sd[mat.features[i]]=(t/(vals-1+population))**(1/2)
                    else:#No valid values found
                        sd[mat.features[i]]=None
                    break
            fi+=1
            
    else:
        try:
            assert col>0 and col<=mat.dim[1]
        except AssertionError:
            print("Col parameter is not valid")
        else:
            sd={}
            mn = mat.mean(col)
            if mn == None:
                raise ValueError(f"Can't get the mean of column{col}")
            a=list(mn.values())[0]
            t=0 #Total
            ind=0 #Index
            vals=0 #How many valid elements were in the column
            while True:#Loop through the column
                try:
                    while ind<mat.dim[0]:
                        t+=(mat._matrix[ind][col-1]-a)**2
                        ind+=1
                        vals+=1
                except:#Value was invalid
                    ind+=1
                    continue
                else:
                    if vals!=0 and not (vals==1 and population==0):
                        sd[mat.features[col-1]]=(t/(vals-1+population))**(1/2)
                    else:#No valid values found
                        sd[mat.features[col-1]]=None
                    break

    #Return a matrix
    if get==2:
        cols = mat.d1 if col==None else 1
        return obj((cols,2),[[i,j] for i,j in sd.items()],features=["Column","Standart_Deviation"],dtype=dFrame,coldtypes=[str,complex],index=None)
    #Return a dictionary
    elif get==1:
        return sd
    #Return a list
    else:
        items=list(sd.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]