def le(mat,other,obj,m,from_wheres,matrixobj):
    if not from_wheres:
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        d0,d1 = mat.dim
        if mat._cMat:
            raise TypeError("Can't compare complex numbers")

        if isinstance(other,(obj,matrixobj)):
            if other._cMat:
                raise TypeError("Can't compare complex numbers")

            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")

            o = other.matrix
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<=o[j][i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<=other[i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<=other else false for i in range(d1)] for j in range(d0)],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<=other else false for i in range(d1)] for j in range(d0)],implicit=True)
          
        else:
            raise TypeError("Invalid type to compare")

        return temp

    else:
       pass
    
def lt(mat,other,obj,m,from_wheres,matrixobj):
    if not from_wheres:
        true ,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        d0,d1 = mat.dim
        if mat._cMat:
            raise TypeError("Can't compare complex numbers")

        if isinstance(other,(obj,matrixobj)):
            if other._cMat:
                raise TypeError("Can't compare complex numbers")

            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")

            o = other.matrix
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<o[j][i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<other[i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<other else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,str):
            temp=obj(dim=mat.dim,data=[[true if m[j][i]<other else false for i in range(d1)] for j in range(d0)],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")
        
        return temp

    else:
        pass
    
def eq(mat,other,obj,m,from_wheres,matrixobj):
    if not from_wheres:
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        d0,d1 = mat.dim
        if isinstance(other,(obj,matrixobj)):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            o = other.matrix
            temp=obj(dim=mat.dim,data=[[true if m[j][i]==o[j][i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]==other[i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]==other else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]==other else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,str):
            temp=obj(dim=mat.dim,data=[[true if m[j][i]==other else false for i in range(d1)] for j in range(d0)],implicit=True)

        elif other is None:
            return False
          
        else:
            raise TypeError("Invalid type to compare")

        return temp

    else:
        pass
    
def ne(mat,other,obj,m,from_wheres,matrixobj):
    if not from_wheres:
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        d0,d1 = mat.dim
        if isinstance(other,(obj,matrixobj)):
            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")
            o = other.matrix
            temp=obj(dim=mat.dim,data=[[true if m[j][i]!=o[j][i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]!=other[i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]!=other else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,complex):
            if not mat._cMat:
                raise TypeError("Can't compare complex numbers to int/float")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]!=other else false for i in range(d1)] for j in range(d0)],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(dim=mat.dim,data=[[true if m[j][i]!=other else false for i in range(d1)] for j in range(d0)],implicit=True)
 
        elif other is None:
            return True
                     
        else:
            raise TypeError("Invalid type to compare")

        return temp
    
    else:
        pass
            
def ge(mat,other,obj,m,from_wheres,matrixobj):
    if not from_wheres:
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        d0,d1 = mat.dim
        if mat._cMat:
            raise TypeError("Can't compare complex numbers")

        if isinstance(other,(obj,matrixobj)):
            if other._cMat:
                raise TypeError("Can't compare complex numbers")

            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")

            o = other.matrix
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>=o[j][i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>=other[i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>=other else false for i in range(d1)] for j in range(d0)],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>=other else false for i in range(d1)] for j in range(d0)],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")

        return temp
    
    else:
        pass

def gt(mat,other,obj,m,from_wheres,matrixobj):
    if not from_wheres:
        true,false = mat.DEFAULT_BOOL[True],mat.DEFAULT_BOOL[False]
        d0,d1 = mat.dim
        if mat._cMat:
            raise TypeError("Can't compare complex numbers")

        if isinstance(other,(obj,matrixobj)):
            if other._cMat:
                raise TypeError("Can't compare complex numbers")

            if mat.dim!=other.dim:
                raise ValueError("Dimensions of the matrices don't match")

            o = other.matrix
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>o[j][i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>other[i] else false for i in range(d1)] for j in range(d0)],implicit=True)
        
        elif isinstance(other,int) or isinstance(other,float):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>other else false for i in range(d1)] for j in range(d0)],implicit=True)
                    
        elif isinstance(other,str):
            temp=obj(dim=mat.dim,data=[[true if m[j][i]>other else false for i in range(d1)] for j in range(d0)],implicit=True)
            
        else:
            raise TypeError("Invalid type to compare")

        return temp
    
    else:
        pass