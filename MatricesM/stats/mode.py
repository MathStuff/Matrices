def mode(mat,col=None):
    """
    Returns the columns' most repeated elements in a dictionary
    col:integer>=1 and <=amount of columns
    """
    try:
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
        
        from MatricesM.stats.freq import freq
        
        freqs = freq(mat,col)
        mode = {}
        
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
                
    except Exception as e:
        print("Error in mode:\n\t",e)
        return None
    else:
        return mode