def setMatrix(mat,d=None,r=None,lis=[],direc=r"",fill="uniform",cmat=False,fmat=True):
    """
    Set the matrix based on the arguments given
    """
    from random import random,randint,uniform,triangular,gauss,seed
    from MatricesM.C_funcs.randgen import getuni,getfill,igetuni,igetrand
    from MatricesM.C_funcs.zerone import pyfill
    from MatricesM.C_funcs.linalg import Ctranspose
    # =============================================================================
    # Argument check
    if lis is None:
        lis = []
    if len(direc)==0 and len(lis)==0:
        if fill == None:
            fill = "uniform"
        elif isinstance(fill,str):
            if fill.lower() not in ["uniform","gauss","triangular"]:
                if mat.dtype != "dataframe":
                    raise TypeError("Can't fill matrix with strings if dtype isn't set to 'dataframe'")
    #Check dimension given
    if isinstance(d,int):
        mat._setDim(d)
    #Set new range    
    if r==None:
        r=mat.initRange
    else:
        mat._Matrix_initRange=r
        
    # =============================================================================
    #Save the seed for reproduction
    if mat.seed==None and (fill in ["random","uniform","gauss","triangular"]) and len(lis)==0 and len(direc)==0:
        randseed = randint(-2**24,2**24)
        mat._Matrix__seed = randseed
    
    elif (fill in ["random","uniform","gauss","triangular"]) and len(lis)==0 and len(direc)==0:
        seed(mat.seed)
    else:
        mat._Matrix__seed=None
        
    # =============================================================================
    #Set the new matrix
    #Matrix from given string
    if isinstance(lis,str):
        mat._matrix=mat._listify(lis)
        if mat.dim == [0,0]:
            mat._Matrix__dim=mat._declareDim()
    #Matrix from a directory
    elif len(direc)>0 and len(lis)==0:
        [lis,mat._Matrix__features] = mat._Matrix__fromFile(direc,mat._header,mat.coldtypes)
        if isinstance(lis,str):
            mat._matrix = mat._listify(lis)
        elif isinstance(lis,list):
            mat._matrix = lis
        else:
            return None
        
        if mat.dim == [0,0]:
            mat._Matrix__dim=mat._declareDim()          
    #Matrix from a list or other filling methods
    else:
        if len(lis)>0:
            if isinstance(lis[0],list):                        
                mat._matrix = [a[:] for a in lis[:]]
                if mat.dim == [0,0]:
                    mat._Matrix__dim=mat._declareDim()
            else:
                try:
                    assert mat.dim[0]*mat.dim[1] == len(lis)
                except Exception as err:
                    print(err)
                else:
                    mat._matrix=[]
                    for j in range(0,len(lis),mat.dim[1]):
                        mat._matrix.append(lis[j:j+mat.dim[1]])
            
        # =============================================================================
        #Same range for all columns
        elif len(lis)==0 and (isinstance(r,list) or isinstance(r,tuple)):
            
            if fill in ["uniform"]:
                m,n=max(r),min(r)
                if cmat:
                    seed(mat.seed)
                    mat._matrix=[[complex(uniform(n,m),uniform(n,m)) for a in range(d[1])] for b in range(d[0])]
                
                elif fmat:
                    if r==[0,1]:
                        mat._matrix=pyfill(d[0],d[1],mat.seed)
                    else:
                        mat._matrix=getuni(d[0],d[1],n,m,mat.seed)
                
                else:
                    if r==[0,1]:
                        mat._matrix=igetrand(d[0],d[1],mat.seed)
                    else:
                        mat._matrix=igetuni(d[0],d[1],n-1,m+1,mat.seed)
                        
            elif fill in ["gauss"]:
                seed(mat.seed)
                m,s=r[0],r[1]
                if cmat:
                    mat._matrix=[[complex(gauss(m,s),gauss(m,s)) for a in range(d[1])] for b in range(d[0])]
                
                elif fmat:
                    mat._matrix=[[gauss(m,s) for a in range(d[1])] for b in range(d[0])]
                
                else:
                    mat._matrix=[[round(gauss(m,s)) for a in range(d[1])] for b in range(d[0])]
                    
            elif fill in ["triangular"]:
                seed(mat.seed)
                n,m,o = r[0],r[1],r[2]
                if cmat:
                    mat._matrix=[[complex(triangular(n,m,o),triangular(n,m,o)) for a in range(d[1])] for b in range(d[0])]
                
                elif fmat:
                    mat._matrix=[[triangular(n,m,o) for a in range(d[1])] for b in range(d[0])]
                else:
                    mat._matrix=[[round(triangular(n,m,o)) for a in range(d[1])] for b in range(d[0])]   
            #Ranged has no affect after this point
            elif type(fill) == list:
                if len(fill)!=d[0]:
                    raise ValueError(f"Given list {fill} can't be used to fill a matrix")
                else:
                    mat._matrix = [fill for _ in range(d[0])]

            elif type(fill) == range:
                l = list(fill)
                if len(l)!=d[0]:
                    raise ValueError(f"Given list {fill} can't be used to fill a matrix")
                else:
                    mat._matrix = [fill for _ in range(d[0])]
            
            else:
                mat._matrix=getfill(d[0],d[1],fill)
        # =============================================================================               
        #Different ranges over individual columns
        elif len(lis)==0 and isinstance(r,dict):
            try:
                assert len([i for i in r.keys()])==mat.dim[1]
                vs=[len(i) for i in r.values()]
                assert vs.count(vs[0])==len(vs)
                feats=[i for i in r.keys()]
                mat.features=feats

            except Exception as err:
                print(err)
            else:
                lis=list(r.values())
                seed(mat.seed)
                if fill in ["uniform"]:                    
                    if cmat:
                        temp=[[complex(uniform(min(lis[i]),max(lis[i])),uniform(min(lis[i]),max(lis[i]))) for _ in range(d[0])] for i in range(d[1])]
                    
                    elif fmat:
                        temp=[[uniform(min(lis[i]),max(lis[i])) for _ in range(d[0])] for i in range(d[1])]                        
                    
                    else:
                        temp=[[round(uniform(min(lis[i]),max(lis[i])+1))//1 for _ in range(d[0])] for i in range(d[1])]
                
                elif fill in ["gauss"]:                    
                    if cmat:
                        temp=[[complex(gauss(lis[i][0],lis[i][1]),uniform(min(lis[i]),max(lis[i]))) for _ in range(d[0])] for i in range(d[1])]
                    
                    elif fmat:
                        temp=[[gauss(lis[i][0],lis[i][1]) for _ in range(d[0])] for i in range(d[1])]                        
                    
                    else:
                        temp=[[round(gauss(lis[i][0],lis[i][1]+1))//1 for _ in range(d[0])] for i in range(d[1])]
                        
                elif fill in ["triangular"]:                    
                    if cmat:
                        temp=[[complex(triangular(lis[i][0],lis[i][1],lis[i][2]),triangular(lis[i][0],lis[i][1],lis[i][2])) for _ in range(d[0])] for i in range(d[1])]
                        
                    elif fmat:
                        
                        temp=[[triangular(lis[i][0],lis[i][1],lis[i][2]) for _ in range(d[0])] for i in range(d[1])]                                                
                    else:
                        temp=[[round(triangular(lis[i][0],lis[i][1]+1,lis[i][2]))//1 for _ in range(d[0])] for i in range(d[1])]
                #Ranged has no affect after this point
                elif type(fill) == list:
                    if len(fill)!=d[0]:
                        raise ValueError(f"Given list {fill} can't be used to fill a matrix")
                    else:
                        mat._matrix = [fill for _ in range(d[0])]
                        return None

                elif type(fill) == range:
                    l = list(fill)
                    if len(l)!=d[0]:
                        raise ValueError(f"Given list {fill} can't be used to fill a matrix")
                    else:
                        mat._matrix = [fill for _ in range(d[0])]
                        return None
                else:
                    mat._matrix=getfill(d[0],d[1],fill)
                    return None

                mat._matrix=Ctranspose(d[1],d[0],temp)
        else:
            return None
