def le(mat,other,obj):
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<=other.matrix[j][i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<=other[i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp
    
def lt(mat,other,obj):
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<other.matrix[j][i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<other[i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]<other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp
    
def eq(mat,other,obj):
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]==other.matrix[j][i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]==other[i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]==other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]==other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,str):
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]==other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])])

        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp
    
def ne(mat,other,obj):
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]!=other.matrix[j][i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]!=other[i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]!=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]!=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]!=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp
            
def ge(mat,other,obj):
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>=other.matrix[j][i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>=other[i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>=other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp
    
def gt(mat,other,obj):
    try:
        if isinstance(other,obj):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>other.matrix[j][i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,list):
            if mat.dim[1]!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>other[i] else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(mat.dim,[[1 if mat.matrix[j][i]>other else 0 for i in range(mat.dim[1])] for j in range(mat.dim[0])],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")
            
    except Exception as err:
        raise err
        
    else:
        return temp