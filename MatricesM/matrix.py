# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""
from MatricesM.validations.validate import *
from MatricesM.errors.errors import *
from random import random,randint,uniform,triangular,gauss,seed

class Matrix:
    """
    dim:int|list|tuple; dimensions of the matrix. Giving integer values creates a square matrix
    
    listed:str|list of lists of numbers|list of numbers|str; Elements of the matrix. Can extract all the numbers from a string.
    
    directory:str; directory of a data file(e.g. 'directory/datafile' or r'directory\datafile')
    
    fill: uniform|triangular|gauss or int|float|complex|str|list|range or None; fills the matrix with chosen distribution or the value, default is uniform distribution

    ranged:->To apply all the elements give a list | tuple
           ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
           ->Arguments should follow one of the following rules:
                1)If 'fill' is uniform, interval to pick numbers from as [minimum,maximum]; 
                2)If 'fill' is gauss, mean and standard deviation are picked from this attribute as [mean,standard_deviation];
                3)If 'fill' is triangular, range of the numbers and the mode as [minimum,maximum,mode]

    header:boolean; takes first row as header title
    
    features:list of strings; column names
    
    seed:int; seed to use while generating random numbers, not useful when fill isn't one of [uniform,triangular,gauss]
    
    decimal:int; Digits to round to and print

    dtype:'integer'|'float'|'complex'|'dataframe'; type of values the matrix will hold, 
            ->'dataframe' requires type specification for each column given to 'coldtypes' parameter
            Example:
                data = Matrix(directory=data_directory, header=1, dtype='dataframe', coldtypes=[str,float,float,int,str])

    coldtypes:tuple|list (Contains the objects, not names of them); data types for each column individually. Only works if dtype is set to 'dataframe'

    implicit:boolean; Skip matrix setting operations if all necessary parameters are given and expected to work without any formatting etc.

    Check https://github.com/MathStuff/MatricesM  for further explanation and examples
    """

    def __init__(self,
                 dim=None,
                 listed=[],
                 directory="",
                 fill=uniform,
                 ranged=[0,1],
                 seed=None,
                 header=False,
                 features=[],
                 decimal=4,
                 dtype="float",
                 coldtypes=[],
                 implicit=False):  
        
        self._matrix = listed
        self._dir = directory
        self._header = header

        self.__dim = dim
        self.__coldtypes = coldtypes
        self.__initRange = ranged
        self.__fill = fill
        self.__seed = seed
        self.__features = features
        self.__decimal = decimal
        self.__dtype = dtype
        self.__seed = seed

        self._setDim(dim)
        self.setInstance()
        if not implicit:
            self.setMatrix(self.__dim,self.__initRange,self._matrix,self._dir,self.__fill,self._cMat,self._fMat)
        self.setFeatures()
        self.setcoldtypes(declare=bool(not implicit))

        self.ROW_LIMIT = 30
        self.COL_LIMIT = 12
        self.EIGEN_ITERS = 150
# =============================================================================
    """Attribute formatting and setting methods"""
# =============================================================================    
    def setInstance(self):
        """
        Set the type
        """
        from MatricesM.setup.instances import _setInstance
        _setInstance(self)
            
    def setFeatures(self):
        """
        Set default feature names
        """
        if len(self.__features)!=self.dim[1]:
            self.__features=["Col {}".format(i+1) for i in range(self.dim[1])]
    
    def setcoldtypes(self,declare=False):
        """
        Set column dtypes
        """
        if not validlist(self.matrix):
            return None
        if len(list(self.coldtypes))!=self.dim[1]:
            self.__coldtypes=[type(self.matrix[0][i]) for i in range(self.dim[1])]
        if declare and self.dtype=="dataframe":
            for i in range(self.dim[0]):
                j=0
                while j<self.dim[1]:
                    try:
                        if self.coldtypes[j] != type: 
                            self._matrix[i][j] = self.coldtypes[j](self._matrix[i][j])
                        j+=1
                    except:
                        j+=1
                        continue
           
    def _setDim(self,d):
        """
        Set the dimension to be a list if it's an integer
        """
        from MatricesM.setup.dims import setDim
        setDim(self,d)
        
    def setMatrix(self,d=None,r=None,lis=[],direc=r"",f=uniform,cmat=False,fmat=True):
        """
        Set the matrix based on the arguments given
        """
        from MatricesM.setup.matfill import setMatrix
        setMatrix(self,d,r,lis,direc,f,cmat,fmat)
        
# =============================================================================
    """Attribute recalculation methods"""
# =============================================================================    
    def _declareDim(self):
        """
        Set new dimension 
        """
        from MatricesM.setup.declare import declareDim
        return declareDim(self)
    
    def _declareRange(self,lis):
        """
        Finds and returns the range of the elements in a given list
        """
        from MatricesM.setup.declare import declareRange
        return declareRange(self,lis)
    
# =============================================================================
    """Methods for rading from the files"""
# =============================================================================
    @staticmethod
    def __fromFile(d,header,dtyps):
        """
        Read all the lines from a file
        """
        from MatricesM.setup.fileops import readAll
        return readAll(d,header,dtyps)
    
# =============================================================================
    """Element setting methods"""
# =============================================================================
    def _listify(self,stringold):
        """
        Finds all the numbers in the given string
        """
        from MatricesM.setup.listify import _listify
        return _listify(self,stringold)
            
    def _stringfy(self,coldtypes=None):
        """
        Turns a list into a grid-like form that is printable
        Returns a string
        """
        from MatricesM.setup.stringfy import _stringfy
        return _stringfy(self,coldtypes)
    
# =============================================================================
    """Row/Column methods"""
