def matmul(mat,other,obj):
    if not mat.dim[1]==other.dim[0]:
        raise ValueError("Dimensions don't match for matrix multiplication")

    temp = [[sum([mat.matrix[r][cs]*other.matrix[cs][rs] for cs in range(other.dim[0])]) for rs in range(other.dim[1])] for r in range(mat.dim[0])]           
    #Return proper the matrix
    if other._cMat or mat._cMat:
        t = "complex"
    elif other._fMat or mat._fMat:
        t = "float"
    else:
        t = "integer"
    return obj(dim=[mat.dim[0],other.dim[1]],listed=temp,features=other.features[:],decimal=other.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
    
def add(mat,other,obj):
        if isinstance(other,obj):
            try:
                assert mat.dim==other.dim                
                temp=[[mat.matrix[rows][cols]+other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except Exception as err:
                print("Can't add: ",err)
                return mat
            else:
                if mat._dfMat or other._dfMat:
                    t = "dataframe"
                elif other._cMat or mat._cMat:
                    t = "complex"
                elif other._fMat or mat._fMat:
                    t = "float"
                else:
                    t = "integer"
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True)    
                #--------------------------------------------------------------------------
                
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[mat.matrix[rows][cols]+other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

            except:
                print("Can't add")
                return mat
            else:
                if mat._dfMat:
                    t = "dataframe"
                elif  mat._cMat or isinstance(other,complex):
                    t = "complex"
                elif  mat._fMat or isinstance(other,float):
                    t = "float"
                else:
                    t = "integer"
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
                #--------------------------------------------------------------------------
        elif isinstance(other,list):

            if len(other)!=mat.dim[1]:
                print("Can't add")
                return mat
            else:
                if mat._dfMat:
                    t = "dataframe"
                elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                    t = "complex"
                elif  mat._fMat or any([1 for i in other if type(i)==float]):
                    t = "float"
                else:
                    t = "integer"
                temp=[[mat.matrix[rows][cols]+other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
                #--------------------------------------------------------------------------
        else:
            print("Can't add")
            return mat
            
def sub(mat,other,obj):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim                
            temp=[[mat.matrix[rows][cols]-other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't subtract: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = "dataframe"
            elif other._cMat or mat._cMat:
                t = "complex"
            elif other._fMat or mat._fMat:
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[mat.matrix[rows][cols]-other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except:
            print("Can't subtract")
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or isinstance(other,complex):
                t = "complex"
            elif  mat._fMat or isinstance(other,float):
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't subtract")
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = "complex"
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = "float"
            else:
                t = "integer"
            temp=[[mat.matrix[rows][cols]-other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    else:
        print("Can't subtract")
        return mat
    
def mul(mat,other,obj):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim                
            temp=[[mat.matrix[rows][cols]*other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't multiply: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = "dataframe"
            elif other._cMat or mat._cMat:
                t = "complex"
            elif other._fMat or mat._fMat:
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True) 
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[mat.matrix[rows][cols]*other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except Exception as err:
            print("Can't multiply: ",err)
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or isinstance(other,complex):
                t = "complex"
            elif  mat._fMat or isinstance(other,float):
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------

    elif isinstance(other,list):
        if len(other)!=mat.dim[1]:
            print("Can't multiply")
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = "complex"
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = "float"
            else:
                t = "integer"
            temp=[[mat.matrix[rows][cols]*other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    else:
        print("Can't multiply")
        return mat

def fdiv(mat,other,obj):
    if isinstance(other,obj):
        if mat._cMat or  other._cMat:
            print("Complex numbers doesn't allow floor division")
        return mat
        try:
            assert mat.dim==other.dim                
            temp=[[mat.matrix[rows][cols]//other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except Exception as err:
            print("Can't divide: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = "dataframe"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True)   
        
    elif isinstance(other,int) or isinstance(other,float):
        try:
            temp=[[mat.matrix[rows][cols]//other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't divide") 
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
            
    elif isinstance(other,list):
        if mat._dfMat:
            t = "dataframe"
        elif  mat._cMat or any([1 for i in other if type(i)==complex]):
            raise TypeError("Complex numbers can't be used with floordiv operator")
        elif  mat._fMat or any([1 for i in other if type(i)==float]):
            t = "float"
        else:
            t = "integer"
        if len(other)!=mat.dim[1]:
            print("Can't divide")
            return mat
        else:
            try:
                temp=[[mat.matrix[rows][cols]//other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return mat
            except:
                print("Can't divide") 
                return mat
            else:
                if mat._dfMat:
                    t = "dataframe"
                else:
                    t = "integer"
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
                #--------------------------------------------------------------------------
    else:
        print("Can't divide")
        return mat
        
def tdiv(mat,other,obj):

    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim                
            temp=[[mat.matrix[rows][cols]/other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except Exception as err:
            print("Can't divide: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = "dataframe"
            elif other._cMat or mat._cMat:
                t = "complex"
            elif other._fMat or mat._fMat:
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features,decimal=mat.decimal[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True) 
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[mat.matrix[rows][cols]/other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't divide") 
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or isinstance(other,complex):
                t = "complex"
            elif  mat._fMat or isinstance(other,float):
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):
        if mat._dfMat:
            t = "dataframe"
        elif  mat._cMat or any([1 for i in other if type(i)==complex]):
            t = "complex"
        elif  mat._fMat or any([1 for i in other if type(i)==float]):
            t = "float"
        else:
            t = "integer"
        if len(other)!=mat.dim[1]:
            print("Can't divide")
            return mat
        else:
            try:
                temp=[[mat.matrix[rows][cols]/other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return mat
            except:
                print("Can't divide") 
                return mat
            else:
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
                #--------------------------------------------------------------------------
    else:
        print("Can't divide")
        return mat

def mod(mat,other,obj):
    if isinstance(other,obj):
        try:
            if mat._cMat or  other._cMat:
                print("Complex numbers doesn't allow floor division")
                return mat
            assert mat.dim==other.dim                
            temp=[[mat.matrix[rows][cols]%other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except Exception as err:
            print("Can't get modular: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = "dataframe"
            elif other._fMat or mat._fMat:
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True) 
        
    elif isinstance(other,int) or isinstance(other,float):
        try:
            temp=[[mat.matrix[rows][cols]%other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't get modular") 
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._fMat or isinstance(other,float):
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):
        if mat._dfMat:
            t = "dataframe"
        elif  mat._cMat or any([1 for i in other if type(i)==complex]):
            raise TypeError("Complex numbers can't be used with modular operator")
        elif  mat._fMat or any([1 for i in other if type(i)==float]):
            t = "float"
        else:
            t = "integer"

        if len(other)!=mat.dim[1]:
            print("Can't get modular")
            return mat
        else:
            try:
                temp=[[mat.matrix[rows][cols]%other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return mat
            except:
                print("Can't get modular") 
                return mat
            else:
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
                #--------------------------------------------------------------------------
    else:
        print("Can't get modular")
        return mat
        
def pwr(mat,other,obj):
    if isinstance(other,obj):
        try:
            assert mat.dim==other.dim                
            temp=[[mat.matrix[rows][cols]**other.matrix[rows][cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except Exception as err:
            print("Can't raise to the given power: ",err)
            return mat
        else:
            if mat._dfMat or other._dfMat:
                t = "dataframe"
            elif other._cMat or mat._cMat:
                t = "complex"
            elif other._fMat or mat._fMat:
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],decimal=mat.decimal,dtype=t,coldtypes=mat.coldtypes[:],implicit=True) 
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[mat.matrix[rows][cols]**other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]

        except:
            print("Can't raise to the given power")            
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or isinstance(other,complex):
                t = "complex"
            elif  mat._fMat or isinstance(other,float):
                t = "float"
            else:
                t = "integer"
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------

    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't raise to the given power")                
            return mat
        else:
            if mat._dfMat:
                t = "dataframe"
            elif  mat._cMat or any([1 for i in other if type(i)==complex]):
                t = "complex"
            elif  mat._fMat or any([1 for i in other if type(i)==float]):
                t = "float"
            else:
                t = "integer"
            temp=[[mat.matrix[rows][cols]**other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=t,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    else:
        print("Can't raise to the given power")
        return mat