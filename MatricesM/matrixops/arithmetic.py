def matmul(mat,other,obj,m,dFrame):
    from MatricesM.C_funcs.linalg import matmultip
    from MatricesM.errors.errors import MatrixError
    if not type(other) == obj:
        raise MatrixError(f"{obj} is not not a matrix")
    if not mat.dim[1]==other.dim[0]:
        raise ValueError("Dimensions don't match for matrix multiplication")
    o = other.matrix   
    cm = 0
    if other._cMat or mat._cMat:
        cm = 1
    temp = matmultip(mat.dim[0],other.dim[0],other.dim[1],mat.matrix,o,cm)         
    #Return proper the matrix
    if mat._dfMat or other._dfMat:
        t = dFrame
    elif other._cMat or mat._cMat:
        t = complex
    elif other._fMat or mat._fMat:
        t = float
    else:
        t = int
    return obj(dim=[mat.dim[0],other.dim[1]],data=temp,features=other.features[:],decimal=other.decimal,dtype=t,implicit=True)
    
def add(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim  
            o = other.matrix                 
            temp=[[m[rows][cols]+o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't add: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            elif other._cMat or mat._cMat:
                t = complex
            elif other._fMat or mat._fMat:
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)    
            #--------------------------------------------------------------------------
            
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[m[rows][cols]+other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except:
            print("Can't add")
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or isinstance(other,complex):
                t = complex
            elif  mat._fMat or isinstance(other,float):
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't add")
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = complex
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = float
            else:
                t = int
            temp=[[m[rows][cols]+other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    else:
        print("Can't add")
        return mat
            
def sub(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim      
            o = other.matrix             
            temp=[[m[rows][cols]-o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't subtract: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            elif other._cMat or mat._cMat:
                t = complex
            elif other._fMat or mat._fMat:
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[m[rows][cols]-other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except:
            print("Can't subtract")
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or isinstance(other,complex):
                t = complex
            elif  mat._fMat or isinstance(other,float):
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't subtract")
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = complex
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = float
            else:
                t = int
            temp=[[m[rows][cols]-other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    else:
        print("Can't subtract")
        return mat
    
def mul(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim
            o = other.matrix            
            temp=[[m[rows][cols]*o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't multiply: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            elif other._cMat or mat._cMat:
                t = complex
            elif other._fMat or mat._fMat:
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname) 
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[m[rows][cols]*other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except Exception as err:
            print("Can't multiply: ",err)
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or isinstance(other,complex):
                t = complex
            elif  mat._fMat or isinstance(other,float):
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------

    elif isinstance(other,list):
        if len(other)!=mat.dim[1]:
            print("Can't multiply")
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = complex
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = float
            else:
                t = int
            temp=[[m[rows][cols]*other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    else:
        print("Can't multiply")
        return mat

def fdiv(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        if mat._cMat or  other._cMat:
            print("Complex numbers doesn't allow floor division")
        return mat
        try:
            assert mat.dim==other.dim
            o = other.matrix              
            temp=[[m[rows][cols]//o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except Exception as err:
            print("Can't divide: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)   
        
    elif isinstance(other,int) or isinstance(other,float):
        try:
            temp=[[m[rows][cols]//other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't divide") 
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
            
    elif isinstance(other,list):
        if mat._dfMat:
            t = dFrame
        elif  mat._cMat or any([1 for i in other if type(i)==complex]):
            raise TypeError("Complex numbers can't be used with floordiv operator")
        elif  mat._fMat or any([1 for i in other if type(i)==float]):
            t = float
        else:
            t = int
        if len(other)!=mat.dim[1]:
            print("Can't divide")
            return mat
        else:
            try:
                temp=[[m[rows][cols]//other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return mat
            except:
                print("Can't divide") 
                return mat
            else:
                if mat._dfMat:
                    t = dFrame
                else:
                    t = int
                return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
                #--------------------------------------------------------------------------
    else:
        print("Can't divide")
        return mat
        
def tdiv(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim
            o = other.matrix               
            temp=[[m[rows][cols]/o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except Exception as err:
            print("Can't divide: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            elif other._cMat or mat._cMat:
                t = complex
            elif other._fMat or mat._fMat:
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname) 
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[m[rows][cols]/other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't divide") 
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or isinstance(other,complex):
                t = complex
            elif  mat._fMat or isinstance(other,float):
                t = float
            else:
                t = integer
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):
        if mat._dfMat:
            t = dFrame
        elif  mat._cMat or any([1 for i in other if type(i)==complex]):
            t = complex
        elif  mat._fMat or any([1 for i in other if type(i)==float]):
            t = float
        else:
            t = int
        if len(other)!=mat.dim[1]:
            print("Can't divide")
            return mat
        else:
            try:
                temp=[[m[rows][cols]/other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return mat
            except:
                print("Can't divide") 
                return mat
            else:
                return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
                #--------------------------------------------------------------------------
    else:
        print("Can't divide")
        return mat

def mod(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        try:
            if mat._cMat or  other._cMat:
                print("Complex numbers doesn't allow floor division")
                return mat
            assert mat.dim==other.dim
            o = other.matrix                 
            temp=[[m[rows][cols]%o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except Exception as err:
            print("Can't get modular: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            elif other._fMat or mat._fMat:
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname) 
        
    elif isinstance(other,int) or isinstance(other,float):
        try:
            temp=[[m[rows][cols]%other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't get modular") 
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._fMat or isinstance(other,float):
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):
        if mat._dfMat:
            t = dFrame
        elif  mat._cMat or any([1 for i in other if type(i)==complex]):
            raise TypeError("Complex numbers can't be used with modular operator")
        elif  mat._fMat or any([1 for i in other if type(i)==float]):
            t = float
        else:
            t = int

        if len(other)!=mat.dim[1]:
            print("Can't get modular")
            return mat
        else:
            try:
                temp=[[m[rows][cols]%other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return mat
            except:
                print("Can't get modular") 
                return mat
            else:
                return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=mat.dtype,implicit=True,index=mat.index[:],indexname=mat.indexname)
                #--------------------------------------------------------------------------
    else:
        print("Can't get modular")
        return mat
        
def pwr(mat,other,obj,m,dFrame):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim
            o = other.matrix                  
            temp=[[m[rows][cols]**o[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't raise to the given power: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = dFrame
            elif other._cMat or mat._cMat:
                t = complex
            elif other._fMat or mat._fMat:
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname) 
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[m[rows][cols]**other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except:
            print("Can't raise to the given power")            
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or isinstance(other,complex):
                t = complex
            elif  mat._fMat or isinstance(other,float):
                t = float
            else:
                t = int
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------

    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't raise to the given power")                
            return mat
        else:
            if mat._dfMat:
                t = dFrame
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = complex
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = float
            else:
                t = int
            temp=[[m[rows][cols]**other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,data=temp,features=mat.features[:],dtype=t,implicit=True,index=mat.index[:],indexname=mat.indexname)
            #--------------------------------------------------------------------------
    else:
        print("Can't raise to the given power")
        return mat