# =============================================================================
    def head(self,rows=5):
        """
        First 'rows' amount of rows of the matrix
        Returns a matrix
        rows : integer>0 | How many rows to return
        """
        if not isinstance(rows,int):
            raise InvalidIndex(rows,"Rows should be a positive integer number")
        if rows<=0:
            raise InvalidIndex(rows,"rows can't be less than or equal to 0")
        if self.dim[0]>=rows:
            return self[:rows]
        return self[:,:]

    def tail(self,rows=5):
        """
        Last 'rows' amount of rows of the matrix
        Returns a matrix
        rows : integer>0 | How many rows to return
        """
        if not isinstance(rows,int):
            raise InvalidIndex(rows,"Rows should be a positive integer number")
        if rows<=0:
            raise InvalidIndex(rows,"rows can't be less than or equal to 0")
        if self.dim[0]>=rows:
            return self[self.dim[0]-rows:]
        return self[:,:]

    def col(self,column=None,as_matrix=True):
        """
        Get a specific column of the matrix
        column:integer>=1 and <=column_amount | column name
        as_matrix:False to get the column as a list, True to get a column matrix (default) 
        """
        if isinstance(column,int):
            if not (column<=self.dim[1] and column>0):
                raise InvalidColumn(column,"Column index out of range")
        elif isinstance(column,str):
            if not column in self.features:
                raise  InvalidColumn(column,f"'{column}' is not in column names")
            column = self.features.index(column)+1
        else:
            raise InvalidColumn(column)

        if as_matrix:
            return self[:,column-1:column]
        return [self._matrix[r][column-1] for r in range(self.dim[0])]
    
    def row(self,row=None,as_matrix=True):
        """
        Get a specific row of the matrix
        row:integer>=1 and <=row_amount
        as_matrix:False to get the row as a list, True to get a row matrix (default) 
        """
        if isinstance(row,int):
            if not (row<=self.dim[0] and row>0):
                raise InvalidIndex(row,"Row index out of range")
        else:
            raise InvalidIndex(row)

        if as_matrix:
            return self[row-1:row]
        return self._matrix[row-1]
                    
    def add(self,lis=[],row=None,col=None,feature="Col",dtype=None):
        """
        Add a row or a column of numbers
        lis: list of numbers desired to be added to the matrix
        row: natural number
        col: natural number 
        row>=1 and col>=1
        
        To append a row, only give the list of numbers, no other arguments
        To append a column, you need to use col = self.dim[1]
        """
        from MatricesM.matrixops.add import add
        add(self,lis,row,col,feature,dtype)
        
    def remove(self,row=None,col=None):
        """
        Deletes the given row and/or column
        row:int>=1
        col:int>=1
        """
        from MatricesM.matrixops.remove import remove
        remove(self,self.dim[0],self.dim[1],row,col)
            
    def concat(self,matrix,concat_as="row"):
        """
        Concatenate matrices row or columns vice
        b:matrix to concatenate to self
        concat_as:"row" to concat b matrix as rows, "col" to add b matrix as columns
        Note: This method concatenates the matrix to self
        """
        from MatricesM.matrixops.concat import concat
        concat(self,matrix,concat_as)
            
    def delDim(self,num):
        """
        Removes desired number of rows and columns from bottom right corner
        """        
        from MatricesM.matrixops.matdelDim import delDim
        delDim(self,num)

# =============================================================================
    """Methods for special matrices and properties"""
# =============================================================================     
    def _determinantByLUForm(self):
        """
        Determinant calculation from LU decomposition
        """
        return self._LU()[1]

    def _transpose(self,hermitian=False):
        """
        Returns the transposed matrix
        hermitian : True|False ; Wheter or not to use hermitian transpose method
        """
        from MatricesM.linalg.transpose import transpose
        return transpose(self,hermitian,obj=Matrix)

    def minor(self,row=None,col=None,returndet=True):
        """
        Returns the minor of the element in the desired position
        row,col : row and column indices of the element, 1<=row and col
        returndet : True if the determinant is wanted, False to return a matrix with the desired row and column removed 
        """
        from MatricesM.linalg.minor import minor
        return minor(self,row,col,returndet)

    def _adjoint(self):
        """
        Returns the adjoint matrix
        """
        from MatricesM.linalg.adjoint import adjoint
        if self.dtype=="complex":
            dt = "complex"
        else:
            dt = "float"
        return Matrix(self.dim,adjoint(self),dtype=dt,implicit=True)
    
    def _inverse(self):
        """
        Returns the inversed matrix
        """
        from MatricesM.linalg.inverse import inverse
        from MatricesM.constructors.matrices import Identity
        return inverse(self,Matrix(listed=Identity(self.dim[0])))

    def _Rank(self):
        """
        Returns the rank of the matrix
        """
        return self._rrechelon()[1]
    
    def nilpotency(self,limit=50):
        """
        Value of k for (A@A@A@...@A) == 0 where the matrix is multipled by itself k times, k in (0,inf) interval
        limit : integer | upper bound to stop iterations
        """
        from MatricesM.linalg.nilpotency import nilpotency
        return nilpotency(self,limit)
    
# =============================================================================
    """Decomposition methods"""
# ============================================================================= 
    def _rrechelon(self):
        """
        Returns reduced row echelon form of the matrix
        """
        from MatricesM.linalg.rrechelon import rrechelon
        return rrechelon(self,[a[:] for a in self._matrix],Matrix)
                    
    def _symDecomp(self):
        """
        Decompose the matrix into a symmetrical and an antisymmetrical matrix
        """
        from MatricesM.linalg.symmetry import symDecomp
        return symDecomp(self,Matrix(self.dim,fill=0))
    
    def _LU(self):
        """
        Returns L and U matrices of the matrix
        ***KNOWN ISSUE:Doesn't always work if determinant is 0 | linear system is inconsistant***
        ***STILL NEEDS CLEAN UP***
        """
        from MatricesM.linalg.LU import LU
        from MatricesM.constructors.matrices import Identity
        return LU(self,Identity(self.dim[0]),[a[:] for a in self.matrix],Matrix)

    def _QR(self):
        """
        Decompose the matrix into Q and R where Q is a orthogonal matrix and R is a upper triangular matrix
        """
        from MatricesM.linalg.QR import QR
        return QR(self,Matrix)
    
    def _hessenberg(self):
        pass
    
# =============================================================================
    """Basic properties"""
