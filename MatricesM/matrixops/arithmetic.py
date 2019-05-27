def matmul(mat,other,obj):
    if not mat.dim[1]==other.dim[0]:
        raise ValueError("Dimensions don't match for matrix multiplication")
    temp=[]    
    for r in range(mat.dim[0]):
        temp.append(list())
        for rs in range(other.dim[1]):
            temp[r].append(0)
            total=0
            for cs in range(other.dim[0]):
                num=mat.matrix[r][cs]*other.matrix[cs][rs]
                total+=num
            if mat._cMat:
                temp[r][rs]=complex(round(total.real,12),round(total.imag,12))
            else:
                temp[r][rs]=round(total,12)
                
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
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
                #--------------------------------------------------------------------------
        elif isinstance(other,list):

            if len(other)!=mat.dim[1]:
                print("Can't add")
                return mat
            else:
                temp=[[mat.matrix[rows][cols]+other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
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
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't subtract")
            return mat
        else:
            temp=[[mat.matrix[rows][cols]-other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
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
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------

    elif isinstance(other,list):
        if len(other)!=mat.dim[1]:
            print("Can't multiply")
            return mat
        else:
            temp=[[mat.matrix[rows][cols]*other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
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
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
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
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):
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
                return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
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
        
    elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
        try:
            temp=[[mat.matrix[rows][cols]%other for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
        except ZeroDivisionError:
            print("Division by 0")
            return mat
        except:
            print("Can't get modular") 
            return mat
        else:
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    elif isinstance(other,list):
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
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------

    elif isinstance(other,list):

        if len(other)!=mat.dim[1]:
            print("Can't raise to the given power")                
            return mat
        else:
            temp=[[mat.matrix[rows][cols]**other[cols] for cols in range(mat.dim[1])] for rows in range(mat.dim[0])]
            return obj(dim=mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)
            #--------------------------------------------------------------------------
    else:
        print("Can't raise to the given power")
        return mat