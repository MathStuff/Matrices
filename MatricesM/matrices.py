# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

class Matrix:
    """
    dim:integer | list | tuple; dimensions of the matrix. Giving integer values creates a square matrix
    
    listed:string | list of lists of numbers | list of numbers; Elements of the matrix. Can extract all the numbers from a string.
    
    directory:string; directory of a data file(e.g. 'directory/datafile' or r'directory\datafile')
    
    fill: 'uniform'|'triangular'|'gauss' or integer | float | complex or None; fills the matrix with chosen distribution or number, None will force uniform distribution

    ranged:->To apply all the elements give a list | tuple
           ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
           ->Arguments should follow one of the following rules:
                1)If 'fill' is 'uniform', interval to pick numbers from as [minimum,maximum]; 
                2)If 'fill' is 'gauss', mean and standard deviation are picked from this attribute as [mean,standard_deviation];
                3)If 'fill' is 'triangular, range of the numbers and the mode as [minimum,maximum,mode]

    header:boolean; takes first row as header title
    
    features:list of strings; column names
    
    seed:int|float|complex|str; seed to use while generating random numbers, not useful without fill is one of ['uniform','triangular','gauss']
    
    Check exampleMatrices.py or https://github.com/MathStuff/MatricesM  for further explanation and examples
    """

    def __init__(self,
                 dim = None,
                 listed = [],
                 directory = "",
                 fill = "uniform",
                 ranged = [-1,1],
                 seed = None,
                 header = False,
                 features = []):  
        
        self._matrix = listed  
        self._string = ""
        self._dir = directory
        self._header = header
        
        self.__initRange = ranged
        self.__fill = fill
        self.__seed = seed
        self.__features = features
        
        self._setDim(dim)
        self.setInstance()
        self.setMatrix(self.__dim,self.__initRange,self._matrix,self._dir,self.__fill)
        self.setFeatures()
# =============================================================================
    """Attribute formatting and setting methods"""
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
        if len(self.__features)!=self.dim[1]:
            self.__features=["Col {}".format(i+1) for i in range(self.dim[1])]    
            
    def _setDim(self,d):
        """
        Set the dimension to be a list if it's an integer
        """
        from MatricesM.setup.dims import setDim
        setDim(self,d)
        
    def setMatrix(self,d=None,r=None,lis=[],direc=r"",f="uniform"):
        """
        Set the matrix based on the arguments given
        """
        from MatricesM.setup.matfill import setMatrix
        
        setMatrix(self,d,r,lis,direc,f)
# =============================================================================
    """Attribute recalculation methods"""
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
                c[self.features[cols]]=[round(min(temp),4),round(max(temp),4)]
        return c
# =============================================================================
    """Methods for rading from the files"""
# =============================================================================
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
            return None
        else:
            f.close()

            return data
# =============================================================================
    """Element setting methods"""
# =============================================================================
    def _listify(self,stringold):
        """
        Finds all the numbers in the given string
        """
        from MatricesM.setup.listify import _listify
        return _listify(self,stringold)
            
    def _stringfy(self):
        """
        Turns a list into a grid-like form that is printable
        Returns a string
        """
        from MatricesM.setup.stringfy import _stringfy
        return _stringfy(self)
# =============================================================================
    """Row/Column methods"""
