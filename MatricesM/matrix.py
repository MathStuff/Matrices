# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

from MatricesM.validations import *
from MatricesM.errors import *
from MatricesM.constructors import *
from MatricesM.customs import *

import re
from typing import Union,Tuple,List,Any,Dict,Optional

from random import random,randint,uniform,triangular,\
                   gauss,gammavariate,betavariate,   \
                   expovariate,lognormvariate,seed


class Vector:
    """
    Column vector

    data: list|list of lists|str; column data
    """
    def __init__(self,data):
        self._cMat = 0
        self._dfMat = 0
        self._fMat = 1
        self.__data = []

        #Data check
        if isinstance(data,(list,tuple)):
            self.__data = [[d] if not isinstance(d,list) else d for d in data]

        elif isinstance(data,str):
            from MatricesM.setup.listify import _listify
            self.__data = _listify(self,data,True)

        else:
            raise TypeError(f"Can't use type {type(data).__name__} for 'data' parameter")

    @property
    def norm(self):
        return sum([i[0]**2 for i in self.__data])**(0.5) if self.d1==1 else None

    @property
    def dim(self):
        return [self.d0,1]
    @property
    def d0(self):
        return len(self.__data)
    @property
    def d1(self):
        return 1
    
    def __getitem__(self,ind):
        return self.__data[ind][0]

    def __setitem__(self,ind,val):
        self.__data[ind][0] = val

    def __repr__(self):
        return "\n"+"\n".join([str(val[0]) for val in self.__data])+f"\n\nsize: [{self.d0}x1]"

class Matrix(Vector):
    """
    dim: int OR list|tuple of 2 integers; dimensions of the matrix. Giving an integer creates assumes square matrix
    
    data: str|list of lists of values|list of values; Elements of the matrix.

    fill: Any; Fills the matrix with chosen distribution or the value, default is uniform distribution
          Available distributions:
            ->uniform,gauss,lognormvariate,triangular,gammavariate,betavariate,expovariate
          
    ranged: list|tuple of numbers OR dict{column names:list|tuple of numbers}; 
        Usage:
           ->To apply all the elements give a list | tuple
           ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
           ->Arguments should follow one of the following rules:
                1)If 'fill' is uniform --> [minimum,maximum]; 
                2)If 'fill' is gauss or lognormvariate --> [mean,standard_deviation];
                3)If 'fill' is triangular --> [minimum,maximum,mode];
                4)If 'fill' is gammavariate or betavariate --> [alpha,beta]
                5)If 'fill' is expovariate --> [lambda]

    features: list of strings|Label; column names
    
    seed: int; seed to use while generating random numbers, not useful when fill isn't a special distribution
    
    decimal: int; Digits to round to and print

    dtype: int|float|complex|dataframe; type of values the matrix will hold

    coldtypes: tuple|list of objects; data types for each column individually.

    index: Label|Matrix|list|tuple of objects; indices to use for rows. Only works if dtype is set to dataframe
    
    implicit: bool; Skip matrix setting operations if dimensions and elements are given

    NOTE:      
        --> Options: ROW_LIMIT:int, PRECISION:int, QR_ITERS:int, EIGENVEC_ITERS:int,
                     NOTES:str, DEFAULT_NULL:object, DISPLAY_OPTIONS:dict

        --> Check https://github.com/MathStuff/MatricesM  for further explanation and examples
    

        --> Example look of a dataframe with multi-level column names and row labels

            *Default options
            *Arrows are just for indicating levels of labels


            
            +-Lvl1 row label 
            I   +-Lvl2 row label
            V   I
                V

            A_group|  A1      A2         <--Lvl 1 column name
            B_group|  B1  B2  B1      <--Lvl 2 column name
               M, N+------------
              M1,N1| 130  30  10
                 N2| 125  36  11
              M3,N2| 135  34  10
              M4,N1| 133  30   9
                 N2| 129  38  12
        
    """
    def __init__(self,
                 dim:Union[int,List[int],Tuple[int],None]=None,
                 data:Union[List[List[Any]],List[Any],Any]=[],
                 fill:Any=None,
                 ranged:Union[List[Any],Tuple[Any],Dict[str,Union[List[Any],Tuple[Any]]],None]=[0,1],
                 seed:int=None,
                 decimal:int=4,
                 dtype:Union[int,float,complex,dataframe]=float,
                 features:Union[List[str],Label]=Label(),
                 coldtypes:List[type]=[],
                 index:Union[List[Any],Tuple[Any],Label]=Label(),
                 implicit:bool=False,
                 **kwargs):

        #Constants to use for printing,rounding etc.
        self.ROW_LIMIT = 30                         #Upper limit for amount of rows to be printed with __repr__
        self.PRECISION = 6                          #Decimals to round
        self.QR_ITERS = 50                          #QR algorithm iterations for eigenvalues
        self.EIGENVEC_ITERS = 10                    #Shifted inverse iteration method iterations for eigenvectors
        self.NOTES = ""                             #Extra info to add to the end of the string used in __repr__
        self.DEFAULT_NULL = null                    #Object to use as invalid value indicator
        self.DIRECTORY = ""                         #Path of the Matrix in disk
        self.DISPLAY_OPTIONS = {                    #Options and symbols used while displaying
                                "allow_label_dupes":False,
                                "dupe_place_holder":"//",
                                "label_seperator":",",
                                "left_top_corner":"+",
                                "left_seperator":"|",
                                "top_seperator":"-",
                                "col_place_holder":"...",
                                "row_place_holder":"...",
                               }
        #Basic attributes
        self.__features = features                  #Column names
        self.__coldtypes = coldtypes                #Column dtypes 
        self.__dim = dim                            #Dimensions
        self._matrix = data                         #Values
        self.__fill = fill                          #Filling method for the matrix
        self.__initRange = ranged                   #Given range for 'fill'
        self.__seed = seed                          #Seed to pick values from 
        self.__decimal = decimal                    #How many digits to display in decimal places
        self.__dtype = dtype                        #Type of the matrix
        self.__index = index                        #Column to use as index column
        self.__implicit = implicit                  #Implicity value
        self._cMat,self._fMat,self._dfMat = 0,0,0   #Types

        ######Overwrite attributes######
        if kwargs != {}:
            overwrite_attributes(self,kwargs)
        ################################
        self.defaults = {                           #Save default arguments for __call__
                         "dim":dim,
                         "data":data,
                         "fill":fill,
                         "ranged":ranged,
                         "seed":seed,
                         "decimal":decimal,
                         "dtype":dtype,
                         "features":features,
                         "coldtypes":coldtypes,
                         "index":index,
                         "ROW_LIMIT":self.ROW_LIMIT,
                         "PRECISION":self.PRECISION,
                         "QR_ITERS":self.QR_ITERS,
                         "EIGENVEC_ITERS":self.EIGENVEC_ITERS,
                         "NOTES":self.NOTES,
                         "DEFAULT_NULL":self.DEFAULT_NULL,
                         "DISPLAY_OPTIONS":self.DISPLAY_OPTIONS
                        }

        #Set/fix attributes
        self._setDim(self.__dim)           #Fix dimensions
        self.setInstance(self.__dtype)     #Store what type of values matrix can hold

        #For the favor of better results, increase iterations for odd numbered dimensions
        # if self.QR_ITERS < 250:
        #     self.QR_ITERS += 400*(self.__dim[0]%2)  
        
        #Setup the matrix and column names,types
        self.setup(True,self.__implicit)
        
# =============================================================================
    """Attribute formatting and setting methods"""
