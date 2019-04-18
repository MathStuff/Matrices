def minor(mat,row=None,col=None):
    try:
        assert row!=None and col!=None
        assert row<=mat.dim[0] and col<=mat.dim[1]
        assert row>0 and col>0
    except AssertionError:
        print("Bad arguments")
    else:
        temp=mat.copy
        if temp.dim[0]==1 and temp.dim[1]==1:
            return temp            
        if not temp.dim[0]<1:   
            temp.remove(row=row)
        if not temp.dim[1]<1: 
            temp.remove(col=col)
        return temp