# =============================================================================  
    @property
    def p(self):
        print(self)
   
    @property
    def grid(self):
        print(self._stringfy(coldtypes=self.coldtypes))
    
    @property
    def copy(self):
        return Matrix(dim=self.dim[:],
                      listed=[a[:] for a in self._matrix],
                      ranged=self.initRange,
                      fill=self.fill,
                      features=self.features[:],
                      header=self._header,
                      directory=self._dir,
                      decimal=self.decimal,
                      seed=self.seed,
                      dtype=self.dtype[:],
                      coldtypes=self.coldtypes[:],
                      implicit=True
                      )

    @property
    def string(self):
        return self._stringfy(coldtypes=self.coldtypes[:])
    
    @property
    def directory(self):
        return self._dir
    
    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self,li):
        if not isinstance(li,(list,tuple)):
            raise NotListOrTuple(li)
        if len(li) != self.dim[1]:
            raise InvalidList(li,self.dim[1],"column names")

        temp=[str(i) for i in li]
        self.__features=temp
                
    @property
    def dim(self):
        return list(self.__dim)
    @dim.setter
    def dim(self,val):
        try:
            a=self.dim[0]*self.dim[1]
            if isinstance(val,int):
                assert val>0
                val=[val,val]
            elif isinstance(val,list) or isinstance(val,tuple):
                assert len(val)==2
            else:
                return None
            assert val[0]*val[1]==a
        except:
            return None
        else:
            els=[self.matrix[i][j] for i in range(self.dim[0]) for j in range(self.dim[1])]
            temp=[[els[c+val[1]*r] for c in range(val[1])] for r in range(val[0])]
            self.__init__(dim=list(val),listed=temp)
    
    @property
    def fill(self):
        return self.__fill
    @fill.setter
    def fill(self,value):
        try:
            assert (value in [uniform,triangular,gauss]) or (type(value) in [int,str,float,complex,range,list]) or value==None
        except AssertionError:
            raise TypeError("fill: uniform|triangular|gauss or int|float|complex|str|range|list|None; fills the matrix with chosen distribution or the value, default is uniform distribution")
        else:
            self.__fill=value
            self.setMatrix(self.__dim,self.__initRange,[],self._dir,self.__fill,self._cMat,self._fMat)

    @property
    def initRange(self):
        return self.__initRange
    @initRange.setter
    def initRange(self,value):
        if not (isinstance(value,list) or isinstance(value,tuple) or isinstance(value,dict)):
            raise TypeError("initRange should be a list or a tuple")
        
        if self.fill in [uniform,gauss] or ( isinstance(self.fill,int) or isinstance(self.fill,float) or isinstance(self.fill,complex) ):
            if isinstance(value,list):
                if len(value)!=2:
                    return IndexError("initRange|ranged should be in the form of [mean,standard_deviation] or [minimum,maximum]")
                if not (isinstance(value[0],float) or isinstance(value[0],int)) and not (isinstance(value[1],float) or isinstance(value[1],int)):
                    return ValueError("list contains non integer and non float numbers")
        elif self.fill in [triangular]:
            if isinstance(value,list):
                if len(value)!=3:
                    return IndexError("initRange|ranged should be in the form of [minimum,maximum,mode]")
                if not (isinstance(value[0],float) or isinstance(value[0],int)) and not (isinstance(value[1],float) or isinstance(value[1],int)) and not (isinstance(value[2],float) or isinstance(value[2],int)):
                    return ValueError("list contains non integer and non float numbers")
        else:
            raise TypeError("Invalid 'fill' attribute, change it first")
        self.__initRange=list(value)
            
    @property
    def rank(self):
        """
        Rank of the matrix
        """
        return self._Rank() 
    
    @property
    def perma(self):
        """
        Permanent of the matrix
        """
        from MatricesM.linalg.perma import perma
        return perma(self)
            
    @property
    def trace(self):
        """
        Trace of the matrix
        """
        if not self.isSquare:
            return None
        return sum([self._matrix[i][i] for i in range(self.dim[0])])
    
    @property
    def matrix(self):
       return self._matrix
   
    @property
    def det(self):
        """
        Determinant of the matrix
        """
        if not self.isSquare:
            return None
        return self._determinantByLUForm()
    
    @property
    def diags(self):
        return [self._matrix[i][i] for i in range(min(self.dim))]
    
    @property
    def eigenvalues(self):
        """
        Returns the eigenvalues using QR algorithm
        """
        try:
            assert self.isSquare and not self.isSingular and self.dim[0]>=2
            if self.dim[0]==2:
                d=self.det
                tr=self.matrix[0][0]+self.matrix[1][1]
                return list(set([(tr+(tr**2 - 4*d)**(1/2))/2,(tr-(tr**2 - 4*d)**(1/2))/2]))
        except:
            return None
        else:
            eigens = []
            q=self.Q
            a1=q.t@self@q
            for i in range(self.EIGEN_ITERS):#Iterations start
                qq=a1.Q
                a1=qq.t@a1@qq
            #Determine which values are real and which are complex eigenvalues
            if self.isSymmetric:#Symmetrical matrices always have real eigenvalues
                return a1.diags

            isodd=(a1.dim[0]%2)         
            #Create rest of the eigenvalues from 2x2 matrices
            if isodd:
                eigens.append(a1[0,0])
            ind=isodd

            while ind<a1.dim[0]-1:
                mat = a1[ind:ind+2,ind:ind+2]
                ind+=2
                if round(mat[1,0],8)==0:
                    eigens.append(mat[0,0])
                    ind-=1
                    continue
                r = mat.trace/2
                v = (mat.det - r**2)**(1/2)

                r = complex(complex(round(r.real.real,12),round(r.real.imag,12)),complex(round(r.imag.real,12),round(r.imag.imag,12)))
                v = complex(complex(round(v.real.real,12),round(v.real.imag,12)),complex(round(v.imag.real,12),round(v.imag.imag,12)))                
                
                c1 = complex(r,v)
                c2 = complex(r,v*(-1))
                
                if c1.imag==0:
                    c1 = c1.real
                if c2.imag==0:
                    c2 = c2.real
                
                eigens.append(c1)
                eigens.append(c2)

            return eigens

    @property
    def eigenvectors(self):
        """
        Returns the eigenvectors
        """
        from MatricesM.constructors.matrices import Identity
        if not self.isSquare or self.isSingular:
            return None
        pass
        
    @property
    def highest(self):
        """
        Highest value in the matrix
        """
        return max([max(a) for a in self.ranged().values()])

        
    @property
    def lowest(self):
        """
        Lowest value in the matrix
        """
        return min([min(a) for a in self.ranged().values()])  

        
    @property
    def obj(self):
        """
        Object call as a string to recreate the matrix
        """
        import re
        cdtype_str,fillstr = str(re.findall(r"'(?P<inner>\w+)'","{}".format(self.coldtypes))).replace("'",""),self.fill
        if type(self.fill).__name__ == "method":
            fillstr = self.fill.__name__
        return "Matrix(dim={0},listed={1},ranged={2},fill={3},features={4},header={5},directory='{6}',decimal={7},seed={8},dtype='{9}',coldtypes={10})".format(self.dim,
                                                                                                                                                                 self._matrix,
                                                                                                                                                                 self.initRange,
                                                                                                                                                                 fillstr,
                                                                                                                                                                 self.features,
                                                                                                                                                                 self._header,
                                                                                                                                                                 self._dir,
                                                                                                                                                                 self.decimal,
                                                                                                                                                                 self.seed,
                                                                                                                                                                 self.dtype,
                                                                                                                                                                 cdtype_str)
 
    @property
    def seed(self):
        return self.__seed
    @seed.setter
    def seed(self,value):
        try:
            if isinstance(value,int):
                self.__seed=value
            else:
                raise TypeError("Seed must be an integer")
        except Exception as err:
            raise err
        else:
            self.setMatrix(self.dim,self.initRange)

    @property
    def decimal(self):
        return self.__decimal
    @decimal.setter
    def decimal(self,val):
        try:
            assert isinstance(val,int)
            assert val>=1
        except:
            print("Invalid argument")
        else:
            self.__decimal=val     
        
    @property
    def dtype(self):
        return self.__dtype
    @dtype.setter
    def dtype(self,val):
        if not val in ['integer','float','complex','dataframe']:
            return DtypeError(val)
        else:
            self.__dtype = val
            self.__init__(dim=self.dim,
                          listed=self._matrix,
                          ranged=self.initRange,
                          fill=self.fill,
                          features=self.features,
                          header=self._header,
                          directory=self._dir,
                          decimal=self.decimal,
                          seed=self.seed,
                          dtype=self.dtype,
                          coldtypes=self.__coldtypes,
                          )

    @property
    def coldtypes(self):
        return self.__coldtypes
    @coldtypes.setter
    def coldtypes(self,val):
        if not isinstance(val,(list,tuple)):
            raise NotListOrTuple(val)
        if len(val) != self.dim[1]:
            raise InvalidList(val,self.dim[1],"column dtypes")

        for i in val:
            if type(i)!=type:
                raise ColdtypeError(i)
        self.__coldtypes=val
        self.setcoldtypes(True)
