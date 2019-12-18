def _match(mat,reg,cols=None,retrow=None,obj=None,lvl=1):
    import re
    from ..customs.objects import Label
    
    #Choose all columns if None given
    if cols == None:
        raise ValueError("Can't match values in all columns at once")
    #Column number given, change it to column name
    if isinstance(cols,tuple):
        colind = mat.features.labels.index(cols)

    if isinstance(cols,int):
        if cols>mat.dim[1] or cols<1:
            raise IndexError(f"{cols} can't be used as column number. Should be in the range from 1 to column amount")
        colind = cols-1

    #Search given column
    elif isinstance(cols,str):
        #Return a column matrix
        colind = mat.features.get_level(lvl).index(cols)

    results = []
    labels = mat.features.get_level(lvl)
    rows = []
    col = mat.col(colind+1,0)
    mm = mat.matrix

    for i in range(mat.dim[0]):
        match = re.findall(reg,str(col[i]))
        if len(match)>0:
            rows.append(i)
            if not retrow:
                results.append([(i,match)])
            else:
                results.append(mm[i][:])

    newfeats = mat.features[colind] if not retrow else mat.features[:]
    newcolds = [tuple] if not retrow else mat.coldtypes[:]

    return obj(data=results,
                features=newfeats,
                dtype=mat.dtype,
                coldtypes=newcolds,
                index=mat.index[rows])
    

    oldinds = mat.index.labels
    foundinds = Label([oldinds[i] for i in inds],mat.index.names) if mat._dfMat else Label()

    return obj(data=temp,features=mat.features,dtype=mat.dtype,coldtypes=mat.coldtypes,
                decimal=mat.decimal,index=foundinds)
        