# =============================================================================
    def head(self,rows=5):
        """
        First 'rows' amount of rows of the matrix
        Returns a matrix
        rows : integer>0 | How many rows to return
        """
        if self.dim[0]>=rows:
            return self.subM(1,rows,1,self.dim[1])
        return self.subM(1,self.dim[0],1,self.dim[1])

    def tail(self,rows=5):
        """
        Last 'rows' amount of rows of the matrix
        Returns a matrix
        rows : integer>0 | How many rows to return
        """
        if self.dim[0]>=rows:
            return self.subM(self.dim[0]-rows+1,self.dim[0],1,self.dim[1])
        return self.subM(1,self.dim[0],1,self.dim[1])

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
                    
    def add(self,lis=[],row=None,col=None,feature="Col"):
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
        add(self,lis,row,col,feature)
        
    def remove(self,row=None,col=None):
        """
        Deletes the given row or column
        Changes the matrix
        Give only 1 parameter, r for row, c for column. (Starts from 1)
        If no parameter name given, takes it as row
        """
        from MatricesM.matrixops.remove import remove
        remove(self,row,col)
            
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
        
    def find(self,element,start=1):
        """
        element: Real number
        start: 0 or 1. Index to start from 
        Returns the indeces of the given elements, multiple occurances are returned in a list
        """
        from MatricesM.matrixops.find import find
        find(self,element,start)
    
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
        from MatricesM.matrixops.subM import subM
        if (rowS,rowE,colS,colE)==(None,None,None,None):
            return None
        if (rowS,rowE)!=(None,None) and (colS,colE)==(None,None):
            colE=rowE
            rowE=rowS
            rowS=1
            colS=1
        if self._cMat:
            typ="CMatrix"
        elif self._fMat:
            typ="FMatrix"
        else:
            typ="Matrix"
        arg = "([{},{}],fill=0)".format(rowE-rowS+1,colE-colS+1)
        ob = eval(typ+arg)
        return subM(self,rowS,rowE,colS,colE,ob)

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
        return transpose(self,hermitian)

    def minor(self,row=None,col=None):
        """
        Returns the minor of the element in the desired position
        """
        from MatricesM.linalg.minor import minor
        return minor(self,row,col)

    def _adjoint(self):
        """
        Returns the adjoint matrix
        """
        from MatricesM.linalg.adjoint import adjoint
        return adjoint(self)
    
    def _inverse(self):
        """
        Returns the inversed matrix
        """
        from MatricesM.linalg.inverse import inverse
        return inverse(self,Identity(self.dim[0]))

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
        return rrechelon(self)
                    
    def _symDecomp(self):
        """
        Decompose the matrix into a symmetrical and an antisymmetrical matrix
        """
        from MatricesM.linalg.symmetry import symDecomp
        return symDecomp(self)
    
    def _LU(self):
        """
        Returns L and U matrices of the matrix
        ***KNOWN ISSUE:Doesn't always work if determinant is 0 | linear system is inconsistant***
        ***STILL NEEDS CLEAN UP***
        """
        from MatricesM.linalg.LU import LU
        return LU(self)

    def _QR(self):
        """
        Decompose the matrix into Q and R where Q is a orthogonal matrix and R is a upper triangular matrix
        """
        from MatricesM.linalg.QR import QR
        return QR(self)
    
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
        if not self._isIdentity:
            self.__dim=self._declareDim()
            self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        print(self._string)
    
    @property
    def copy(self):
        if self._isIdentity:
            if self.matrix==Identity(self.dim[0]).matrix:
                return Identity(self.dim[0])
            else:
                return FMatrix(dim=self.dim)
        return eval(self.obj)
    @property
    def string(self):
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        return " ".join(self.__features)+self._string
    
    @property
    def directory(self):
        return self._dir
    
    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self,li):
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
            assert isinstance(value,int) or isinstance(value,bool)
        except AssertionError:
            raise TypeError("fill should be an integer or a boolean")
        else:
            self.__fill=bool(value)
            
    @property
    def initRange(self):
        return self.__initRange
    @initRange.setter
    def initRange(self,value):
        if not (isinstance(value,list) or isinstance(value,tuple) or isinstance(value,dict)):
            raise TypeError("initRange should be a list or a tuple")
        
        if self.fill in ["uniform","gauss"] or ( isinstance(self.fill,int) or isinstance(self.fill,float) or isinstance(self.fill,complex) ):
            if isinstance(value,list):
                if len(value)!=2:
                    return IndexError("initRange|ranged should be in the form of [mean,standard_deviation] or [minimum,maximum]")
                if not (isinstance(value[0],float) or isinstance(value[0],int)) and not (isinstance(value[1],float) or isinstance(value[1],int)):
                    return ValueError("list contains non integer and non float numbers")
        elif self.fill in ["triangular"]:
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
        Rank of the matrix ***HAVE ISSUES WORKING WITH SOME MATRICES***
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
        *** CAN NOT FIND THE COMPLEX EIGENVALUES *** 
        Returns the eigenvalues
        """
        try:
            if self._cMat:
                return None
            assert self.isSquare and not self.isSingular and self.dim[0]>=2
            if self.dim[0]==2:
                d=self.det
                tr=self.matrix[0][0]+self.matrix[1][1]
                return list(set([(tr+(tr**2 - 4*d)**(1/2))/2,(tr-(tr**2 - 4*d)**(1/2))/2]))
        except:
            return None
        else:
            q=self.Q
            a1=q.t@self@q
            for i in range(50):
                qq=a1.Q
                a1=qq.t@a1@qq
            
            return a1.diags
        
    @property
    def eigenvectors(self):
        """
        *** CAN NOT FIND THE EIGENVECTORS RESPONDING TO THE COMPLEX EIGENVALUES ***
        *** CURRENTLY DOESN'T RETURN ANYTHIN ***
        Returns the eigenvectors
        """
        if not self.isSquare or self.isSingular:
            return None
        eigs=self.eigenvalues
        vecs=[]

        for eigen in eigs:
            temp = self-Identity(self.dim[0])*eigen
            temp.concat([0]*self.dim[0],"col")
            temp = temp.rrechelon
            diff=0
            for i in range(self.dim[0]-temp.rank):
                diff+=1
            pass
        
    @property
    def highest(self):
        """
        Highest value in the matrix
        """
        if not self._isIdentity:
            return max([max(a) for a in self.ranged().values()])
        else:
            return 1
        
    @property
    def lowest(self):
        """
        Lowest value in the matrix
        """
        if not self._isIdentity:
            return min([min(a) for a in self.ranged().values()])  
        else:
            return 0
        
    @property
    def obj(self):
        """
        Object call as a string to recreate the matrix
        """
        #ranged and fill arguments are NOT required to create the same matrix
        if self._cMat:
            return "CMatrix(dim={0},listed={1},ranged={2},fill='{3}',features={4},header={5},directory='{6}',decimal={7},seed={8})".format(self.dim,self._matrix,self.initRange,self.fill,self.features,self._header,self._dir,self.decimal,self.seed)
        elif self._fMat:
            return "FMatrix(dim={0},listed={1},ranged={2},fill='{3}',features={4},header={5},directory='{6}',decimal={7},seed={8})".format(self.dim,self._matrix,self.initRange,self.fill,self.features,self._header,self._dir,self.decimal,self.seed)
        elif not self._isIdentity:
            return "Matrix(dim={0},listed={1},ranged={2},fill='{3}',features={4},header={5},directory='{6}',seed={7})".format(self.dim,self._matrix,self.initRange,self.fill,self.features,self._header,self._dir,self.seed)
        else:
            return None
        
    @property
    def seed(self):
        return self.__seed
    @seed.setter
    def seed(self,value):
        try:
            if isinstance(value,int) or isinstance(value,float) or isinstance(value,complex) or isinstance(value,str):
                self.__seed=value
            else:
                raise TypeError("Seed must be one of the following types:\n1.An integer\n2.A float number\n3.A complex number\n4.A string")
        except Exception as err:
            raise err
        else:
            self.setMatrix(self.dim,self.initRange)
            
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
       
# =============================================================================
    """Get special formats"""
# =============================================================================    
    @property
    def signs(self):
        """
        Determine the signs of the elements
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        if self._cMat:
            return {"Real":self.realsigns,"Imag":self.imagsigns}
        signs=[[1 if self._matrix[i][j]>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs)
    
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
    def Q(self):
        return self._QR()[0]
    
    @property
    def R(self):
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
        
        if self._fMat:
            a=self.decimal
            return FMatrix(self.dim,listed=t,features=self.features,decimal=a,seed=self.seed,directory=self._dir)
        
        return FMatrix(self.dim,listed=t,features=self.features,seed=self.seed,directory=self._dir)
    
    def roundForm(self,decimal=1):
        """
        Elements rounded to the desired decimal after dot
        """
        return round(self,decimal)
    
# =============================================================================
    """Filtering methods"""
# =============================================================================     
    def where(self,column,condition):
        pass
    
    def apply(self,operator,value):
        pass
    
    def indexSet(self):
        pass
    
    def sortBy(self,column,order):
        pass
    
    def shuffle(self):
        pass
    
    def same(self,matrix):
        pass
# =============================================================================
    """Statistical methods"""
# =============================================================================      
    def sample(self,size=1):
        pass
    
    def normalize(self,col=None,inplace=True,zerobound=12):
        """
        Original matrix should be an FMatrix or there will be printing issues when "inplace" is used.
        Use name=name.floatForm to get better results
         
        Normalizes the data to be valued between 0 and 1
        col : int>=1 ; column number
        inplace : boolean ; True to apply changes to matrix, False to return a new matrix
        zerobound : integer ; limit of the decimals after dot to round the max-min of the columns to be considered 0
        """
        from MatricesM.stats.normalize import normalize
        return normalize(self,col,inplace,zerobound)

    def stdize(self,col=None,inplace=True,zerobound=12):
        """
        Original matrix should be an FMatrix or there will be printing issues when "inplace" is used.
        Use name=name.floatForm to get better results
        
        Standardization to get mean of 0 and standard deviation of 1
        col : int>=1 ; column number
        inplace : boolean ; True to apply changes to matrix, False to return a new matrix
        zerobound : integer ; limit of the decimals after dot to round the sdev to be considered 0
        """ 
        from MatricesM.stats.stdize import stdize
        return stdize(self,col,inplace,zerobound)

    def ranged(self,col=None,asDict=True):
        """
        col:integer|None ; column number
        Range of the columns
        asDict: True|False ; Wheter or not to return a dictionary with features as keys ranges as lists, if set to False:
            1) If there is only 1 column returns the list as it is
            2) If there are multiple columns returns the lists in order in a list        
        """    
        from MatricesM.stats.ranged import ranged
        return ranged(self,col,asDict)

    def mean(self,col=None,asDict=True):
        """
        col:integer|None ; column number
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
        col:integer>=1 and <=amount of columns
        """
        from MatricesM.stats.mode import mode
        return mode(self,col)
    
    def median(self,col=None):
        """
        Returns the median of the columns
        col:integer>=1 and <=column amount
        """ 
        from MatricesM.stats.median import median
        return median(self,col)
    
    def sdev(self,col=None,population=1,asDict=True):
        """
        Standard deviation of the columns
        col:integer>=1
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
        col:integer>=1 |None ; Number of the column, None to get all columns 
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        asDict: True|False ; Wheter or not to return a dictionary with features as keys variance as values, if set to False:
            1) If there is only 1 column returns the value as it is
            2) If there are multiple columns returns the values in order in a list
        """   
        from MatricesM.stats.var import var
        return var(self,col,population,asDict)      
    
    def z(self,row=None,col=None,population=1):
        """
        z-scores of the elements
        row:integer>=1 |None ; z-score of the desired row
        column:integer>=1 |None ; z-score of the desired column
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        
        Give no arguments to get the whole scores in a matrix
        """
        from MatricesM.stats.z import z
        return z(self,row,col,population)        
    
    def iqr(self,col=None,as_quartiles=False,asDict=True):
        """
        Returns the interquartile range(IQR)
        col:integer>=1 and <=column amount
        
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
        col:column
        """
        from MatricesM.stats.freq import freq
        return freq(self,col)   
     
    def cov(self,col1=None,col2=None,population=1):
        """
        Covariance of two columns
        col1,col2: integers>=1  ; column numbers
        population: 0 or 1 ; 0 for samples, 1 for population
        """
        from MatricesM.stats.cov import cov
        return cov(self,col1,col2,population)
        
    def corr(self,col1=None,col2=None,population=1):
        """
        Correlation of 2 columns
        col1,col2: integers>=1 or both None; column numbers. For correlation matrix give None to both
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        """     
        from MatricesM.stats.corr import _corr
        temp = FMatrix(self.dim[1],fill=0,features=self.features)
        temp += Identity(self.dim[1])
        return _corr(self,col1,col2,population,temp)
    
    @property   
    def describe(self):
        from MatricesM.stats.describe import describe
        return describe(self)
    
# =============================================================================
    """Other magic methods """
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
    
    def __contains__(self,val):
        """
        val:value to search for in the whole matrix
        Returns True or False
        syntax: "value" in a.matrix
        """
        inds=self.find(val)
        return bool(inds)
                  
    def __getitem__(self,pos):
        try:
            if isinstance(pos,slice) or isinstance(pos,int):
                return self._matrix[pos]
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
            return self
    
    def __len__(self):
        return self.dim[0]*self.dim[1]
    
# =============================================================================
    """Arithmetic methods"""        
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
                    if self._cMat:
                        temp[r][rs]=complex(round(total.real,12),round(total.imag,12))
                    else:
                        temp[r][rs]=round(total,12)
            #Get decimals after the decimal point
            if self._fMat:
                a=self.decimal
            if other._fMat:
                a=other.decimal
             
            #Return proper the matrix
            if other._cMat or self._cMat:
                return CMatrix(dim=[self.dim[0],other.dim[1]],listed=temp,features=other.features,decimal=a)
            
            if other._fMat or self._fMat:
                return FMatrix(dim=[self.dim[0],other.dim[1]],listed=temp,features=other.features,decimal=a)
            return Matrix(dim=[self.dim[0],other.dim[1]],listed=temp,features=other.features)
################################################################################    
    def __add__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]+other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except Exception as err:
                print("Can't add: ",err)
                return self
            else:
                if self._fMat:
                    a=self.decimal
                if other._fMat:
                    a=other.decimal
                    
                #--------------------------------------------------------------------------
                if other._cMat or self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
            
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------
                
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]+other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't add")
                return self
            else:
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't add")
                return self
            else:
                temp=[[self.matrix[rows][cols]+other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
        else:
            print("Can't add")
            return self
################################################################################            
    def __sub__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]-other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except Exception as err:
                print("Can't subtract: ",err)
                return self
            else:
                if self._fMat:
                    a=self.decimal
                if other._fMat:
                    a=other.decimal
                #--------------------------------------------------------------------------
                if other._cMat or self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
            
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------
                
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]-other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't subtract")
                return self
            else:
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't subtract")
                return self
            else:
                temp=[[self.matrix[rows][cols]-other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
        else:
            print("Can't subtract")
            return self
################################################################################     
    def __mul__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]*other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except Exception as err:
                print("Can't multiply: ",err)
                return self
            else:
                if self._fMat:
                    a=self.decimal
                if other._fMat:
                    a=other.decimal
                #--------------------------------------------------------------------------
                if other._cMat or self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
            
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------
            
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]*other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except Exception as err:
                print("Can't multiply: ",err)
                return self
            else:
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------

        elif isinstance(other,list):
            if len(other)!=self.dim[1]:
                print("Can't multiply")
                return self
            else:
                temp=[[self.matrix[rows][cols]*other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
        else:
            print("Can't multiply")
            return self
################################################################################
    def __floordiv__(self,other):
        if isinstance(other,Matrix):
            if self._cMat or  other._cMat:
                print("CMatrix doesn't allow floor division")
            return self
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]//other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except Exception as err:
                print("Can't divide: ",err)
                return self
            else:
                #--------------------------------------------------------------------------
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=1)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------   
            
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]//other for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't divide") 
                return self
            else:
                #--------------------------------------------------------------------------
                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=1)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
                
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
                    #--------------------------------------------------------------------------
                    if self._fMat:                
                        return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                    return Matrix(dim=self.dim,listed=temp,features=self.features)
                    #--------------------------------------------------------------------------
        else:
            print("Can't divide")
            return self
