def freq(mat,col=None):
    try:
        if col==None:
            temp=mat.t
            feats=mat.features[:]
        else:
            if isinstance(col,str):
                col=mat.features.index(col)+1
            assert col>=1 and col<=mat.dim[1]
            temp=mat[:,col-1].t
            feats=mat.features[col-1]

        res={}
        if col==None:
            r=mat.dim[1]
        else:
            r=1

        for rows in range(r):
            a={}
            for els in temp.matrix[rows]:
                if els not in a.keys():
                    a[els]=1
                else:
                    a[els]+=1
            if col!=None:
                res[feats]=a
            else:
                res[feats[rows]]=a
    except:
        print("Bad indeces in freq method")
    else:
        return res