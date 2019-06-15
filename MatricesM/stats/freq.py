def freq(mat,col=None,dic=True):
    from collections import Counter
    from MatricesM.errors.errors import MatrixError
    try:
        #Get the parts needed
        #No argument given
        if col==None:
            temp=mat.t
            feats=mat.features[:]
            r=mat.dim[1]
        #Column index or name given
        else:
            if isinstance(col,str):
                col=mat.features.index(col)+1
            assert col>=1 and col<=mat.dim[1]
            temp=mat[:,col-1].t
            feats=mat.features[col-1]
            r=1

        res={}

        #Iterate over the transposed rows
        for rows in range(r):
            a=dict(Counter(temp.matrix[rows]))

            #Add to dictionary
            if col!=None:
                res[feats]=a
            else:
                res[feats[rows]]=a
    except Exception as e:
        raise MatrixError(f"Error in freq: {e}")
    else:
        if dic:
            return res
        
        items=list(res.values())
        if len(items)==1:
            return items[0]
        
        if col==None:
            return items
        return items[col-1]