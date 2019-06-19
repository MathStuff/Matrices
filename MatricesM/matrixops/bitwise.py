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
    """
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            o = other.matrix
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) and bool(o[j][i])) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) and bool(other[i])) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) and bool(other)) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) and bool(other)) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp

def _or(mat,other,obj,m):
    """
    Can only be used with '|' operator not with 'or'
    """
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            o = other.matrix
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) or bool(o[j][i])) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) or bool(other[i])) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) or bool(other)) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if (bool(m[j][i]) or bool(other)) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp
    
def _xor(mat,other,obj,m):
    """
    Can only be used with '^' operator 
    """
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            o = other.matrix
            temp=obj(mat.dim,[[1 if bool(m[j][i])!=bool(o[j][i]) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if bool(m[j][i])!=bool(other[i]) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if bool(m[j][i])!=bool(other) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if bool(m[j][i])!=bool(other) else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],dtype=int,implicit=True)
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp