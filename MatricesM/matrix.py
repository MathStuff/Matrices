# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

from MatricesM.validations.validate import *
from MatricesM.errors.errors import *
from MatricesM.constructors.matrices import *

import re
from typing import *

from random import random,randint,uniform,triangular,\
                   gauss,gammavariate,betavariate,   \
                   expovariate,lognormvariate,seed

def read_file(directory:str,encoding:str="utf8",delimiter:str=","):
    """
    Read data from files
    """
    from MatricesM.setup.fileops import readAll
    directory = directory.replace("\\","/")
    (feats,data,cdtypes) = readAll(directory,encoding,delimiter)
    return Matrix(listed=data,features=feats,dtype=dataframe,coldtypes=cdtypes,DIRECTORY=directory)

def roundto(val:Any,decimal:int=8,force:bool=False):
    """
    Better round function which works with complex numbers and lists
    val:Any; value to round
    decimal:int>=0; decimal places to round to
    force:bool; force value rounding as complex number rounding
    """
    if isinstance(val,complex) or force:
        return complex(round(val.real,decimal),round(val.imag,decimal))
    elif isinstance(val,(int,float)):
        return round(val,decimal)
    elif isinstance(val,list):
        return [roundto(value,decimal) for value in val]
    else:
        return TypeError(f"Can't round type {type(val)}.")

class date:
    """
    Date object, define patterns for the date and time data
    data: str; string format of the data
    pattern: str; string to format the data with. Usage:
        day "d"
        month "m"
        year "y"

        hour "h"
        minute "n"
        second "s"
 
        milli "3"
        micro "6"
        nano "9"

        timezone "t"

        Create a pattern using the terms above. Example:

            Example pattern               Expected input pattern                     Expected input sample

             yyyy/mm/dd               -->  Year/Month/Day                        -->  2019/10/25
             dd hh:nn:ss              -->  Day Hours:Minutes:Seconds             -->  25 16:32:55
             yyyymmdd,ttttt,hh:nn     -->  YearMonthDay,timezone,Hours:Minutes   -->  19980409,UTC+3,21:45

    """
    def __init__(self,date:str,pattern:str,delimiters:List[str],config:str="default"):
        self.date = date
        self.delimiters = delimiters
        self.pattern = self.fixpattern(pattern)
    
    @staticmethod
    def fixpattern(pattern,cfg):
        if cfg == "default":
            day,month,year = "d","m","y"
            hour,minute,second = "h","n","s"
            milli,micro,nano = "3","6","9"
            tzone = "t"
            terms = [day,month,year,hour,minute,second,milli,micro,nano,tzone]
            delims = self.delimiters[:]

            #Assert given delimiters are valid
            for delimiter in self.delimiters:
                if delimiter in terms:
                    raise ValueError(f"Character {delimiter} can't be used as a delimiter")

            input_pattern_term_indices = {"d":None,"m":None,"y":None,"h":None,"n":None,"s":None,"3":None,"6":None,"9":None}
            delimiter_indices = {i:[] for i in delims}
            #Check for terms' every appearance
            for term in terms:
                #Regex pattern for repeated characters
                term_pattern = term + "+"
                
                #Find out what repeated characters patterns are
                partition = {i:[] for i in sorted(re.findall(term_pattern,pattern),reverse=True)}
                
                #Store starting and the ending points of the found patterns
                for part in list(partition.keys()):
                    pattern_copy = pattern[:]
                    while True:
                        lap = 0
                        try:
                            #Start getting all indices of the pattern
                            while part in pattern_copy:
                                l = len(part)
                                ind = pattern_copy.index(part)
                                #Replace the used part with question marks
                                pattern_copy = pattern_copy[:ind] + pattern_copy[ind+l:]
                        except:
                            #Store them
                            input_pattern_term_indices[term][part].append((ind+l*lap,ind+l*(lap+1)))
                            lap += 1
                        else:
                            #All indices stored, get to the next pattern
                            break
                #Should have input_pattern_term_indices -> {"d":{"ddd":[(1,4),(5,8)],"d":[(15,16)]},"m":...}
                
                #Create a regex pattern for the entire pattern using collected indices
                pass

    def __repr__(self):
        return "".join(re.findall(self.date,self.pattern))

class dataframe:
    pass

class Matrix:
    """
    dim:int|list|tuple; dimensions of the matrix. Giving integer values creates a square matrix
    
    listed:str|list of lists of numbers|list of numbers|str; Elements of the matrix. Can extract all the numbers from a string.

    fill: uniform|triangular|gauss|gammavariate|betavariate|expovariate|lognormvariate or int|float|complex|str|list|range or None; 
          Fills the matrix with chosen distribution or the value, default is uniform distribution

    ranged:->To apply all the elements give a list | tuple
           ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
           ->Arguments should follow one of the following rules:
                1)If 'fill' is uniform, interval to pick numbers from as [minimum,maximum]; 
                2)If 'fill' is gauss or lognormvariate mean and standard deviation are picked from this attribute as [mean,standard_deviation];
                3)If 'fill' is triangular, range of the numbers and the mode as [minimum,maximum,mode];
                4)If 'fill' is gammavariate or betavariate, alpha and beta values are picked as [alpha,beta]
                5)If 'fill' is expovariate, lambda value have to be given in a list as [lambda]

    features:list of strings; column names
    
    seed:int; seed to use while generating random numbers, not useful when fill isn't one of [uniform,triangular,gauss,gammavariate,betavariate,lognormvariate,expovariate]
    
    decimal:int; Digits to round to and print

    dtype:int|float|complex|dataframe; type of values the matrix will hold

    coldtypes:tuple|list (Contains the objects, not names of them); data types for each column individually. Only works if dtype is set to dataframe

    index:Matrix|list|tuple; indices to use for rows. Only works if dtype is set to dataframe

    indexname:str; name of the index column
    
    implicit:boolean; Skip matrix setting operations if dimensions and elements are given

    NOTE:
        - Matrix(kwargs={'dim':4,'fill':triangular,'ranged'=(0,10,6)})        --> Use **kwargs with a dictionary

        - Check https://github.com/MathStuff/MatricesM  for further explanation and examples
    """

    def __init__(self,
                 dim:Union[int,List[int],Tuple[int]]=None,
                 listed:Union[List[List[Any]],List[Any]]=[],
                 fill:Any=uniform,
                 ranged:Union[List[Union[float,int]],Tuple[Union[float,int]],Dict[str,Union[List[Union[float,int]],Tuple[Union[float,int]]]]]=[0,1],
                 seed:int=None,
                 features:List[str]=[],
                 decimal:int=4,
                 dtype:Union[int,float,complex,dataframe]=float,
                 coldtypes:List[Any]=[],
                 index:Union[List[Any],Tuple[Any]]=[],
                 indexname:str="",
                 implicit:bool=False,
                 **kwargs):  

        #Basic attributes
        self.__features = features                  #Column names
        self.__dim = dim                            #Dimensions
        self._matrix = listed                       #Values
        self.__fill = fill                          #Filling method for the matrix
        self.__initRange = ranged                   #Given range for 'fill'
        self.__seed = seed                          #Seed to pick values from 
        self.__decimal = decimal                    #How many digits to display in decimal places
        self.__dtype = dtype                        #Type of the matrix
        self.__coldtypes = coldtypes                #Column dtypes
        self.__index = index                        #Column to use as index column
        self.__indexname = indexname                #Index column's name
        self.__implicit = implicit                  #Implicity value
        self._cMat,self._fMat,self._dfMat = 0,0,0   #Types

        #Constants to use for printing,rounding etc.
        self.PRECISION = 6                          #Decimals to round
        self.ROW_LIMIT = 30                         #Upper limit for amount of rows to print
        self.COL_LIMIT = 12                         #Upper limit for amount of columns to print
        self.EIGEN_ITERS = 100                      #QR algorithm iterations for eigenvalues
        self.NOTES = ""                             #Extra info to add to the end of the string used in __repr__

        #Override the attributes given in kwargs with new values
        attributes = ["dim","listed","fill","ranged","seed","features","decimal","dtype","coldtypes","index","indexname","implicit"]
        options = ["PRECISION","ROW_LIMIT","COL_LIMIT","EIGEN_ITERS","NOTES","DIRECTORY"]
        for key,val in kwargs.items():
            if isinstance(val,dict) and key=="kwargs":
                for k,v in val.items():
                    if k=="listed":
                        self._matrix = v
                    elif k=="ranged":
                        self.__initRange = v
                    elif k in attributes:
                        exec(f"self._Matrix__{k}=v")
                    elif k in options:
                        exec(f"self.{k}=v")
                    else:
                        raise ParameterError(k,attributes+options)
            else:
                exec(f"self.{key}=val")

        #Set/fix attributes
        self._setDim(self.__dim)           #Fix dimensions
        self.setInstance(self.__dtype)     #Store what type of values matrix can hold

        #For the favor of better results, increase iterations for odd numbered dimensions
        if self.EIGEN_ITERS < 250:
            self.EIGEN_ITERS+= 400*(self.__dim[0]%2)  
        
        #Setup the matrix and column names,types
        self.setup(True,self.__implicit)
        
