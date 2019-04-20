def setDim(mat,d):
    """
    Set the dimension to be a list if it's an integer
    """
    if isinstance(d,int):
        if d>=1:
            mat._Matrix__dim=[d,d]
        else:
            mat._Matrix__dim=[0,0]
    elif isinstance(d,list) or isinstance(d,tuple):
        if len(d)!=2:
            mat._Matrix__dim=[0,0]
        else:
            if isinstance(d[0],int) and isinstance(d[1],int):
                if d[0]>0 and d[1]>0:
                    mat._Matrix__dim=d[:]
                else:
                    mat._Matrix__dim=[0,0]
    elif d==None:
        mat._Matrix__dim=[0,0] 