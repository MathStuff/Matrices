def rnd(mat,n,obj):
    from MatricesM.matrix import dataframe
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[round(mat.matrix[i][j],n) if (dts[j] in [int,float,complex]) else mat.matrix[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=dataframe,implicit=True) 
    if (mat._fMat or mat._dfMat) and n<0:
        n=1
    if mat._cMat:
        temp=[[complex(round(mat.matrix[i][j].real,n),round(mat.matrix[i][j].imag,n)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=complex,implicit=True)               
    else:
        temp=[[round(mat.matrix[i][j],n) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=float,implicit=True) 

def flr(mat,obj):
    from MatricesM.matrix import dataframe
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[int(mat.matrix[i][j]) if (dts[j] in [int,float,complex]) else mat.matrix[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=dataframe,implicit=True) 
    if mat._cMat:
        temp=[[complex(int(mat.matrix[i][j].real),int(mat.matrix[i][j].imag)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=complex,implicit=True)              
    else:
        temp=[[int(mat.matrix[i][j]) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=int,implicit=True)       

def ceil(mat,obj):
    from MatricesM.matrix import dataframe
    from math import ceil
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[ceil(mat.matrix[i][j]) if (dts[j] in [int,float,complex]) else mat.matrix[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=dataframe,implicit=True) 
    if mat._cMat:
        temp=[[complex(ceil(mat.matrix[i][j].real),ceil(mat.matrix[i][j].imag)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=complex,implicit=True)                  
    else:
        temp=[[ceil(mat.matrix[i][j]) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=int,implicit=True)    

def _abs(mat,obj):
    from MatricesM.matrix import dataframe
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[abs(mat.matrix[i][j]) if (dts[j] in [int,float,complex]) else mat.matrix[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=dataframe,implicit=True) 
    if mat._cMat:
        temp=[[complex(abs(mat.matrix[i][j].real),abs(mat.matrix[i][j].imag)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=complex,coldtypes=mat.coldtypes[:],implicit=True)               
    else:
        temp=[[abs(mat.matrix[i][j]) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,listed=temp,features=mat.features[:],dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)   