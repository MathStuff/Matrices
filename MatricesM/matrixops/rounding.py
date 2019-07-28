def rnd(mat,n,obj,m,dFrame):
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[round(m[i][j],n) if ((dts[j] in [int,float]) and isinstance(m[i][j],(int,float))) else m[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=dFrame,index=mat.index[:],indexname=mat.indexname,implicit=True) 
    if (mat._fMat or mat._dfMat) and n<0:
        n=1
    if mat._cMat:
        temp=[[complex(round(m[i][j].real,n),round(m[i][j].imag,n)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=complex,implicit=True)               
    else:
        temp=[[round(m[i][j],n) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=float,implicit=True) 

def flr(mat,obj,m,dFrame):
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[int(m[i][j]) if ((dts[j] in [int,float]) and isinstance(m[i][j],(int,float))) else m[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=dFrame,index=mat.index[:],indexname=mat.indexname,implicit=True) 
    if mat._cMat:
        temp=[[complex(int(m[i][j].real),int(m[i][j].imag)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=complex,implicit=True)              
    else:
        temp=[[int(m[i][j]) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=int,implicit=True)       

def ceil(mat,obj,m,dFrame):
    from math import ceil
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[ceil(m[i][j]) if ((dts[j] in [int,float]) and isinstance(m[i][j],(int,float))) else m[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=dFrame,index=mat.index[:],indexname=mat.indexname,implicit=True) 
    if mat._cMat:
        temp=[[complex(ceil(m[i][j].real),ceil(m[i][j].imag)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=complex,implicit=True)                  
    else:
        temp=[[ceil(m[i][j]) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=int,implicit=True)    

def _abs(mat,obj,m,dFrame):
    if mat._dfMat:
        dts = mat.coldtypes[:]
        temp=[[abs(m[i][j]) if ((dts[j] in [int,float]) and isinstance(m[i][j],(int,float))) else m[i][j] for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=dFrame,index=mat.index[:],indexname=mat.indexname,implicit=True) 
    if mat._cMat:
        temp=[[complex(abs(m[i][j].real),abs(m[i][j].imag)) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=complex,coldtypes=mat.coldtypes[:],implicit=True)               
    else:
        temp=[[abs(m[i][j]) for j in range(mat.dim[1])] for i in range(mat.dim[0])]
        return obj(mat.dim,data=temp,features=mat.features[:],decimal=mat.decimal,dtype=mat.dtype,coldtypes=mat.coldtypes[:],implicit=True)   