# =============================================================================    
    def __getattr__(self,attr:str):
        """
        Column names can be treated as attribute names

        Example:

            >>> df
                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
            this_group_2,that_class_3|      0        1        1       -1
            this_group_3,that_class_2|     -1       -2        0        2
            this_group_1,that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
            this_group_2,that_class_3|      1        1       -2        1
            this_group_3,that_class_2|      0        2        0       -1
            this_group_1,that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2
            this_group_2,that_class_3|      0       -1       -1        2

            >>> df.groups.group_3    #Short way of using df.colname["groups"].name["group_3"]

                               groups|group_3
                              classes|class_2
                    this,        that+-------
            this_group_1,that_class_1|     -1
            this_group_2,that_class_3|      1
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|      1
            this_group_2,that_class_3|     -2
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|     -2
            this_group_2,that_class_3|     -1

            n:10,type:int,invalid:0
            
        """
        try:
            return object.__getattribute__(self,attr)
        except:
            try:
                if attr == "_Matrix__use_value_based_comparison":
                    return False
                
                #Try as column label name
                if attr in self.features.names:
                    return self.level[self.features.names.index(attr)+1].name

                #Try as a level-1 column name
                return self.level[1].name[attr]
                
            except MatrixError:#Nothing worked ¯\_(ツ)_/¯
                raise AttributeError(f"'{attr}' is not a column name nor an attribute or a method of Matrix")

    def setup(self,first:bool,implicit:bool=False):
        #Whetere or not there are random numbers involved
        randomly_filled = True if self._matrix in [None,[],{},[[]]] else False
        #Matrix fix
        if first and not implicit:
            self.setMatrix(self.dim,self.initRange,self._matrix,self.fill,self._cMat,self._fMat)
        
        d0,d1 = self.__dim
        df = self._dfMat
        dt = self.dtype
        cdts = self.coldtypes
        names = self.features if self.features != None else []

        #Column names
        if len(names) != d1:
            names = Label([(f"col_{i}",) for i in range(1,d1+1)],[""],implicit=True)

        #Column types
        if not validlist(self._matrix):
            return None

        if not type(self.DEFAULT_NULL).__name__ in ["type","null"]:
            raise TypeError("'DEFAULT_NULL' should be a 'type' or 'null' type")

        #Set column dtypes
        #Not enough types given, reset given types
        if len(cdts) != d1:
            if self.fill == self.DEFAULT_NULL:
                self.__coldtypes = [self.DEFAULT_NULL for _ in range(d1)]
            elif df:
                from MatricesM.setup.declare import declareColdtypes
                self.__coldtypes = declareColdtypes(self.matrix,self.DEFAULT_NULL.__name__)
            else:
                self.__coldtypes = [dt]*d1

        cdts = self.__coldtypes

        #Index shouldn't be None
        if self.__index in [[],None]:
            self.__index = Label()

        #Apply coldtypes to values in the matrix, set indices, update names
        if df:

            mm = self.matrix

            #Apply column dtypes to each column's values if they weren't randomly picked
            if not randomly_filled:
                def_null_name = self.DEFAULT_NULL.__name__
                for i in range(d0):
                    j=0
                    rowcopy = mm[i][:]
                    while j<d1:
                        try:
                            cdtype = cdts[j]
                            if cdtype != type:
                                val = rowcopy[j]
                                if type(val).__name__ != def_null_name:
                                    rowcopy[j] = cdtype(val)
                            j+=1
                        except:
                            j+=1
                            continue
                    mm[i] = rowcopy[:]

            ind = self.__index
            
            if isinstance(ind,Label):
                label_len = len(ind)
                if label_len == 0:
                    if first:
                        self.__index = Label(list(range(d0)),"")
                    else:
                        raise IndexError(f"Expected {d0} labels, got {label_len} instead")
                elif label_len == d0:
                    self.__index = ind[:]
                else:
                    raise IndexError(f"Expected {d0} labels, got {label_len} instead")

            elif isinstance(ind,Matrix):
                if ind.d1 != 1:
                    raise TypeError("Index parameter only accepts column matrices")
                if ind.d0 != d0:
                    raise ValueError(f"Invalid index matrix; expected {d0} rows, got {ind.d0}")
                
                self.__index = Label([tuple(row) for row in ind.matrix],ind.features.get_level(1))

            elif isinstance(ind,(list,tuple)):
                if len(ind) == 0:
                    self.__index = Label(list(range(d0)),"")
                elif len(ind) != d0:
                    raise ValueError(f"Invalid index list; expected {d0} values, got {len(ind)}")
                else:
                    self.__index = Label(list(ind)[:])
            else:
                raise TypeError(f"Type {type(ind).__name__} can't be used as indices")
            
            self._matrix = mm

        if not isinstance(names,Label):
            names = Label(names)
        self.__features = names

    def setInstance(self,dt:Union[int,float,complex,dataframe]):
        """
        Set the type
        """
        self._fMat = 1 if (dt in [complex,float]) else 0
        self._cMat = 1 if (dt == complex) else 0
        self._dfMat = 1 if (dt == dataframe) else 0 
               
    def _setDim(self,d:Union[int,list,tuple]):
        """
        Set the dimension to be a list if it's an integer
        """
        valid = 0
        if isinstance(d,int):
            if d>=1:
                self.__dim=[d,d]
                valid = 1
        elif isinstance(d,(list,tuple)):
            if len(d)==2:
                if isinstance(d[0],int) and isinstance(d[1],int):
                    if d[0]>0 and d[1]>0:
                        self.__dim=list(d)
                        valid = 1
        if not valid:
            self.__dim = [0,0]
        
    def setMatrix(self,
                  dim:Union[int,list,tuple,None]=None,
                  ranged:Union[List[Any],Tuple[Any],Dict[str,Union[List[Any],Tuple[Any]]],None]=None,
                  lis:Union[List[List[Any]], List[Any]]=[],
                  fill:Any=uniform,
                  cmat:bool=False,
                  fmat:bool=True):
        """
        Set the matrix based on the arguments given
        """
        from MatricesM.setup.matfill import _setMatrix
        _setMatrix(self,dim,ranged,lis,fill,cmat,fmat,uniform=uniform,seed=seed,null=self.DEFAULT_NULL)
        
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
        return declareRange(self,lis,dataframe)

# =============================================================================
    """Element setting methods"""
# =============================================================================
    def _listify(self,stringold:str):
        """
        Finds all the numbers in the given string
        """
        from MatricesM.setup.listify import _listify
        return _listify(self,stringold,False)
            
    def _stringfy(self,coldtypes:Union[List[Any],None]=None,returnbounds:bool=False,grid:bool=False):
        """
        Turns a list into a grid-like form that is printable
        Returns a string
        """
        from MatricesM.setup.stringfy import _stringfy
        return _stringfy(self,coldtypes,returnbounds,grid)

# =============================================================================
    """Row labels used as indices"""