################################################################################            
    def __truediv__(self,other):

        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]/other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except ZeroDivisionError:
                print("Division by 0")
                return self
            except Exception as err:
                print("Can't divide: ",err)
                return self
            else:
                if self._fMat:
                    a=self.decimal
                if other._fMat:
                    a=other.decimal
                #--------------------------------------------------------------------------
                if other._cMat or self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
            
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------
            
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]/other for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't divide") 
                return self
            else:
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
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
                    #--------------------------------------------------------------------------
                    if self._cMat:
                        return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
    
                    if self._fMat:                
                        return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                    return Matrix(dim=self.dim,listed=temp,features=self.features)
                    #--------------------------------------------------------------------------
        else:
            print("Can't divide")
            return self
################################################################################
    def __mod__(self, other):
        if isinstance(other,Matrix):
            try:
                if self._cMat or  other._cMat:
                    print("CMatrix doesn't allow floor division")
                    return self
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]%other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except ZeroDivisionError:
                print("Division by 0")
                return self
            except Exception as err:
                print("Can't get modular: ",err)
                return self
            else:
                if self._fMat:
                    a=self.decimal
                if other._fMat:
                    a=other.decimal
                #--------------------------------------------------------------------------
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------
            
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]%other for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except ZeroDivisionError:
                print("Division by 0")
                return self
            except:
                print("Can't get modular") 
                return self
            else:
                #--------------------------------------------------------------------------
                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
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
                    #--------------------------------------------------------------------------
                    if self._fMat:                
                        return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                    return Matrix(dim=self.dim,listed=temp,features=self.features)
                    #--------------------------------------------------------------------------
        else:
            print("Can't get modular")
            return self