# =============================================================================
    """Check special cases"""
# =============================================================================    
    @property
    def isSquare(self):
        """
        A.dim == (i,j) where i == j
        """
        return self.dim[0] == self.dim[1]
    
    @property
    def isIdentity(self):
        if not self.isSquare:
            return False
        from MatricesM.constructors.matrices import Identity
        return self.matrix == Identity(self.dim[0])
    
    @property
    def isSingular(self):
        """
        A.det == 0
        """
        if not self.isSquare:
            return False
        return self.det == 0
    
    @property
    def isSymmetric(self):
        """
        A(i)(j) == A(j)(i)
        """        
        if not self.isSquare:
            return False
        return self.t.matrix == self.matrix
        
    @property  
    def isAntiSymmetric(self):
        """
        A(i)(j) == -A(j)(i)
        """
        if not self.isSquare:
            return False
        return (self.t*-1).matrix == self.matrix
    
    @property
    def isPerSymmetric(self):
        if not self.isSquare:
            return False
        d=self.dim[0]
        for i in range(d):
            for j in range(d):
                if self.matrix[i][j] != self.matrix[d-1-j][d-1-i]:
                    return False
        return True
    
    @property
    def isHermitian(self):
        """
        A.ht == A
        """
        return (self.ht).matrix == self.matrix
        
    @property
    def isTriangular(self):
        """
        A(i)(j) == 0 where i < j XOR i > j
        """
        from functools import reduce
        if not self.isSquare:
            return False
        return self.det == reduce((lambda a,b: a*b),[self.matrix[a][a] for a in range(self.dim[0])])
    
    @property
    def isUpperTri(self):
        """
        A(i)(j) == 0 where i > j
        """
        if self.isTriangular:
            for i in range(1,self.dim[0]):
                for j in range(i):
                    if self.matrix[i][j]!=0:
                        return False
            return True
        return False
    
    @property
    def isLowerTri(self):
        """
        A(i)(j) == 0 where i < j
        """
        return self.t.isUpperTri
    
    @property
    def isDiagonal(self):
        """
        A(i)(j) == 0 where i != j
        """
        if not self.isSquare:
            return False
        return self.isUpperTri and self.isLowerTri

    @property
    def isBidiagonal(self):
        """
        A(i)(j) == 0 where ( i != j OR i != j+1 ) XOR ( i != j OR i != j-1 )
        """
        return self.isUpperBidiagonal or self.isLowerBidiagonal
    
    @property
    def isUpperBidiagonal(self):
        """
        A(i)(j) == 0 where i != j OR i != j+1
        """
        #Assure the matrix is upper triangular
        if not self.isUpperTri or self.dim[0]<=2:
            return False
        
        #Assure diagonal and superdiagonal have non-zero elements 
        if 0 in [self._matrix[i][i] for i in range(self.dim[0])] + [self._matrix[i][i+1] for i in range(self.dim[0]-1)]:
            return False
        
        #Assure the elements above first superdiagonal are zero
        for i in range(self.dim[0]-2):
            if [0]*(self.dim[0]-2-i) != self._matrix[i][i+2:]:
                return False
            
        return True

    @property
    def isLowerBidiagonal(self):
        """
        A(i)(j) == 0 where i != j OR i != j-1
        """
        return self.t.isUpperBidiagonal          

    @property
    def isUpperHessenberg(self):
        """
        A(i)(j) == 0 where i<j-1
        """
        if not self.isSquare or self.dim[0]<=2:
            return False
        
        for i in range(2,self.dim[0]):
            if [0]*(i-1) != self._matrix[i][0:i-1]:
                return False
                
        return True
    
    @property
    def isLowerHessenberg(self):
        """
        A(i)(j) == 0 where i>j+1
        """
        return self.t.isUpperHessenberg
    
    @property
    def isHessenberg(self):
        """
        A(i)(j) == 0 where i>j+1 XOR i<j-1
        """
        return self.isUpperHessenberg or self.isLowerHessenberg
    
    @property
    def isTridiagonal(self):
        """
        A(i)(j) == 0 where abs(i-j) > 1 AND A(i)(j) != 0 where 0 <= abs(i-j) <= 1
        """
        if not self.isSquare or self.dim[0]<=2:
            return False
        
        #Check diagonal and first subdiagonal and first superdiagonal
        if 0 in [self._matrix[i][i] for i in range(self.dim[0])] + [self._matrix[i][i+1] for i in range(self.dim[0]-1)] + [self._matrix[i+1][i] for i in range(self.dim[0]-1)]:
            return False
        
        #Assure rest of the elements are zeros
        for i in range(self.dim[0]-2):
            #Non-zero check above first superdiagonal
            if [0]*(self.dim[0]-2-i) != self._matrix[i][i+2:]:
                return False
            
            #Non-zero check below first subdiagonal
            if [0]*(self.dim[0]-2-i) != self._matrix[self.dim[0]-i-1][:self.dim[0]-i-2]:
                return False
        return True

    @property
    def isToeplitz(self):
        """
        A(i)(j) == A(i+1)(j+1) when 0 < i < row number, 0 < j < column number
        """
        for i in range(self.dim[0]-1):
            for j in range(self.dim[1]-1):
                if self._matrix[i][j] != self._matrix[i+1][j+1]:
                    return False
        return True
    
    @property
    def isIdempotent(self):
        """
        A@A == A
        """
        if not self.isSquare:
            return False
        return self.roundForm(4).matrix == (self@self).roundForm(4).matrix
    
    @property
    def isOrthogonal(self):
        """
        A.t == A.inv
        """
        if not self.isSquare or self.isSingular:
            return False
        return self.inv.roundForm(4).matrix == self.t.roundForm(4).matrix
    
    @property
    def isUnitary(self):
        """
        A.ht == A.inv
        """
        if not self.isSquare or self.isSingular:
            return False
        return self.ht.roundForm(4).matrix == self.inv.roundForm(4).matrix
    
    @property
    def isNormal(self):
        """
        A@A.ht == A.ht@A OR A@A.t == A.t@A
        """
        if not self.isSquare:
            return False
        return (self@self.ht).roundForm(4).matrix == (self.ht@self).roundForm(4).matrix
    
    @property
    def isCircular(self):
        """
        A.inv == A.conj
        """
        if not self.isSquare or self.isSingular:
            return False
        return self.inv.roundForm(4).matrix == self.roundForm(4).matrix
    
    @property
    def isPositive(self):
        """
        A(i)(j) > 0 for every i and j 
        """
        if self._cMat:
            return False
        return bool(self>0)
    
    @property
    def isNonNegative(self):
        """
        A(i)(j) >= 0 for every i and j 
        """
        if self._cMat:
            return False
        return bool(self>=0)
    
    @property
    def isProjection(self):
        """
        A.ht == A@A == A 
        """
        if not self.isSquare:
            return False
        return self.isHermitian and self.isIdempotent

    @property
    def isInvolutory(self):
        """
        A@A == Identity
        """
        if not self.isSquare:
            return False
        from MatricesM.constructors.matrices import Identity
        return (self@self).roundForm(4).matrix == Matrix(listed=Identity(self.dim[0])).matrix
    
    @property
    def isIncidence(self):
        """
        A(i)(j) == 0 | 1 for every i and j
        """
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if not self._matrix[i][j] in [0,1]:
                    return False
        return True
    
