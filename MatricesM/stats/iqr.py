def iqr(mat,col=None,as_quartiles=False,asDict=True):
    if isinstance(col,str):
        col=mat.features.index(col)+1
        
    if mat._dfMat:
        temp = mat.copy
        dts = mat.coldtypes[:]
        feats = temp.features[:]
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
            feats = mat.features[:]
        else:
            assert col>=1 and col<=mat.dim[1]
            temp = mat[:,col-1].t
            feats = mat.features[col-1]
            
    iqr={}
    qmeds={}
    for rows in range(temp.dim[0]):
        r = [i for i in temp.matrix[rows] if isinstance(i,(int,float))]
        low=sorted(r)[:temp.dim[1]//2]
        low=low[len(low)//2]
        
        up=sorted(r)[temp.dim[1]//2:]
        up=up[len(up)//2]
        
        if len(feats)!=0 and isinstance(feats,list):
            iqr[feats[rows]]=up-low
            qmeds[feats[rows]]=[low,mat.median(col)[feats[rows]],up]
            
        else:
            iqr[feats]=up-low
            qmeds[feats]=[low,mat.median(col)[feats],up]


    if asDict:
        if as_quartiles:
            return qmeds
        return iqr
    
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