# =============================================================================
    @property
    class level:
        def __init__(self,mat):
            if not mat._dfMat:
                raise TypeError("Can't use row label indexing with non-dataframe matrices") 
            self.mat = mat

        def __getitem__(self,pos):
            if not isinstance(pos,int):
                raise TypeError("Level can't be non-int")
            if pos <=0:
                raise ValueError("Level can't be lower than 1")
            
            self.level = pos
            return self

        @property
        class name:
            def __init__(self,parent):
                self.mat = parent.mat
                self.level = parent.level
                self.df = parent.mat._dfMat

            def __getattr__(self,attr:str):
                try:
                    return object.__getattribute__(self,attr)
                except:
                    try:
                        return self[attr]
                    except:
                        raise AttributeError(f"{attr} is not a column name nor an attribute of 'name' class")

            def __getitem__(self,pos):
                """
                Using row indices/labels:
                    --> Use it after sorting the dataframe for the best results for slices
                    
                    >>> df = dataframe()    #Constructor

                    >>> df.level[1].name['core_a']   #Returns all the rows where the level 1 column name is 'core_a'

                    >>> df.level[3].name['layer_1','layer_5','none']   #Returns all the rows where 
                                                                        level 3 row label's are
                                                                        one of ['layer_1','layer_5','none'] 

                    >>> df.level[2].name["sub2":"sub5"]    #Return all the rows with first 'sub2' column name appearance
                                                            until 'sub5' s first appearance on level 2 column names
                    
                """
                from MatricesM.matrixops.getsetdel import getitem
                return getitem(mat=self.mat,
                               pos=pos,
                               obj=Matrix,
                               usename=True,
                               namelevel=self.level)

            def __setitem__(self,pos,val):
                from MatricesM.matrixops.getsetdel import setitem
                setitem(mat=self.mat,
                        pos=pos,
                        item=val,
                        obj=Matrix,
                        usename=True,
                        namelevel=self.level)

            def __delitem__(self,val:object):
                """
                Works 'similar' to __getitem__ , but can only be used to delete columns 
                Example:
                    >>> del Matrix.level[2].name["core_a","core_c"]   #Delete all rows with level 1 row labeled "core_a" and "core_c"
                """
                from MatricesM.matrixops.getsetdel import delitem
                delitem(mat=self.mat,
                        pos=val,
                        obj=Matrix,
                        usename=True,
                        namelevel=self.level)  

        @property
        class ind:
            def __init__(self,level_class):
                self.mat = level_class.mat
                self.level = level_class.level
                self.df = level_class.mat._dfMat

            def __getitem__(self,pos):
                """
                Using row indices/labels:
                    --> Use it after sorting the dataframe for the best results for slices
                    
                    >>> df = dataframe()    #Constructor

                    >>> df.level[1].ind["pending"]   #Returns all the rows where the row label at level 1 is 'pending'

                    >>> df.level[3].ind[1990,"Score"]   #Returns the 'Score' column of all the rows where level 3 row label is 1990

                    >>> df.level[2].ind[50:150]    #Return the rows with index higher than 50 and less than 150 in level 2 row labels
                                                   #starts and stops with limits' first appearances
                                                            
                    >>> df.level[1].ind["Average":,"Final_Score"]   #Return the rows' 'Final_Score' columns from where the level 1 
                                                                    #labels start from 'Average'
                    
                """
                from MatricesM.matrixops.getsetdel import getitem
                return getitem(mat=self.mat,
                               pos=pos,
                               obj=Matrix,
                               uselabel=1,
                               rowlevel=self.level)

            def __setitem__(self,pos,val):
                from MatricesM.matrixops.getsetdel import setitem
                setitem(mat=self.mat,
                        pos=pos,
                        item=val,
                        obj=Matrix,
                        uselabel=1,
                        rowlevel=self.level)

            def __delitem__(self,val:object):
                """
                Works 'similar' to __getitem__ , but can only be used to delete rows
                Example:
                    >>> del Matrix.level[1].ind["parrot"]     #Delete all rows with level 1 row labeled "parrot"
                """
                from MatricesM.matrixops.getsetdel import delitem
                delitem(mat=self.mat,
                        pos=val,
                        obj=Matrix,
                        uselabel=1,
                        rowlevel=self.level)  

    @property
    class rowname:
        """
        Use Label object's column names for indexing to get filter matrix's rows

        Example:

            >>> df
                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
            this_group_2,that_class_3|      0        1        1       -1
            this_group_3,that_class_2|     -1       -2        0        2
            this_group_1,that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
            this_group_2,that_class_3|      1        1       -2        1
            this_group_3,that_class_2|      0        2        0       -1
            this_group_1,that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2
            this_group_2,that_class_3|      0       -1       -1        2

            >>> df.rowname["this"].ind["this_group_1"] #Same as df.level[1].ind["this_group_1"]

                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
                      // that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
                      // that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2


        NOTE:

        -> Since '__getitem__' is returning a Matrix.level object, following calls will return the same results

                >>> df.level[1].name["group_3"]

                >>> df.rowname["this"].name["group_3"]

                #Because 'this' is the level-1 of the row label names

        """
        def __init__(self,mat):
            if not mat._dfMat:
                raise TypeError("Can't use row name indexing with non-dataframe matrices") 
            self.mat = mat

        def __getitem__(self,pos):
            if not isinstance(pos,str):
                raise TypeError("Row label column name can't be non-str")

            if not pos in self.mat.index.names:
                raise TypeError(f"{pos} is not a row label column name")

            lvl = self.mat.index.names.index(pos) + 1
            return self.mat.level[lvl]

    @property
    class colname:
        """
        Use Label object's column names for indexing to get filter matrix's columns
        
        Example:

            >>> df
                               groups|group_1  group_2  group_3  group_1
                              classes|class_1  class_3  class_2  class_3
                    this,        that+----------------------------------
            this_group_1,that_class_1|      0       -1       -1        2
            this_group_2,that_class_3|      0        1        1       -1
            this_group_3,that_class_2|     -1       -2        0        2
            this_group_1,that_class_3|      1        0        0       -1
                      // that_class_1|      1        0        1        1
            this_group_2,that_class_3|      1        1       -2        1
            this_group_3,that_class_2|      0        2        0       -1
            this_group_1,that_class_3|     -1        0        0        0
                      // that_class_1|      1        1       -2        2
            this_group_2,that_class_3|      0       -1       -1        2

            >>> df.colname["groups"].name["group_3"]

                               groups|group_3
                              classes|class_2
                    this,        that+-------
            this_group_1,that_class_1|     -1
            this_group_2,that_class_3|      1
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|      1
            this_group_2,that_class_3|     -2
            this_group_3,that_class_2|      0
            this_group_1,that_class_3|      0
                      // that_class_1|     -2
            this_group_2,that_class_3|     -1

            n:10,type:int,invalid:0

        """
        def __init__(self,mat):
            if not mat._dfMat:
                raise TypeError("Can't use column name indexing with non-dataframe matrices") 
            self.mat = mat

        def __getitem__(self,pos):
            if not isinstance(pos,str):
                raise TypeError("Column names can't be non-str")

            if not pos in self.mat.features.names:
                raise TypeError(f"{pos} is not a name for column name rows")

            lvl = self.mat.features.names.index(pos) + 1
            return self.mat.level[lvl]

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
        if self.d0>=rows:
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
        if self.d0>=rows:
            return self[self.d0-rows:]
        return self[:,:]

    def col(self,column:Union[int,str],as_matrix:bool=True):
        """
        Get a specific column of the matrix
        column:integer>=1 and <=column_amount | column name
        as_matrix:False to get the column as a list, True to get a column matrix (default) 
        """
        #Column number given
        if isinstance(column,int):
            if not (column<=self.d1 and column>0):
                raise InvalidColumn(column,"Column index out of range")
            
            #Return matrix
            if as_matrix:
                return self[:,column-1]

        #Column name given
        elif isinstance(column,str):
            if not column in self.features.get_level(1):
                raise InvalidColumn(column,f"'{column}' is not in column names")

            #Return matrix
            if as_matrix:
                return self.__getattr__(attr=column)

            column = self.features.index(column)+1

        #Invalid type
        else:
            raise InvalidColumn(column)

        #Return list
        mm = self._matrix
        return [mm[r][column-1] for r in range(self.d0)]
    
    def row(self,row:int=None,as_matrix:bool=True):
        """
        Get a specific row of the matrix
        row:integer>=1 and <=row_amount
        as_matrix:False to get the row as a list, True to get a row matrix (default) 
        """
        if isinstance(row,int):
            if not (row<=self.d0 and row>0):
                raise InvalidIndex(row,"Row index out of range")
        else:
            raise InvalidIndex(row)

        if as_matrix:
            return self[row-1:row]
        return self._matrix[row-1][:]
                    
    def add(self,lis:List[Any],
            row:Union[int,None]=None,
            col:Union[int,None]=None,
            feature:Union[str,None]=None,
            dtype:Any=None,
            index:Any="",
            returnmat:bool=False,
            fillnull=False):
        """
        Add a row or a column of numbers

        lis: list; list of objects desired to be added to the matrix
        row: int>=1; row index
        col: int>=1; column index
        feature:str; new column's name
        dtype: type; type of data the new column will hold, doesn't work if a row is inserted
        returnmat:bool; wheter or not to return self
        fillnull:bool; wheter or not to use null object to fill values in missing indices

        To append a row, use row=self.d0
        To append a column, use col=self.d1
        """
        from MatricesM.matrixops.add import add
        add(self,lis,row,col,feature,dtype,index,fillnull)
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
        remove(self,self.d0,self.d1,row,col)
        if returnmat:
            return self  

    def concat(self,matrix:object,axis:[0,1]=1,returnmat:bool=False,fillnull=False):
        """
        Concatenate matrices row or columns vice

        matrix:Matrix; matrix to concatenate to self
        axis:0|1; 0 to add 'matrix' as rows, 1 to add 'matrix' as columns
        returnmat:bool; wheter or not to return self
        fillnull:bool; wheter or not to use null object to fill values in missing indices
        """
        from MatricesM.matrixops.concat import concat
        concat(self,matrix,axis,fillnull,Matrix)
        if returnmat:
            return self
            
    def delDim(self,num:int):
        """
        Removes desired number of rows and columns from bottom right corner
        """        
        from MatricesM.matrixops.matdelDim import delDim
        delDim(self,num)

    def swap(self,index1:Union[int,str],index2:Union[int,str],axis:[0,1]=1,returnmat:bool=False):
        """
        Swap two rows or columns

        index1:int>0|str; first row index OR column index|name
        index2:int>0|str; second row index OR column index|name
        axis:0|1; 0 for row swap, 1 for column swap
        returnmat:bool; wheter or not to return self after evaluation
        """
        feats = self.features[:]
        for index in [index1,index2]:
            if axis==1:
                if isinstance(index,str):
                    index = feats.index(index)
            assert index>0 and index<=self.d0
        assert axis in [0,1], "axis should be 0 for row swap, 1 for column swap"

        if axis==0:
            self._matrix[index1],self._matrix[index2] = self._matrix[index2][:],self._matrix[index1][:]
            if self._dfMat:
                self.__index[index1],self.__index[index2] = self.__index[index2],self.__index[index1]
        else:
            self[feats[index1]],self[feats[index2]] = self[feats[index2]],self[feats[index1]]
            self.__coldtypes[index1],self.__coldtypes[index2] = self.__coldtypes[index2],self.__coldtypes[index1]
            self.__features[index1],self.__features[index2] = self.__features[index2],self.__features[index1]

        if returnmat:
            return self

    def setdiag(self,val:Union[Tuple[Any],List[Any],object]):
        """
        Set new diagonal elements

        val:Any; object to set as new diagonals. 
            -> If a Matrix is given, new diagonals are picked as given matrix's diagonals
            -> If a list/tuple is passed, it should have the length of the smaller dimension of the matrix
            -> Any different value types are treated as single values, all diagonal values get replaced with given object
        """
        expected_length = min(self.dim)
        if isinstance(val,Matrix):
            if min(val.dim)!=expected_length:
                raise DimensionError(f"Expected {expected_length} diagonal elements, got {min(val.dim)}.")

            for i in range(expected_length):
                self._matrix[i][i] = val.matrix[i][i]

        elif isinstance(val,(list,tuple)):
            if len(val) != expected_length:
                raise DimensionError(f"Expected {expected_length} elements, got {len(val)}.")

            for i in range(expected_length):
                self._matrix[i][i] = val[i]

        else:
            for i in range(expected_length):
                self._matrix[i][i] = val
    
    def drop_null(self,axis=0,returnmat=False):
        """
        Remove rows or columns with default null values
        """
        if not self._dfMat:
            raise TypeError("Can't drop null values from non-dataframe matrices")
        
        assert axis in [0,1] , "'axis' should be 0 for rows, 1 for columns"

        def_null = self.DEFAULT_NULL
        null_indices = self.find(def_null,0,False)

        #Drop rows
        if axis == 0:
            row_inds = list(set([i for i,j in null_indices]))
            for leap,i in enumerate(row_inds):
                del self._matrix[i-leap]
                del self.__index[i-leap]

            self.__dim[0] -= len(row_inds)
    
        #Drop columns
        else:
            col_inds = list(set([j for i,j in null_indices]))
            for row in range(self.d0):
                for leap,j in enumerate(col_inds):
                    del self._matrix[row][j-leap]
            
            for leap,j in enumerate(col_inds):
                del self.__features[j-leap]
            
            self.__dim[1] -= len(col_inds)

        if returnmat:
            return self

    def fill_null(self,item,returnmat=False):
        """
        Replace null values with the given object
        """
        return self.replace(self.DEFAULT_NULL,item,returnmat=returnmat)
        
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
        return transpose(self,hermitian,obj=Matrix,labelobj=Label)

    def minor(self,row:int,col:int,returndet:bool=True):
        """
        Returns the minor of the element in the desired position
        row,col : row and column indices of the element, 1<=row and col
        returndet : True if the determinant is wanted, False to return the matrix the determinant is calculated from 
        """
        from MatricesM.linalg.minor import minor
        return minor(self,row,col,returndet)

    def _adjoint(self):
        """
        Returns the adjoint matrix
        """
        from MatricesM.linalg.adjoint import adjoint
        dt = complex if self.dtype==complex else float
        return Matrix(self.dim,adjoint(self),dtype=dt,implicit=True)
    
    def _inverse(self):
        """
        Returns the inversed matrix
        """
        from MatricesM.linalg.inverse import inverse
        return inverse(self,Identity(self.d0))

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
    
    def _eigenvals(self):
        """
        Returns the eigenvalues using QR algorithm
        """
        try:
            assert self.isSquare and self.d0>=2
            if self.d0==2:
                d=self.det
                tr=self.matrix[0][0]+self.matrix[1][1]
                return list(set([(tr+(tr**2 - 4*d)**(1/2))/2,(tr-(tr**2 - 4*d)**(1/2))/2]))
        
            eigens = []
            q=self.Q
            a1=q.t@self@q
            for i in range(self.QR_ITERS):#Iterations start
                qq=a1.Q
                a1=qq.t@a1@qq
            #Determine which values are real and which are complex eigenvalues
            if self.isSymmetric:#Symmetrical matrices always have real eigenvalues
                return a1.diags

            #Wheter or not dimensions are odd
            isOdd=(a1.d0%2)
            precision = self.PRECISION
            #Decide wheter or not to skip the bottom right 2x2 matrix
            if a1._cMat: 
                neighbor = a1[-1,-2]
                if round(neighbor.real,precision)==0 and round(neighbor.imag,precision):
                    eigens.append(a1[-1,-1])
            else:
                if round(a1[-1,-2],precision)==0:
                    eigens.append(a1[-1,-1])

            #Create rest of the eigenvalues from 2x2 matrices
            ind=0
            while ind<a1.d0-1:
                mat = a1[ind:ind+2,ind:ind+2]
                ind+=1+isOdd

                #Decide wheter or not to skip the top right corner 2x2 matrix
                done=0
                if a1._cMat:
                    if round(mat[1,0].real,precision)==0 and round(mat[1,0].imag,precision):
                        eigens.append(mat[0,0])
                        ind-=isOdd
                        done=1

                elif round(mat[1,0],precision)==0:
                    eigens.append(mat[0,0])
                    ind-=isOdd
                    done=1

                #2x2 matrices in the middle
                if not done:
                    ind+=1-isOdd
                    r = mat.trace/2
                    v = (mat.det - r**2)**(1/2)
                    
                    r = complex(complex(roundto(r.real,precision,True)),complex(roundto(r.imag,precision,True)))
                    v = complex(complex(roundto(v.real,precision,True)),complex(roundto(v.imag,precision,True)))               
                    
                    c1 = complex(r,v)
                    c2 = complex(r,v*(-1))
                    
                    if c1.imag==0:
                        c1 = c1.real
                    if c2.imag==0:
                        c2 = c2.real
                    
                    eigens.append(c1)
                    eigens.append(c2)
        except:
            return None
        else:
            return eigens

    def _eigenvecs(self,iters,alpha=1+1e-5):
        """
        Returns the eigenvectors, eigenvector matrix and diagonal matrix
        """
        eigens = self.eigenvalues or self.diags
        if eigens in [None,[]]:
            return None
        
        d0,d1 = self.dim[:]
        ones = Matrix((self.d0,1),fill=1)
        vectors = []
        
        for eig in eigens:
            i = 0
            c = None
            x = ones.copy
            eigen = eig*alpha
            identity = Identity(d0)*(eigen)
            
            while i<iters:
                try:
                    y = ((self - identity).inv)@x
                except:#Guess converged
                    break
                else:
                    c = (y.t@x).matrix[0][0]/(x.t@x).matrix[0][0]
                    if c == 0:
                        c = None

                    m = (y**2).sum("col_1",get=0)**(0.5)
                    if m == 0:
                        break

                    x = y/m
                    i += 1

            guess = (1/c)+eig if c != None else eig
            vectors.append((f"{i} iters for {eig}",guess,x))

        ########################################################
        eigenmat = vectors[0][2].copy
        dtype_changed = False

        for i in range(1,len(vectors)):
            colvec = vectors[i][2]

            if colvec.dtype == complex and not dtype_changed:
                eigenmat.dtype = complex
                dtype_changed == True

            eigenmat.concat(colvec,axis=1)

        ########################################################
        diagmat = Matrix(len(vectors),fill=0,dtype=float)
        dtype_changed = False

        for i in range(len(vectors)):
            eigvalue = vectors[i][1]
            if isinstance(eigvalue,complex) and not dtype_changed:
                diagmat.dtype = complex
                dtype_changed = True

            diagmat._matrix[i][i] = eigvalue

        ########################################################

        return (vectors,eigenmat,diagmat)

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
        return LU(self,Identity(self.d0).matrix,[a[:] for a in self.matrix],Matrix)

    def _QR(self):
        """
        Returns Q and R matrices from QR decomposition
        """
        from MatricesM.linalg.QR import QR
        return QR(self,Matrix)
    
    def _EIGENDEC(self):
        """
        Returns eigenvecmat, diagmat and the inverse eigenvecmat from eigenvalue decomposition
        """
        results = self._eigenvecs(self.EIGENVEC_ITERS)
        if results in [None,[]]:
            return (None,None,None)
        return (results[1],results[2],results[1].inv)

    def _SVD(self):
        """
        Singular value decomposition, Matrix = U@E@V.ht
        """
        try:
            transposed = self.t
            
            #self.t@self@V = V@E**2 --> solve eigenvalue problem
            left_hand_side = transposed@self
            E_and_V = left_hand_side.EIGENDEC
            E = E_and_V[1]**(0.5) #square root of diagonal matrix
            V = E_and_V[0].ht #hermitian transpose of the eigenvector matrix
            
            #self@self.t@U = U@E**2 --> solve eigenvalue problem
            left_hand_side = self@transposed
            U = left_hand_side.eigenvecmat

            for diagonal in E.diags:
                if isinstance(diagonal,complex):
                    E.dtype = complex
                    break
                    
        except:
            return (None,None,None)
        else:
            return (U,E,V)

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
        print(self.string)
    
    @property
    def copy(self):
        return Matrix(**self.kwargs)

    @property
    def string(self):
        return self._stringfy(coldtypes=self.coldtypes[:],grid=True)

    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self,li:Union[List[str],Tuple[str]]):
        if isinstance(li,Label):
            assert len(li) == self.d1 , f"Expected {self.d1} labels, got {len(li)} instead."
            
            str_labels = [tuple([str(lbl) for lbl in row]) for row in li.labels]    
            temp = Label(str_labels,li.names)

        elif not isinstance(li,(list,tuple)):
            raise NotListOrTuple(li)
        
        else:
            if len(li) != self.d1:
                raise InvalidList(li,self.d1,"column names")

            temp = []
            for i in range(len(li)):
                name = li[i]
                while name in temp:
                    name = "_"+name
                temp.append(name)

            temp = Label(temp)

        self.__features=temp
                
    @property
    def dim(self):
        return self.__dim
    @dim.setter
    def dim(self,val:Union[int,List[int],Tuple[int]]):
        amount = self.__dim[0]*self.__dim[1]
        if isinstance(val,int):
            assert val>0 , "Dimensions can't be <=0"
            val=[val,val]
        elif isinstance(val,list) or isinstance(val,tuple):
            assert len(val)==2 , f"Matrices accept 2 dimensions, {len(val)} length {type(val)} type can't be used."
        else:
            raise TypeError("dim setter only accepts int>0 or list/tuple with length of 2")

        assert val[0]*val[1]==amount , f"{amount} elements can't fill a matrix with {val} dimensions"

        m = self.matrix
        els=[m[i][j] for i in range(self.d0) for j in range(self.d1)]
        temp=[[els[c+val[1]*r] for c in range(val[1])] for r in range(val[0])]
        self.__init__(dim=list(val),data=temp,dtype=self.dtype,implicit=True)
    
    @property
    def d0(self):
        return self.__dim[0]
    @property
    def d1(self):
        return self.__dim[1]

    @property
    def fill(self):
        return self.__fill
    @fill.setter
    def fill(self,value:[object]):
        try:
            spec_names = ["method","function","builtin_function_or_method",self.DEFAULT_NULL.__name__]
            assert (type(value).__name__ in spec_names) \
                or (type(value) in [int,str,float,complex,range,list]) \
                or  value==None
        except AssertionError:
            raise FillError(value)
        else:
            self.__fill=value
            self.setMatrix(self.__dim,self.__initRange,[],value,self._cMat,self._fMat)

    @property
    def initRange(self):
        return self.__initRange
    @initRange.setter
    def initRange(self,value:Union[ List[Union[float,int]], Tuple[Union[float,int]], Dict[str,Union[Tuple,List]] ]):

        #Check given lists compatability with matrix's 'fill' attribute
        def list_checker(value,fill):
            if ( fill in [uniform,gauss,gammavariate,betavariate,lognormvariate] ) \
            or ( isinstance(fill,(int,float,complex)) ):
                if len(value)!=2:
                    raise IndexError("""initRange|ranged should be in the following formats:
                                        fill is gauss|lognormvariate --> [mean,standard_deviation]
                                        fill is (gamma|beta)variate --> [alpha,beta]
                                        fill is uniform --> [minimum,maximum]""")
                if not (isinstance(value[0],(float,int))) and not (isinstance(value[1],(float,int))):
                    raise ValueError("list contains non integer and non float numbers")
            
            elif fill in [triangular]:
                if len(value)!=3:
                    raise IndexError("initRange|ranged should be in the form of [minimum,maximum,mode]")
                if not (isinstance(value[0],(float,int))) and not (isinstance(value[1],(float,int))) \
                and not (isinstance(value[2],(float,int))):
                    raise ValueError("list contains non integer and non float numbers")
            
            elif fill in [expovariate]:
                if len(value)!=1:
                    raise IndexError("initRange|ranged should be in the form of [lambda]")
                
            else:
                pass

        if isinstance(value,dict):
            names,ranges = list(value.keys()),list(value.values())
            fill = self.fill

            if len(names) != self.d1:
                raise IndexError(f"Expected {self.d1} items in dictionary, got {len(names)} instead.")
            if not all([1 if name in self.features else 0 for name in names]):
                raise NameError("Dictionary keys should match column names")
            
            for lis in ranges:
                if not isinstance(lis,(tuple,list)):
                    raise TypeError(f"Values in dictionary should be lists or tuples")
                list_checker(lis,fill)

            self.__initRange = value

        elif isinstance(value,(list,tuple)):
            list_checker(value,self.fill)
            self.__initRange = list(value)

        else:
            raise TypeError(f"Can't use type '{type(value)} as a list,tuple or a dictionary")

        self.setMatrix(self.__dim,self.__initRange,[],self.__fill,self._cMat,self._fMat)

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
    def data(self):
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
        return self._eigenvals()

    @property
    def eigenvectors(self):
        res = self._eigenvecs(self.EIGENVEC_ITERS,1+1e-4)
        return [vec[2] for vec in res[0]] if not res in [None,[]] else []

    @property
    def eigenvecmat(self):
        res = self._eigenvecs(self.EIGENVEC_ITERS,1+1e-4)
        return res[1] if not res in [None,[]] else None
    
    @property
    def diagmat(self):
        res = self._eigenvecs(self.EIGENVEC_ITERS,1+1e-4)
        return res[2] if not res in [None,[]] else None

    @property
    def obj(self):
        """
        Object call as a string to recreate the matrix
        """
        f,cd = self.fill,str([i.__name__ for i in self.coldtypes]).replace("'","")
        if type(self.fill).__name__ == "method":
            f=self.fill.__name__
            
        dm,m,r,d = self.dim,self.matrix,self.initRange,self.decimal
        s,dt = self.seed,self.dtype.__name__
        i = "Label("+str(self.index.labels)+","+str(self.index.names)+")"
        fs = "Label("+str(self.features.labels)+","+str(self.features.names)+")"
        return f"Matrix(dim={dm},data={m},ranged={r},fill={f},features={fs},decimal={d},seed={s},dtype={dt},coldtypes={cd},index={i})"
 
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
                          data=self._matrix,
                          ranged=self.initRange,
                          fill=self.fill,
                          features=self.features,
                          decimal=self.decimal,
                          seed=self.seed,
                          dtype=self.dtype,
                          coldtypes=self.__coldtypes,
                          index=self.index,
                          )

    @property
    def coldtypes(self):
        return self.__coldtypes
    @coldtypes.setter
    def coldtypes(self,val:Union[List[str],Tuple[str]]):
        if not isinstance(val,(list,tuple)):
            raise NotListOrTuple(val)
        if len(val) != self.d1:
            raise InvalidList(val,self.d1,"column dtypes")

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
            if val.d0 != self.d0:
                raise ValueError(f"Given matrix can't be used as indices; expected {self.d0} rows, got {val.d0}")
            new_label = Label(val)
            self.__index = new_label

        elif isinstance(val,(list,tuple)):
            if len(val) != self.d0:
                raise ValueError(f"Given list can't be used as indices; expected {self.d0} values, got {len(val)}")
            self.__index = Label(list(val),self.index.names)

        elif val == None:
            self.__index = Label()

        elif isinstance(val,Label):
            if len(val) != self.d0:
                raise ValueError(f"Given Label can't be used as indices; expected {self.d0} labels, got {len(val)}")
            self.__index = val
        else:
            raise TypeError(f"Type {type(val).__name__} can't be used as indices")     

