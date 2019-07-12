def median(mat,col,get,obj,dFrame):

    if isinstance(col,str):
        col=mat.features.index(col)+1
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")

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
                raise TypeError(f"Can't use {dts[col-1]} dtype of column:{mat.features[col-1]} to calculate median")
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
            
    meds={}
    for rows in range(temp.dim[0]):

        r = [j for j in temp.matrix[rows] if isinstance(j,(int,float))]
        n=sorted(r)[mat.dim[0]//2]
        
        if len(feats)!=0 and isinstance(feats,list):
            meds[feats[rows]]=n
        else:
            meds[feats]=n

    #Return a matrix
    if get == 2:
        cols = mat.d1 if col==None else 1
        return obj((cols,2),[[i,j] for i,j in meds.items()],features=["Column","Median"],dtype=dFrame,coldtypes=[str,float])    
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
