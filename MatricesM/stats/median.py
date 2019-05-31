def median(mat,col=None):
    if isinstance(col,str):
        col=mat.features.index(col)+1
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
            r = [j for j in rows if isinstance(j,(int,float))]
            n=sorted(r)[mat.dim[0]//2]
            
            if len(feats)!=0 and isinstance(feats,list):
                meds[feats[i-1]]=n
            elif len(feats)==0:
                meds["Col "+str(i)]=n
            else:
                meds[feats]=n
            i+=1
    except Exception as err:
        print("Error getting median:\n\t\t",err)
    else:
        return meds