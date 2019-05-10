def median(mat,col=None):
    """
    Returns the median of the columns
    col:integer>=1 and <=column amount
    """
    try:
        if col==None:
            temp=mat.t
            feats=mat.features
        else:
            assert col>=1 and col<=mat.dim[1]
            temp=mat[:,col-1].t
            feats=mat.features[col-1]
                
        meds={}
        i=1
        for rows in temp.matrix:
            
            n=sorted(rows)[mat.dim[0]//2]
            
            if len(feats)!=0 and isinstance(feats,list):
                meds[feats[i-1]]=n
            elif len(feats)==0:
                meds["Col "+str(i)]=n
            else:
                meds[feats]=n
            i+=1
    except:
        print("Error getting median")
    else:
        return meds