################################################################################         
    def __pow__(self,other):
        if isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[[self.matrix[rows][cols]**other.matrix[rows][cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
            except Exception as err:
                print("Can't raise to the given power: ",err)
                return self
            else:
                if self._fMat:
                    a=self.decimal
                if other._fMat:
                    a=other.decimal
                #--------------------------------------------------------------------------
                if other._cMat or self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
            
                if self._fMat or other._fMat:               
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=a)
                return Matrix(dim=self.dim,listed=temp,features=self.features)    
                #--------------------------------------------------------------------------  
            
        elif isinstance(other,int) or isinstance(other,float) or isinstance(other,complex):
            try:
                temp=[[self.matrix[rows][cols]**other for cols in range(self.dim[1])] for rows in range(self.dim[0])]

            except:
                print("Can't raise to the given power")            
            else:
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------

        elif isinstance(other,list):

            if len(other)!=self.dim[1]:
                print("Can't raise to the given power")                
                return self
            else:
                temp=[[self.matrix[rows][cols]**other[cols] for cols in range(self.dim[1])] for rows in range(self.dim[0])]
                #--------------------------------------------------------------------------
                if self._cMat:
                    return CMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)

                if self._fMat:                
                    return FMatrix(dim=self.dim,listed=temp,features=self.features,decimal=self.decimal)
                return Matrix(dim=self.dim,listed=temp,features=self.features)
                #--------------------------------------------------------------------------
        else:
            print("Can't raise to the given power")
            return self
################################################################################                    
    def __le__(self,other):
        try:
            if isinstance(other,Matrix):
                if self.dim!=other.dim:
                    raise ValueError("Dimensions of the matrices don't match")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<=other.matrix[j][i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,list):
                if self.dim[1]!=len(other):
                    raise ValueError("Length of the list doesn't match matrix's column amount")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<=other[i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,int) or isinstance(other,float):
                if self._cMat:
                    raise TypeError("Can't compare int/float to complex numbers")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<=other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,complex):
                if not self._cMat:
                    raise TypeError("Can't compare complex numbers to int/float")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<=other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            else:
                raise TypeError("Invalid type to compare")
                
        except Exception as err:
            raise err
            
        else:
            return temp
        
    def __lt__(self,other):
        try:
            if isinstance(other,Matrix):
                if self.dim!=other.dim:
                    raise ValueError("Dimensions of the matrices don't match")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<other.matrix[j][i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,list):
                if self.dim[1]!=len(other):
                    raise ValueError("Length of the list doesn't match matrix's column amount")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<other[i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,int) or isinstance(other,float):
                if self._cMat:
                    raise TypeError("Can't compare int/float to complex numbers")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,complex):
                if not self._cMat:
                    raise TypeError("Can't compare complex numbers to int/float")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]<other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            else:
                raise TypeError("Invalid type to compare")
                
        except Exception as err:
            raise err
            
        else:
            return temp
        
    def __eq__(self,other):
        try:
            if isinstance(other,Matrix):
                if self.dim!=other.dim:
                    raise ValueError("Dimensions of the matrices don't match")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]==other.matrix[j][i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,list):
                if self.dim[1]!=len(other):
                    raise ValueError("Length of the list doesn't match matrix's column amount")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]==other[i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,int) or isinstance(other,float):
                if self._cMat:
                    raise TypeError("Can't compare int/float to complex numbers")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]==other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,complex):
                if not self._cMat:
                    raise TypeError("Can't compare complex numbers to int/float")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]==other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            else:
                raise TypeError("Invalid type to compare")
                
        except Exception as err:
            raise err
            
        else:
            return temp
        
    def __ne__(self,other):
        try:
            if isinstance(other,Matrix):
                if self.dim!=other.dim:
                    raise ValueError("Dimensions of the matrices don't match")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]!=other.matrix[j][i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,list):
                if self.dim[1]!=len(other):
                    raise ValueError("Length of the list doesn't match matrix's column amount")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]!=other[i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,int) or isinstance(other,float):
                if self._cMat:
                    raise TypeError("Can't compare int/float to complex numbers")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]!=other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,complex):
                if not self._cMat:
                    raise TypeError("Can't compare complex numbers to int/float")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]!=other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            else:
                raise TypeError("Invalid type to compare")
                
        except Exception as err:
            raise err
            
        else:
            return temp
                
    def __ge__(self,other):
        try:
            if isinstance(other,Matrix):
                if self.dim!=other.dim:
                    raise ValueError("Dimensions of the matrices don't match")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>=other.matrix[j][i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,list):
                if self.dim[1]!=len(other):
                    raise ValueError("Length of the list doesn't match matrix's column amount")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>=other[i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,int) or isinstance(other,float):
                if self._cMat:
                    raise TypeError("Can't compare int/float to complex numbers")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>=other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,complex):
                if not self._cMat:
                    raise TypeError("Can't compare complex numbers to int/float")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>=other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            else:
                raise TypeError("Invalid type to compare")
                
        except Exception as err:
            raise err
            
        else:
            return temp
        
    def __gt__(self,other):
        try:
            if isinstance(other,Matrix):
                if self.dim!=other.dim:
                    raise ValueError("Dimensions of the matrices don't match")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>other.matrix[j][i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,list):
                if self.dim[1]!=len(other):
                    raise ValueError("Length of the list doesn't match matrix's column amount")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>other[i] else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,int) or isinstance(other,float):
                if self._cMat:
                    raise TypeError("Can't compare int/float to complex numbers")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            
            elif isinstance(other,complex):
                if not self._cMat:
                    raise TypeError("Can't compare complex numbers to int/float")
                temp=Matrix(self.dim,[[1 if self.matrix[j][i]>other else 0 for i in range(self.dim[1])] for j in range(self.dim[0])])
            else:
                raise TypeError("Invalid type to compare")
                
        except Exception as err:
            raise err
            
        else:
            return temp
        