# =============================================================================
    """Attribute formatting and setting methods"""
# =============================================================================    
    def __getattr__(self,attr:str,fromset:[0,1]=0):
        try:
            property_names = ['_Matrix__features','_Matrix__dim','_Matrix__fill','_Matrix__initRange','_Matrix__dtype','_Matrix__coldtypes',
            '_Matrix__seed','_Matrix__decimal','_Matrix_initRange','_Matrix__implicit','_Matrix__index','_Matrix__indexname','_Matrix__useind',
            '_matrix','p', 'grid', 'copy', 'string','features', 'dim','d0', 'd1', 'fill', 'initRange', 'rank','perma', 'trace', 'matrix', 'det', 
            'diags','eigenvalues', 'eigenvectors','obj', 'seed', 'decimal', 'dtype', 'coldtypes','isSquare', 'isIdentity', 'isSingular', 'isSymmetric', 
            'isAntiSymmetric', 'isPerSymmetric', 'isHermitian', 'isTriangular', 'isUpperTri','isLowerTri', 'isDiagonal', 'isBidiagonal', 
            'isUpperBidiagonal','isLowerBidiagonal', 'isUpperHessenberg', 'isLowerHessenberg','isHessenberg', 'isTridiagonal', 'isToeplitz', 
            'isIdempotent','isOrthogonal', 'isUnitary', 'isNormal', 'isCircular', 'isPositive','isNonNegative', 'isProjection', 'isInvolutory',
            'isIncidence','isZero', 'realsigns', 'imagsigns', 'signs', 'echelon', 'rrechelon','conj', 't', 'ht', 'adj', 'inv', 'pseudoinv','LU', 
            'U','L', 'symdec', 'sym', 'anti', 'QR', 'Q', 'R', 'floorForm', 'ceilForm','intForm', 'floatForm', 'describe', 'info', 'kwargs','index',
            'indexname','_dfMat','_cMat','_fMat',"PRECISION","ROW_LIMIT","COL_LIMIT","EIGEN_ITERS","NOTES","DIRECTORY"]
            if attr in property_names:
                return object.__getattr__(self,attr)

            return (self[attr],True)[fromset]

        except:
            return None

    def __setattr__(self,attr:str,val:Any):
        if isinstance(self.__getattr__(attr,1),bool):
            self.__setitem__(attr,val)
        else:
            object.__setattr__(self,attr,val)

    def setup(self,first:bool,implicit:bool=False):
        #Matrix fix
        if first and not implicit:
            self.setMatrix(self.dim,self.initRange,self._matrix,self.fill,self._cMat,self._fMat)
        
        #Variables
        d0,d1 = self.dim
        df = self._dfMat
        dt = self.dtype
        cdts = self.coldtypes

        #Column names set
        if len(self.features)!=d1:
            self.__features=[f"col_{i}" for i in range(1,d1+1)]

        #Column types
        if not validlist(self._matrix):
            return None

        if len(cdts) != d1:
            if df:
                self.__coldtypes = [type(i) for i in self.matrix[0]]
            else:
                self.__coldtypes = [dt]*d1

        #Apply coldtypes to values in the matrix, set indices
        if df:
            r = range(d0)
            mm = self.matrix
            for i in r:
                j=0
                while j<d1:
                    try:
                        if cdts[j] != type: 
                            mm[i][j] = cdts[j](mm[i][j])
                        j+=1
                    except:
                        j+=1
                        continue

            ind = self.__index
            if isinstance(ind,Matrix):
                if ind.d1 > 1:
                    raise TypeError("Index parameter only accepts column matrices")
                if ind.d0 != d0:
                    raise ValueError(f"Given matrix can't be used as indices; expected {d0} rows, got {ind.d0}")
                
                self.__index = ind.col(1,0)

            elif isinstance(ind,(list,tuple)):
                if len(ind) == 0:
                    self.__index = list(r)
                elif len(ind) != d0:
                    raise ValueError(f"Given list can't be used as indices; expected {d0} values, got {len(ind)}")

            elif ind == None:
                self.__index = ["" for _ in range(self.d0)]
            else:
                raise TypeError(f"Type {type(ind).__name__} can't be used as indices")
            
            self._matrix = mm

    def setInstance(self,dt:Union[int,float,complex,dataframe]):
        """
        Set the type
        """
        if dt==complex:
            self._fMat=1
            self._cMat=1
        elif dt==float:
            self._fMat=1
        elif dt==int:
            pass
        elif dt==dataframe:
            self._dfMat=1
        else:
            raise ValueError("dtype should be one of the following: int, float, complex, dataframe")       
            
        
    def _setDim(self,d:Union[int,list,tuple]):
        """
        Set the dimension to be a list if it's an integer
        """
        valid = 0
        if isinstance(d,int):
            if d>=1:
                self.__dim=[d,d]
                valid = 1
        elif isinstance(d,list) or isinstance(d,tuple):
            if len(d)==2:
                if isinstance(d[0],int) and isinstance(d[1],int):
                    if d[0]>0 and d[1]>0:
                        self.__dim=d[:]
                        valid = 1
        if not valid:
            self.__dim = [0,0]
        
    def setMatrix(self,
                  d:Union[int,list,tuple,None]=None,
                  r:Union[List[Union[float,int]],Tuple[Union[float,int]],Dict[str,Union[List[Union[float,int]],Tuple[Union[float,int]]]],None]=None,
                  lis:Union[List[List[Any]], List[Any]]=[],
                  f:Any=uniform,
                  cmat:bool=False,
                  fmat:bool=True):
        """
        Set the matrix based on the arguments given
        """
        from MatricesM.setup.matfill import _setMatrix
        _setMatrix(self,d,r,lis,f,cmat,fmat)
        
# =============================================================================
    """Attribute recalculation methods"""
# =============================================================================    
    def _declareDim(self):
        """
        Set new dimension 
        """
        from MatricesM.setup.declare import declareDim
        return declareDim(self)
    
    def _declareRange(self,lis:Union[List[List[Any]], List[Any] ]):
        """
        Finds and returns the range of the elements in a given list
        """
        from MatricesM.setup.declare import declareRange
        return declareRange(self,lis)

# =============================================================================
    """Element setting methods"""
