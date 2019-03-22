# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""
import os

try:
    p=os.environ["PYTHONPATH"].split(os.pathsep)[-1]
    p+=r"\MatricesM\randgen_source"
    a=os.getcwd()
    os.chdir(p)
    from randgen import getrand,rgetrand,getuni,igetuni,getzeros
    os.chdir(a)
    del a,p
    
except ImportError:
    i=input("Use Cython to get ~2x faster performance ? (y/n)")
    assert i in ["y","Y","n","N"]
    if i in ["y","Y"]:
        print("Compiling the proper pyd library for your system...")
        print("This process won't be executed again unless you reinstall the MatricesM library")
        try:
            os.system("python setup.py build_ext --inplace")
        except Exception as err:
            print("Error compiling the randgen\nAre you sure you have GCC and Cython installed?")
            print(err)
        else:
            from randgen import getrand,rgetrand,getuni,igetuni,getzeros
            print("Compilation done.\nIf you get asked the same question again, it means pyd libary wasn't created successfully")
            print("Open an Issue Report on the source page site if so:https://github.com/MathStuff/MatricesM/issues/new/choose")
    else:
        from random import random
        from random import uniform
        print("Imported built-in random library\nYou will be asked again next time you import MatricesM.matrices")
    os.chdir(a)
    del a,p,i

NAMES_IN_SCOPE=dir()   

class Matrix:
    """
    dim:integer | list; dimensions of the matrix. Giving integer values creates a square matrix
    
    listed:string | list of lists of numbers | list of numbers; Elements of the matrix. Can extract all the numbers from a string.
    
    directory:string; directory of a data file(e.g. 'directory/datafile' or r'directory\datafile')
    
    ranged:list of 2 numbers; interval to pick numbers from
    
    randomFill:boolean; fills the matrix with random numbers
    
    header=boolean; takes first row as header title
    
    features=list of strings; column names
    
    Check exampleMatrices.py or https://github.com/MathStuff/MatricesM  for further explanation and examples
    """

    def __init__(self,
                 dim = None,
                 listed = [],
                 directory = "",
                 ranged = [-5,5],
                 randomFill = True,
                 header = False,
                 features = []):  
        
        self._valid = 1
        self._badDims = 0
        self.__adjCalc = 0
        self.__detCalc = 0
        self.__invCalc = 0
        self.__rankCalc = 0    
        self._matrix = []   
        self._initRange = ranged
        self._randomFill = randomFill
        self._string = ""
        self._dir = directory
        self.__features = features
        self._header = header
        
        self._setDim(dim)
        self.setInstance()                     
        self.setMatrix(self.dim,self._initRange,listed,directory)
        self.setFeatures()
# =============================================================================
    def setInstance(self):
        """
        Set the type
        """
        if isinstance(self,CMatrix):
            self._isIdentity=0
            self._fMat=1
            self._cMat=1
        elif isinstance(self,FMatrix):
            self._isIdentity=0
            self._fMat=1
            self._cMat=0
        elif isinstance(self,Identity):
            self._isIdentity=1
            self._fMat=0
            self._cMat=0
        else:
            self._isIdentity=0
            self._fMat=0
            self._cMat=0
            
    def setFeatures(self):
        """
        Set default feature names
        """
        if len(self.features)!=self.dim[1]:
            self.__features=["Col {}".format(i+1) for i in range(self.dim[1])]    
            
    def _setDim(self,d):
        """
        Set the dimension to be a list if it's an integer
        """
        if isinstance(d,int):
            if d>=1:
                self.__dim=[d,d]
            else:
                self.__dim=[0,0]
        elif isinstance(d,list):
            if len(d)!=2:
                self.__dim=[0,0]
            else:
                if isinstance(d[0],int) and isinstance(d[1],int):
                    if d[0]>0 and d[1]>0:
                        self.__dim=d[:]
                    else:
                        self.__dim=[0,0]
        elif d==None:
            self.__dim=[0,0]  
            
    def setMatrix(self,d=None,r=None,lis=[],direc=r""):
        """
        Set the matrix based on the arguments given
        """
        global NAMES_IN_SCOPE
        from random import uniform
        #Set new dimension
        if d!=None:
            self._setDim(d)
        d=self.dim

        #Set new range    
        if r==None:
            r=self._initRange[:]
        else:
            self._initRange=r
        
        #Set the new matrix
        if isinstance(lis,str):
            self._matrix=self._listify(lis)

        elif len(direc)>0:
            lis=self.__fromFile(direc)
            if not lis==None:
                self._matrix=self._listify(lis)
            else:
                return None                      
        else:
            if len(lis)>0:
                if isinstance(lis[0],list):                        
                    self._matrix = [a[:] for a in lis[:]]
                else:
                    try:
                        assert self.dim[0]*self.dim[1] == len(lis)
                    except Exception as err:
                        print(err)
                    else:
                        self._matrix=[]
                        for j in range(0,len(lis),self.dim[1]):
                                self._matrix.append(lis[j:j+self.dim[1]])
            #Same range for all columns
            elif len(lis)==0 and isinstance(r,list):
                if self._randomFill:
                    m,n=max(self._initRange),min(self._initRange)
                    if self._cMat:
                        self._matrix=[[complex(uniform(n,m),uniform(n,m)) for a in range(d[1])] for b in range(d[0])]
                    
                    elif self._fMat:
                        if self._initRange==[0,1]:
                            if "getrand" in NAMES_IN_SCOPE:
                                self._matrix=getrand(d[0],d[1])
                            else:
                                self._matrix=[[random() for a in range(d[1])] for b in range(d[0])]
                        else:
                            if "getuni" in NAMES_IN_SCOPE:
                                self._matrix=getuni(d[0],d[1],n,m)
                            else:
                                self._matrix=[[uniform(n,m) for a in range(d[1])] for b in range(d[0])]
                    
                    else:
                        if self._initRange==[0,1]:
                            if "rgetrand" in NAMES_IN_SCOPE:
                                self._matrix=rgetrand(d[0],d[1])
                            else:
                                self._matrix=[[round(random()) for a in range(d[1])] for b in range(d[0])]
                        else:
                            n-=1
                            m+=1
                            if "igetuni" in NAMES_IN_SCOPE:
                                self._matrix=igetuni(d[0],d[1],n,m)
                            else:
                                self._matrix=[[int(uniform(n,m)) for a in range(d[1])] for b in range(d[0])]
                
                else:
                    if "getzeros" in NAMES_IN_SCOPE:
                        self._matrix=getzeros(d[0],d[1])
                    else:
                        self._matrix=[[0 for a in range(d[1])] for b in range(d[0])]
                    
            #Different ranges over individual columns
            elif len(lis)==0 and isinstance(r,dict):
                try:
                    assert len([i for i in r.keys()])==self.dim[1]
                    vs=[len(i) for i in r.values()]
                    assert vs.count(vs[0])==len(vs)
                    feats=[i for i in r.keys()]
                    self.__features=feats
  
                except Exception as err:
                    print(err)
                else:                        
                    if self._cMat:
                        i=0
                        temp=[]
                        while i<d[1]:
                            m,n=max(r[feats[i]]),min(r[feats[i]])
                            temp.append([complex(uniform(n,m),uniform(n,m)) for a in range(d[0])])
                            i+=1
                        self._matrix=CMatrix([self.dim[1],self.dim[0]],listed=temp).t.matrix
                        
                    elif self._fMat:
                        i=0
                        temp=[]
                        while i<d[1]:
                            m,n=max(r[feats[i]]),min(r[feats[i]])
                            temp.append([uniform(n,m) for a in range(d[0])])
                            i+=1
                        self._matrix=FMatrix([self.dim[1],self.dim[0]],listed=temp).t.matrix 
                    else:
                        i=0
                        temp=[]
                        while i<d[1]:
                            m,n=max(r[feats[i]]),min(r[feats[i]])
                            temp.append([int(uniform(n,m)) for a in range(d[0])])
                            i+=1
                        self._matrix=Matrix([self.dim[1],self.dim[0]],listed=temp).t.matrix 
                    
            else:
                self._valid=0
                return None
