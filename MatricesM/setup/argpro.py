def _setup(mat,first,implicit,Labelobj,obj,vlist):
    #Whetere or not there are random numbers involved
    randomly_filled = True if mat._matrix in [None,[],{},[[]]] else False
    #Matrix fix
    if first and not implicit:
        mat.setMatrix(mat.dim,mat.initRange,mat._matrix,mat.fill,mat._cMat,mat._fMat)
    
    d0,d1 = mat.dim
    df = mat._dfMat
    dt = mat.dtype
    cdts = mat.coldtypes
    names = mat.features if mat.features != None else []

    #Column names
    if len(names) != d1:
        names = Labelobj([(f"col_{i}",) for i in range(1,d1+1)],[""],implicit=True)

    #Column types
    if not vlist(mat._matrix):
        return None

    if not type(mat.DEFAULT_NULL).__name__ in ["type","null"]:
        raise TypeError("'DEFAULT_NULL' should be a 'type' or 'null' type")

    #Set column dtypes
    #Not enough types given, reset given types
    if len(cdts) != d1:
        if mat.fill == mat.DEFAULT_NULL:
            mat._Matrix__coldtypes = [mat.DEFAULT_NULL for _ in range(d1)]
        elif df:
            from .declare import declareColdtypes
            mat._Matrix__coldtypes = declareColdtypes(mat.matrix,mat.DEFAULT_NULL.__name__)
        else:
            mat._Matrix__coldtypes = [dt]*d1

    cdts = mat.coldtypes

    #Index shouldn't be None
    if mat.index in [[],None]:
        mat._Matrix__index = Labelobj()

    #Apply coldtypes to values in the matrix, set indices, update names
    if df:
        mm = mat.matrix

        #Apply column dtypes to each column's values if they weren't randomly picked
        if not randomly_filled and not implicit:
            def_null_name = mat.DEFAULT_NULL.__name__
            for i in range(d0):
                j=0
                rowcopy = mm[i][:]
                while j<d1:
                    try:
                        cdtype = cdts[j]
                        if cdtype != type:
                            val = rowcopy[j]
                            if type(val).__name__ != def_null_name:
                                rowcopy[j] = cdtype(val)
                        j+=1
                    except:
                        j+=1
                        continue
                mm[i] = rowcopy[:]

        ind = mat._Matrix__index
        
        if isinstance(ind,Labelobj):
            label_len = len(ind)
            if label_len == 0:
                if first:
                    mat._Matrix__index = Labelobj(list(range(d0)),"")
                else:
                    raise IndexError(f"Expected {d0} labels, got {label_len} instead")
            elif label_len == d0:
                mat._Matrix__index = ind[:]
            else:
                raise IndexError(f"Expected {d0} labels, got {label_len} instead")

        elif isinstance(ind,obj):
            if ind.d0 != d0:
                raise ValueError(f"Invalid index matrix; expected {d0} rows, got {ind.d0}")
            
            mat._Matrix__index = Labelobj([tuple(row) for row in ind.matrix],ind.features.get_level(1))

        elif isinstance(ind,(list,tuple)):
            if len(ind) == 0:
                mat._Matrix__index = Labelobj(list(range(d0)),"")
            elif len(ind) != d0:
                raise ValueError(f"Invalid index list; expected {d0} values, got {len(ind)}")
            else:
                mat._Matrix__index = Labelobj(list(ind)[:])
        else:
            raise TypeError(f"Type {type(ind).__name__} can't be used as indices")
        
        mat._matrix = mm

    if not isinstance(names,Labelobj):
        names = Labelobj(names)
    mat._Matrix__features = names
