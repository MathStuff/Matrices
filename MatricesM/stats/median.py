def median(mat,col,get,obj,dFrame):
    from ..customs.objects import Label

    nullobj = mat.DEFAULT_NULL

    feats = mat.features.labels
    if mat.features.level == 1:
        feats = [row[0] for row in feats]

    col = feats.index(col)+1 if isinstance(col,(tuple,str)) else col

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
                raise TypeError(f"Can't use {dts[col-1]} dtype of column:{mat.features[col-1]} to calculate median")
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
            
    meds={}
    tm = temp.matrix
    for rows in range(temp.dim[0]):
        r = [j for j in tm[rows] if isinstance(j,(int,float))]
        length = len(r)
        #Not enough values
        if length <=1:
            n = nullobj
        else:
            n=sorted(r)[length//2]

        if len(feats)!=0 and isinstance(feats,list):
            meds[feats[rows]]=n
        else:
            meds[feats]=n

    #Return a matrix
    if get == 2:
        cols = list(meds.keys())
        return obj((len(cols),1),[i for i in meds.values()],features=["Median"],dtype=dFrame,coldtypes=[float],index=Label(cols,mat.features.names[:]))
    #Return a dictionary
    elif get == 1:
        return meds
    #Return a list
    else:
        items=list(meds.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]