# =============================================================================           
    def _declareDim(self):
        """
        Set new dimension 
        """
        try:
            rows=0
            cols=0
            for row in self._matrix:
                rows+=1
                cols=0
                for ele in row:
                    cols+=1
        except Exception as err:
            print("Error getting matrix")
            return None
        else:

            return [rows,cols]
        
    def _declareRange(self,lis):
        """
        Finds and returns the range of the elements in a given list
        """
        c={}
        self.setFeatures()
        if self._cMat:
            for i in range(self.dim[1]):
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(lis[rows][i].real)
                    temp.append(lis[rows][i].imag)
                c[self.__features[i]]=[round(min(temp),4),round(max(temp),4)]
        else:
            for cols in range(self.dim[1]):
                temp=[lis[rows][cols] for rows in range(self.dim[0])]
                c[self.__features[cols]]=[round(min(temp),4),round(max(temp),4)]
        return c
        
    def __fromFile(self,d):
        try:
            data="" 
            with open(d,"r",encoding="utf8") as f:
                for lines in f:
                    data+=lines
        except FileNotFoundError:
            try:
                f.close()
            except:
                pass
            print("No such file or directory")
            self._valid=0
            return None
        else:
            f.close()

            return data
# =============================================================================  
    def _listify(self,stringold):
        """
        Finds all the numbers in the given string
        """
        #Get the features from the first row if header exists
        import re
        string=stringold[:]
        if self._header:
            i=0
            for ch in string:
                if ch!="\n":
                    i+=1
                else:
                    if len(self.__features)!=self.dim[1]:
                        pattern=r"(?:\w+ ?[0-9]*)+"
                        self.__features=re.findall(pattern,string[:i])
                        if len(self.__features)!=self.dim[1]:
                            print("Can't get enough column names from the header")
                            self.setFeatures()
                    string=string[i:]
                    break
                
        #Get all integer and float values       
        pattern=r"-?\d+\.?\d*"
        found=re.findall(pattern,string)
        
        #String to number
        try:
            if not isinstance(self,FMatrix):
                found=[int(a) for a in found]
            elif isinstance(self,FMatrix):
                found=[float(a) for a in found]
        except ValueError as v:
            print("If your matrix has float values, use FMatrix. If not use Matrix\n",v)
            return []
        #Fix dimensions to create a row matrix   
        if self.__dim==[0,0]:
            self.__dim=[1,len(found)]
            self._badDims=1
            self.setFeatures()
        #Create the row matrix
        temp=[]
        e=0            
        for rows in range(self.dim[0]):
            temp.append(list())
            for cols in range(self.dim[1]):
                temp[rows].append(found[cols+e])
            e+=self.dim[1]

        return temp
            
    def _stringfy(self):
        """
        Turns a square matrix shaped list into a grid-like form that is printable
        Returns a string
        """
        import re
        def __digits(num):
            dig=0
            if num==0:
                return 1
            if num<0:
                dig+=1
                num*=-1
            while num!=0:
                num=num//10
                dig+=1
            return dig

        string=""
        if self._cMat:
            ns=""
            for i in self._matrix:
                for j in i:
                    ns+=str(round(j.real,self.decimal))
                    im=j.imag
                    if im<0:
                        ns+=str(round(im,self.decimal))+"j "
                    else:
                        ns+="+"+str(round(im,self.decimal))+"j "
                        
            pattern=r"\-?[0-9]+(?:\.?[0-9]*)[-+][0-9]+(?:\.?[0-9]*)j"
            bound=max([len(a) for a in re.findall(pattern,ns)])-2
        elif not self._isIdentity:
            try:
                i=min([min(a) for a in self._inRange.values()])
                j=max([max(a) for a in self._inRange.values()])
                b1=__digits(i)
                b2=__digits(j)
                bound=max([b1,b2])
            except ValueError:
                print("Dimension parameter is required")
                return ""
        else:
            bound=2
            
        if self._fMat or self._cMat:
            pre="0:.{}f".format(self.decimal)
            st="{"+pre+"}"
            interval=[float("-0."+"0"*(self.decimal-1)+"1"),float("0."+"0"*(self.decimal-1)+"1")] 
            
        for rows in range(self.dim[0]):
            string+="\n"
            for cols in range(self.dim[1]):
                num=self._matrix[rows][cols]

                if self._cMat:
                    if num.imag>=0:
                        item=str(round(num.real,self.decimal))+"+"+str(round(num.imag,self.decimal))+"j "
                    else:
                        item=str(round(num.real,self.decimal))+str(round(num.imag,self.decimal))+"j "
                    s=len(item)-4
                    
                elif self._fMat:
                    if num>interval[0] and num<interval[1]:
                        num=0.0
                    item=st.format(round(num,self.decimal))
                    s=__digits(num)
                    
                else:
                    item=str(num)
                    s=__digits(num)
                    
                string += " "*(bound-s)+item+" "

        return string
