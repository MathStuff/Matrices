def sdev(mat,col,population,get,obj,dFrame):
    from MatricesM.customs.objects import null

    d0,d1 = mat.dim
    feats = mat.features[:]

    if isinstance(col,str):
        col=feats.index(col)+1
    if d0<=1:
        raise ValueError("Not enough rows")
    if not population in [0,1]:
        raise ValueError("'population' should be either 0 or 1")

    #All valid columns
    if col==None:
        sd={}
        avgs=mat.mean()
        valid_names = list(avgs.keys())
        valid_col_inds = [i for i in range(d1) if feats[i] in valid_names]
        fi = 0
        for i in valid_col_inds:
            t=0 #Total
            ind=0 #Row index
            valids=0 #How many valid elements were in the column
            mm = mat._matrix
            if avgs[valid_names[fi]]==null: #Invalid column mean
                sd[feats[i]]=null
                continue
                
            while True:#Loop through the column
                try:
                    while ind<d0:
                        value = mm[ind][i]
                        t+=(value-avgs[valid_names[fi]])**2
                        valids+=1
                        ind+=1
                except:#Value was invalid
                    ind+=1
                    continue
                else:
                    if valids!=0 and not (valids==1 and population==0):
                        sd[feats[i]]=(t/(valids-1+population))**(1/2)
                    else:#No valid values found
                        sd[feats[i]]=null
                    break
            fi+=1
    #Single column 
    else:
        try:
            assert col>0 and col<=d1
        except AssertionError:
            print("Col parameter is not valid")
        else:
            sd={}
            a = mat.mean(col,get=0)
            if a in [null,None]:
                raise ValueError(f"Can't get the mean of column{col}")
            t=0 #Total
            ind=0 #Index
            valids=0 #How many valid elements were in the column
            mm = mat._matrix
            while True:#Loop through the column
                try:
                    while ind<d0:
                        value = mm[ind][col-1]
                        t+=(value-a)**2
                        valids+=1
                        ind+=1
                except:#Value was invalid
                    ind+=1
                    continue
                else:
                    if valids!=0 and not (valids==1 and population==0):
                        sd[feats[col-1]]=(t/(valids-1+population))**(1/2)
                    else:#No valid values found
                        sd[feats[col-1]]=null
                    break

    #Return a matrix
    if get==2:
        cols = list(sd.keys())
        sdevs = [i for i in sd.values()]
        cdtypes = [complex] if any([1 if isinstance(val,complex) else 0 for val in sdevs]) else [float]
        return obj((len(cols),1),sdevs,features=["Standart_Deviation"],dtype=dFrame,coldtypes=cdtypes,index=cols,indexname="Column")
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