# =============================================================================
    def _listify(self,stringold:str):
        """
        Finds all the numbers in the given string
        """
        from MatricesM.setup.listify import _listify
        return _listify(self,stringold)
            
    def _stringfy(self,coldtypes:Union[List[Any],None]=None,returnbounds:bool=False):
        """
        Turns a list into a grid-like form that is printable
        Returns a string
        """
        from MatricesM.setup.stringfy import _stringfy
        return _stringfy(self,coldtypes,returnbounds)
    
# =============================================================================
    """Row/Column methods"""
# =============================================================================
    def head(self,rows:int=5):
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

    def tail(self,rows:int=5):
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

    def col(self,column:Union[int,str],as_matrix:bool=True):
        """
        Get a specific column of the matrix
        column:integer>=1 and <=column_amount | column name
        as_matrix:False to get the column as a list, True to get a column matrix (default) 
        """
        if isinstance(column,int):
            if not (column<=self.dim[1] and column>0):
                raise InvalidColumn(column,"Column index out of range")
        elif isinstance(column,str):
            name = column
            if not column in self.features:
                raise  InvalidColumn(column,f"'{column}' is not in column names")
            column = self.features.index(column)+1
        else:
            raise InvalidColumn(column)

        if as_matrix:
            return self[:,column-1]
        mm = self._matrix
        return [mm[r][column-1] for r in range(self.dim[0])]
    
    def row(self,row:Union[int,str]=None,as_matrix:bool=True):
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
        return self._matrix[row-1][:]
                    
    def add(self,lis:List[Any],row:Union[int,None]=None,col:Union[int,None]=None,feature:str=None,dtype:Any=None,returnmat:bool=False):
        """
        Add a row or a column of numbers
        lis: list of numbers desired to be added to the matrix
        row: natural number
        col: natural number 
        row>=1 and col>=1

        feature: new column's name
        dtype: type of data the new column will hold, doesn't work if a row is inserted

        returnmat:bool; wheter or not to return self

        To append a row, use row=self.d0
        To append a column, use col=self.d1
        """
        from MatricesM.matrixops.add import add
        add(self,lis,row,col,feature,dtype)
        if returnmat:
            return self

    def remove(self,row:int=None,col:int=None,returnmat:bool=False):
        """
        Deletes the given row and/or column
        row:int>=1
        col:int>=1
        returnmat:bool; wheter or not to return self
        """
        from MatricesM.matrixops.remove import remove
        remove(self,self.dim[0],self.dim[1],row,col)
        if returnmat:
            return self  

    def concat(self,matrix:object,concat_as:["row","col"]="col",returnmat:bool=False):
        """
        Concatenate matrices row or columns vice
        matrix:Matrix; matrix to concatenate to self
        concat_as:'row'|'col'; "row" to concat b matrix as rows, "col" to add b matrix as columns
        returnmat:bool; wheter or not to return self
        """
        from MatricesM.matrixops.concat import concat
        concat(self,matrix,concat_as)
        if returnmat:
            return self
            
    def delDim(self,num:int):
        """
        Removes desired number of rows and columns from bottom right corner
        """        
        from MatricesM.matrixops.matdelDim import delDim
        delDim(self,num)

    @property
    def ind(self):
        if not self._dfMat:
            raise TypeError("Can't use 'ind' with non-dataframe matrices")
        self.__useind = 1
        return self
        

# =============================================================================
    """Methods for special matrices and properties"""
# =============================================================================     
    def _determinantByLUForm(self):
        """
        Determinant calculation from LU decomposition
        """
        return self._LU()[1]

    def _transpose(self,hermitian:bool=False):
        """
        Returns the transposed matrix
        hermitian : True|False ; Wheter or not to use hermitian transpose method
        """
        from MatricesM.linalg.transpose import transpose
        return transpose(self,hermitian,obj=Matrix)

    def minor(self,row:int,col:int,returndet:bool=True):
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
        if self.dtype==complex:
            dt = complex
        else:
            dt = float
        return Matrix(self.dim,adjoint(self),dtype=dt,implicit=True)
    
    def _inverse(self):
        """
        Returns the inversed matrix
        """
        from MatricesM.linalg.inverse import inverse
        return inverse(self,Matrix(listed=Identity(self.dim[0])))

    def _Rank(self):
        """
        Returns the rank of the matrix
        """
        return self._rrechelon()[1]
    
    def nilpotency(self,limit:int=50):
        """
        Value of k for (A@A@A@...@A) == 0 where the matrix is multipled by itself k times, k in (0,inf) interval
        limit : integer | upper bound to stop iterations
        """
        from MatricesM.linalg.nilpotency import nilpotency
        return nilpotency(self,limit)
    
# =============================================================================
    """Decomposition methods"""