# =============================================================================
            
    def add(self,feature="Col",lis=[],row=None,col=None):
        """
        Add a row or a column of numbers
        lis: list of numbers desired to be added to the matrix
        row: natural number
        col: natural number 
        row>=1 and col>=1
        
        To append a row, only give the list of numbers, no other arguments
        To append a column, you need to use col = self.dim[1]
        """
        try:
            if row==None or col==None:
                if row==None and col==None:
                    """Append a row """
                    if self.dim[0]>0:
                        if self.dim[1]>0:
                            assert len(lis)==self.dim[1]
                    self._matrix.append(lis)
    
                        
                elif col==None and row>0:
                    """Insert a row"""
                    if row<=self.dim[0]:
                        self.matrix.insert(row-1,lis)
    
                    else:
                        print("Bad arguments")
                        return None
                elif row==None and col>0:
                    if len(lis)!=self.dim[0] and self.dim[0]>0:
                        raise Exception()
                    if col<=self.dim[1]:
                        """Insert a column"""
                        i=0
                        for rows in self._matrix:
                            rows.insert(col-1,lis[i])
                            i+=1
                    elif col-1==self.dim[1]:
                        """Append a column"""
                        i=0
                        for rows in self._matrix:
                            rows.append(lis[i])
                            i+=1
                    else:
                        print("Bad arguments")
                        return None
                else:
                    return None
            else:
                return None
        except Exception as err:
            print("Bad arguments")
            #print(Matrix.__doc__,"\n")
            if self._valid:
                print(err)   
            else:
                return "Invalid matrix"
            return None
        else:
            self._valid=1
            if col!=None and self.__features!=[]:
                self.__features.insert(col-1,feature)
            self.__dim=self._declareDim()
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0     

        
    def remove(self,r=None,c=None):
        """
Deletes the given row or column
Changes the matrix
Give only 1 parameter, r for row, c for column. (Starts from 1)
If no parameter name given, takes it as row
        """
        try:
            assert (r==None or c==None) and (r!=None or c!=None) 
            newM=[]
            if c==None:
                    if r>1:
                        newM+=self.matrix[:r-1]
                        if r<self.dim[0]:
                            newM+=self.matrix[r:]  
                    if r==1:
                        newM=[b[:] for b in self.matrix[r:]]
            elif r==None:
                for rows in range(self.dim[0]):
                    newM.append(list())
                    if c>1:
                        newM[rows]=self.matrix[rows][:c-1]
                        if c<self.dim[1]:
                            newM[rows]+=self.matrix[rows][c:]
                    if c==1:
                        newM[rows]=self.matrix[rows][c:]
        except:
            print("Bad arguments")
            
        else:
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0
            
            if c!=None and len(self.__features)>0:
                del(self.__features[c-1])        
            self._matrix=[a[:] for a in newM]
            self.__dim=self._declareDim()
            
    def delDim(self,num):
        """
Removes desired number of dimensions from bottom right corner
        """        
        try:
            if self.matrix==[]:
                return "Empty matrix"
            assert isinstance(num,int) and num>0 and self.dim[0]-num>=0 and self.dim[1]-num>=0
            goal1=self.dim[0]-num
            goal2=self.dim[1]-num
            if goal1==0 and goal2==0:
                print("All rows have been deleted")
            self.__dim=[goal1,goal2]
            temp=[]
            for i in range(goal1):
                temp.append(self._matrix[i][:goal2])
            self._matrix=temp
            self._string=self._stringfy()
        except AssertionError:
            print("Enter a valid input")
        except Exception as err:
            print(err)
        else:
            if self.__features!=[]:
                self.__features=self.__features[:goal2]
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0  
            return self
        
    def find(self,element,start=1):
        """
        element: Real number
        start: 0 or 1. Index to start from 
        Returns the indeces of the given elements, multiple occurances are returned in a list
        """
        indeces=[]
        temp=self.copy.matrix
        try:
            assert start==0 or start==1
            assert isinstance(element,int) or isinstance(element,float) or isinstance(element,complex)
            for row in range(self.dim[0]):
                while element in temp[row]:
                    n=temp[row].index(element)
                    indeces.append((row+start,n+start))
                    temp[row][n]=""
        except AssertionError:
            print("Invalid arguments")
        else:
            if len(indeces):
                return indeces
            print("Value not in the matrix")
            return None
    
    def subM(self,rowS=None,rowE=None,colS=None,colE=None):
        """
Get a sub matrix from the current matrix
rowS:Desired matrix's starting row (starts from 1)
rowE:Last row(included)
colS:First column
colE:Last column(included)
    |col1 col2 col3
    |---------------
row1|1,1  1,2  1,3
row2|2,1  2,2  2,3
row3|3,1  3,2  3,3

EXAMPLES:
    ->a.subM(1)==gets the first element of the first row
    ->a.subM(2,2)==2by2 square matrix from top left as starting point
***Returns a new grid class/matrix***
        """
        try:
            temp2=[]
            if (rowS,rowE,colS,colE)==(None,None,None,None):
                return None
            #IF 2 ARGUMENTS ARE GIVEN, SET THEM AS ENDING POINTS
            if (rowS,rowE)!=(None,None) and (colS,colE)==(None,None):
                colE=rowE
                rowE=rowS
                rowS=1
                colS=1
            #IF MORE THAN 2 ARGUMENTS ARE GIVEN MAKE SURE IT IS 4 OF THEM AND THEY ARE VALID
            else:
                assert (rowS,rowE,colS,colE)!=(None,None,None,None) and (rowS,rowE,colS,colE)>(0,0,0,0)
            assert rowS<=self.dim[0] and rowE<=self.dim[0] and colS<=self.dim[1] and colE<=self.dim[1]
            
        except AssertionError:
            print("Bad arguments")
            print(self.subM.__doc__)
            return ""
        except Exception as err:
            print(err)
            return ""
        else:
            temp=self._matrix[rowS-1:rowE]
            if len(temp):
                temp2=[temp[c][colS-1:colE] for c in range(len(temp))]
                if isinstance(self,Identity):
                    return Identity(dim=len(temp2))
                elif isinstance(self,FMatrix):
                    return FMatrix(dim=[rowE-rowS+1,colE-colS+1],listed=temp2,features=self.__features[colS-1:colE],decimal=self.decimal)
                elif isinstance(self,CMatrix):
                    return CMatrix(dim=[rowE-rowS+1,colE-colS+1],listed=temp2,features=self.__features[colS-1:colE],decimal=self.decimal)
                else:
                    return Matrix(dim=[rowE-rowS+1,colE-colS+1],listed=temp2,features=self.__features[colS-1:colE])

# =============================================================================
    def _determinantByLUForm(self):
        try:
            if self.isSquare and self.dim[0]==1:
                return self.matrix[0][0]
            if not self.__detCalc:
                self._det=self._LU()[1]
                self.__detCalc=1
        except Exception as e:
            print("error ",e)
            return 0
        else:
            return self._det
# =============================================================================    
    def _transpose(self):
        try:
            assert self._valid==1
            temp=[a[:] for a in self.matrix]
            transposed=[]
            d0,d1=self.dim[0],self.dim[1]
            
        except Exception as err:
            print(err)
        else:
            for rows in range(d1):
                transposed.append(list())
                for cols in range(d0):
                    transposed[rows].append(temp[cols][rows])
            if self._fMat:
                return FMatrix([self.dim[1],self.dim[0]],listed=transposed,decimal=self.decimal)
            else:
                return Matrix([self.dim[1],self.dim[0]],listed=transposed)
# =============================================================================                
    def _minor(self,row=None,col=None):
        try:
            assert self._valid==1
            assert row!=None and col!=None
            assert row<=self.dim[0] and col<=self.dim[1]
            assert row>0 and col>0
        except AssertionError:
            print("Bad arguments")
        else:
            temp=self.copy
            if temp.dim[0]==1 and temp.dim[1]==1:
                return temp            
            if not temp.dim[0]<1:   
                temp.remove(r=row)
            if not temp.dim[1]<1: 
                temp.remove(c=col)
            return temp
# =============================================================================    
    def _adjoint(self):
        def __sign(pos):
            return (-1)**(pos[0]+pos[1])   
        try:
            assert self._valid==1
            assert self.isSquare
        except AssertionError:
            print("Not a square matrix")
        except Exception as err:
            print(err)
        else:
            adjL=[]
            for rows in range(0,self.dim[0]):
                adjL.append(list())
                for cols in range(0,self.dim[1]):
                    res=self._minor(rows+1,cols+1).det*__sign([rows,cols])
                    adjL[rows].append(res)
                    
            adjM=FMatrix(dim=self.dim,listed=adjL)
            self._adj=adjM.t
            self.__adjCalc=1
            return self._adj