# =============================================================================
    """Get special formats"""
# =============================================================================    
    @property
    def realsigns(self):
        """
        Determine the signs of the elements' real parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        signs=[[1 if self._matrix[i][j].real>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs,dtype="integer",implicit=True)
    
    @property
    def imagsigns(self):
        """
        Determine the signs of the elements' imaginary parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        signs=[[1 if self._matrix[i][j].imag>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs,dtype="integer",implicit=True)
    
    @property
    def signs(self):
        """
        Determine the signs of the elements
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        if self._cMat:
            return {"Real":self.realsigns,"Imag":self.imagsigns}
        signs=[[1 if self._matrix[i][j]>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs,dtype="integer",implicit=True)
    
    @property
    def rrechelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._rrechelon()[0]
    
    @property
    def conj(self):
        """
        Conjugated matrix
        """
        temp=self.copy
        temp._matrix=[[self.matrix[i][j].conjugate() for j in range(self.dim[1])] for i in range(self.dim[0])]
        return temp
    
    @property
    def t(self):
        """
        Transposed matrix
        """
        return self._transpose()
    
    @property
    def ht(self):
        """
        Hermitian-transposed matrix
        """
        return self._transpose(hermitian=True)    
    
    @property
    def adj(self):
        """
        Adjoint matrix
        """
        return self._adjoint()
    
    @property
    def inv(self):
        """
        Inversed matrix
        """
        return self._inverse()  
    
    @property
    def pseudoinv(self):
        """
        Pseudo-inversed matrix
        """
        if self.isSquare:
            return self.inv
        if self.dim[0]>self.dim[1]:
            return ((self.t@self).inv)@(self.t)
        return None
    
    @property
    def LU(self):
        lu = self._LU()
        return (lu[2],lu[0])
        
    @property
    def uptri(self):
        """
        Upper triangular part of the matrix
        """
        return self._LU()[0]
    
    @property
    def lowtri(self):
        """
        Lower triangular part of the matrix
        """
        return self._LU()[2]
    
    @property
    def symdec(self):
        ant_sym = self._symDecomp()
        return (ant_sym[0],ant_sym[1])

    @property
    def sym(self):
        """
        Symmetrical part of the matrix
        """
        if self.isSquare:
            return self._symDecomp()[0]
        return []
    
    @property
    def anti(self):
        """
        Anti-symmetrical part of the matrix
        """
        if self.isSquare:
            return self._symDecomp()[1]
        return []    
    
    @property
    def QR(self):
        qr = self._QR()
        return (qr[0],qr[1])

    @property
    def Q(self):
        """
        Q matrix from QR decomposition
        """
        return self._QR()[0]
    
    @property
    def R(self):
        """
        R matrix from QR decomposition
        """
        return self._QR()[1]    
    
    @property
    def floorForm(self):
        """
        Floor values elements
        """
        return self.__floor__()
    
    @property
    def ceilForm(self):
        """
        Ceiling value of the elements
        """
        return self.__ceil__()
    
    @property   
    def intForm(self):
        """
        Integer part of the elements
        """
        return self.__floor__()
    
    @property   
    def floatForm(self):
        """
        Elements in float values
        """
        if self._cMat:
            return eval(self.obj)
        
        t=[[float(self._matrix[a][b]) for b in range(self.dim[1])] for a in range(self.dim[0])]
        
        return Matrix(self.dim,listed=t,features=self.features,decimal=self.decimal,seed=self.seed,directory=self._dir,implicit=True)

    
    def roundForm(self,decimal=1):
        """
        Elements rounded to the desired decimal after dot
        """
        return round(self,decimal)
# =============================================================================
    """Filtering methods"""
# =============================================================================     
    def select(self,columns=None):
        """
        Returns a matrix with chosen columns
        
        columns: tuple|list of strings; Desired column names as strings in a tuple or list
        """
        if columns == None:
            return None
        temp = self.col(self.features.index(columns[0])+1)
        for col in columns[1:]:
            temp.concat(self.col(self.features.index(col)+1),"col")
        return temp

    def find(self,element,start=1):
        """
        element: Real number
        start: 0 or 1. Index to start from 
        Returns the indices of the given elements, multiple occurances are returned in a list
        """
        from MatricesM.filter.find import find
        return find([a[:] for a in self.matrix],self.dim,element,start)

    def joint(self,matrix):
        """
        Returns the rows of self which are also in the compared matrix
        
        matrix: matrix object
        """
        if not isinstance(matrix,Matrix):
            raise TypeError("Not a matrix")
        return Matrix(listed=[i[:] for i in self.matrix if i in matrix.matrix],features=self.features[:],dtype=self.dtype,coldtypes=self.coldtypes[:])

    def where(self,conditions=None):
        """
        Returns a matrix where the conditions are True for the desired columns.
        
        conditions:tuple/list of strings; Desired conditions to apply as a filter
        
        Syntax:
            Matrix.where((" ('Column_Name' (<|>|==|...) obj (and|or|...) 'Column_Name' ...") and ("'Other_column' (<|...) ..."), ...)
        
        Example:
            #Get the rows with scores in range [0,10) or Hours is higher than mean, where the DateOfBirth is higher than 1985
            data.where( " ( (Score>=0 and Score<10) or Hours>={mean} ) and DateOfBirth>1985 ".format(mean=self.mean()["Hours"]) )
        """
        from MatricesM.filter.where import wheres
        return Matrix(listed=wheres(self,conditions,self.features[:])[0],features=self.features[:],dtype=self.dtype,coldtypes=self.coldtypes[:])
    
    def apply(self,expressions,columns=(None,),conditions=None,returnmat=False):
        """
        Apply arithmetic or logical operations to every column individually inplace
        
        expressions: str(1 column only)|tuple|list of strings; Operations to do for each column given. Multiple operations can be applied if given in a single string. 
            ->One white space required between each operation and no space should be given between operator and operand
        
        columns: str(1 column only)|tuple|list|None; Column names to apply the given expression
        
        conditions: str|None; Conditions of rows to apply changes to

        returnmat: boolean; True to return self after evaluation, False to return None
        Example:
            #Multiply all columns with 3 and then add 10
                Matrix.apply( ("*3 +10") ) 
            #Multiply Prices with 0.9 and subtract 5 also add 10 to Discounts where Price is higher than 100 and Discount is lower than 5
                Matrix.apply( ("*0.9 -5","+10"), ("Price","Discount"), "(Price>100) and (Discount<5)" )
        """
        from MatricesM.filter.apply import applyop
        if returnmat:
            return applyop(self,expressions,columns,conditions,self.features[:])
        applyop(self,expressions,columns,conditions,self.features[:])

    def replace(self,old,new,column=None,condition=None):
        """
        Replace single values,rows and/or columns

        #Required parameters:
        old: all available types|boolean *column* matrix; value(s) to be replaced
        new:all available types; value(s) to replace old ones with
        column: str|tuple of strings|None;  which column(s) to apply replacements, None for all columns
        #Optional parameters:
        condition: boolean *column* matrix|None; row(s) to apply replacements, None for all rows
            Example:
                #Replace all 0's with 1's
                data.replace(old=0,new=1)

                #Replace all "Pending" values to "Done" in "Order1" and "Order2" columns
                data.replace(old="Pending", #(data["Order1"]=="Pending") & (data["Order2"]=="Pending") can also be used
                             new="Done",
                             column=("Order1","Order2")
                             )

                #Replace all '' values in the column "Length" with the mean of the "Length" column
                data.replace=(old='', #data["Length"]=="" can also be used
                              new=data.mean("Length",asDict=False),
                              column="Length"
                              )

                #Replace all "FF" values in "Grade" column with "AA" in the column "Grade" where "Year" is less than 2019
                data.replace(old="FF", #data["Grade"]=="FF" can also be used
                             new="AA",
                             column="Grade",
                             condition=data["Year"]<=2019
                             )

                #Replace all numbers below 0 in with 0's in column named "F5" where "Score1" is less than "Score2"
                data.replace(old=data["F5"]<0,
                             new=0,
                             column="F5",
                             condition=data["Score1"]<data["Score2"]
                             )

        """
        from MatricesM.filter.replace import _replace
        _replace(self,old,new,column,condition)
        
    def indexSet(self,name="Index",start=0,returnmat=False):
        """
        Add a column with values corresponding to the row number

        name: str. Name of the index column
        start: int. Starting index
        """
        self.add(list(range(start,self.dim[0]+start)),col=1,feature=name,dtype=int)
        if returnmat:
            return self

    def sortBy(self,column=None,reverse=False,returnmat=False):
        """
        Sort the rows by the desired column
        column:column name as string
        reverse:boolean; wheter or not to sort the matrix in reversed order
        returnmat:boolean; wheter or not to return self
        """
        self._matrix=sorted(self.matrix,key=lambda c,i=0:c[i+self.features.index(column)],reverse=reverse)
        if returnmat:
            return self

    def shuffle(self,iterations=1,returnmat=False):
        """
        Shuffle the rows of the matrix
        iterations : int; Times to shuffle
        returnmat:boolean; wheter or not to return self        
        """
        from random import shuffle
        for i in range(iterations):
            shuffle(self.matrix)
        if returnmat:
            return self

    def sample(self,size=10,condition=None):
        """
        Get a sample of the matrix

        size:int. How many samples to take
        condition:str. Conditionas to set as a base for sampling, uses 'where' method to filter 
        """
        from MatricesM.filter.sample import samples
        return Matrix(listed=samples(self,size,condition),decimal=self.decimal,dtype=self.dtype,features=self.features[:],coldtypes=self.coldtypes[:])

# =============================================================================
    """Statistical methods"""
# =============================================================================      
    
    def normalize(self,col=None,inplace=True,zerobound=12):
        """
        Use 'float' dtype for the best results
         
        Normalizes the data to be valued between 0 and 1
        col:integer>=1 | column name as string
        inplace : boolean ; True to apply changes to matrix, False to return a new matrix
        zerobound : integer ; limit of the decimals after dot to round the max-min of the columns to be considered 0
        """
        from MatricesM.stats.normalize import normalize
        return normalize(self,col,inplace,zerobound)

    def stdize(self,col=None,inplace=True,zerobound=12):
        """
        Use 'float' dtype for the best results
        
        Standardization to get mean of 0 and standard deviation of 1
        col:integer>=1 | column name as string
        inplace : boolean ; True to apply changes to matrix, False to return a new matrix
        zerobound : integer ; limit of the decimals after dot to round the sdev to be considered 0
        """ 
        from MatricesM.stats.stdize import stdize
        return stdize(self,col,inplace,zerobound)

    def ranged(self,col=None,asDict=True):
        """
        col:integer>=1 | column name as string
        Range of the columns
        asDict: True|False ; Wheter or not to return a dictionary with features as keys ranges as lists, if set to False:
            1) If there is only 1 column returns the list as it is
            2) If there are multiple columns returns the lists in order in a list        
        """    
        from MatricesM.stats.ranged import ranged
        return ranged(self,col,asDict)

    def mean(self,col=None,asDict=True):
        """
        col:integer>=1 | column name as string
        Mean of the columns
        asDict: True|False ; Wheter or not to return a dictionary with features as keys means as values, if set to False:
            1) If there is only 1 column returns the value as it is
            2) If there are multiple columns returns the values in order in a list
        """  
        from MatricesM.stats.mean import mean
        return mean(self,col,asDict)
    
    def mode(self,col=None):
        """
        Returns the columns' most repeated elements in a dictionary
        col:integer>=1 | column name as string
        """
        from MatricesM.stats.mode import mode
        return mode(self,col)
    
    def median(self,col=None):
        """
        Returns the median of the columns
        col:integer>=1 | column name as string
        """ 
        from MatricesM.stats.median import median
        return median(self,col)
    
    def sdev(self,col=None,population=1,asDict=True):
        """
        Standard deviation of the columns
        col:integer>=1 | column name as string
        population: 1 for σ, 0 for s value (default 1)
        asDict: True|False ; Wheter or not to return a dictionary with features as keys standard deviations as values, if set to False:
            1) If there is only 1 column returns the value as it is
            2) If there are multiple columns returns the values in order in a list
        """
        from MatricesM.stats.sdev import sdev
        return sdev(self,col,population,asDict)    
    
    def var(self,col=None,population=1,asDict=True):
        """
        Variance in the columns
        col:integer>=1 |None|column name as string ; Index/name of the column, None to get all columns 
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        asDict: True|False ; Wheter or not to return a dictionary with features as keys variance as values, if set to False:
            1) If there is only 1 column returns the value as it is
            2) If there are multiple columns returns the values in order in a list
        """   
        from MatricesM.stats.var import var
        return var(self,col,population,asDict)      
    
    def z(self,col=None,population=1):
        """
        z-scores of the elements
        column:integer>=1 |None|column name as string ; z-scores of the desired column
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        
        Give no arguments to get the whole scores in a matrix
        """
        from MatricesM.stats.z import z
        return z(self,col,population,Matrix(self.dim,fill=0,features=self.__features))        
    
    def iqr(self,col=None,as_quartiles=False,asDict=True):
        """
        Returns the interquartile range(IQR)
        col:integer>=1 and <=column amount | column name
        
        as_quartiles:
            True to return dictionary as:
                {Column1=[First_Quartile,Median,Third_Quartile],Column2=[First_Quartile,Median,Third_Quartile],...}
            False to get iqr values(default):
                {Column1=IQR_1,Column2=IQR_2,...}
                
        asDict: True|False ; Wheter or not to return a dictionary with features as keys iqr's as values, if set to False:
            1) If there is only 1 column returns the value as it is
            2) If there are multiple columns returns the values in order in a list
                
        Usage:
            self.iqr() : Returns a dictionary with iqr's as values
            self.iqr(None,True) : Returns a dictionary where the values are quartile medians in lists
            self.iqr(None,True,False) : Returns a list of quartile medians in lists
            self.iqr(None,False,False) : Returns a list of iqr's
            -> Replace "None" with any column number to get a specific column's iqr
        """ 
        from MatricesM.stats.iqr import iqr
        return iqr(self,col,as_quartiles,asDict)   
     
    def freq(self,col=None):
        """
        Returns the frequency of every element on desired column(s)
        col:column index>=1 or column name
        """
        from MatricesM.stats.freq import freq
        return freq(self,col)   
     
    def cov(self,col1=None,col2=None,population=1):
        """
        Covariance of two columns
        col1,col2: integers>=1 |str|None; column numbers/names.
        population: 0 or 1 ; 0 for samples, 1 for population
        """
        from MatricesM.stats.cov import cov
        return cov(self,col1,col2,population)
        
    def corr(self,col1=None,col2=None,population=1):
        """
        Correlation of 2 columns
        col1,col2: integers>=1 |str|None; column numbers/names. For correlation matrix give None to both
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        """
        from MatricesM.stats.corr import _corr
        from MatricesM.constructors.matrices import Identity
        temp = Matrix(self.dim[1],Identity(self.dim[1]),features=self.features[:],dtype="dataframe",coldtypes=[float for _ in range(self.dim[1])])
        return _corr(self,col1,col2,population,temp)
    
    @property   
    def describe(self):
        """
        Returns a matrix describing the matrix with features: Column, dtype, count,mean, sdev, min, max, 25%, 50%, 75%
        """
        from MatricesM.stats.describe import describe
        return describe(self,Matrix)

    def sum(self,col=None,asDict=True):
        """
        Return the sum of the desired column, give no arguments to get all columns'.
        col: int|str|None ; Column index or name
        asDict: boolean ; Wheter or not to return values in a dictionary. If col and asDict both None, values are returned in a list. If col is given value is returned
        """
        if col==None:
            if asDict:
                return {self.features[i]:sum(self.col(i+1,0)) for i in [j for j in range(self.dim[1]) if self.coldtypes[j] in [int,float]]}
            return [sum(self.col(i+1,0)) for i in [j for j in range(self.dim[1]) if self.coldtypes[j] in [int,float]]]
        else:
            if isinstance(col,str):
                col = self.features.index(col)
            if isinstance(col,int):
                if asDict:
                    return {self.features[col]:sum(self.col(col+1,0))}
                return sum(self.col(col+1,0))

    def prod(self,col=None,asDict=True):
        """
        Return the product of the desired column, give no arguments to get all columns'.
        col: int|str|None ; Column index or name
        asDict: boolean ; Wheter or not to return values in a dictionary. If col and asDict both None, values are returned in a list. If col is given value is returned
        """
        def p(lis):
            prd=1;
            for i in lis:
                prd*=i
            return prd;

        if col==None:
            if asDict:
                return {self.features[i]:p(self.col(i+1,0)) for i in [j for j in range(self.dim[1]) if self.coldtypes[j] in [int,float]]}
            return [p(self.col(i+1,0)) for i in [j for j in range(self.dim[1]) if self.coldtypes[j] in [int,float]]]
        else:
            if isinstance(col,str):
                col = self.features.index(col)
            if isinstance(col,int):
                if asDict:
                    return {self.features[col]:p(self.col(col+1,0))}
                return p(self.col(col+1,0))

    @property
    def info(self):
        """
        Prints out all available attributes
        """
        pass
# =============================================================================
    """Logical-bitwise magic methods """
# =============================================================================
    def __bool__(self):
        """
        Returns True if all the elements are equal to 1, otherwise returns False
        """
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if self.matrix[i][j] != 1:
                    return False
        return True

    def __invert__(self):
        """
        Returns a matrix filled with inverted elements, that is the 'not' bitwise operator
        """
        from MatricesM.matrixops.bitwise import _invert
        return _invert(self)
    
    def __and__(self,other):
        """
        Can only be used with '&' operator not with 'and'
        """        
        from MatricesM.matrixops.bitwise import _and
        return _and(self,other,Matrix)
    
    def __or__(self,other):
        """
        Can only be used with '|' operator not with 'or'
        """
        from MatricesM.matrixops.bitwise import _or
        return _or(self,other,Matrix)
        
    def __xor__(self,other):
        """
        Can only be used with '^' operator 
        """
        from MatricesM.matrixops.bitwise import _xor
        return _xor(self,other,Matrix)
     
# =============================================================================
    """Other magic methods """
# =============================================================================
    def __contains__(self,val):
        """
        val:value to search for in the whole matrix
        Returns True or False
        syntax: "value" in a.matrix
        """
        inds=self.find(val)
        return bool(inds)

    def __len__(self):
        return self.dim[0]*self.dim[1]    

    def __getitem__(self,pos):
        """
        Indices for full rows:
            Matrix[int]     --> Return a row
            Matrix[slice]   --> Return 0 or more rows
            Matrix[Matrix]  --> Return filtered rows

        Indices for full columns:
            Matrix[str]                  --> Return all rows of a column
            Matrix[:,slice]              --> Return 0 or more columns
            Matrix[:,(str,str,...,str)]  --> Return all rows of the desired columns passed as a tuple of strings (Can include duplicates)
            Matrix[str,str,...,str]      --> Return all rows of many columns (Can include duplicates) (Same as the previous one)

        Filtered rows and columns:
            Matrix[slice,(str,str,...,str)]   --> Return 0 or more rows of the desired columns
            Matrix[Matrix,(str,str,...,str)]  --> Return filtered rows of the desired columns 

        Indices for single values:
            Matrix[int,int]  --> Return the value in the matrix using row and column indices
            Matrix[int,str]  --> Return the value in the matrix using row index and column name
        """
        from MatricesM.matrixops.getsetdel import getitem
        return getitem(self,pos,Matrix)

    def __setitem__(self,pos,item):
        """
        Set new values to desired parts of the matrix.
        Uses same logic __getitem__ method uses.

        If a single value is given on the right-hand-side, value replaces all other values where left-hand-side represents
        Example:
            #Every row with even index numbers gets their 'Col 3' column changed to value 99
                Matrix[::2,"Col 3"] = 99                        
                
            #Rows where their 'Score1' is lower than 50 gets their 'Pass1' and 'Pass2' columns replaced with value 0   
                Matrix[Matrix["Score1"]<50,('Pass1','Pass2')] = 0
            
                #Following method does the same changes, slightly faster on most cases
                Matrix.replace(Matrix["Score1"]<50,0,('Pass1','Pass2'))
            
            Check README.md and exampleMatrices.py for more examples
        """
        from MatricesM.matrixops.getsetdel import setitem
        setitem(self,pos,item,Matrix)

    def __delitem__(self,val):
        """
        Works 'similar' to __getitem__ , but can only be used to delete entire columns and/or rows
        """
        from MatricesM.matrixops.getsetdel import delitem
        delitem(self,val,Matrix)

    def __repr__(self):
        rowlimit,collimit = min(self.dim[0],self.ROW_LIMIT),min(self.dim[1],self.COL_LIMIT)
        for i in [rowlimit,collimit]:
            if not isinstance(i,int):
                raise TypeError("ROW/COL limit can't be non-integer values")
            else:
                if i<1:
                    raise ValueError("ROW/COL limit should be >=1")
                    
        #Not too many rows or columns
        if self.dim[0]<=rowlimit and self.dim[1]<=collimit:
            return self._stringfy(coldtypes=self.coldtypes[:])

        halfrow = rowlimit//2
        halfcol = collimit//2
        if collimit%2 != 0:
            halfcol = collimit//2 + 1
        if rowlimit%2 != 0:
            halfrow = rowlimit//2 + 1

        #Too many rows
        if self.dim[0]>rowlimit:
            #Too many columns
            if self.dim[1]>collimit:
                #Divide matrix into 4 parts
                topLeft = self[:halfrow,:halfcol].roundForm(self.decimal)
                topRight = self[:halfrow,-(collimit//2):].roundForm(self.decimal)
                bottomLeft = self[-(rowlimit//2):,:halfcol].roundForm(self.decimal)
                bottomRight = self[-(rowlimit//2):,-(collimit//2):].roundForm(self.decimal)

                #Change dtypes to dataframes filled with strings
                for i in [topLeft,topRight,bottomLeft,bottomRight]:
                    if i.dtype != "dataframe":
                        i.dtype = "dataframe"
                topLeft.coldtypes = [str]*(halfcol)
                topRight.coldtypes = [str]*(collimit//2)
                bottomLeft.coldtypes = [str]*(halfcol)
                bottomRight.coldtypes = [str]*(collimit//2)

                #Add . . . to represent missing column's existence
                topLeft.add([". . ."]*(halfrow),col=halfcol + 1,dtype=str,feature="")
                bottomLeft.add([". . ."]*(rowlimit//2),col=halfcol + 1,dtype=str,feature="")
                
                #Concat left part with right, dots in the middle
                topLeft.concat(topRight,concat_as="col")
                bottomLeft.concat(bottomRight,concat_as="col")
                topLeft.concat(bottomLeft,concat_as="row")
                
                #Add dots as middle row and spaces below and above it
                topLeft.add([""]*(collimit+1),row=halfrow+1)
                topLeft.add([". . ."]*(collimit+1),row=halfrow+1)
                topLeft.add([""]*(collimit+1),row=halfrow+1)
                return topLeft._stringfy(coldtypes=topLeft.coldtypes)

            #Just too many rows
            else:
                #Get needed parts
                top = self[:halfrow,:].roundForm(self.decimal)
                bottom = self[-(rowlimit//2):,:].roundForm(self.decimal)
                #Set new dtypes
                for i in [top,bottom]:
                    if i.dtype != "dataframe":
                        i.dtype = "dataframe"
                    i.coldtypes = [str]*(collimit)
                #Concat last items
                top.concat(bottom,concat_as="row")
                #Add middle part
                top.add([""]*self.dim[1],row=halfrow+1)
                top.add([". . ."]*self.dim[1],row=halfrow+1)
                top.add([""]*self.dim[1],row=halfrow+1)

                return top._stringfy(coldtypes=top.coldtypes)
                
        #Just too many columns
        elif self.dim[1]>collimit:
            #Get needed parts
            left = self[:,:halfcol].roundForm(self.decimal)
            right = self[:,-(collimit//2):].roundForm(self.decimal)
            #Set new dtypes
            for i in [left,right]:
                if i.dtype != "dataframe":
                    i.dtype = "dataframe"
            left.coldtypes = [str]*(halfcol)
            right.coldtypes = [str]*(collimit//2)
            #Add and concat rest of the stuff
            left.add([". . ."]*self.dim[0],col=halfcol + 1,dtype=str,feature="")
            left.concat(right,concat_as="col")

            return left._stringfy(coldtypes=left.coldtypes)
        #Should't go here
        else:
            raise ValueError("Something is wrong with the matrix, check dimensions and values")
    
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        self.__dim=self._declareDim()
        self._inRange=self._declareRange(self._matrix)
        s=self._stringfy(coldtypes=self.coldtypes[:])
        if not self.isSquare:
            print("\nDimension: {0}x{1}".format(self.dim[0],self.dim[1]))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}".format(self.dim[0]))
        return s+"\n"   
    
    def __call__(self):
        return self.__str__()
                
# =============================================================================
    """Arithmetic methods"""        
# =============================================================================
    def __matmul__(self,other):
        from MatricesM.matrixops.arithmetic import matmul
        return matmul(self,other,Matrix)
    
    def __add__(self,other):
        from MatricesM.matrixops.arithmetic import add
        return add(self,other,Matrix)
            
    def __sub__(self,other):
        from MatricesM.matrixops.arithmetic import sub
        return sub(self,other,Matrix)
     
    def __mul__(self,other):
        from MatricesM.matrixops.arithmetic import mul
        return mul(self,other,Matrix)

    def __floordiv__(self,other):
        from MatricesM.matrixops.arithmetic import fdiv
        return fdiv(self,other,Matrix)
            
    def __truediv__(self,other):
        from MatricesM.matrixops.arithmetic import tdiv
        return tdiv(self,other,Matrix)

    def __mod__(self, other):
        from MatricesM.matrixops.arithmetic import mod
        return mod(self,other,Matrix)
         
    def __pow__(self,other):
        from MatricesM.matrixops.arithmetic import pwr
        return pwr(self,other,Matrix)

# =============================================================================
    """ Comparison operators """                    
# =============================================================================
    def __le__(self,other):
        from MatricesM.matrixops.comparison import le
        return le(self,other,Matrix)
        
    def __lt__(self,other):
        from MatricesM.matrixops.comparison import lt
        return lt(self,other,Matrix)
        
    def __eq__(self,other):
        from MatricesM.matrixops.comparison import eq
        return eq(self,other,Matrix)
        
    def __ne__(self,other):
        from MatricesM.matrixops.comparison import ne
        return ne(self,other,Matrix)
                
    def __ge__(self,other):
        from MatricesM.matrixops.comparison import ge
        return ge(self,other,Matrix)
        
    def __gt__(self,other):
        from MatricesM.matrixops.comparison import gt
        return gt(self,other,Matrix)
        
# =============================================================================
    """ Rounding etc. """                    
# =============================================================================   
    def __round__(self,n=-1):
        from MatricesM.matrixops.rounding import rnd
        return rnd(self,n,Matrix)
    
    def __floor__(self):
        from MatricesM.matrixops.rounding import flr
        return flr(self,Matrix)     
    
    def __ceil__(self):
        from MatricesM.matrixops.rounding import ceil
        return ceil(self,Matrix)
    
    def __abs__(self):
        from MatricesM.matrixops.rounding import _abs
        return _abs(self,Matrix)

# =============================================================================

