def iqr(mat,col=None,as_quartiles=False,asDict=True):
    """
    Returns the interquartile range(IQR)
    col:integer>=1 and <=column amount
    
    as_quartiles:
        True to return dictionary as:
            {Column1=[First_Quartile,Median,Third_Quartile],Column2=[First_Quartile,Median,Third_Quartile],...}
        False to get iqr values(default):
            {Column1=IQR_1,Column2=IQR_2,...}
            
    asDict: True|False ; Wheter or not to return a dictionary with features as keys iqr's as values, if set to False:
        1) If there is only 1 column returns the value as it is
        2) If there are multiple columns returns the values in order in a list
            
    Usage:
        self.iqr() : Returns a dictionary with iqr's as values
        self.iqr(None,True) : Returns a dictionary where the values are quartile medians in lists
        self.iqr(None,True,False) : Returns a list of quartile medians in lists
        self.iqr(None,False,False) : Returns a list of iqr's
        -> Replace "None" with any column number to get a specific column's iqr
    """
    
    try:
        if col==None:
            temp=mat.t
            feats=mat.features[:]
        else:
            assert col>=1 and col<=mat.dim[1]
            temp=mat.subM(1,mat.dim[0],col,col).t
            feats=mat.features[col-1]
                
        iqr={}
        qmeds={}
        i=1
        for rows in temp.matrix:
            low=sorted(rows)[:mat.dim[0]//2]
            low=low[len(low)//2]
            
            up=sorted(rows)[mat.dim[0]//2:]
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
    except Exception as err:
        print("Error getting iqr: ",err)
    else:
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