# =============================================================================                           
    def _inverse(self):
        """
        Returns the inversed matrix
        """
        try:
            assert self.dim[0] == self.dim[1]
            assert self.det!=0
        except AssertionError:    
            if self.det==0:
                print("Determinant of the matrix is 0, can't find inverse")
            else:
                print("Must be a square matrix")
            return None
        except:
            print("Error getting inverse of the matrix")
        else:
            temp=self.copy
            temp.concat(Identity(self.dim[0]),"col")
            self._inv=temp.rrechelon.subM(1,self.dim[0],self.dim[1]+1,self.dim[1]*2)
            self.__invCalc=1
            return self._inv
# =============================================================================    
    def _Rank(self):
        """
        Returns the rank of the matrix
        """
        try:
            r=0
            temp=self._LU()[0]
            for rows in temp._matrix:
                if rows!=[0]*self.dim[1]:
                    r+=1
        except:
            return self._echelon()[1]
        else:
            return r
# =============================================================================        

    def _echelon(self):
        """
        Returns reduced row echelon form of the matrix
        """
        temp=self.copy
        i=0
        zeros=[0]*self.dim[1]
        while i <min(self.dim):
            #Find any zero-filled rows and make sure they are on the last row
            if zeros in temp.matrix:
                del(temp.matrix[temp.matrix.index(zeros)])
                temp.matrix.append(zeros)
                
            #Swap rows if diagonal is 0       
            if temp[i][i]==0:
                try:
                    i2=i
                    old=temp[i][:]
                    while temp[i2][i]==0 and i2<self.dim[0]:
                        i2+=1
                    temp[i]=temp[i2][:]
                    temp[i2]=old[:]
                except:
                    break
                
            #Do the calculations to reduce rows
            temp[i]=[temp[i][j]/temp[i][i] for j in range(self.dim[1])]
            temp._matrix=[[temp[k][m]-temp[i][m]*temp[k][i] for m in range(self.dim[1])] if k!=i else temp[i] 
                                                                                           for k in range(self.dim[0])]

            i+=1
        
        #Fix -0.0 issue
        temp._matrix=[[temp[i][j] if str(temp[i][j])!="-0.0" else 0 for j in range(temp.__dim[1])] for i in range(temp.__dim[0])]
        
        z=temp.matrix.count(zeros)   
        return (FMatrix(self.dim,temp.matrix),self.dim[0]-z)
            
# =============================================================================            
        
    def _symDecomp(self):
        try:
            assert self.isSquare
        except:
            print("Cant decompose the matrix into symmetric and antisymmetric matrices")
        else:
            m=self.matrix
            anti=FMatrix(self.dim,randomFill=0)
            for i in range(0,self.dim[0]-1):
                for j in range(i+1,self.dim[1]):
                    avg=(m[i][j]+m[j][i])/2
                    anti.matrix[i][j]=m[i][j]-avg
                    anti.matrix[j][i]=m[j][i]-avg
            sym=self-anti
            return (sym,anti)
        
    def _LU(self):
        """
        Returns L and U matrices of the matrix
        ***KNOWN ISSUE:Doesn't always work if determinant is 0 | linear system is inconsistant***
        ***STILL NEEDS CLEAN UP***
        """
        temp = self.copy
        rowC=0
        prod=1
        dia=[]
        i=0
        L=FMatrix(self.dim,randomFill=0)
        #Set diagonal elements to 1
        for diags in range(self.dim[0]):
            L[diags][diags]=1
        while i <min(self.dim):
            #Swap lines if diagonal has 0, stop when you find a non zero in the column
            if temp[i][i]==0:
                try:
                    i2=i
                    old=temp[i][:]
                    while temp[i2][i]==0 and i2<min(self.dim):
                        rowC+=1
                        i2+=1
                    temp[i]=temp[i2][:]
                    temp[i2]=old[:]
                except:
                    print("Determinant is 0, can't get lower/upper triangular matrices")
                    self.__detCalc=1
                    self._det=0
                    return [None,0,None]
                
            #Loop through the ith column find the coefficients to multiply the diagonal element with
            #to make the elements under [i][i] all zeros
            rowMulti=[temp[j][i]/temp[i][i] for j in range(i+1,self.dim[0])]
            #Loop to substitute ith row times the coefficient found from the i+n th row (n>0 & n<rows)
            k0=0
            for k in range(i+1,self.dim[0]):
                temp[k]=[temp[k][m]-(rowMulti[k0]*temp[i][m]) for m in range(self.dim[1])]
                #Lower triangular matrix
                L[k][i]=rowMulti[k0]
                k0+=1   
            #Get the diagonal for determinant calculation
            dia.append(temp[i][i])
            i+=1

        for element in dia:
            prod*=element
        U=FMatrix(temp.dim,listed=temp.matrix)
        return (U,((-1)**(rowC))*prod,L)

# =============================================================================
          
    def col(self,column=None,as_matrix=True):
        """
        Get a specific column of the matrix
        column:integer>=1 and <=column_amount
        as_matrix:False to get the column as a list, True to get a column matrix (default) 
        """
        try:
            assert isinstance(column,int)
            assert column>0 and column<=self.dim[1]
        except:
            print("Bad arguments")
            return None
        else:
            temp=[]
            for rows in self._matrix:
                temp.append(rows[column-1])
            
            if as_matrix:
                return self.subM(1,self.dim[0],column,column)
            return temp
    
    def row(self,row=None,as_matrix=True):
        """
        Get a specific row of the matrix
        row:integer>=1 and <=row_amount
        as_matrix:False to get the row as a list, True to get a row matrix (default) 
        """
        try:
            assert isinstance(row,int)
            assert row>0 and row<=self.dim[0]
        except:
            print("Bad arguments")
            return None
        else:
            if as_matrix:
                return self.subM(row,row,1,self.dim[1])
            return self._matrix[row-1]
            
# =============================================================================
    """Properties available for public"""               