# ============================================================================= 
    def _rrechelon(self,rr:bool=True):
        """
        Returns reduced row echelon form of the matrix
        """
        from MatricesM.linalg.rrechelon import rrechelon
        return rrechelon(self,[a[:] for a in self._matrix],Matrix,rr)
                    
    def _symDecomp(self):
        """
        Decompose the matrix into a symmetrical and an antisymmetrical matrix
        """
        from MatricesM.linalg.symmetry import symDecomp
        return symDecomp(self,Matrix(self.dim,fill=0))
    
    def _LU(self):
        """
        Returns L and U matrices from LU decomposition
        """
        from MatricesM.linalg.LU import LU
        return LU(self,Identity(self.dim[0]),[a[:] for a in self.matrix],Matrix)

    def _QR(self):
        """
        Returns Q and R matrices from QR decomposition
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
        return Matrix(kwargs=self.kwargs)

    @property
    def string(self):
        return self._stringfy(coldtypes=self.coldtypes[:])

    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self,li:Union[List[str],Tuple[str]]):
        if not isinstance(li,(list,tuple)):
            raise NotListOrTuple(li)
        if len(li) != self.d1:
            raise InvalidList(li,self.d1,"column names")

        temp = []
        for i in range(len(li)):
            name = li[i]
            while name in temp:
                name = "_"+name
            temp.append(name)

        self.__features=temp
                
    @property
    def dim(self):
        return list(self.__dim)
    @dim.setter
    def dim(self,val:Union[int,List[int],Tuple[int]]):
        amount = self.dim[0]*self.dim[1]

        if isinstance(val,int):
            assert val>0 , "Dimensions can't be <=0"
            val=[val,val]
        elif isinstance(val,list) or isinstance(val,tuple):
            assert len(val)==2 , f"Matrices accept 2 dimensions, {len(val)} length {type(val)} type can't be used."
        else:
            raise TypeError("dim setter only accepts int>0 or list/tuple with length of 2")

        assert val[0]*val[1]==amount , f"{amount} elements can't fill a matrix with {val} dimensions"

        m = self.matrix
        els=[m[i][j] for i in range(self.dim[0]) for j in range(self.dim[1])]
        temp=[[els[c+val[1]*r] for c in range(val[1])] for r in range(val[0])]
        self.__init__(dim=list(val),listed=temp,dtype=self.dtype,implicit=True)
    
    @property
    def d0(self):
        return self.dim[0]
    @property
    def d1(self):
        return self.dim[1]

    @property
    def fill(self):
        return self.__fill
    @fill.setter
    def fill(self,value:[object]):
        try:
            assert (value in [uniform,triangular,gauss,expovariate,gammavariate,betavariate,lognormvariate]) or (type(value) in [int,str,float,complex,range,list]) or value==None
        except AssertionError:
            raise FillError(value)
        else:
            self.__fill=value
            self.setMatrix(self.__dim,self.__initRange,[],value,self._cMat,self._fMat)

    @property
    def initRange(self):
        return self.__initRange
    @initRange.setter
    def initRange(self,value:Union[List[Union[float,int]],Tuple[Union[float,int]]]):
        if not (isinstance(value,list) or isinstance(value,tuple)):
            raise TypeError("initRange should be a list or a tuple")
        
        if self.fill in [uniform,gauss,gammavariate,betavariate,lognormvariate] or ( isinstance(self.fill,int) or isinstance(self.fill,float) or isinstance(self.fill,complex) ):
            if len(value)!=2:
                return IndexError("initRange|ranged should be in the form of [mean,standard_deviation] or [minimum,maximum] or [alpha,beta]")
            if not (isinstance(value[0],float) or isinstance(value[0],int)) and not (isinstance(value[1],float) or isinstance(value[1],int)):
                return ValueError("list contains non integer and non float numbers")
        
        elif self.fill in [triangular]:
            if len(value)!=3:
                return IndexError("initRange|ranged should be in the form of [minimum,maximum,mode]")
            if not (isinstance(value[0],float) or isinstance(value[0],int)) and not (isinstance(value[1],float) or isinstance(value[1],int)) and not (isinstance(value[2],float) or isinstance(value[2],int)):
                return ValueError("list contains non integer and non float numbers")
        
        elif self.fill in [expovariate]:
            if len(value)!=1:
                return IndexError("initRange|ranged should be in the form of [lambda]")
            
        else:
            raise TypeError("Invalid 'fill' attribute to use 'initRange' with, change it to a method to use this setter.")
        l=list(value)
        self.__initRange=l
        self.setMatrix(self.__dim,l,[],self.__fill,self._cMat,self._fMat)

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
        return perma(self,self._matrix)
            
    @property
    def trace(self):
        """
        Trace of the matrix
        """
        if not self.isSquare:
            return None
        return sum(self.diags)
    
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
        m = self._matrix
        return [m[i][i] for i in range(min(self.dim))]
    
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

            #Wheter or not dimensions are odd
            isOdd=(a1.dim[0]%2)

            #Decide wheter or not to skip the bottom right 2x2 matrix
            if a1._cMat: 
                neighbor = a1[-1,-2]
                if round(neighbor.real,8)==0 and round(neighbor.imag,8):
                    eigens.append(a1[-1,-1])
            else:
                if round(a1[-1,-2],8)==0:
                    eigens.append(a1[-1,-1])

            #Create rest of the eigenvalues from 2x2 matrices
            ind=0
            while ind<a1.dim[0]-1:
                mat = a1[ind:ind+2,ind:ind+2]
                ind+=1+isOdd

                #Decide wheter or not to skip the top right corner 2x2 matrix
                done=0
                if a1._cMat:
                    if round(mat[1,0].real,6)==0 and round(mat[1,0].imag,6):
                        eigens.append(mat[0,0])
                        ind-=isOdd
                        done=1

                elif round(mat[1,0],8)==0:
                    eigens.append(mat[0,0])
                    ind-=isOdd
                    done=1

                #2x2 matrices in the middle
                if not done:
                    ind+=1-isOdd
                    r = mat.trace/2
                    v = (mat.det - r**2)**(1/2)
                    
                    r = complex(complex(roundto(r.real,6,True)),complex(roundto(r.imag,6,True)))
                    v = complex(complex(roundto(v.real,6,True)),complex(roundto(v.imag,6,True)))               
                    
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
        if not self.isSquare or self.isSingular:
            return None
        pass
               
    @property
    def obj(self):
        """
        Object call as a string to recreate the matrix
        """
        fill_str,cdtype_str = self.fill,str([i.__name__ for i in self.coldtypes]).replace("'","")
        if type(self.fill).__name__ == "method":
            fill_str=self.fill.__name__
        return "Matrix(dim={0},listed={1},ranged={2},fill={3},features={4},decimal={5},seed={6},dtype={7},coldtypes={8})".format(
                self.dim,self._matrix,self.initRange,fill_str,self.features,self.decimal,self.seed,self.dtype.__name__,cdtype_str)
 
    @property
    def seed(self):
        return self.__seed
    @seed.setter
    def seed(self,value:int):
        if not isinstance(value,int):
            raise TypeError("Seed must be an integer")
        self.__seed = value
        self.setMatrix(self.dim,self.initRange,[],"",self.fill,self._cMat,self._fMat)

    @property
    def decimal(self):
        return self.__decimal
    @decimal.setter
    def decimal(self,val:int):
        try:
            assert isinstance(val,int)
            assert val>=1
        except:
            raise ValueError("Seed should be an integer higher or equal to 1")
        else:
            self.__decimal=val     
        
    @property
    def dtype(self):
        return self.__dtype
    @dtype.setter
    def dtype(self,val:Union[int,float,complex,dataframe]):
        if not val in [int,float,complex,dataframe]:
            return DtypeError(val.__name__)
        else:
            self.__dtype = val
            self.__init__(dim=self.dim,
                          listed=self._matrix,
                          ranged=self.initRange,
                          fill=self.fill,
                          features=self.features,
                          decimal=self.decimal,
                          seed=self.seed,
                          dtype=self.dtype,
                          coldtypes=self.__coldtypes,
                          index=self.index,
                          indexname=self.indexname
                          )

    @property
    def coldtypes(self):
        return self.__coldtypes
    @coldtypes.setter
    def coldtypes(self,val:Union[List[str],Tuple[str]]):
        if not isinstance(val,(list,tuple)):
            raise NotListOrTuple(val)
        if len(val) != self.dim[1]:
            raise InvalidList(val,self.dim[1],"column dtypes")

        for i in val:
            if type(i)!=type:
                raise ColdtypeError(i)
        self.__coldtypes=val
        self.setup(True)
    
    @property
    def index(self):
        return self.__index
    @index.setter
    def index(self,val:Union[object,list,tuple]):
        if isinstance(val,Matrix):
            if val.d1 > 1:
                raise TypeError("Index parameter only accepts column matrices")
            if val.d0 != self.d0:
                raise ValueError(f"Given matrix can't be used as indices; expected {self.d0} rows, got {val.d0}")
            
            self.__index = val.col(1,0)
            self.__indexname = val.features[0]

        elif isinstance(val,(list,tuple)):
            if len(val) != self.d0:
                raise ValueError(f"Given list can't be used as indices; expected {self.d0} values, got {len(val)}")
            self.__index = list(val)

        elif val == None:
            self.__index = ["" for _ in range(self.d0)]

        else:
            raise TypeError(f"Type {type(val).__name__} can't be used as indices")     

    @property
    def indexname(self):
        return self.__indexname
    @indexname.setter
    def indexname(self,val:str):
        if not isinstance(val,str):
            raise TypeError("indexname only accepts strings")
        self.__indexname = val

# =============================================================================
    """Check special cases"""
# =============================================================================    
    @property
    def isSquare(self):
        """
        Matrix.dim == [i,j] where i == j
        """
        return self.dim[0] == self.dim[1]
    
    @property
    def isIdentity(self):
        """
        Matrix[i,j] == 1 where i==j and Matrix[i,j] == 0 where i!=j 
        """
        if not self.isSquare:
            return False
        return round(self,self.PRECISION).matrix == Identity(self.dim[0])
    
    @property
    def isSingular(self):
        """
        Matrix.det == 0
        """
        if not self.isSquare:
            return False
        return roundto(self.det,self.PRECISION) == 0
    
    @property
    def isSymmetric(self):
        """
        Matrix[i,j] == Matrix[j,i]
        """        
        if not self.isSquare:
            return False
        dig = self.PRECISION
        return self.t.roundForm(dig).matrix == self.roundForm(dig).matrix
        
    @property  
    def isAntiSymmetric(self):
        """
        Matrix[i,j] == -Matrix[j,i]
        """
        if not self.isSquare:
            return False
        dig = self.PRECISION
        return (self.t*-1).roundForm(dig).matrix == self.roundForm(dig).matrix
    
    @property
    def isPerSymmetric(self):
        """
        Matrix[i,j] == Matrix[n+1-j,n+1-i] , for nxn Matrix 
        """
        if not self.isSquare:
            return False

        m = self.matrix
        dig = self.PRECISION
        d = self.d0
        for i in range(d):
            for j in range(d):
                if roundto(m[i][j],dig) != roundto(m[d-1-j][d-1-i],dig):
                    return False
        return True
    
    @property
    def isHermitian(self):
        """
        Matrix.ht == Matrix
        """
        return (self.ht).matrix == self.matrix
        
    @property
    def isTriangular(self):
        """
        Matrix[i,j] == 0 where i < j XOR i > j
        """
        if not (self.isSquare and (self.isUpperTri or self.isLowerTri)):
            return False
        return True

    @property
    def isUpperTri(self):
        """
        Matrix[i,j] == 0 where i > j
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(1,self.dim[0]):
            for j in range(i):
                if roundto(m[i][j],dig)!=0: #Check elements below diagonal to be 0
                    return False
        return True
    
    @property
    def isLowerTri(self):
        """
        Matrix[i,j] == 0 where i < j
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(1,self.dim[0]):
            for j in range(i):
                if roundto(m[j][i],dig)!=0: #Check elements above diagonal to be 0
                    return False
        return True
    
    @property
    def isDiagonal(self):
        """
        Matrix[i,j] == 0 where i != j
        """
        from functools import reduce
        if not self.isSquare:
            return False
        return self.isUpperTri and self.isLowerTri and (roundto(self.det,self.PRECISION) == reduce((lambda a,b: a*b),self.diags))

    @property
    def isBidiagonal(self):
        """
        Matrix[i,j] == 0 where ( i != j OR i != j+1 ) XOR ( i != j OR i != j-1 )
        """
        return self.isUpperBidiagonal or self.isLowerBidiagonal
    
    @property
    def isUpperBidiagonal(self):
        """
        Matrix[i,j] == 0 where i != j OR i != j+1
        """
        #Assure the matrix is upper triangular
        if not self.isSquare:
            return False
        
        dig = self.PRECISION
        m=self.matrix
        #Assure diagonal and superdiagonal have non-zero elements 
        if 0 in [roundto(m[i][i],dig) for i in range(self.dim[0])] + [roundto(m[i][i+1],dig) for i in range(self.dim[0]-1)]:
            return False
        
        #Assure the elements above first superdiagonal are zero
        for i in range(self.dim[0]-2):
            if [0]*(self.dim[0]-2-i) != roundto(m[i][i+2:],dig):
                return False
            
        return True

    @property
    def isLowerBidiagonal(self):
        """
        Matrix[i,j] == 0 where i != j OR i != j-1
        """
        #Assure the matrix is upper triangular
        if not self.isSquare:
            return False

        m=self.matrix
        dig = self.PRECISION
        #Assure diagonal and subdiagonal have non-zero elements 
        if 0 in [roundto(m[i][i],dig) for i in range(self.dim[0])] + [roundto(m[i+1][i],dig) for i in range(self.dim[0]-1)]:
            return False
        
        #Assure the elements above first subdiagonal are zero
        for i in range(self.dim[0]-2):
            if [0]*(self.dim[0]-2-i) != roundto(m[i][i+2:],dig):
                return False
            
        return True
        
    @property
    def isUpperHessenberg(self):
        """
        Matrix[i,j] == 0 where i<j-1
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(2,self.dim[0]):
            for j in range(i):
                if roundto(m[i][j],dig)!=0: #Check elements below subdiagonal to be 0
                    return False
        return True
    
    @property
    def isLowerHessenberg(self):
        """
        Matrix[i,j] == 0 where i>j+1
        """
        if not self.isSquare:
            return False
        m = self.matrix
        dig = self.PRECISION
        for i in range(2,self.dim[0]):
            for j in range(i):
                if roundto(m[j][i],dig)!=0: #Check elements above superdiagonal to be 0
                    return False
        return True
    
    @property
    def isHessenberg(self):
        """
        Matrix[i,j] == 0 where i>j+1 XOR i<j-1
        """
        return self.isUpperHessenberg or self.isLowerHessenberg
    
    @property
    def isTridiagonal(self):
        """
        Matrix[i,j] == 0 where abs(i-j) > 1 AND Matrix[i,j] != 0 where 0 <= abs(i-j) <= 1
        """
        if not self.isSquare or self.dim[0]<=2:
            return False
        m = self.matrix
        dig = self.PRECISION
        #Check diagonal and first subdiagonal and first superdiagonal
        if 0 in [roundto(m[i][i],dig) for i in range(self.dim[0])] + [roundto(m[i][i+1],dig) for i in range(self.dim[0]-1)] + [roundto(m[i+1][i],dig) for i in range(self.dim[0]-1)]:
            return False
        
        #Assure rest of the elements are zeros
        for i in range(self.dim[0]-2):
            #Non-zero check above first superdiagonal
            if [0]*(self.dim[0]-2-i) != roundto(m[i][i+2:],dig):
                return False
            
            #Non-zero check below first subdiagonal
            if [0]*(self.dim[0]-2-i) != roundto(m[self.dim[0]-i-1][:self.dim[0]-i-2],dig):
                return False
        return True

    @property
    def isToeplitz(self):
        """
        Matrix[i,j] == Matrix[i+1,j+1] for every i and j
        """
        m = self.matrix
        dig = self.PRECISION
        for i in range(self.dim[0]-1):
            for j in range(self.dim[1]-1):
                if roundto(m[i][j],dig) != roundto(m[i+1][j+1],dig):
                    return False
        return True
    
    @property
    def isIdempotent(self):
        """
        Matrix@Matrix == Matrix
        """
        if not self.isSquare:
            return False
        dig = self.PRECISION            
        return self.roundForm(dig).matrix == (self@self).roundForm(dig).matrix
    
    @property
    def isOrthogonal(self):
        """
        Matrix.t == Matrix.inv
        """
        if not self.isSquare or self.isSingular:
            return False
        dig = self.PRECISION
        return self.inv.roundForm(dig).matrix == self.t.roundForm(dig).matrix
    
    @property
    def isUnitary(self):
        """
        Matrix.ht == Matrix.inv
        """
        if not self.isSquare or self.isSingular:
            return False
        dig = self.PRECISION
        return self.ht.roundForm(dig).matrix == self.inv.roundForm(dig).matrix
    
    @property
    def isNormal(self):
        """
        Matrix@Matrix.ht == Matrix.ht@Matrix OR Matrix@Matrix.t == Matrix.t@Matrix
        """
        if not self.isSquare:
            return False
        dig = self.PRECISION
        return (self@self.ht).roundForm(dig).matrix == (self.ht@self).roundForm(dig).matrix
    
    @property
    def isCircular(self):
        """
        Matrix.inv == Matrix.conj
        """
        if not self.isSquare or self.isSingular:
            return False
        dig = self.PRECISION
        return self.inv.roundForm(dig).matrix == self.roundForm(dig).matrix
    
    @property
    def isPositive(self):
        """
        Matrix[i,j] > 0 for every i and j 
        """
        if self._cMat:
            return False
        return bool(self>0)
    
    @property
    def isNonNegative(self):
        """
        Matrix[i,j] >= 0 for every i and j 
        """
        if self._cMat:
            return False
        return bool(self>=0)
    
    @property
    def isProjection(self):
        """
        Matrix.ht == Matrix@Matrix == Matrix 
        """
        if not self.isSquare:
            return False
        return self.isHermitian and self.isIdempotent

    @property
    def isInvolutory(self):
        """
        Matrix@Matrix == Identity
        """
        if not self.isSquare:
            return False
        return (self@self).roundForm(4).matrix == Matrix(listed=Identity(self.dim[0])).matrix
    
    @property
    def isIncidence(self):
        """
        Matrix[i,j] == 0 | 1 for every i and j
        """
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if not self._matrix[i][j] in [0,1]:
                    return False
        return True
    
    @property
    def isZero(self):
        """
        Matrix[i,j] == 0 for every i and j
        """
        m = self.matrix
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if m[i][j] != 0:
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
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def imagsigns(self):
        """
        Determine the signs of the elements' imaginary parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        signs=[[1 if self._matrix[i][j].imag>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def signs(self):
        """
        Determine the signs of the elements
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        if self._cMat:
            return {"Real":self.realsigns,"Imag":self.imagsigns}
        signs=[[1 if self._matrix[i][j]>=0 else -1 for j in range(self.dim[1])] for i in range(self.dim[0])]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def echelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._rrechelon(rr=False)[0]

    @property
    def rrechelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._rrechelon(rr=True)[0]
    
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
        """
        L and U matrices from LU decomposition
        """
        lu = self._LU()
        return (lu[2],lu[0])
        
    @property
    def U(self):
        """
        Upper triangular part of the matrix
        """
        return self._LU()[0]
    
    @property
    def L(self):
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
        """
        Q and R matrices from QR decomposition
        """
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
        Returns a matrix with all possible values' floor values
        """
        return self.__floor__()
    
    @property
    def ceilForm(self):
        """
        Returns a matrix with all possible values' ceiling values
        """
        return self.__ceil__()
    
    @property   
    def intForm(self):
        """
        Returns a matrix with all possible values as integers
        """
        return self.__floor__()
    
    @property   
    def floatForm(self):
        """
        Returns a matrix with all possible values as floats
        """
        if self._cMat:
            return self
        if self._dfMat:
            return Matrix(self.dim,listed=[a[:] for a in self.matrix],features=self.features,coldtypes=[float if i in [int,float] else i for i in self.coldtypes],
                          decimal=self.decimal,seed=self.seed,dtype=dataframe,index=self.index,indexname=self.indexname,implicit=True)

        mm = self.matrix
        t=[[float(mm[a][b]) for b in range(self.dim[1])] for a in range(self.dim[0])]

        return Matrix(self.dim,listed=t,features=self.features,decimal=self.decimal,seed=self.seed,implicit=True)

    
    def roundForm(self,decimal:int=1):
        """
        Elements rounded to the desired decimal after dot
        """
        return round(self,decimal)
# =============================================================================
    """Filtering methods"""
# =============================================================================     
    def select(self,columns:Union[List[str],Tuple[str]]=None):
        """
        Returns a matrix with chosen columns
        
        columns: tuple|list of strings; Desired column names as strings in a tuple or list
        """
        if columns == None:
            return None
        temp = self.col(self.features.index(columns[0])+1)
        for col in columns[1:]:
            temp.concat(self.col(self.features.index(col)+1))
        return temp

    def find(self,value:Any,start:[0,1]=1,onlyrow:bool=False):
        """
        value: object
        start: 0 or 1. Index to start from
        onlyrow: boolean; Wheter or not to return only the row indices of value's appearances
        Returns the indices of the given value in a list
        """
        from MatricesM.filter.find import find
        return find([a[:] for a in self.matrix],self.dim,value,start,onlyrow)

    def joint(self,matrix:object):
        """
        Returns the rows of self which are also in the compared matrix
        
        matrix: matrix object
        """
        if not isinstance(matrix,Matrix):
            raise TypeError("Not a matrix")
        return Matrix(listed=[i[:] for i in self.matrix if i in matrix.matrix],features=self.features[:],dtype=self.dtype,coldtypes=self.coldtypes[:])

    def where(self,conditions:Union[List[str],Tuple[str]]):
        """
        Returns a matrix where the conditions are True for the desired columns.
        
        conditions:tuple/list of strings; Desired conditions to apply as a filter
        
        Syntax:
            Matrix.where((" ('Column_Name' (<|>|==|...) obj (and|or|...) 'Column_Name' ...") and ("'Other_column' (<|...) ..."), ...)
        
        Example:
            #Get the rows with Score in range [0,10) or Hours is higher than mean, where the DateOfBirth is higher than 1985
            
                data.where( f" ( ( (Score>=0) and (Score<10) ) or ( Hours>={data.mean('Hours',0)} ) ) 
                            and ( DateOfBirth>1985 ) ")
            #Same as
                data[(((data["Score"]>=0) & (data["Score"]<10)) | (data["Hours"]>=data.mean("Hours",0))) 
                      & (data["DateOfBirth"]>1985) ]

        NOTE:
            # Every statement HAVE TO BE enclosed in parentheses as shown in the examples above
        """
        from MatricesM.filter.where import wheres
        return Matrix(listed=wheres(self,conditions,self.features[:])[0],features=self.features[:],dtype=self.dtype,coldtypes=self.coldtypes[:])
    
    def apply(self,expressions:Union[str,List[str],Tuple[str]],
              columns:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=(None,),
              conditions:Union[str,None]=None,
              returnmat:bool=False):
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

    def replace(self,old:Any,new:Any,
                column:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=None,
                condition:Optional[object]=None,
                returnmat:bool=False):
        """
        Replace single values,rows and/or columns

        old: all available types|boolean *column* matrix; value(s) to be replaced

        new:all available types; value(s) to replace old ones with

        column: str|tuple or list of strings|None;  which column(s) to apply replacements, None for all columns

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
        
        returnmat: boolean; True to return self after evaluation, False to return None

        """
        from MatricesM.filter.replace import _replace
        _replace(self,old,new,column,condition)
        if returnmat:
            return self
        
    def sortBy(self,column:Union[str,None]=None,key=lambda a:a[1],reverse:bool=False,returnmat:bool=False):
        """
        Sort the rows by the desired column
        column:str|None; column name as string, None to sort by index column
        key:function; function to use while sorting
        reverse:boolean; wheter or not to sort the matrix in reversed order
        returnmat:boolean; wheter or not to return self
        """
        if column == None:
            if self._dfMat:
                temp = Matrix(listed=self.index,dtype=dataframe,index=None).t.concat(self.copy,returnmat=True).sortBy("col_1",key=key,reverse=reverse,returnmat=True)
                self.__index = temp.col("col_1",0)
                self._matrix = temp[:,1:].matrix
            else:
                raise TypeError("Indexing by index column is not allowed on non-dataframe matrices")
        else:       
            temp=sorted([(i,row) for i,row in enumerate(self.col(column,0))],key=key,reverse=reverse)
            if self._dfMat:
                inds = self.index
                newinds = [r[0] for r in temp]
                self.__index = [inds[i] for i in newinds]

            mm = self.matrix
            self._matrix = [mm[r[0]] for r in temp]

        if returnmat:
            return self

    def shuffle(self,iterations:int=1,returnmat:bool=False):
        """
        Shuffle the rows of the matrix
        iterations : int; Times to shuffle
        returnmat:boolean; wheter or not to return self        
        """
        from random import shuffle

        inds = list(range(self.d0))
        mm = self.matrix
        inds = self.index
        
        for i in range(iterations):
            shuffle(inds)
    
        if self._dfMat:
            self.__index = [inds[i] for i in inds]
        self._matrix = [mm[i][:] for i in inds]

        if returnmat:
            return self

    def sample(self,size:int=10,condition:str=None):
        """
        Get a sample of the matrix

        size:int. How many samples to take
        condition:str. Conditions to set as a base for sampling, uses 'where' method to filter 
        """
        from random import sample

        mat = self.where(condition) if condition != None else self  
        if size > mat.d0:
            raise ValueError("Sample size is too big")

        i = mat.index
        mm = mat.matrix
        sample_inds = sample(list(range(mat.d0)),size)
        indices = [i[row] for row in sample_inds] if mat._dfMat else []
        
        return Matrix(listed=[mm[row][:] for row in sample_inds],decimal=self.decimal,
                      dtype=self.dtype,features=self.features[:],coldtypes=self.coldtypes[:],
                      index=indices,indexname=self.indexname)

    def match(self,expression:str,columns:Union[str,int,List[Union[str,None]],Tuple[Union[str,None]],None]=None,as_row:bool=True):
        """
        Return the values or rows that match the given expression

        expression: str; regular expression, uses re.findall
        columns: str|tuple or list of strings|int(starts from 1)|None; Column names/numbers
        as_row: boolean; True to return rows with the matching values, False to return:
            1)A dictionary if 'columns' == None|tuple or list as {'column_name':[(row_index,matching_value), ...], ...}
            2)A list if 'columns' == str [(row_index,matching_values), ...]

        Example:
            #Return the rows of all email adresses using gmail.com domain in the column 'mail'
            Matrix.match(expression=r"\w+@gmail.com",
                         columns="mail",
                         as_row=True)
        NOTE:
            #This method is CURRENTLY faster in most cases than using boolean matrices as indices:
                Matrix[Matrix[column]==value] --> Using boolean matrices as indices
                Matrix.match(value,column)    --> Corresponding method call for the same result as previous one

        """
        if not self._dfMat:
            raise MatrixError("'match' method only works with dataframes.")
        from MatricesM.filter.match import _match
        return _match(self,expression,columns,as_row,Matrix)

    def indexreset(self,start=0):
        self.__index = list(range(start,self.d0+start))
        
# =============================================================================
    """Statistical methods"""
# =============================================================================      
    
    def normalize(self,col:Union[int,str,None]=None,inplace:bool=True):
        """
        Normalizes the data to be valued between 0 and 1
        col:integer>=1 | column name as string | None
        inplace : boolean ; True to apply changes to matrix, False to return a new matrix
        """
        from MatricesM.stats.normalize import normalize
        return normalize(self,col,inplace,self.PRECISION)

    def stdize(self,col:Union[int,str,None]=None,inplace:bool=True):
        """
        Standardization to get mean of 0 and standard deviation of 1
        col:integer>=1 | column name as string
        inplace : boolean ; True to apply changes to matrix, False to return a new matrix
        """ 
        from MatricesM.stats.stdize import stdize
        return stdize(self,col,inplace,self.PRECISION)

    def ranged(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Range of the columns
        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """    
        from MatricesM.stats.ranged import ranged
        return ranged(self,col,get,Matrix,dataframe)

    def max(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Highest value(s) in the desired column(s)
        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.minmax import _minmax
        return _minmax(self,col,get,1,Matrix,dataframe)

    def min(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Lowest value(s) in the desired column(s)
        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.minmax import _minmax
        return _minmax(self,col,get,0,Matrix,dataframe)

    def mean(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Mean of the columns
        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """  
        from MatricesM.stats.mean import mean
        return mean(self,col,get,Matrix,dataframe)
    
    def mode(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Returns the columns' most repeated elements in a dictionary
        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a tuple of Matrices for every column individually
        """
        from MatricesM.stats.mode import mode
        return mode(self,col,get,Matrix,dataframe)
    
    def median(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Returns the median of the columns
        col:integer>=1 | column name as string
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """ 
        from MatricesM.stats.median import median
        return median(self,col,get,Matrix,dataframe)
    
    def sdev(self,col:Union[int,str,None]=None,population:[0,1]=1,get:[0,1,2]=1):
        """
        Standard deviation of the columns
        col:integer>=1 | column name as string
        population: 1 for σ, 0 for s value (default 1)
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.sdev import sdev
        return sdev(self,col,population,get,Matrix,dataframe)    
    
    def var(self,col:Union[int,str,None]=None,population:[0,1]=1,get:[0,1,2]=1):
        """
        Variance in the columns
        col:integer>=1 |None|column name as string ; Index/name of the column, None to get all columns 
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """   
        from MatricesM.stats.var import var
        return var(self,col,population,get,Matrix,dataframe)     
    
    def ranked(self,col:Union[int,str,None]=None,reverse:bool=False,key=lambda a:a[1],get:[-1,0,1,2]=1,start:int=0):
        """
        Ranks of the values in the columns when they are sorted
        col:int|str|None; column number/name, None for all columns
        reverse:bool; wheter or not to use reversed sorting
        key:function; function to use while sorting
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.ranked import _rank
        return _rank(self,col,reverse,key,get,start)

    def z(self,col:Union[int,str,None]=None,population:[0,1]=1):
        """
        z-scores of the elements
        column:integer>=1 |None|column name as string ; z-scores of the desired column
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample

        Give no arguments to get all the scores in a matrix
        """
        from MatricesM.stats.z import z
        return z(self,col,population,Matrix(self.dim,fill=0,features=self.features[:]))        
    
    def iqr(self,col:Union[int,str,None]=None,as_quartiles:bool=False,get:[0,1,2]=1):
        """
        Returns the interquartile range(IQR)
        col:integer>=1 and <=column amount | column name
        
        as_quartiles:
            True to return dictionary as:
                {Column1=[First_Quartile,Median,Third_Quartile],Column2=[First_Quartile,Median,Third_Quartile],...}
            False to get iqr values(default):
                {Column1=IQR_1,Column2=IQR_2,...}
                
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
                
        Usage:
            self.iqr() : Returns a dictionary with iqr's as values
            self.iqr(None,True) : Returns a dictionary where the values are quartile medians in lists
            self.iqr(None,True,0) : Returns a list of quartile medians in lists
            self.iqr(None,False,2) : Returns a matrix of iqr's
            -> Replace "None" with any column number to get a specific column's iqr
        """ 
        from MatricesM.stats.iqr import iqr
        return iqr(self,col,as_quartiles,get,Matrix,dataframe)   
     
    def freq(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Returns the frequency of every element on desired column(s)
        col:column index>=1 or column name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a list of Matrices for every column individually
        """
        from MatricesM.stats.freq import freq
        return freq(self,col,get,Matrix,dataframe)   
     
    def cov(self,col1:Union[int,str,None]=None,col2:Union[int,str,None]=None,population:[0,1]=1):
        """
        Covariance of two columns
        col1,col2: integers>=1 |str|None; column numbers/names. For covariance matrix give None to both
        population: 0 or 1 ; 0 for samples, 1 for population
        """
        from MatricesM.stats.cov import cov
        return cov(self,col1,col2,population,Matrix,dataframe)
        
    def corr(self,col1:Union[int,str,None]=None,col2:Union[int,str,None]=None,population:[0,1]=1,method:["pearson","kendall","spearman"]="pearson"):
        """
        Correlation of 2 columns
        col1,col2: integers>=1 |str|None; column numbers/names. For correlation matrix give None to both
        population:1|0 ; 1 to calculate for the population or a 0 to calculate for a sample
        """
        from MatricesM.stats.corr import _corr
        temp = Matrix(self.dim[1],Identity(self.dim[1]),features=self.features[:],dtype=dataframe,coldtypes=[float for _ in range(self.dim[1])])
        return _corr(self,col1,col2,population,temp,method)
    
    @property   
    def describe(self):
        """
        Returns a matrix describing the matrix with features: Column, dtype, count,mean, sdev, min, 25%, 50%, 75%, max
        """
        from MatricesM.stats.describe import describe
        return describe(self,Matrix,dataframe)

    def sum(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Return the sum of the desired column, give no arguments to get all columns'.
        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.prodsum import _prodsum
        return _prodsum(self,col,get,Matrix,dataframe,1)

    def prod(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Return the product of the desired column, give no arguments to get all columns'.
        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.prodsum import _prodsum
        return _prodsum(self,col,get,Matrix,dataframe,0)

    def count(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Return the count of the valid values in column(s), give no arguments to get all columns'.
        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.freq import _count
        return _count(self,col,get,Matrix,dataframe)

    @property
    def info(self):
        """
        Prints out column info
        """
        feats,cdtyps = self.features[:],self.coldtypes[:]
        counts = self.count(get=0) if self.d1>1 else [self.count(get=0)]
        uniques = self.freq(get=0) if self.d1>1 else [self.freq(get=0)]
        invalids = [self.d0-j for j in counts]
        return Matrix((self.d1,5),[[feats[i],cdtyps[i],counts[i],invalids[i],len(list(uniques[i].keys()))] for i in range(self.d1)],
                       dtype=dataframe,
                       coldtypes=[str,type,int,int,int],
                       features=["Column","dtype","Valid_data","Invalid_data","Unique_data"],
                       implicit=True,
                       index=None,
                       NOTES=f"Size: {self.dim}")

    def groupBy(self):
        pass

# =============================================================================
    """Logical-bitwise magic methods """
# =============================================================================
    def __bool__(self):
        """
        Returns True if all the elements are equal to 1, otherwise returns False
        """
        m = self.matrix
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                if m[i][j] != 1:
                    return False
        return True

    def __invert__(self):
        """
        Returns a matrix filled with inverted elements, that is the 'not' bitwise operator
        """
        from MatricesM.matrixops.bitwise import _invert
        return _invert(self,self.intForm)
    
    def __and__(self,other:Union[object,list,int,float,complex]):
        """
        Can only be used with '&' operator not with 'and'
        """        
        from MatricesM.matrixops.bitwise import _and
        return _and(self,other,Matrix,self.matrix)
    
    def __or__(self,other:Union[object,list,int,float,complex]):
        """
        Can only be used with '|' operator not with 'or'
        """
        from MatricesM.matrixops.bitwise import _or
        return _or(self,other,Matrix,self.matrix)
        
    def __xor__(self,other:Union[object,list,int,float,complex]):
        """
        Can only be used with '^' operator 
        """
        from MatricesM.matrixops.bitwise import _xor
        return _xor(self,other,Matrix,self.matrix)
     
# =============================================================================
    """Other magic methods """
# =============================================================================
    def __contains__(self,val:object):
        """
        val: object; value to search for in the whole matrix
        Returns True or False
        syntax: "value" in Matrix
        """
        inds=self.find(val)
        return bool(inds)

    def __len__(self):
        return self.dim[0]*self.dim[1]    

    def __getitem__(self,pos:Union[object,int,str,slice,list,Tuple[Union[str,int,slice,list,Tuple[str]]]]):
        """
        Using list indices:

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

        Using row indices:
            --> Use it after sorting the dataframe for the best results for slices

            Matrix.ind["pending"]                      --> Returns all the rows where the row index is 'pending'

            Matrix.ind[1990,"Score"]                   --> Returns the 'Score' column of all the rows with index 1990

            Matrix.ind[50:150]                         --> Return the rows with index higher than 50 and less than 150, starts and stops with limits' first appearances
                                                       
            Matrix.ind["Average":,"Final_Score"] --> Return the rows' 'Final_Score' columns where indices start from 'Average'
            
        """
        from MatricesM.matrixops.getsetdel import getitem
        useind = self.__useind or 0
        return getitem(self,pos,Matrix,useind)

    def __setitem__(self,pos:Union[object,int,str,slice,Tuple[Union[str,int,slice,Tuple[str]]]],item:Any):
        """
        Set new values to desired parts of the matrix.
        Uses same logic __getitem__ method uses.

        If a single value is given on the right-hand-side, value replaces all other values where left-hand-side represents
        Example:
            #Every row with even index numbers gets their 'Col 3' column changed to value 99
                Matrix[::2,"col_3"] = 99                        
                
            #Rows where their 'Score1' is lower than 50 gets their 'Pass1' and 'Pass2' columns replaced with value 0   
                Matrix[Matrix["Score1"]<50,('Pass1','Pass2')] = 0
            
                #Following method does the same changes, slightly faster on most cases
                Matrix.replace(Matrix["Score1"]<50,0,('Pass1','Pass2'))
            
            Check README.md and exampleMatrices.py for more examples
        """
        from MatricesM.matrixops.getsetdel import setitem
        setitem(self,pos,item,Matrix)

    def __delitem__(self,val:object):
        """
        Works 'similar' to __getitem__ , but can only be used to delete entire columns and/or rows
        Example:
            del Matrix['col_2']     #Delete 2nd column of the matrix
        """
        from MatricesM.matrixops.getsetdel import delitem
        delitem(self,val,Matrix)

    def __repr__(self):
        """
        Returns the matrix's string form using its row and column limits
        """
        from MatricesM.matrixops.repr import _repr
        return _repr(self,self.NOTES,dataframe)
    
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        self.__dim=self._declareDim()
        s=self._stringfy(coldtypes=self.coldtypes[:])
        notes = self.NOTES
        if not isinstance(notes,str):
            raise TypeError(f"NOTES option can only be used with strings, not {type(notes).__name__}")
        if not self.isSquare:
            print("\nDimension: {0}x{1}".format(self.dim[0],self.dim[1]))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}".format(self.dim[0]))
        return s+"\n\n" + notes 
    
    @property
    def kwargs(self):
        return {"dim":self.dim[:],
                "listed":[a[:] for a in self._matrix],
                "fill":self.fill,
                "ranged":self.initRange,
                "seed":self.seed,
                "features":self.features[:],
                "decimal":self.decimal,
                "dtype":self.dtype,
                "coldtypes":self.coldtypes[:],
                "index":self.index[:],
                "indexname":self.indexname,
                "implicit":True}
                
    @classmethod
    def __new__(cls,*args,**kwargs):
        return object.__new__(cls)

    def __call__(self,*args,**kwargs):
        if len(args)==0 and len(kwargs.keys())==0:
            return Matrix
        return Matrix(*args,**kwargs)

# =============================================================================
    """Arithmetic methods"""        
# =============================================================================
    def __matmul__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import matmul
        return matmul(self,other,Matrix,self.matrix)
    
    def __add__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import add
        return add(self,other,Matrix,self.matrix,dataframe)
            
    def __sub__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import sub
        return sub(self,other,Matrix,self.matrix,dataframe)
     
    def __mul__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import mul
        return mul(self,other,Matrix,self.matrix,dataframe)

    def __floordiv__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import fdiv
        return fdiv(self,other,Matrix,self.matrix,dataframe)
            
    def __truediv__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import tdiv
        return tdiv(self,other,Matrix,self.matrix,dataframe)

    def __mod__(self, other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import mod
        return mod(self,other,Matrix,self.matrix,dataframe)
         
    def __pow__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import pwr
        return pwr(self,other,Matrix,self.matrix,dataframe)

# =============================================================================
    """ Comparison operators """                    
# =============================================================================
    def __le__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import le
        return le(self,other,Matrix,self.matrix)
        
    def __lt__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import lt
        return lt(self,other,Matrix,self.matrix)
        
    def __eq__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import eq
        return eq(self,other,Matrix,self.matrix)
        
    def __ne__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import ne
        return ne(self,other,Matrix,self.matrix)
                
    def __ge__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import ge
        return ge(self,other,Matrix,self.matrix)
        
    def __gt__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import gt
        return gt(self,other,Matrix,self.matrix)
        
# =============================================================================
    """ Rounding etc. """                    
# =============================================================================   
    def __round__(self,n:int=-1):
        from MatricesM.matrixops.rounding import rnd
        return rnd(self,n,Matrix,self.matrix,dataframe)
    
    def __floor__(self):
        from MatricesM.matrixops.rounding import flr
        return flr(self,Matrix,self.matrix,dataframe)     
    
    def __ceil__(self):
        from MatricesM.matrixops.rounding import ceil
        return ceil(self,Matrix,self.matrix,dataframe)
    
    def __abs__(self):
        from MatricesM.matrixops.rounding import _abs
        return _abs(self,Matrix,self.matrix,dataframe)

# =============================================================================

