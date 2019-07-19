def mode(mat,col,get,obj,dFrame):

    if isinstance(col,str):
        col=mat.features.index(col)+1
    if col != None:
        if col<=0 or col>mat.d1:
            raise IndexError(f"Column index is out of range, expected range: [1,{mat.d1}]")
    #Set feature name and the matrix to use dependent on the column desired
    if col==None:
        feats=mat.features[:]
    else:
        assert col>=1 and col<=mat.dim[1] and isinstance(col,int)
        feats=mat.features[col-1]
    #Set keys in the dictionary which will be returned at the end
    mode={}
    if len(feats)!=0 and isinstance(feats,list):
        for fs in feats:
            mode[fs]=None
    elif len(feats)==0:
        for fs in range(mat.dim[1]):
            mode["Col "+str(fs+1)]=None
        
    freqs = mat.freq(col)
    
    #Check which element(s) repeat most
    for k,v in freqs.items():
        repeats = []
        vmax = max(list(v.values()))
        for i in v.keys():
            if v[i] == vmax:
                repeats.append(i)
        
        if len(repeats)==1:
            repeats=repeats[0]
        elif len(repeats)==len(list(v.keys())):
            mode[k] = {"All":vmax}
            continue
        else:
            repeats=tuple(sorted(repeats))
        mode[k] = {repeats:vmax}

    #Return a tuple of matrices
    if get==2:
        return tuple([obj((len(list(c.keys())),2),[[i,j] for i,j in c.items()],features=[feat+" Mode(s)","Frequency"],dtype=dFrame,coldtypes=[str,int],index=None) for feat,c in mode.items()])
    #Return a dictionary
    elif get==1:
        return mode
    #Return a list
    else:
        items=list(mode.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]