# =============================================================================
    """Check special cases"""
# =============================================================================    
    @property
    def isSquare(self):
        """
        Matrix.dim == [i,j] where i == j
        """
        return self.d0 == self.d1
    
    @property
    def isIdentity(self):
        """
        Matrix[i,j] == 1 where i==j and Matrix[i,j] == 0 where i!=j 
        """
        if not self.isSquare:
            return False
        return round(self,self.PRECISION).matrix == Identity(self.d0).matrix
    
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
        for i in range(1,self.d0):
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
        for i in range(1,self.d0):
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
        if 0 in [roundto(m[i][i],dig) for i in range(self.d0)] + [roundto(m[i][i+1],dig) for i in range(self.d0-1)]:
            return False
        
        #Assure the elements above first superdiagonal are zero
        for i in range(self.d0-2):
            if [0]*(self.d0-2-i) != roundto(m[i][i+2:],dig):
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
        if 0 in [roundto(m[i][i],dig) for i in range(self.d0)] + [roundto(m[i+1][i],dig) for i in range(self.d0-1)]:
            return False
        
        #Assure the elements above first subdiagonal are zero
        for i in range(self.d0-2):
            if [0]*(self.d0-2-i) != roundto(m[i][i+2:],dig):
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
        for i in range(2,self.d0):
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
        for i in range(2,self.d0):
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
        if not self.isSquare or self.d0<=2:
            return False
        m = self.matrix
        dig = self.PRECISION
        #Check diagonal and first subdiagonal and first superdiagonal
        if 0 in [roundto(m[i][i],dig) for i in range(self.d0)] \
              + [roundto(m[i][i+1],dig) for i in range(self.d0-1)] \
              + [roundto(m[i+1][i],dig) for i in range(self.d0-1)]:
            return False
        
        #Assure rest of the elements are zeros
        for i in range(self.d0-2):
            #Non-zero check above first superdiagonal
            if [0]*(self.d0-2-i) != roundto(m[i][i+2:],dig):
                return False
            
            #Non-zero check below first subdiagonal
            if [0]*(self.d0-2-i) != roundto(m[self.d0-i-1][:self.d0-i-2],dig):
                return False
        return True

    @property
    def isToeplitz(self):
        """
        Matrix[i,j] == Matrix[i+1,j+1] for every i and j
        """
        m = self.matrix
        dig = self.PRECISION
        for i in range(self.d0-1):
            for j in range(self.d1-1):
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
        return (self@self).roundForm(4).matrix == Identity(self.d0).matrix
    
    @property
    def isIncidence(self):
        """
        Matrix[i,j] == 0 | 1 for every i and j
        """
        for i in range(self.d0):
            for j in range(self.d1):
                if not self._matrix[i][j] in [0,1]:
                    return False
        return True
    
    @property
    def isZero(self):
        """
        Matrix[i,j] == 0 for every i and j
        """
        m = self.matrix
        for i in range(self.d0):
            for j in range(self.d1):
                if m[i][j] != 0:
                    return False
        return True

    @property
    def isDefective(self):
        """
        len(set(roundto(Matrix.eigenvalues,3))) != len(Matrix.eigenvalues)
        """
        eigs = self.eigenvalues
        return len(set(roundto(eigs,3))) != len(eigs) if not eigs in [None,[]] else False