# =============================================================================
    
    def __round__(self,n=-1):
        if self._fMat and n<0:
            n=1
        if self._cMat:
            temp=[[complex(round(self.matrix[i][j].real,n),round(self.matrix[i][j].imag,n)) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return CMatrix(self.dim[:],listed=temp)               
        else:
            temp=[[round(self.matrix[i][j],n) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return FMatrix(self.dim[:],listed=temp) 
    
    def __floor__(self):
        if self._cMat:
            temp=[[complex(int(self.matrix[i][j].real),int(self.matrix[i][j].imag)) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return CMatrix(self.dim[:],listed=temp)               
        else:
            temp=[[int(self.matrix[i][j]) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return Matrix(self.dim[:],listed=temp)       
    
    def __ceil__(self):
        from math import ceil
        
        if self._cMat:
            temp=[[complex(ceil(self.matrix[i][j].real),ceil(self.matrix[i][j].imag)) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return CMatrix(self.dim[:],listed=temp)               
        else:
            temp=[[ceil(self.matrix[i][j]) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return Matrix(self.dim[:],listed=temp)    
    
    def __abs__(self):
        if self._cMat:
            temp=[[complex(abs(self.matrix[i][j].real),abs(self.matrix[i][j].imag)) for j in range(self.dim[1])] for i in range(self.dim[0])]
            return CMatrix(self.dim[:],listed=temp)               
        else:
            temp=[[abs(self.matrix[i][j]) for j in range(self.dim[1])] for i in range(self.dim[0])]
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
        if not self.isSquare:
            print("\nDimension: {0}x{1}\nFeatures: {2}".format(self.dim[0],self.dim[1],self.features))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}\nFeatures: {1}".format(self.dim[0],self.features))
        return self._string+"\n"

# =============================================================================
class Identity(Matrix):
    """
    Identity matrix
    """
    def __init__(self,dim=1):     
        try:
            assert isinstance(dim,int)
            assert dim>0
        except AssertionError:
            print("Give integer as the dimension")
            return None
        else:
            super().__init__(dim,fill=0)
            self._setMatrix()

                
    def _setMatrix(self):
        self._matrix=[[0 for a in range(self.dim[1])] for b in range(self.dim[0])]
        for row in range(0,self.dim[0]):
            self._matrix[row][row]=1          
                
    def addDim(self,num):
        """
        Add dimensions to identity matrix
        """
        from MatricesM.matrixops.idaddDim import addDim
        addDim(self,num)
        
    def delDim(self,num):
        """
        Delete dimensions to identity matrix
        """
        from MatricesM.matrixops.iddelDim import delDim
        delDim(self,num)
        
    @property
    def obj(self):
        return "Identity(dim={0})".format(self.dim)
    
    def __str__(self):
        if self._isIdentity:
            self._string=self._stringfy()
            print("\nIdentity Matrix\nDimension: {0}x{1}".format(self.dim[0],self.dim[1]))
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
                 fill = "uniform",
                 ranged = [0,1],
                 seed = None,
                 header = False,
                 features = [],
                 decimal = 4):
        
        self.__decimal = decimal
        super().__init__(dim,listed,directory,fill,ranged,seed,header,features)
        
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        print("\nFloat Matrix",end="")
        self.__dim=self._declareDim()
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        if not self.isSquare:
            print("\nDimension: {0}x{1}\nFeatures: {2}".format(self.dim[0],self.dim[1],self.features))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}\nFeatures: {1}".format(self.dim[0],self.features))
        return self._string+"\n"
    
    @property
    def decimal(self):
        return self.__decimal
    @decimal.setter
    def decimal(self,val):
        try:
            assert self._fMat or self._cMat
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
                 fill = "uniform",
                 ranged = [-1,1],
                 seed = None,
                 header = False,
                 features = [],
                 decimal = 4):
        
        self.__decimal=decimal
        super().__init__(dim,listed,directory,fill,ranged,seed,header,features,decimal)

    def __str__(self):
        print("\nComplex Matrix",end="")
        self.__dim=self._declareDim()
        self._inRange=self._declareRange(self._matrix)
        self._string=self._stringfy()
        if not self.isSquare:
            print("\nDimension: {0}x{1}".format(self.dim[0],self.dim[1]))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}".format(self.dim[0]))            
            
        return self._string+"\n"
        
    @property
    def realsigns(self):
        """
        Determine the signs of the elements' real parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        signs=[[1 if self._matrix[i][j].real>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs)
    
    @property
    def imagsigns(self):
        """
        Determine the signs of the elements' imaginary parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        signs=[[1 if self._matrix[i][j].imag>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs)

class SMatrix(Matrix):
    """
    Data frame matrix
    """
    def __init__(self,*args,**kwargs):
        pass