# =============================================================================
    @property
    def p(self):
        print(self)
   
    @property
    def grid(self):
        if not self._isIdentity:
            self.__dim=self._declareDim()
            self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        print(self._string)
    
    @property
    def copy(self):
        if self._isIdentity:
            if self==Identity(self.dim[0]):
                return Identity(self.dim[0])
            else:
                return FMatrix(dim=self.dim[:],listed=self.matrix,features=self.features)
        elif self._fMat:
            return FMatrix(dim=self.dim[:],listed=self._matrix,randomFill=0,header=self._header,directory=self._dir,features=self.__features,decimal=self.decimal)
        else:
            return Matrix(dim=self.dim[:],listed=self._matrix,randomFill=0,header=self._header,directory=self._dir,features=self.__features)
    
    @property
    def string(self):
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        return " ".join(self.__features)+self._string
    
    @property
    def directory(self):
        return self._dir[:]
    
    @property
    def features(self):
        return self.__features[:]
    @features.setter
    def features(self,li):
        if self._valid:
            try:
                assert isinstance(li,list)
                assert len(li)==self.dim[1]
            except AssertionError:
                print("Give the feature names as a list of strings with the right amount")
            else:
                temp=[str(i) for i in li]
                self.__features=temp
                
    @property
    def dim(self):
        return self.__dim[:]
    @dim.setter
    def dim(self,val):
        if self._valid:
            try:
                a=self.dim[0]*self.dim[1]
                if isinstance(val,int):
                    assert val>0
                    val=[val,val]
                elif isinstance(val,list):
                    assert len(val)==2
                else:
                    return None
                assert val[0]*val[1]==a
            except:
                return None
            else:
                els=[]
                for rows in self.matrix:
                    for cols in rows:
                        els.append(cols)
                new=[]
                i=-1
                for r in range(val[0]):
                    i+=1
                    new.append([])
                    for c in range(val[1]):
                        new[i].append(els[c+val[1]*r])
                self.__init__(dim=val,listed=new)
            
    @property
    def uptri(self):
        return self._LU()[0]
    
    @property
    def lowtri(self):
        return self._LU()[2]
    
    @property
    def rank(self):
        if not self.__rankCalc:
            self._rank=self._Rank()
        return self._rank
    
    @property
    def rrechelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._echelon()[0]
    
    @property
    def t(self):
        return self._transpose()
    
    @property
    def adj(self):
        if self.__adjCalc:
            return self._adj
        return self._adjoint()
    
    @property
    def inv(self):
        if self.__invCalc:
            return self._inv
        return self._inverse()    
    
    @property
    def matrix(self):
       return self._matrix
   
    @property
    def det(self):
        try:
            assert self.isSquare
        except AssertionError:
            print("Not a square matrix")
        else:
            if self.__detCalc:
                return self._det
            else:
                return self._determinantByLUForm()  
            
    @property
    def highest(self):
        if not self._isIdentity:
            return max([max(a) for a in self.ranged().values()])
        else:
            return 1
        
    @property
    def lowest(self):
        if not self._isIdentity:
            return min([min(a) for a in self.ranged().values()])  
        else:
            return 0
        
    @property
    def obj(self):
        #ranged and randomFill arguments are NOT required to create the same matrix
        if self._cMat:
            return "CMatrix(dim={0},listed={1},ranged={2},randomFill={3},features={4},header={5},directory='{6}',decimal={7})".format(self.dim,self._matrix,self._initRange,self._randomFill,self.__features,self._header,self._dir,self.decimal)
        elif self._fMat:
            return "FMatrix(dim={0},listed={1},ranged={2},randomFill={3},features={4},header={5},directory='{6}',decimal={7})".format(self.dim,self._matrix,self._initRange,self._randomFill,self.__features,self._header,self._dir,self.decimal)
        elif not self._isIdentity:
            return "Matrix(dim={0},listed={1},ranged={2},randomFill={3},features={4},header={5},directory='{6}')".format(self.dim,self._matrix,self._initRange,self._randomFill,self.__features,self._header,self._dir)
        else:
            return None

    @property
    def sym(self):
        return self._symDecomp()[0]
    
    @property
    def anti(self):
        return self._symDecomp()[1]
    
    @property
    def isSquare(self):
        return self.dim[0]==self.dim[1]
    
    @property
    def isSymmetric(self):
        if not self.isSquare:
            return False
        return self.t==self
        
    @property  
    def isAntiSymmetric(self):
        if not self.isSquare:
            return False
        return self.t*-1==self
    
    @property
    def isSkewSymmetric(self):
        if self.isSymmetric:
            return self.dim[0] == [1 if self.matrix[a][a]==0 else 0 for a in range(self.dim[0])].count(1)
        return False
    
    @property
    def isTriangular(self):
        from functools import reduce
        if not self.isSquare:
            return False
        return self.det == reduce((lambda a,b: a*b),[self.matrix[a][a] for a in range(self.dim[0])])
    
    @property
    def isUpperTri(self):
        if not self.isSquare:
            return False
        if self.isTriangular:
            for i in range(1,self.dim[0]):
                for j in range(i):
                    if self.matrix[i][j]!=0:
                        return False
            return True
        return False
    
    @property
    def isLowerTri(self):
        if not self.isSquare:
            return False
        if self.isTriangular:
            for i in range(self.dim[0]):
                for j in range(i+1,self.dim[1]):
                    if self.matrix[i][j]!=0:
                        return False
            return True
        return False
    
    @property
    def isDiagonal(self):
        return self.isUpperTri and self.isLowerTri
    
    @property
    def isIdempotent(self):
        return self==self*self
    
    @property
    def isOrthogonal(self):
        pass
    
    @property
    def nilpotency(self):
        pass
    
    @property
    def floorForm(self):
        return Matrix(self.dim[:],listed=self.__floor__().matrix)  
    
    @property
    def ceilForm(self):
        return Matrix(self.dim[:],listed=self.__ceil__().matrix)   
    
    @property   
    def intForm(self):
        return Matrix(self.dim[:],listed=self.__floor__().matrix)
    
    @property   
    def floatForm(self):
        t=[]
        for a in self._matrix:
            t.append([float(b) for b in a])            
        return FMatrix(self.dim[:],listed=t)
    
    def roundForm(self,decimal=1):
        if decimal==0:
            return Matrix(self.dim[:],listed=round(self,decimal).matrix)
        return FMatrix(self.dim[:],listed=round(self,decimal).matrix)
    
    def head(self,rows=5):
        if self.dim[0]>=rows:
            return self.subM(1,rows,1,self.dim[1])
        return self.subM(1,self.dim[0],1,self.dim[1])

    def tail(self,rows=5):
        if self.dim[0]>=rows:
            return self.subM(self.dim[0]-rows+1,self.dim[0],1,self.dim[1])
        return self.subM(1,self.dim[0],1,self.dim[1])
    
    def minor(self,r=None,c=None):
        return self._minor(row=r,col=c)
    
    def ranged(self,col=None):
        self._inRange=self._declareRange(self._matrix)
        if col==None:
            return self._inRange
        return self._inRange[self.__features[col-1]]
    
    def mean(self,col=None):
        """
        Sets the "mean" attribute of the matrix as the mean of it's elements
        """
        try:
            assert (isinstance(col,int) and col>=1 and col<=self.dim[1]) or col==None
            avg={}
            feats=self.features[:]
            if len(feats)==0:
                for nn in range(self.dim[1]):
                    feats.append("Col "+str(nn+1))
      
            if col==None:
                cLow=0
                cUp=self.dim[1]
            else:
                cLow=col-1
                cUp=col        
                    
            for c in range(cLow,cUp):
                t=0
                for r in range(self.dim[0]):
                    t+=self[r][c]
                avg[feats[c]]=t/self.dim[0]
   
        except AssertionError:
            print("Col parameter should be in range [1,amount of columns]")
        except Exception as err:
            print("Bad matrix and/or dimension")
            print(err)
            return None
        
        else:
            return avg    

    def sdev(self,col=None,population=0):
        """
        Standard deviation of the columns
        col:integer>=1
        population: 1 for σ, 0 for s value (default 0)
        """
        try:
            assert self.dim[0]>1
            assert population==0 or population==1
        except:
            print("Can't get standard deviation")
        else:
            if col==None:
                sd={}
                avgs=self.mean()
                for i in range(self.dim[1]):
                    e=0
                    for j in range(self.dim[0]):
                        e+=(self.matrix[j][i]-avgs[self.__features[i]])**2
                    sd[self.__features[i]]=(e/(self.dim[0]-1+population))**(1/2)
                return sd
            else:
                try:
                    assert col>0 and col<=self.dim[1]
                except AssertionError:
                    print("Col parameter is not valid")
                else:
                    sd={}
                    a=list(self.mean(col).values())[0]

                    e=0
                    for i in range(self.dim[0]):
                        e+=(self.matrix[i][col-1]-a)**2
                        
                    sd[self.__features[col-1]] = (e/(self.dim[0]-1+population))**(1/2)
                    return sd
                
    def median(self,col=None):
        """
        Returns the median of the columns
        col:integer>=1 and <=column amount
        """
        try:
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                feats=self.__features[col-1]
                    
            meds={}
            i=1
            for rows in temp.matrix:
                
                n=sorted(rows)[self.dim[0]//2]
                
                if len(feats)!=0 and isinstance(feats,list):
                    meds[feats[i-1]]=n
                elif len(feats)==0:
                    meds["Col "+str(i)]=n
                else:
                    meds[feats]=n
                i+=1
        except:
            print("Error getting median")
        else:
            return meds
    
    def mode(self,col=None):
        """
        Returns the columns' most repeated elements
        col:integer>=1 and <=amount of columns
        """
        try:
            #Set feature name and the matrix to use dependent on the column desired
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                feats=self.features[col-1]
            #Set keys in the dictionary which will be returned at the end
            mods={}
            if len(feats)!=0 and isinstance(feats,list):
                for fs in feats:
                    mods[fs]=None
            elif len(feats)==0:
                for fs in range(self.dim[1]):
                    mods["Col "+str(fs+1)]=None
                   
            #Set column amount
            if col==None:
                r=self.dim[1]
            else:
                r=1
                
            #Loop through the transpozed matrices (From column to row matrices to make calculations easier)               
            for rows in range(r):
                #Variables to keep track of the frequency of the numbers
                a={}
                #Loop through the column to get frequencies
                for els in temp[rows]:
                    if els not in a.keys():
                        a[els]=1
                    else:
                        a[els]+=1

                #Get a list of the values from the frequency dictionary
                temp2=[]
                for k,v in a.items():
                    temp2.append(v)
                
                #Find the maximum repetation
                m=max(temp2)
                #Create a dictionary to store the most repated key(s) as keys and frequency as the value
                n={}
                s=""
                allSame=0
                #Check if there are multiple most repeated elements
                for k,v in a.items(): 
                    if v==m:
                        allSame+=1
                        if len(s)!=0:
                            s+=", "+str(k)
                        else:
                            s+=str(k)
                #If all the elements repeated same amount don't get all the numbers, just set the name to "All"          
                if allSame==len(temp2):
                    n["All"]=temp2[0]
                else:
                    n[s]=m
                
                #Set the final dictionary's key(s) and  value(s) calculated
                if len(feats)!=0 and isinstance(feats,list):
                    mods[feats[rows]]=n
                elif len(feats)==0:
                    mods["Col "+str(rows+1)]=n
                else:
                    mods[feats]=n
                #END
        except Exception as err:
            print("Bad arguments given to mode method\n",err)
        else:
            return mods
        
    def freq(self,col=None):
        """
        returns the frequency of every element on desired column(s)
        col:column
        """
        try:
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                feats=self.features[col-1]

    
            res={}
            if col==None:
                r=self.dim[1]
            else:
                r=1

            for rows in range(r):
                a={}
                for els in temp[rows]:
                    if els not in a.keys():
                        a[els]=1
                    else:
                        a[els]+=1
                if col!=None:
                    res[feats]=a
                else:
                    res[feats[rows]]=a
        except:
            print("Bad indeces in freq method")
        else:
            return res

    def iqr(self,col=None,as_quartiles=False):
        """
        Returns the interquartile range(IQR)
        col:integer>=1 and <=column amount
        as_quartiles:
            True to return dictionary as:
                {Column1=[First_Quartile,Median,Third_Quartile],Column2=[First_Quartile,Median,Third_Quartile],...}
            False to get iqr values(default):
                {Column1=IQR_1,Column2=IQR_2,...}
        """
        
        try:
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                feats=self.__features[col-1]
                    
            iqr={}
            qmeds={}
            i=1
            for rows in temp.matrix:
                low=sorted(rows)[:self.dim[0]//2]
                low=low[len(low)//2]
                
                up=sorted(rows)[self.dim[0]//2:]
                up=up[len(up)//2]
                
                if len(feats)!=0 and isinstance(feats,list):
                    iqr[feats[i-1]]=up-low
                    qmeds[feats[i-1]]=[low,self.median(col)[feats[i-1]],up]
                elif len(feats)==0:
                    iqr["Col "+str(i)]=up-low
                    qmeds["Col "+str(i)]=[low,self.median(col)["Col "+str(i)],up]
                else:
                    iqr[feats]=up-low
                    qmeds[feats]=[low,self.median(col)[feats],up]
                i+=1
        except Exception as err:
            print("Error getting iqr: ",err)
        else:
            if as_quartiles:
                return qmeds
            return iqr
        
    def variance(self,col=None,population=0):
        s=self.sdev(col,population)
        vs={}
        for k,v in s.items():
            vs[k]=v**2
        return vs
    
    def z(self,row=None,col=None):
        try:
            if col==None:
                assert (isinstance(row,int) and row>=1 and row<=self.dim[1]) or row==None
                dims=self.dim
                feats=self.features
                sub=self.copy
            elif isinstance(col,int) and col>=1 and col<=self.dim[1] and row==None:
                dims=[self.dim[0],1]
                feats=self.features[col-1]
                sub=self.subM(1,self.dim[0],col,col)
                col=1
            else:
                assert isinstance(col,int) and col>=1 and col<=self.dim[1]
                assert isinstance(row,int) and row>=1 and row<=self.dim[0]
                return (self[row-1][col-1]-self.mean(col))/self.sdev(col)
                
        except:
            print("error getting z scores")
        else:
            scores=FMatrix(dims,randomFill=0,features=feats)
            m=sub.mean(col)
            s=sub.sdev(col,1)
            names=[n for n in m.keys()]

            for c in range(scores.dim[1]):
                key=names[c]
                for r in range(scores.dim[0]):
                    scores[r][c]=(sub.matrix[r][c]-m[key])/s[key]
            if row!=None and col==None:
                return scores.subM(row,row,1,self.dim[1])    
            return scores
        
    def corr(self,col1=None,col2=None):
        """
        Pearson correlation coefficient r
        Not optimal for big datasets yet
        """
        def calc(c1,c2):
            z1=self.z(col=c1)
            z2=self.z(col=c2)
            prod=(z1*z2).col(1,as_matrix=False)
            return sum(prod)/(self.dim[0]-1)
        
        try:
            if self.dim[1]<2 or self.dim[0]<=1:
                print("Not enough columns/rows")
                return None            
            if col1!=None and col2!=None:
                assert isinstance(col1,int) and isinstance(col1,int)
                assert col1>=1 and col1<=self.dim[1] and col2>=1 and col2<=self.dim[1]
                return calc(col1,col2)
            
            elif col1==None and col2==None:
                temp=FMatrix(self.dim[1],randomFill=0)+Identity(self.dim[1])
                for i in range(self.dim[1]):
                    for j in range(1+i,self.dim[1]):
                        c=calc(i+1,j+1)
                        temp[j][i]=c
                        temp[i][j]=c
                return temp
        except Exception as err:
            print("Error getting pearson correlation:",err)
    
    def _eigenvalues(self):
        """
        ***** Currently doesn't work as intended for matrices bigger than 3x3 *****
        return the eigenvalues
        """
        try:
            assert self.isSquare and self.dim[0]>=2
            if self.dim[0]==2:
                d=self.det
                tr=self.matrix[0][0]+self.matrix[1][1]
                return list(set([(tr+(tr**2 - 4*d)**(1/2))/2,(tr-(tr**2 - 4*d)**(1/2))/2]))
        except:
            print("error getting eigenvalues")
        else:
            temp=self.copy
            for i in range(self.dim[0]):
                temp[i][i]="("+str(temp[i][i])+"-x)"
            st=temp.chareq
            print(st)
            ce=(lambda x:eval(st))
            return ce
    
    @property
    def eigenvalues(self):
        return self._eigenvalues()
    
    @property
    def chareq(self):
        m=self.matrix
        if self.dim[0]==2:
            return  f"(({m[0][0]}*{m[1][1]})-({m[0][1]}*{m[1][0]}))"
        s=""
        sign=0
        for co in range(self.dim[1]):
            
            c=m[0][co]*((-1)**sign)
            sign+=1
            
            temp=self.copy
            temp.remove(r=1)
            temp.remove(c=co+1)
            
            s+=f"(({c})*"
            s+=temp.chareq
            
            if co!=self.dim[1]-1:
                s+=")+"
            else:
                s+=")"
        return s
                
        
# =============================================================================
    def __contains__(self,val):
        """
        val:value to search for in the whole matrix
        Returns True or False
        syntax: "value" in a.matrix
        """
        inds=self.find(val)
        return bool(inds)
    
    def concat(self,matrix,concat_as="row"):
        """
        Concatenate matrices row or columns vice
        b:matrix to concatenate to self
        concat_as:"row" to concat b matrix as rows, "col" to add b matrix as columns
        Note: This method concatenates the matrix to self
        """
        try:
            assert isinstance(matrix,Matrix)
            if concat_as=="row":
                assert matrix.dim[1]==self.dim[1]
            elif concat_as=="col":
                assert matrix.dim[0]==self.dim[0]
            b=matrix.copy
        except AssertionError:
            print("Bad dimensions at concat")
        else:
            if concat_as=="row":
                for rows in b.matrix:
                    self._matrix.append(rows)

            else:
                i=0
                for rows in self.matrix:
                    for cols in range(b.dim[1]):
                        rows.append(b[i][cols])
                    i+=1
                    
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0  
            self.__dim=self._declareDim()
            if concat_as=="col":
                if isinstance(matrix,Identity):
                    self.__features+=["Col {}".format(i+1) for i in range(self.dim[1]-matrix.dim[1],self.dim[1])]
                else:
                    self.__features+=matrix.features
            self._inRange=self._declareRange(self._matrix)    
            self._string=self._stringfy()
                  
# =============================================================================

    def __getitem__(self,pos):
        try:
            self.__rankCalc=0
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            if isinstance(pos,slice) or isinstance(pos,int):
                return self.matrix[pos]
        except:
            return None
        
    def __setitem__(self,pos,item):
        try:
            if isinstance(pos,slice) and  isinstance(item,list):
                if len(item)>0:
                    if isinstance(item[0],list):
                        self._matrix[pos]=item
                    else:
                        self._matrix[pos]=[item]
                
            elif isinstance(pos,int) and isinstance(item,list):
                if len(item)==self.dim[1]: 
                    row=pos
                    self._matrix[row]=item[:]
                    self.__dim=self._declareDim()
                else:
                    print("Check the dimension of the given list")
        except:
            print(pos,item)
            return None
        else:
            self.__rankCalc=0
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            return self
    
    def __len__(self):
        return self.dim[0]*self.dim[1]
# =============================================================================

    def __matmul__(self,other):
        try:
            assert self.dim[1]==other.dim[0]
        except:
            print("Can't multiply")
        else:
            temp=[]
            
            for r in range(self.dim[0]):
                temp.append(list())
                for rs in range(other.dim[1]):
                    temp[r].append(0)
                    total=0
                    for cs in range(other.dim[0]):
                        num=self.matrix[r][cs]*other.matrix[cs][rs]
                        total+=num
                    temp[r][rs]=total
            if isinstance(self,FMatrix):
                a=self.decimal
            if isinstance(other,FMatrix):
                a=other.decimal
            if isinstance(other,FMatrix) or isinstance(self,FMatrix):
                return FMatrix(dim=[self.dim[0],other.dim[1]],listed=temp,decimal=a)
            return Matrix(dim=[self.dim[0],other.dim[1]],listed=temp)
################################################################################    
    def __add__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]+other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except:
                print("Can't add")
                return self
            else:
                if isinstance(self,FMatrix):
                    a=self.decimal
                if isinstance(other,FMatrix):
                    a=other.decimal
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=a)
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]+other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't add")
                return self
            else:
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)

        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't add")
                return self
            else:
                temp=[[self.matrix[rows][cols]+other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't add")
################################################################################            
    def __sub__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]-other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except:
                print("Can't subtract")
                return self
            else:
                if isinstance(self,FMatrix):
                    a=self.decimal
                if isinstance(other,FMatrix):
                    a=other.decimal
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=a)
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]-other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't subtract")
                return self
            else:
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)

        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't subtract")
                return self
            else:
                temp=[[self.matrix[rows][cols]-other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't subtract")
################################################################################     
    def __mul__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]*other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except:
                print("Can't multiply")
            else:
                if isinstance(self,FMatrix):
                    a=self.decimal
                if isinstance(other,FMatrix):
                    a=other.decimal
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=a)
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]*other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't multiply") 
            else:
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)

        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't multiply")
                return self
            else:
                temp=[[self.matrix[rows][cols]*other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't multiply")
################################################################################
    def __floordiv__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]//other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't divide") 
                return self
            else:
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]//other for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't divide") 
                return self
            else:
                return Matrix(dim=self.dim,listed=temp)
                
        elif isinstance(other,list):
            if len(other)!=self.dim[1]:
                print("Can't divide")
                return self
            else:
                try:
                    temp=[[self.matrix[rows][cols]//other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                except ZeroDivisionError:
                    print("Division by 0")
                    return self
                except:
                    print("Can't divide") 
                    return self
                else:
                    return Matrix(dim=self.dim,listed=temp) 
        else:
            print("Can't divide")
################################################################################            
    def __truediv__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]/other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't divide") 
                return self
            else:
                if isinstance(self,FMatrix):
                    a=self.decimal
                if isinstance(other,FMatrix):
                    a=other.decimal
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=a)
                return Matrix(dim=self.dim,listed=temp)  
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]/other for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't divide") 
                return self
            else:
                if isinstance(self,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)  
        elif isinstance(other,list):
            if len(other)!=self.dim[1]:
                print("Can't divide")
                return self
            else:
                try:
                    temp=[[self.matrix[rows][cols]/other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                except ZeroDivisionError:
                    print("Division by 0")
                    return self
                except:
                    print("Can't divide") 
                    return self
                else:
                    if isinstance(self,FMatrix):               
                        return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                    return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't divide")
################################################################################
    def __mod__(self, other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]%other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't get modular") 
                return self
            else:
                if isinstance(self,FMatrix):
                    a=self.decimal
                if isinstance(other,FMatrix):
                    a=other.decimal
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=a)
                return Matrix(dim=self.dim,listed=temp)  
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]%other for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't get modular") 
                return self
            else:
                if isinstance(self,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)  
        elif isinstance(other,list):
            if len(other)!=self.dim[1]:
                print("Can't get modular")
                return self
            else:
                try:
                    temp=[[self.matrix[rows][cols]%other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                except ZeroDivisionError:
                    print("Division by 0")
                    return self
                except:
                    print("Can't get modular") 
                    return self
                else:
                    if isinstance(self,FMatrix):               
                        return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                    return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't get modular")
################################################################################         
    def __pow__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]**other[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except:
                print("Can't raise to the given power")
            else:
                if isinstance(self,FMatrix):
                    a=self.decimal
                if isinstance(other,FMatrix):
                    a=other.decimal
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):               
                    return FMatrix(dim=self.dim,listed=temp,decimal=a)
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(other,int) or isinstance(other,float):
            try:
                temp=[[self.matrix[rows][cols]**other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't raise to the given power")            
            else:
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)

        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't raise to the given power")                
                return self
            else:
                temp=[[self.matrix[rows][cols]**other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                if isinstance(self,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't raise to the given power")
################################################################################                    
    def __lt__(self,other):
        if self._valid==1 and other._valid==1:
            if self.dim==other.dim:
                if self.matrix==other.matrix:
                    return False
                elif self.isSquare:
                    return self.det<other.det
                else:
                    return None
            elif self.isSquare and other._dim[0]==other._dim[1] :   
                return self.det<other.det
            else:
                return None
        print("Invalid matrices")
        return None
    
    def __eq__(self,other):
        if self._valid==1 and other._valid==1:
            if self.dim==other.dim:
                if self.matrix==other.matrix:
                    return True
                return False
            else:   
                return False
        print("Invalid matrices")
        return None
    
    def __gt__(self,other):
        if self._valid==1 and other._valid==1:
            if self.dim==other.dim:
                if self.matrix==other.matrix:
                    return False
                elif self.isSquare:
                    return self.det>other.det
                else:
                    return None
            elif self.isSquare and other._dim[0]==other._dim[1] :   
                return self.det>other.det
            else:
                return None
        print("Invalid matrices")
        return None
# =============================================================================
    
    def __round__(self,n=-1):
        if self._fMat and n<0:
            n=1
        temp=[]
        for elements in self._matrix:
            temp.append([round(a,n) for a in elements])
        return FMatrix(self.dim[:],listed=temp)
    
    def __floor__(self):
        temp=[]
        for elements in self._matrix:
            temp.append([int(a) for a in elements if isinstance(a,float) or isinstance(a,int)])
        return Matrix(self.dim[:],listed=temp)       
    
    def __ceil__(self):
        temp=[]
        for elements in self._matrix:
            temp.append([int(a)+1 for a in elements if isinstance(a,float) or isinstance(a,int)])
        return Matrix(self.dim[:],listed=temp)    
    
    def __abs__(self):
        temp=[]
        for elements in self._matrix:
            temp.append([abs(a) for a in elements])
        if isinstance(self,FMatrix):
            return FMatrix(self.dim[:],listed=temp)   
        return Matrix(self.dim[:],listed=temp)
    
    def __repr__(self):
        return str(self.matrix)
    
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        self.__dim=self._declareDim()
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        if self._badDims:
            print("You should give proper dimensions to work with the data\nExample dimension:[data_amount,feature_amount]")
        if self._valid:
            if not self.isSquare:
                print("\nDimension: {0}x{1}\nFeatures: {2}".format(self.dim[0],self.dim[1],self.features))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nFeatures: {1}".format(self.dim[0],self.features))
            return self._string+"\n"
            
        else:
            return "Invalid matrix\n"
    
# =============================================================================

class Identity(Matrix):
    """
Identity matrix
    """
    def __init__(self,dim=1):     
        self._valid=1
        try:
            assert isinstance(dim,int)
            assert dim>0
        except AssertionError:
            print("Give integer as the dimension")
            self._valid=0
            return None
        else:
            super().__init__(dim,randomFill=0)
            self._setMatrix()
                
    def _setMatrix(self):
        self._matrix=[[0 for a in range(self.dim[1])] for b in range(self.dim[0])]
        for row in range(0,self.dim[0]):
            self._matrix[row][row]=1          
                
    def addDim(self,num):
        """
        Add dimensions to identity matrix
        """
        try:
            assert isinstance(num,int) and num>0
        except AssertionError:
            print("Invalid input in addDim")
        except Exception as err:
            print(err)
        else:
            goal=self.dim[0]+num
            self.__dim=[goal,goal]
            self._setMatrix()
            self._string=self._stringfy()
            return self
        
    def delDim(self,num):
        """
        Delete dimensions to identity matrix
        """
        try:
            if self.matrix==[]:
                return "Empty matrix"
            assert isinstance(num,int) and num>0 and self.dim[0]-num>=0
        except AssertionError:
            print("Invalid input in delDim")
        except Exception as err:
            print(err)
        else:
            goal=self.dim[0]-num
            if goal==0:
                print("All rows have been deleted")
            self.__dim=[goal,goal]
            self._setMatrix()
            self._string=self._stringfy()
            return self
        
    @property
    def obj(self):
        return "Identity(dim={0})".format(self.dim)
    
    def __str__(self):
        if self._isIdentity:
            self._string=self._stringfy()
            print("\nIdentity Matrix\nDimension: {0}x{0}".format(self.dim[0]))
            return self._string+"\n"
        
class FMatrix(Matrix):
    """
Matrix which contain float numbers
decimal: digits to round up to 
    """
    def __init__(self,
                 dim = None,
                 listed = [],
                 directory = r"",
                 ranged = [0,1],
                 randomFill = True,
                 header = False,
                 features = [],
                 decimal = 4):
        
        self.__decimal=decimal
        super().__init__(dim,listed,directory,ranged,randomFill,header,features)
        
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        if self._badDims:
            print("You should give proper dimensions to work with the data\nExample dimension:[data_amount,feature_amount]")

        print("\nFloat Matrix",end="")
        self.__dim=self._declareDim()
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        if self._valid:
            if not self.isSquare:
                print("\nDimension: {0}x{1}\nFeatures: {2}".format(self.dim[0],self.dim[1],self.features))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nFeatures: {1}".format(self.dim[0],self.features))
            return self._string+"\n"
        else:
            return "Invalid matrix\n"
    @property
    def decimal(self):
        return self.__decimal
    @decimal.setter
    def decimal(self,val):
        try:
            assert isinstance(self,FMatrix) or isinstance(self,CMatrix)
            assert isinstance(val,int)
            assert val>=1
        except:
            print("Invalid argument")
        else:
            self.__decimal=val 
            
class CMatrix(FMatrix):
    """
Matrix which contain complex numbers
    """
    def __init__(self,
                 dim = None,
                 listed = [],
                 directory = r"",
                 ranged = [0,1],
                 randomFill = True,
                 header = False,
                 features = [],
                 decimal = 4):
        
        self.__decimal=decimal
        super().__init__(dim,listed,directory,ranged,randomFill,header,features,decimal)
        
    def __str__(self):
        print("\nComplex Matrix",end="")
        self.__dim=self._declareDim()
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        if self._valid:
            if not self.isSquare:
                print("\nDimension: {0}x{1}".format(self.dim[0],self.dim[1]))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}".format(self.dim[0]))            
                
            return self._string+"\n"

class SMatrix(Matrix):
    """
Matrix with strings as elements
    """
    def __init__(self,*args,**kwargs):
        pass