# =============================================================================
    """Get special formats"""
# =============================================================================    
    @property
    def realsigns(self):
        """
        Determine the signs of the elements' real parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        mm = self._matrix
        signs=[[1 if mm[i][j].real>=0 else -1 for j in range(self.d1)] for i in range(self.d0)]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def imagsigns(self):
        """
        Determine the signs of the elements' imaginary parts
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        mm = self._matrix
        signs=[[1 if mm[i][j].imag>=0 else -1 for j in range(self.d1)] for i in range(self.d0)]
        return Matrix(self.dim,signs,dtype=int,implicit=True)
    
    @property
    def signs(self):
        """
        Determine the signs of the elements
        Returns a matrix filled with -1s and 1s dependent on the signs of the elements in the original matrix
        """
        mm = self._matrix
        if self._cMat:
            return {"Real":self.realsigns,"Imag":self.imagsigns}
        signs=[[1 if mm[i][j]>=0 else -1 for j in range(self.d1)] for i in range(self.d0)]
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
        mm = temp.matrix
        temp._matrix=[[mm[i][j].conjugate() if isinstance(mm[i][j],complex) else mm[i][j] for j in range(self.d1)] for i in range(self.d0)]
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
        if self.d0>self.d1:
            return ((self.t@self).inv)@(self.t)
        return None
    
    @property
    def EIGENDEC(self):
        """
        X, lambda and X.inv matrices from eigenvalue decomposition
        """
        return self._EIGENDEC()

    @property
    def SVD(self):
        """
        U,sigma and V.ht matrices from singular value decomposition
        """
        return self._SVD()

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
            return Matrix(self.dim,data=[a[:] for a in self.matrix],features=self.features,
                          coldtypes=[float if i in [int,float] else i for i in self.coldtypes],
                          decimal=self.decimal,seed=self.seed,dtype=dataframe,index=self.index,
                          implicit=True)

        mm = self.matrix
        t=[[float(mm[a][b]) for b in range(self.d1)] for a in range(self.d0)]

        return Matrix(self.dim,t,features=self.features,decimal=self.decimal,seed=self.seed,implicit=True)

    
    def roundForm(self,decimal:int=1,printing_decimal:Union[int,None]=None):
        """
        Elements rounded to the desired decimal after dot

        decimal: int; digits to round to
        printing_decimal: int; returned matrix's 'decimal' parameter
        """
        return self.__round__(decimal,printing_decimal)
        
# =============================================================================
    """Filtering methods"""
