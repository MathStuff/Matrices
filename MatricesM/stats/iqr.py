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
                if dts[i] == str:
                    temp.remove(col=i+1-j)
                    del feats[i-j]
                    j+=1
        else:
            assert col>=1 and col<=temp.dim[1]
            if dts[col-1] == str:
                raise TypeError(f"Can't use str dtype (column{col}) to calculate interquartile range")
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
    i=1
    for rows in temp.matrix:
        r = [i for i in rows if isinstance(i,(int,float))]
        low=sorted(r)[:temp.dim[1]//2]
        low=low[len(low)//2]
        
        up=sorted(r)[temp.dim[1]//2:]
        up=up[len(up)//2]
        
        if len(feats)!=0 and isinstance(feats,list):
            iqr[feats[i-1]]=up-low
            qmeds[feats[i-1]]=[low,mat.median(col)[feats[i-1]],up]
        elif len(feats)==0:
            iqr["Col "+str(i)]=up-low
            qmeds["Col "+str(i)]=[low,mat.median(col)["Col "+str(i)],up]
        else:
            iqr[feats]=up-low
            qmeds[feats]=[low,mat.median(col)[feats],up]
        i+=1


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