def eq(mat,other,obj,m,from_wheres,matrixobj):
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
            data = []
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if mrow[j]==orow[j] else false for j in range(d1)])
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]==other[j] else false for j in range(d1)])

        else:
            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]==other else false for j in range(d1)])
            
        
        return obj(dim=mat.dim,
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        pass
    
def ne(mat,other,obj,m,from_wheres,matrixobj):
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
            data = []
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if mrow[j]!=orow[j] else false for j in range(d1)])
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]!=other[j] else false for j in range(d1)])

        else:
            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]!=other else false for j in range(d1)])
            
        
        return obj(dim=mat.dim,
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        pass

def le(mat,other,obj,m,from_wheres,matrixobj):
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
            data = []
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if mrow[j]<=orow[j] else false for j in range(d1)])
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]<=other[j] else false for j in range(d1)])

        elif isinstance(other,(int,float,str)):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]<=other else false for j in range(d1)])
            
        else:
            raise TypeError("Invalid type to compare")
        
        return obj(dim=mat.dim,
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

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
            data = []
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if mrow[j]<orow[j] else false for j in range(d1)])
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]<other[j] else false for j in range(d1)])

        elif isinstance(other,(int,float,str)):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]<other else false for j in range(d1)])
            
        else:
            raise TypeError("Invalid type to compare")
        
        return obj(dim=mat.dim,
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        pass
            
def ge(mat,other,obj,m,from_wheres,matrixobj):
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
            data = []
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if mrow[j]>=orow[j] else false for j in range(d1)])
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]>=other[j] else false for j in range(d1)])

        elif isinstance(other,(int,float,str)):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]>=other else false for j in range(d1)])
            
        else:
            raise TypeError("Invalid type to compare")
        
        return obj(dim=mat.dim,
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        pass

def gt(mat,other,obj,m,from_wheres,matrixobj):
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
            data = []
            for i in range(d0):
                mrow,orow = m[i],o[i]
                data.append([true if mrow[j]>orow[j] else false for j in range(d1)])
        
        elif isinstance(other,list):
            if d1!=len(other):
                raise ValueError("Length of the list doesn't match matrix's column amount")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]>other[j] else false for j in range(d1)])

        elif isinstance(other,(int,float,str)):
            if mat._cMat:
                raise TypeError("Can't compare int/float to complex numbers")

            data = []
            for i in range(d0):
                mrow= m[i]
                data.append([true if mrow[j]>other else false for j in range(d1)])
            
        else:
            raise TypeError("Invalid type to compare")
        
        return obj(dim=mat.dim,
                   data=data,
                   features=mat.features[:],
                   index=mat.index[:],
                   implicit=True,BOOL_MAT=True,DEFAULT_BOOL={True:true,False:false})

    else:
        pass