# =============================================================================     
    def select(self,columns:Union[List[str],Tuple[str],str]):
        """
        Returns a matrix with chosen columns
        
        columns: tuple|list of strings; Desired column names as strings in a tuple or list
        """
        if columns == None:
            return None
        if isinstance(columns,str):
            columns = (columns,)
        temp = self.col(self.features.index(columns[0])+1)
        for col in columns[1:]:
            temp.concat(self.col(self.features.index(col)+1))
        return temp

    def find(self,value:Any,
             start:[0,1]=1,
             onlyrow:bool=False):
        """
        value: object
        start: 0 or 1. Index to start from
        onlyrow: bool; Wheter or not to return only the row indices of value's appearances
        Returns the indices of the given value in a list
        """
        from MatricesM.filter.find import find
        return find([a[:] for a in self.matrix],self.dim,value,start,onlyrow)

    def join(self,
             SELECT:Union[Tuple[object],List[object]],
             METHOD:['INNER','LEFT','LEFT-EX','RIGHT','RIGHT-EX','FULL','FULL-EX','CROSS'],
             JOIN:object,
             ON:Union[str,None]=None):
        """
        Joins two matrices with given methods and conditions

        SELECT: list or tuple of column matrices|None; columns to return, '*' to use all columns
        METHOD: 'INNER'|'LEFT'|'LEFT-EX'|'RIGHT'|'RIGHT-EX'|'FULL'|'FULL-EX'|'CROSS'; joining method
        JOIN: Matrix object|None; matrix to use as the 2nd table
        ON: str|None; conditions to verify

        SQL:

            SELECT Table1.T_ID, Table2.Name, Table1.T_Date
            FROM Table1 
            INNER JOIN Table2 ON Table1.STD_ID=Table2.ID;

        Corresponding call:

            >>> Table1.join(SELECT=(Table1.T_ID, Table2.Name, Table1.T_Date),
                            METHOD='INNER',
                            JOIN=Table2,
                            ON='Table1.STD_ID == Table2.ID')

            # Notice that 'FROM' is always the dataframe that the join method is called from


        Example representation of methods:
            -> 1's represent the values which will be kept, 0's won't be used.
            -> Each number represents a row
            -> Left most 3 elements represent rows in self, right most are compared matrix's rows
            -> Middle 3 elements represent rows that are in both self and compared matrix

            --- Method ----------- Visually ---

                                    0  1  0
                INNER               0  1  0
                                    0  1  0
                
                                    1  1  0
                LEFT                1  1  0
                                    1  1  0

                                    1  0  0
               LEFT-EX              1  0  0
                                    1  0  0

                                    0  1  1
                RIGHT               0  1  1
                                    0  1  1
        
                                    0  0  1
               RIGHT-EX             0  0  1
                                    0  0  1

                                    1  1  1
                FULL                1  1  1
                                    1  1  1

                                    1  0  1
               FULL-EX              1  0  1
                                    1  0  1                   

        Example usage:
            ->Join Matrix and otherMatrix where Matrix.usr_id==otherMatrix.id,
            using left join, return usr_id and department columns

                >>> Matrix.join(SELECT=(Matrix.usr_id,otherMatrix.depertment),
                                FROM=otherMatrix,
                                JOIN='left',
                                ON='Matrix.usr_id == otherMatrix.id'
                                )
        
        NOTE:
            -> '-EX' methods guarantees a matrix with null values or an empty matrix
            -> If method is 'CROSS', 'ON' doesn't get used; If 'ON' is None, method is forced to 'CROSS'
        """
        from MatricesM.matrixops.joins import joins
        return joins(self,SELECT,METHOD,JOIN,ON,null,Matrix)

    def where(self,conditions:Union[List[str],Tuple[str]],inplace:bool=True):
        """
        Returns a matrix where the conditions are True for the desired columns.
        
        conditions:tuple/list of strings; Desired conditions to apply as a filter
        inplace:bool; True to compare values in place, False to search the values of self in 
                      given matrix with 'find' method and return matching rows as a Group object

        Syntax:
            Matrix.where((" ('Column_Name' (<|>|==|...) obj (and|or|...) 'Column_Name' ...") and ("'Other_column' (<|...) ..."), ...)
        
        Example:
            #Get the rows with Score in range [0,10) or Hours is higher than mean, where the DateOfBirth is higher than 1985
            
                >>> data.where( f" ( ( (Score>=0) and (Score<10) ) or ( Hours>={data.mean('Hours',0)} ) ) 
                                  and ( DateOfBirth>1985 ) ")
                #Same as
                    >>> data[(((data["Score"]>=0) & (data["Score"]<10)) | (data["Hours"]>=data.mean("Hours",0))) 
                            & (data["DateOfBirth"]>1985) ]

            #Return groups where ID of self matches EMP_ID in the given matrix

                >>> data.where("data.ID == table.EMP_ID",inplace=False)

        NOTE:
            -> Every statement HAVE TO BE enclosed in parentheses as shown in the examples above

        """
        from MatricesM.filter.where import wheres
        if inplace:
            results,indices = wheres(self,conditions,self.features[:],True),self.index[:]
            temp,found_inds = results
            lastinds = [indices[i] for i in found_inds] if self._dfMat else []

            return Matrix(data=temp,
                          features=self.features[:],
                          dtype=self.dtype,
                          coldtypes=self.coldtypes[:],
                          index=lastinds)
        else:
            return wheres(self,contiditions,self.features[:],False)
        
    def apply(self,expressions:Union[str,List[str],Tuple[str]],
              columns:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=(None,),
              conditions:Union[str,object,None]=None,
              returnmat:bool=False):
        """
        Apply arithmetic, logical, indexing etc. operations to values in desired columns individually inplace

        expressions: str(1 column only)|tuple|list of strings; Operations to do for each column given.
            ->Multiple operations can be applied if given in a single string. 
            ->One white space required between each operation and no space should 
            be given between operator and operand
        
        columns: str(1 column only)|tuple|list|None; Column names to apply the given expression
        
        conditions: str|boolean column Matrix|None; Conditions of rows to apply changes to

        returnmat: bool; True to return self after evaluation, False to return None

        Given operation is applied as:
            >>> exec("values[row][col] = eval('values[row][col]'+operation)")

        Example:

            #Multiply all columns with 3 and then add 10
                >>> Matrix.apply( ("*3 +10") ) 

            #Multiply Prices with 0.9 and subtract 5 also add 10 to Discounts where Price>100 and Discount<5
                >>> Matrix.apply( ("*0.9 -5","+10"), ("Price","Discount"), "(Price>100) and (Discount<5)" )

                #Same as the following process
                >>> filtered = market_base[(market_base.Price>100) & (market_base.Discount<5)]
                >>> filtered['Price'] *= 0.9
                >>> filtered['Price'] -= 5
                >>> filtered['Discount'] += 10
                >>> market_base[(market_base.Price>100) & (market_base.Discount<5)] = filtered

            #Turn strings in "Name" column into their lengths
                >>> Matrix.apply(".__len__()","Name")
        
        NOTE:
            Some tweaks to 'coldtypes' may be needed after operations

        """
        from MatricesM.filter.apply import applyop
        if returnmat:
            return applyop(self,expressions,columns,conditions,self.features[:],True,Matrix)
        applyop(self,expressions,columns,conditions,self.features[:],True,Matrix)

    def transform(self,function:object,
                  columns:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=(None,),
                  conditions:Union[str,object,None]=None,
                  returnmat:bool=False):
        """
        Pass values in the matrix to functions and replace them with the outputs

        function: function; A function to pass values to

        columns: str(1 column only)|tuple|list|None; Column names to use

        conditions: str|boolean column Matrix|None; Conditions of rows to apply changes to

        returnmat: bool; True to return self after evaluation, False to return None

        Examples:

            #Apply 'sum' function to 'Scores_list' column
                >>> Matrix.transform(function=sum,
                                     columns='Scores_list')

                Visually:

                  Rank  Scores_list            Rank  Scores_list
                 +------------------           +----------------
                0|   9       [3, 4]   --->   0|   9            7
                1|   3    [2, 4, 6]          1|   3           12


            #Apply a custom function called 'calculate' to 'Bonus' column where 'extra_time_spent' >= 3
                >>> Matrix.transform(function=calculate,
                                     columns="Bonus",
                                     conditions=Matrix.extra_time_spent >= 3)
        
        NOTE:
            Some tweaks to 'coldtypes' may be needed after transformations
            
        """
        from MatricesM.filter.apply import applyop
        if returnmat:
            return applyop(self,function,columns,conditions,self.features[:],False,Matrix)
        applyop(self,function,columns,conditions,self.features[:],False,Matrix)

    def combine(self,columns,function,feature,dtype,inplace=True):
        """
        Combine values in given columns with by passing them into the given function and use the output
        to create a single column matrix

        columns: tuple or list of strings; column names to use
        function: function; function to pass values in the desired columns
        feature: str; column's new name
        dtype: type; column's new dtype
        inplace: bool; True to swap the first column given with the column matrix, False to return the column matrix

        Example:
            #Use Year, Month and Day to create a new column named 'DATE' with dtype str, concatenate the result
                >>> Matrix.combine(columns=('Year','Month','Day'),
                                   function=lambda y,m,d:str(y)+"/"+str(m)+"/"+str(d),
                                   feature="DATE",
                                   dtype=str,
                                   inplace=True)
        
        NOTE:
            Values which returned an error when passed to the given function will be returned as a tuple
        """
        pass

    def replace(self,old:Any,
                new:Any,
                column:Union[str,List[Union[str,None]],Tuple[Union[str,None]],None]=None,
                condition:Optional[object]=None,
                returnmat:bool=False):
        """
        Replace single values,rows and/or columns

        old: all available types|boolean *column* matrix; value(s) to be replaced

        new:all available types; value(s) to replace old ones with

        column: str|tuple or list of strings|None;  which column(s) to apply replacements, None for all columns

        condition: boolean *column* matrix|None; row(s) to apply replacements, None for all rows
        
        returnmat: bool; True to return self after evaluation, False to return None
        
        Example:
                #Replace all 0's in all columns with 1's
                >>> data.replace(old=0,new=1)

                #Replace all "Pending" values to "Done" in "Order1" and "Order2" columns
                >>> data.replace(old="Pending",
                                 new="Done",
                                 column=("Order1","Order2"))

                #Replace all '' values in the column "Length" with the mean of the "Length" column
                >>> data.replace=(old='',
                                  new=data.mean("Length",get=0),
                                  column="Length")

                #Replace all "FF" values in "Grade" column with "AA" in the column "Grade" where "Year"<=2019
                >>> data.replace(old="FF",
                                 new="AA",
                                 column="Grade",
                                 condition=data["Year"]<=2019)

                #Replace all numbers below 0 in with 0's in column named "F5" where "Score1" is less than "Score2"
                >>> data.replace(old=data["F5"]<0,
                                 new=0,
                                 column="F5",
                                 condition=data["Score1"]<data["Score2"])

        """
        from MatricesM.filter.replace import _replace
        _replace(self,old,new,column,condition,Matrix)
        if returnmat:
            return self
        
    def sortBy(self,column:Union[str,int,None]=None,key=lambda a:a[1],reverse:bool=False,returnmat:bool=False,level:int=1):
        """
        Sort the rows by the desired column

        column:str|int|None; column name as string, column number, None to sort by label column level 1
        key:function; function to use while sorting
        reverse:bool; wheter or not to sort the matrix in reversed order
        returnmat:bool; wheter or not to return self
        level:int; level of labels to sort by if no column given
        """
        if column == None:

            if self._dfMat:
                label_mat = self.index.as_df
                temp_mat = self.copy
                real_names = temp_mat.features[:]

                label_mat.concat(temp_mat,returnmat=True). \
                          sortBy(column=label_mat.features[level-1],key=key,reverse=reverse)

                lbls = label_mat[:,:self.index.level]
                self.__index = Label([tuple(row) for row in lbls.matrix],lbls.features)
                self._matrix = label_mat[:,self.index.level:].matrix
                self.__features = real_names

            else:
                raise TypeError("Indexing by index column is not allowed on non-dataframe matrices")
        else:
            if isinstance(column,int):
                assert (column>0) and (column<=self.d1) , f"'column' can't be {column}"
    
            temp=sorted([(i,row) for i,row in enumerate(self.col(column,0))],key=key,reverse=reverse)
            if self._dfMat:
                inds = self.index.labels
                newinds = [r[0] for r in temp]
                self.__index = Label([inds[i] for i in newinds],self.index.names)

            mm = self.matrix
            self._matrix = [mm[r[0]] for r in temp]

        if returnmat:
            return self

    def shuffle(self,returnmat:bool=False):
        """
        Shuffle the rows of the matrix

        returnmat:bool; wheter or not to return self        
        """
        from random import shuffle

        inds = list(range(self.d0))
        unshuffled = inds[:]

        mm = self.matrix
        oldind = self.index.labels
        
        while inds == unshuffled:
            shuffle(inds)

        if self._dfMat:
            self.__index = Label([oldind[i] for i in inds],self.index.names)
        self._matrix = [mm[i][:] for i in inds]

        if returnmat:
            return self

    def sample(self,size:int=10,condition:str=None):
        """
        Get a sample of the matrix

        size:int. How many samples to take
        condition:str. Conditions to set as a base for sampling, uses 'where' method to filter 
        """
        from MatricesM.filter.sample import samples
        return samples(self,size,condition,Matrix)

    def match(self,expression:str,
              columns:Union[str,int,List[Union[str,None]],Tuple[Union[str,None]],None]=None,
              as_row:bool=True):
        """
        Return the values or rows that match the given expression

        expression: str; regular expression, uses re.findall
        columns: str|tuple or list of strings|int(starts from 1)|None; Column names/numbers
        as_row: bool; True to return rows with the matching values, False to return:
            1)A dictionary if 'columns' == None|tuple or list as {'column_name':[(row_index,matching_value), ...], ...}
            2)A list if 'columns' == str [(row_index,matching_values), ...]

        Example:
            #Return the rows of all email adresses using gmail.com domain in the column 'mail'
                >>> Matrix.match(expression=r"\w+@gmail.com",
                                columns="mail",
                                as_row=True)
        NOTE:
            #This method is CURRENTLY faster in most cases than using boolean matrices as indices:
                >>> Matrix[Matrix[column]==value] --> Using boolean matrices as indices
                >>> Matrix.match(value,column)    --> Corresponding method call for the same result as previous one

        """
        if not self._dfMat:
            raise MatrixError("'match' method only works with dataframes.")
        from MatricesM.filter.match import _match
        return _match(self,expression,columns,as_row,Matrix)

