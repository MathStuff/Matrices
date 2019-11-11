def iqr(mat,col,as_quartiles,get,obj,dFrame):
    from MatricesM.customs.objects import Label
    nullobj = mat.DEFAULT_NULL

    if isinstance(col,str):
        col = mat.features.index(col)+1
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")

    if mat._dfMat:
        temp = mat.copy
        dts = mat.coldtypes[:]
        feats = mat.features.labels
        if mat.features.level == 1:
            feats = [row[0] for row in feats]
        j=0
        if col==None:
            for i in range(len(dts)):
                if not dts[i] in [float,int]:
                    temp.remove(col=i+1-j)
                    del feats[i-j]
                    j+=1
        else:
            assert col>=1 and col<=temp.dim[1]
            if dts[col-1] not in [float,int]:
                raise TypeError(f"Can't use {dts[col-1]} dtype of column:{mat.features[col-1]} to calculate interquartile range")
            else:
                temp = temp[:,col-1]
                feats = feats[col-1]
        temp = temp.t
    else:
        if col==None:
            temp = mat.t
            feats = mat.features.labels
            if mat.features.level == 1:
                feats = [row[0] for row in feats]
        else:
            assert col>=1 and col<=mat.dim[1]
            temp = mat[:,col-1].t
            feats = mat.features.labels[col-1]
            if mat.features.level == 1:
                feats = feats[0]
            
    iqr={}
    qmeds={}
    for rows in range(temp.dim[0]):
        r = sorted([i for i in temp.matrix[rows] if isinstance(i,(int,float))])
        valid_length = len(r)
        #Not enough values
        if valid_length <= 1:
            iqr[feats[rows]]=nullobj
            qmeds[feats[rows]]=[nullobj,nullobj,nullobj]
            continue

        low=r[:valid_length//2]
        low=low[len(low)//2]
        
        up=r[valid_length//2:]
        up=up[len(up)//2]

        if len(feats)!=0 and isinstance(feats,list):
            iqr[feats[rows]]=up-low
            qmeds[feats[rows]]=[low,mat.median(col)[feats[rows]],up]
            
        else:
            iqr[feats]=up-low
            qmeds[feats]=[low,mat.median(col)[feats],up]

    #Return a matrix
    if get==2:
        name = 1 if as_quartiles else 0
        dic = qmeds if as_quartiles else iqr
        cols = list(dic.keys())
        return obj((len(cols),1),[[i] for i in dic.values()],features=[["IQR","Quartiles"][name]],dtype=dFrame,coldtypes=[[float,list][name]],index=Label(cols,mat.features.names[:]))
    #Return a dictionary
    elif get==1:
        if as_quartiles:
            return qmeds
        return iqr
    #Return a list
    else:
        if as_quartiles:
            items=list(qmeds.values())
            if len(items)==1:
                return items[0]
            
            if col==None:
                return items
            return items[col-1]
        else:
            items=list(iqr.values())
            if len(items)==1:
                return items[0]
            
            if col==None:
                return items
            return items[col-1]