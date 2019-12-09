def _invert(mat,intform):
    if mat._fMat:
        raise TypeError("~ operator can not be used for non-integer value matrices")
    temp = intform
    m = temp.matrix
    temp._matrix = [[~m[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
    return temp

def _and(mat,other,obj,m):
    """
    Can only be used with '&' operator not with 'and'

    Multi-column boolean matrices' values are compared with 'and' operator, meaning that 1 false value
    causes whole row to be reduced to a false value
    """
    if mat.BOOL_MAT:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            if not other.BOOL_MAT:
                raise TypeError("Can't compare bool matrix to non-bool matrix")
            
            d0,d1 = mat.dim
            o = other.matrix
            true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
            data = []
            
            #Reduce multiple columns into one
            #Remove rows with false boolean values
            for i in range(d0):
                mrow,orow = m[i],o[i]
                if (false in mrow) or (false in orow):
                    data.append([false])
                    continue
                data.append([true])

            return obj(dim=[d0,1],
                       data=data,
                       features=mat.features[:1],
                       index=mat.index[:],
                       implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        d0,d1 = mat.dim
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        data = []

        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            if other.BOOL_MAT:
                raise TypeError("Can't compare non-bool matrix to bool matrix")

            o = other.matrix
            
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if (bool(mrow[j]) and bool(orow[j])) else false for j in range(d1)])
        
        elif isinstance(other,list):
            if mat.d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            for i in range(d0):
                mrow = m[i]
                data.append([true if (bool(mrow[j]) and bool(other[j])) else false for j in range(d1)])

        else:
            for i in range(d0):
                mrow = m[i]
                data.append([true if (bool(mrow[j]) and bool(other)) else false for j in range(d1)])
            
        return obj(dim=[d0,d1],
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

def _or(mat,other,obj,m):
    """
    Can only be used with '|' operator not with 'or'
    """
    if mat.BOOL_MAT:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            if not other.BOOL_MAT:
                raise TypeError("Can't compare bool matrix to non-bool matrix")
            
            d0,d1 = mat.dim
            o = other.matrix
            true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
            data = []
            
            #Reduce multiple columns into one
            #Remove rows with false boolean values
            for i in range(d0):
                mrow,orow = m[i],o[i]
                if (false in mrow) and (false in orow):
                    data.append([false])
                    continue
                data.append([true])

            return obj(dim=[d0,1],
                       data=data,
                       features=mat.features[:1],
                       index=mat.index[:],
                       implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        d0,d1 = mat.dim
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        data = []

        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            if other.BOOL_MAT:
                raise TypeError("Can't compare non-bool matrix to bool matrix")

            o = other.matrix
            
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if (bool(mrow[j]) or bool(orow[j])) else false for j in range(d1)])
        
        elif isinstance(other,list):
            if mat.d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            for i in range(d0):
                mrow = m[i]
                data.append([true if (bool(mrow[j]) or bool(other[j])) else false for j in range(d1)])

        else:
            for i in range(d0):
                mrow = m[i]
                data.append([true if (bool(mrow[j]) or bool(other)) else false for j in range(d1)])
            
        return obj(dim=[d0,d1],
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})
    
def _xor(mat,other,obj,m):
    """
    Can only be used with '^' operator 
    """
    if mat.BOOL_MAT:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            if not other.BOOL_MAT:
                raise TypeError("Can't compare bool matrix to non-bool matrix")
            
            d0,d1 = mat.dim
            o = other.matrix
            true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
            data = []
            
            #Reduce multiple columns into one
            #Remove rows with false boolean values
            for i in range(d0):
                mrow,orow = m[i],o[i]
                false_mrow = false in mrow
                false_orow = false in orow
                if false_mrow == false_orow:
                    data.append([false])
                    continue
                data.append([true])

            return obj(dim=[d0,1],
                       data=data,
                       features=mat.features[:1],
                       index=mat.index[:],
                       implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        d0,d1 = mat.dim
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        data = []

        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            if other.BOOL_MAT:
                raise TypeError("Can't compare non-bool matrix to bool matrix")

            o = other.matrix
            
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if (bool(mrow[j]) != bool(orow[j])) else false for j in range(d1)])
        
        elif isinstance(other,list):
            if mat.d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            for i in range(d0):
                mrow = m[i]
                data.append([true if (bool(mrow[j]) != bool(other[j])) else false for j in range(d1)])

        else:
            for i in range(d0):
                mrow = m[i]
                data.append([true if (bool(mrow[j]) != bool(other)) else false for j in range(d1)])
            
        return obj(dim=[d0,d1],
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})