# =============================================================================
    """Statistical methods"""
# =============================================================================      
    
    def normalize(self,col:Union[int,str,None]=None,inplace:bool=True):
        """
        Normalizes the data to be valued between 0 and 1

        col:integer>=1 | column name as string | None
        inplace: bool ; True to apply changes to matrix, False to return a new matrix
        """
        from MatricesM.stats.normalize import normalize
        return normalize(self,col,inplace,self.PRECISION)

    def stdize(self,col:Union[int,str,None]=None,inplace:bool=True):
        """
        Standardization to get mean of 0 and standard deviation of 1

        col:integer>=1 | column name as string
        inplace: bool ; True to apply changes to matrix, False to return a new matrix
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
            #Returns a dictionary with iqr's as values
            >>> self.iqr()

            #Returns a dictionary where the values are quartile medians in lists
            >>> self.iqr(None,True)

            #Returns a list of quartile medians in lists
            >>> self.iqr(None,True,0)

            #Returns a matrix of iqr's
            >>> self.iqr(None,False,2)

        NOTE:
            Replace "None" with any column number to get a specific column's iqr
        """ 
        from MatricesM.stats.iqr import iqr
        return iqr(self,col,as_quartiles,get,Matrix,dataframe)   
     
    def freq(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Returns the frequency of every element on desired column(s)
        col:column index>=1 or column name
        get: 0|1|2 ; 0 to return a dictionary (uniques as keys, freq as values),
                     1 to return a dictionary (column names as keys, option 0 as values),
                     2 to return a list of Matrices for every column individually
        """
        from MatricesM.stats.freq import freq
        return freq(self,col,get,Matrix,dataframe)   

    def sum(self,col:Union[int,str,None]=None,get:[0,1,2]=1,inf_limit=2**512):
        """
        Return the sum of the desired column, give no arguments to get all columns'.

        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.prodsum import _prodsum
        return _prodsum(self,col,get,Matrix,dataframe,1,inf_limit)

    def prod(self,col:Union[int,str,None]=None,get:[0,1,2]=1,inf_limit=2**512):
        """
        Return the product of the desired column, give no arguments to get all columns'.

        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.prodsum import _prodsum
        return _prodsum(self,col,get,Matrix,dataframe,0,inf_limit)

    def count(self,col:Union[int,str,None]=None,get:[0,1,2]=1):
        """
        Return the count of the valid values in column(s), give no arguments to get all columns'.

        col: int|str|None ; Column index or name
        get: 0|1|2 ; 0 to return a list, 1 to return a dictionary, 2 to return a Matrix
        """
        from MatricesM.stats.freq import _count
        return _count(self,col,get,Matrix,dataframe)

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
        temp = Identity(self.d1,features=self.features[:],dtype=dataframe,coldtypes=[float for _ in range(self.d1)])
        return _corr(self,col1,col2,population,temp,method)
    
    @property   
    def describe(self):
        """
        Returns a matrix describing the matrix with features: Column, dtype, count,mean, sdev, min, 25%, 50%, 75%, max
        """
        from MatricesM.stats.describe import describe
        return describe(self,Matrix,dataframe,Label)

    @property
    def info(self):
        """
        Prints out column info
        """
        feats,cdtyps = self.features[:],self.coldtypes[:]
        counts = self.count(get=0) if self.d1>1 else [self.count(get=0)]
        uniques = self.freq(get=0) if self.d1>1 else [self.freq(get=0)]
        invalids = [self.d0-j for j in counts]
        return dataframe(dim=(self.d1,4),
                         data=[[cdtyps[i],counts[i],invalids[i],len(uniques[i].keys())] for i in range(self.d1)],
                         coldtypes=[type,int,int,int],
                         features=["dtype","Valid_data","Invalid_data","Unique_data"],
                         implicit=True,
                         index=feats,
                         NOTES=f"Size: {self.dim}")

    def uniques(self,column:Union[str,None]=None):
        """
        Return a list of unique values in a column

        column: str|None; column name, None to return a list of lists
        """
        if column == None:
            return [list(col.keys()) for col in self.freq(get=0)]
        return list(self.freq(column)[column].keys())

    def groupBy(self,column:Union[str,List[str],None]=None):
        """
        Group values in 'column' of a dataframe by row indices/labels

        column: str|list of strings|None; column name(s), None to use index column

        Returns a dataframe or a Group object

        NOTE:
            If there are list type indices passed to 'groups', method will try to find matching indices with the values INSIDE the list
            In such case, pass the argument in a list to use the list itself as a row index
        
        """
        from MatricesM.filter.grouping import grouping
        return grouping(self,column,dataframe)

    def oneHotEncode(self,column:str,level:int=1,concat:bool=True,removecol:bool=False,returnmat:bool=True):
        """
        One-hot encode a given column 

        column: str; column name to encode
        concat: bool; wheter or not to concatanate the encoded matrix
        removecol: bool; wheter or not to remove the used column after encoding, doesn't apply if 'concat' is False
        returnmat: bool; wheter or not to return self after encoding, doesn't apply if 'concat' is False
        """
        if not column in self.features.get_level(level):
            raise NameError(f"{column} is not a column name")

        uniq = self.uniques(column)
        temp = Matrix([self.d0,len(uniq)],fill=0,dtype=dataframe).matrix
        
        for i,value in enumerate(self.col(column,0)):
            temp[i][uniq.index(value)] = 1
        encoded_matrix = Matrix(data=temp,features=uniq,dtype=int)

        if concat:
            if removecol:
                del self[column]
            return self.concat(encoded_matrix,returnmat=returnmat)
        else:
            return encoded_matrix

# =============================================================================
    """Logical-bitwise magic methods """
# =============================================================================
    def __bool__(self):
        """
        Returns True if all the elements are equal to 1, otherwise returns False
        """
        m = self.matrix
        for i in range(self.d0):
            for j in range(self.d1):
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

        NOTE:
            -> Level 1 column names and row labels are used as default, use 'level' property for better indexing options
        """

        from MatricesM.matrixops.getsetdel import getitem
        return getitem(self,pos,Matrix,0)

    def __setitem__(self,pos:Union[object,int,str,slice,Tuple[Union[str,int,slice,Tuple[str]]]],item:Any):
        """
        Set new values to desired parts of the matrix.
        Uses same logic __getitem__ method uses.

        If a single value is given on the right-hand-side, value replaces all other values where left-hand-side represents
        Example:
            #Every row with even index numbers gets their 'Col 3' column changed to value 99
                >>> Matrix[::2,"col_3"] = 99                        
                
            #Rows where their 'Score1' is lower than 50 gets their 'Pass1' and 'Pass2' columns replaced with value 0   
                >>> Matrix[Matrix["Score1"]<50,('Pass1','Pass2')] = 0
            
                #Following method does the same changes, slightly faster on most cases
                >>> Matrix.replace(Matrix["Score1"]<50,0,('Pass1','Pass2'))
            
            Check README.md and exampleMatrices.py for more examples
        """
        from MatricesM.matrixops.getsetdel import setitem
        setitem(self,pos,item,Matrix,0)

    def __delitem__(self,val:object):
        """
        Works 'similar' to __getitem__ , but can only be used to delete entire columns and/or rows
        Example:
            >>> del Matrix['col_2']     #Delete 2nd column of the matrix
        """
        from MatricesM.matrixops.getsetdel import delitem
        delitem(self,val,Matrix,0)

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
            print("\nDimension: {0}x{1}".format(self.d0,self.d1))
        else:
            print("\nSquare matrix\nDimension: {0}x{0}".format(self.d0))
        return s+"\n\n" + notes 
    
    @property
    def kwargs(self):
        return {"dim":self.dim[:],
                "data":[a[:] for a in self._matrix],
                "fill":self.fill,
                "ranged":self.initRange,
                "seed":self.seed,
                "features":self.features[:],
                "decimal":self.decimal,
                "dtype":self.dtype,
                "coldtypes":self.coldtypes[:],
                "index":self.index,
                "implicit":True,
                "ROW_LIMIT":self.ROW_LIMIT,
                "PRECISION":self.PRECISION,
                "QR_ITERS":self.QR_ITERS,
                "EIGENVEC_ITERS":self.EIGENVEC_ITERS,
                "NOTES":self.NOTES,
                "DIRECTORY":self.DIRECTORY,
                "DEFAULT_NULL":self.DEFAULT_NULL,
                "DISPLAY_OPTIONS":self.DISPLAY_OPTIONS
               }

    @property
    def options(self):
        return {
                "ROW_LIMIT":self.ROW_LIMIT,
                "PRECISION":self.PRECISION,
                "QR_ITERS":self.QR_ITERS,
                "EIGENVEC_ITERS":self.EIGENVEC_ITERS,
                "NOTES":self.NOTES,
                "DIRECTORY":self.DIRECTORY,
                "DEFAULT_NULL":self.DEFAULT_NULL,
                "DISPLAY_OPTIONS":self.DISPLAY_OPTIONS
               }

    def __len__(self):
        return self.__dim[0]*self.__dim[1]

    def __call__(self,*args,**kwargs):
        r"""
        Use custom constructors.

        EXAMPLE USAGE:

        >>> from MatricesM import *

        >>> In[2]: df = dataframe(decimal=2,PRECISION=8)

        >>> In[3]: data = df([[0.525624, 0.902228, 0.655355, 0.852382],
                            [0.077884, 0.896945, 0.622809, 0.401988],
                            [0.175817, 0.051629, 0.742711, 0.492171],
                            [0.939892, 0.500976, 0.630512, 0.728549]])

        >>> In[4]: data
        >>> Out[4]:

              col_1  col_2  col_3  col_4
             +--------------------------
            0| 0.53   0.90   0.66   0.85
            1| 0.08   0.90   0.62   0.40
            2| 0.18   0.05   0.74   0.49
            3| 0.94   0.50   0.63   0.73
        

        >>> In[5]: mat = Matrix(decimal=5,PRECISION=9,
                         NOTES="9 decimal places are used in calculations\nDisplaying 5 decimals")

        >>> In[6]: matrix_1 = mat(6)

        >>> In[7]: matrix_1
        >>> Out[7]:
            
            0.29136 0.04569 0.62581 0.56670 0.56908 0.98096
            0.30619 0.69436 0.79888 0.09577 0.62117 0.55394
            0.45677 0.46080 0.36360 0.25382 0.25730 0.31367
            0.17618 0.29789 0.89245 0.46773 0.45167 0.51045
            0.38179 0.88610 0.73467 0.45546 0.94040 0.70342
            0.78188 0.88076 0.77035 0.47594 0.93677 0.21937

            9 decimal places are used in calculations
            Displaying 5 decimals

        NOTE:
            -> Positional arguments OVERWRITE keyword arguments. In the given example:
             -> mat(6,dim=100) will create a 6x6 matrix, because the first positional argument gets
                used as 'dim' instead.

            -> mat(6) is the same as mat(dim=6)    

        """
        kwargs = {**self.defaults, **kwargs} #Overwrite defaults with new values if any given
        keys = list(kwargs.keys())

        for i in range(len(args)): #Use positional arguments over keyword ones
            kwargs[keys[i]] = args[i]
                
        return Matrix(**kwargs)

    @property
    def __name__(self):
        return "Matrix"
        
# =============================================================================
    """Arithmetic methods"""        
# =============================================================================
    def __matmul__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.arithmetic import matmul
        return matmul(self,other,Matrix,self.matrix,dataframe)
    
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
    def __le__(self,other:Union[object,list,int,float]):
        from MatricesM.matrixops.comparison import le
        from_wheres = self.__use_value_based_comparison or False
        return le(self,other,Matrix,self.matrix,from_wheres)
        
    def __lt__(self,other:Union[object,list,int,float]):
        from MatricesM.matrixops.comparison import lt
        from_wheres = self.__use_value_based_comparison or False
        return lt(self,other,Matrix,self.matrix,from_wheres)
        
    def __eq__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import eq
        from_wheres = self.__use_value_based_comparison or False
        return eq(self,other,Matrix,self.matrix,from_wheres)
        
    def __ne__(self,other:Union[object,list,int,float,complex]):
        from MatricesM.matrixops.comparison import ne
        from_wheres = self.__use_value_based_comparison or False
        return ne(self,other,Matrix,self.matrix,from_wheres)
                
    def __ge__(self,other:Union[object,list,int,float]):
        from MatricesM.matrixops.comparison import ge
        from_wheres = self.__use_value_based_comparison or False
        return ge(self,other,Matrix,self.matrix,from_wheres)
        
    def __gt__(self,other:Union[object,list,int,float]):
        from MatricesM.matrixops.comparison import gt
        from_wheres = self.__use_value_based_comparison or False
        return gt(self,other,Matrix,self.matrix,from_wheres)
        
# =============================================================================
    """ Rounding etc. """                    
# =============================================================================   
    def __round__(self,n:int=-1,dec:Union[int,None]=None):
        from MatricesM.matrixops.rounding import rnd
        return rnd(self,n,dec,Matrix,self.matrix,dataframe)
    
    def __floor__(self):
        from MatricesM.matrixops.rounding import flr
        return flr(self,Matrix,self.matrix,dataframe)     
    
    def __ceil__(self):
        from MatricesM.matrixops.rounding import ceil
        return ceil(self,Matrix,self.matrix,dataframe)
    
    def __abs__(self):
        from MatricesM.matrixops.rounding import _abs
        return _abs(self,Matrix,self.matrix,dataframe)

###############################################################################

class dataframe(Matrix):
    def __init__(self,
                 data:Union[List[Any],List[List[Any]],Any]=[],
                 features:Union[Label,List[str]]=[],
                 coldtypes:List[type]=[],
                 **kwargs):
        
        kwargs = {**{"data":data,"dtype":dataframe,
                     "decimal":3,"features":features,
                     "coldtypes":coldtypes},
                  **kwargs}

        super().__init__(**kwargs)

    def __call__(self,*args,**kwargs):
        kwargs = {**self.defaults, **kwargs} #Overwrite defaults with new values if any given
        keys = list(kwargs.keys())

        for i in range(len(args)): #Use positional arguments over keyword ones
            kwargs[keys[i+1]] = args[i] # i+1 to skip first
        
        return dataframe(**kwargs)

###############################################################################

class Identity(Matrix):
    def __init__(self,dim,**kwargs):
        super().__init__(dim=dim,data=eye(dim),**kwargs)

###############################################################################

class Symmetrical(Matrix):
    def __init__(self,dim,**kwargs):
        super().__init__(dim=dim,data=sym(dim),**kwargs)

###############################################################################
