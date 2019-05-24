# <a href="https://pypi.org/project/MatricesM/">MatricesM (Alpha)</a>
#### Python(>=3.6) library for creating matrices and doing matrix operations related to statistics and algebra mathematics
#### [Join MathStuff's Slack](https://join.slack.com/t/mathstuffm/shared_invite/enQtNjE1NzE4NjM2ODM0LTk3ODEyNDVhY2Y5OGU1ZjZmZDc0YjQwMmE2YTJkZTczMGI1ODdmZGY2ZTQ2ZGRiMTM3MmQ0NjczODdmMzBiYjI) workspace for questions and discussions.
 
### Install using pip:
   
   <code>pip install MatricesM</code>
   
### Import by using:
   ```python 
   import MatricesM.matrix as mm #Use by calling : mm.Matrix(arguments)
   ```
   #### OR
   ```python 
   from MatricesM.matrix import Matrix #Use matrices directly : Matrix(arguments)
   ```
### Import and print example matrices:
   ```python 
   from MatricesM.exampleMatrices import *
   ```

### Basic syntax:
```python 

matrix_name = Matrix(dim=dimension,#Required(UNLESS 'listed' or 'directory' is given), int | list/tuple as [rows,cols]

                     listed=elements, #Optional, list of numbers | list of lists containing numbers | string. If no argument is passed matrix is filled depending on the 'fill' and 'ranged' 

                     directory=directory, #Optional, string. Path to the dataset. listed parameter shouldn't get any value if directory is given

                     fill=value, #Optional,Available distributions: 'uniform'|'triangular'|'gauss'; also accepts int|float|complex|str, fills the matrix with chosen distribution or number, None will force 'uniform' distribution. Doesn't affect the matrix if "listed" or "directory" is given

                     ranged=[*args] | dict;"""
                              ->To apply all the elements give a list | tuple
                              ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
                              ->Arguments should follow one of the following rules:
                                   1)If 'fill' is 'uniform', interval to pick numbers from as [minimum,maximum]; 
                                   2)If 'fill' is 'gauss', mean and standard deviation are picked from this attribute as [mean,standard_deviation];
                                   3)If 'fill' is 'triangular, range of the numbers and the mode as [minimum,maximum,mode]  """                     

                     header=hasHeader, #Optional, boolean. Default is 0. Wheter or not the dataset in the "directory" has a header row

                     features=columnNames #Optional, list of strings. If no argument given, columns get named "Col {}".format(colNumber) 
                     
                     seed=randomSeed #Optional, int. Seed to generate the random numbers from, doesn't affect anything if numbers are provided.
                       
                     dtype=dataType #Optional, 'integer'|'float'|'complex'|'dataframe' . Data type the matrix will hold, default is 'float'.
                     
                     coldtypes=listOfTypes #Requires dtype=="dataframe" to work. Contains the data types each column will hold. If nothing is passed, types get declared by the first row.
                     
                     implicit=False #Optional, boolean. If necessary parameters are given, this can be set to True to speed up the setup process. Don't change if you aren't sure what your matrix requires to work properly.
                     )

```         
   ##### -[matrix.py](https://github.com/MathStuff/MatricesM/blob/master/MatricesM/matrix.py) contains the main Matrix class.
   
   ##### -[matrices.py](https://github.com/MathStuff/MatricesM/blob/master/MatricesM/constructors/matrices.py) contains functions to create special matrices.
   
   ##### -[exampleMatrices.py](https://github.com/MathStuff/MatricesM/blob/master/MatricesM/exampleMatrices.py) contains example matrices.
   
   ##### -Check the [project tab](https://github.com/semihM/Matrices/projects) to see the progress
-------------- 
Some examples:
--------------
##### Create matrices filled with random numbers or given values
```python 
#Creates a 4x4 matrix filled with random float numbers
A = Matrix(4) 

#Creates a 3x5 matrix with elements uniformly distributed in the range from 10 to 25
B = Matrix([3,5],ranged=[10,25]) 

#Create a 6x6 square matrix filled with random integer numbers in the default range: [0,1]
E = Matrix(6,dtype="integer") 

#Create a 200x5 matrix using Gauss distribution with mean=50 and standard deviation=10
F = Matrix([200,5],fill='gauss',ranged=[50,10]) 

#Create a 10x10 matrix filled with 1's
G = Matrix(10,fill=1)

#Create a 200x4 matrix filled with integer numbers using triangular distribution where the range is [0,20] and mode is around if not 18
H = Matrix((200,4),fill='triangular',ranged=[0,20,18],dtype="integer") 

#Create a 9x9 matrix filled with complex numbers using gauss distribution for both real and imaginary parts with mean=5 and sdev=2
C1 = Matrix(9,fill="gauss",ranged=[5,2],dtype="complex")

#Create a 10x1 matrix filled with the given string
S = Matrix((10,1),fill="hello",dtype="dataframe")
```
----------------------------------------
##### Generate randomly filled matrices using special distributions
```python
#Create a 10000x3 integer numbers matrix using a triangular distribution that is symmetrical by the modes 50,25 and 20 for each column limited by [0,100], [-50,50] and [10,20] in order with the seed 32141. Column names are selected from ranged.keys()
randomData1 = Matrix((10000,3),
                     fill='triangular',
                     ranged={"Feature_1":(0,100,50),"Feature_2":(-50,50,25),"Feature_3":(10,20,20)},
                     seed=32141,
                     dtype="integer")

#Create a 10000x4 float numbers matrix using uniform distribution where columns' ranges are in order [10,100], [200,500], [200,1000] and [0,10] with the seed 39598 for each column. Column names are selected from ranged.keys()
randomData2 = Matrix([10000,4],
                     ranged={"height":[10,100],"weight":[200,500],"cost":[200,1000],"quality":[0,10]},
                     seed=39598)

#Create a 10000x4 matrix float numbers using normal(gauss) distribution where [0,25], [100,200], [1000,10000] and [1,100] are columns' means and standard deviations and the seed is 4472142 for each column. Column names are selected from ranged.keys()
randomData3 = Matrix([10000,4],
                     fill='gauss',
                     ranged={"feature1":[0,25],"feature2":[100,200],"feature3":[1000,10000],"feature4":[1,100]},
                     seed=4472142)

```
----------------------------------------
##### Create special matrices
```python 
from MatricesM.constructors.matrices import Identity

#3x3 identity matrix
id3 = Matrix(listed=Identity(3))

from MatricesM.constructors.matrices import Symmetrical

#A 8x8 symmetrical matrix filled with numbers in range from 0 to 1 with uniform distribution 
sym1 = Matrix(listed=Symmetrical(8))

``` 
----------------------------------------
##### Give list of numbers to create matrices
```python 
#Creates a matrix with the given list of numbers
filled_rows = [[1,2,3],[4,5,6],[7,8,9]]

C = Matrix(listed=filled_rows) 

#Create a dataframe from a list
data = [["James",180.4,85],
        ["Tom",172,73],
        ["Sophia",168.25,65]]
        
df = Matrix(listed=data,
            dtype="dataframe",
            features=["Name","Height","Weight"],
            decimal=1)

#coldtypes parameter may be required in cases where the data given doesn't represent the desired data types
``` 
----------------------------------------
##### Give a string filled with data and use the numbers in it to create a matrix
```python 
#Creates a 3x3 matrix from the given string
C1 = Matrix(3,"1 0 -1 4 5 5 1 2 2") 

#Creates a 2x4 matrix from the given string
C2 = Matrix([2,4],"5 -2 -3 2 1 0 0 4")

#Create a matrix from the given string, dimension is *required* as [dataAmount,features]. Only numbers are picked up
data="""1,K,60,69900,6325
2,K,30,79000,5200
3,E,52,85500,7825
4,E,57,17100,8375
5,E,55,5500,5450
6,E,68,27200,8550
7,E,41,20500,4500
8,E,20,69000,5050
9,K,33,13200,8325
10,E,37,31800,5975"""

#As an integer matrix
intMat = Matrix(dim=[10,4],
                listed=data,
                features=["id","age","num1","num2"],
                dtype="integer") 

#Or as a dataframe
df = Matrix(dim=[10,4],
            listed=data,
            features=["id","age","num1","num2"],
            dtype="dataframe",
            coldtypes=[int]*4)

```
----------------------------------------

##### Read data from files (Only tested on CSV and TXT files)
###### If there is a header, set header to any boolean value == True . Float numbers considered to be using dot(.) to separate decimal places and cammas(,) are used to separate columns. Will be updated in the future for more options
```python 
data_directory = r"Example\Directory\DATAFILE"

data_matrix = Matrix(directory=data_directory,header=1,dtype="dataframe",coldtypes=[str,float,...]) #Create a dataframe matrix from a csv file

#If you're having issues with setting the dimension, try explicitly providing it as dim=[data_amount,feature_amount]
#More options for reading the file will be added in the future

#Example dataset: https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
winedata = Matrix(directory="...\Data\winequality-red.csv",header=1,dtype="dataframe",coldtypes=[float]*12)
```
----------------------------------------
##### Get specific parts of the matrix
```python
#All rows' second to forth columns as a matrix
C[:,1:4] == C.t[1:4,:].t

#Nineth column of every even numbered row as a matrix
C[::2,8] == C[::2,8:9] == C.col(9)[::2] == C["Col 9"][::2] == C.select(("Col 9"))[::2]

#Forth to seventh rows as a matrix
C[3:7] 

#Fifth row's eighth element (returns the value as it is, not a new matrix)
C[4,7] == C.matrix[4][7]

#Use column names
C["Col 3","Col 1","Col 2"] == C.select(("Col 3","Col 1","Col 2"))
```
----------------------------------------
##### Filter out depending on what you need
```python 
#Using example dataset, get the rows where the "quality" feature is higher or equal to 6 and pH in range (3,3.3)
#All statements should be properly closed with parentheses
wineOverSix = winedata.where("(quality>6) and ((pH<3.3) and (pH>3))")

#Select the columns of pH and quality and assign them to another matrix
filtered = winedata.select(("pH","quality"))

#Sort by given column and shuffle the data 
winedata.indexSet() #Set index column to reverse further actions
winedata.sortBy("quality") #Data is sorted in increasing order, use reverse=True for decreasing order
winedata.shuffle() #Shuffle the rows

#Get 20 samples from the data under desired conditions
winedata.sample(20,"(quality>5) and ((alcohol<11) or (density>0.95))")

#More examples using different datasets will be added soon.
```
----------------------------------------
##### Apply arithmetic operations to individual rows and columns.
```python
#Multiply Prices with 0.9 and subtract 5 also add 10 to Discounts under the conditions: Price>100 and Discount<5
marketData.apply( ("*0.9 -5","+10"), ("Price","Discount"), "(Price>100) and (Discount<5)" )

```
----------------------------------------
#### Use your matrix's methods and properties
##### Basics
```python 
C.grid #Prints the matrix's elements as a grid, if dtype is 'dataframe', column names also get printed

C.p #Print the dimensions, wheter or not the matrix is square and the grid. If dtype is 'dataframe', column names are also printed

C.decimal #Returns the chosen amount of decimal digits to round while printing. Can be used to set it's value

C.directory #Returns the directory of the matrix if there is any given

C.matrix #Returns the matrix's rows as lists in a list

C.dim #Returns the dimension of the matrix; can be used to change the dimensions, ex: [4,8] can be set to [1,32] where rows carry over as columns in order from left to right

C.string #Returns the string form of the matrix's elements, this is the string the 'grid' property prints

C.col(n,as_matrix) #Returns nth column of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

C.row(n,as_matrix) #Returns nth row of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

C.concat(matrix,concat_as) #Merges a matrix to itself. concat_as is set to "row" by default; if concatenation required is as columns, give "col" as the argument

C.add(values,row,col,feature,dtype) #Adds list to given index in row or col, indeces start from 1. If a column is added, dtype and feature are used determine type and name.

C.remove(row,col) #Removes the desired row and/or column

C.copy #Returns a copy of the matrix

C.obj #Returns the string form of the Matrix object which can be evaluated to create the same matrix

C.seed #Returns the seed used to generate the random numbers in the matrix, returns None if matrix wasn't filled randomly. Seed can be changed to refill the matrix in-place

C.intForm #Returns integer form of the matrix

C.floatForm #Returns integer form of the matrix

C.ceilForm #Returns a matrix of all the elements' ceiling value

C.floorForm #Returns the same matrix as "intForm"

C.roundForm(n) #Returns a matrix of elements' rounded up to n decimal digits. Same as round(C,n)

#Available arithmetic operators : "@", "+", "-", "*", "/", "//", "**", "%"

#Available comparison operators : "<" ,"<=", ">", ">=", "==", "!=", "&", "|", "~"

```
##### Algebric properties
```python 
C.uptri #Returns the upper triangular form of the matrix

C.lowtri #Returns the lower triangular form of the matrix

C.sym #Returns the symmetric part of the matrix 

C.anti #Returns the antisymmetric part of the matrix

C.det #Returns the determinant of the matrix

C.perma #Returns the permanent of the matrix

C.t #Returns the transposed matrix

C.ht #Returns the hermitian-transpose of the matrix

C.conj #Returns the conjugated forms of the elements in a matrix

C.minor(m,n,returndet) #Returns the mth row's nth element's minor matrix's determinant, set returndet to False to get the matrix of which the determinant was calculated

C.adj #Returns the adjoint matrix

C.inv #Returns the inversed matrix

C.pseudoinv #Returns the pseudo inverse of the matrix

C.Q #Returns the orthonormal matrix from the QR decomposition

C.R #Returns the upper-triangular matrix from the QR decomposition

C.trace #Returns the trace of the matrix

C.nilpotency(limit) #Returns the nilpotency degree of the matrix, returns None if some elements diverge. Limit parameter is for iteration amount

C.rank #Returns the rank of the matrix

C.rrechelon #Returns the reduced row echelon form of the matrix

C.eigenvalues #Returns the eigenvalues (CAN'T FIND COMPLEX EIGENS,CHECK ISSUE#32 : https://github.com/MathStuff/MatricesM/issues/32)

C.isSquare #Returns True if the matrix is a square matrix

C.isSymmetric #Returns True if the matrix is a symmetric matrix

C.isAntiSymmetric #Returns True if the matrix is an antisymmetric matrix

C.isPerSymmetric #Returns True if the matrix is a persymmetric matrix

C.isHermitian #Returns True if the matrix is a hermitian matrix

C.isTriangular #Returns True if the matrix is a triangular matrix

C.isUpperTri #Returns True if the matrix is a upper-trianguar matrix

C.isLowerTri #Returns True if the matrix is a lower-triangular matrix

C.isDiagonal #Returns True if the matrix is a diagonal matrix

C.isUpperBidiagonal #Returns True if the matrix is an upper-bidiagonal matrix

C.isLowerBidiagonal #Returns True if the matrix is a lower-bidiagonal matrix

C.isBidiagonal #Returns True if the matrix is an upper-bidiagonal or a lower-bidiagonal matrix

C.isTridiagonal #Returns True if the matrix is a tridiagonal matrix

C.isUpperHessenberg #Returns True if the matrix is an upper-Hessenberg matrix

C.isLowerHessenberg #Returns True if the matrix is a lower-Hessenberg matrix

C.isHessenberg #Returns True if the matrix is an upper-Hessenberg or a lower-Hessenberg matrix

C.isToeplitz #Returns True if the matrix is a Toeplitz matrix

C.isUnitary #Returns True if the matrix is a unitary matrix

C.isIdempotent #Returns True if the matrix is an idempotent matrix

C.isOrthogonal #Returns True if the matrix is an orthogonal matrix

C.isCircular #Returns True if the matrix is a circular matrix

C.isPositive #Returns True if the matrix is a positive valued matrix

C.isNonNegative #Returns True if the matrix is a non-negative matrix

C.isProjection #Returns True if the matrix is a projection matrix
```
##### Statistical properties 
```python 

C.head(n) #Returns the first n rows (if there are less than n rows it returns all the rows)

C.tail(n) #Returns the last n rows (if there are less than n rows it returns all the rows)

C.describe #Returns a description matrix with columns describing the matrix holding column_name, dtype, mean, sdev, min, max, %25, %50, %75.

C.find(element,indexStart) #Returns a list of the element's indeces as tuples. Returns None if element not in matrix

C.select(columns) #Returns a matrix where the desired columns are concatenated in order. Only works if 'columns' is a tuple or a list

C.where(condition) #Returns a matrix where the given condition(s) are True. Example: C.where("(Col 1>=0.5) and (Col 2!=0)") 

C.apply(expressions,columns,conditions,returnmat) #Apply given 'expression' to given 'columns' where the 'conditions' are True, set returnmat wheter or not to return self. If 'columns' is None, 'expressions' is applied to all columns. 

C.indexSet(name,start,returnmat) #Set an indexing column named 'name', starting from 'start' and return self if 'returnmat' is True

C.sortBy(column,reverse,returnmat) #Sort the matrix by the desired 'column', do it in decreasing order if 'reverse'==True, and return self if 'returnmat'==True

C.shuffle(iterations,returnmat) #Shuffle the rows 'iterations' times and return self if 'returnmat'==True

C.sample(size,condition) #Get a sample sized 'size' where the 'condition' is True

C.joint(matrix) #Returns a matrix of shared rows with given 'matrix'

C.mean(n,asDict) #Returns the nth column's average, give None as argument to get the all columns' averages; asDict: True to get return a dictionary of features as keys and means as values, False to get means in a list. If n is given and asDict is False, returns a number.

C.ranged(n,asDict) #Returns the nth column's range, give None as argument to get the all columns' ranges; asDict: True to get return a dictionary of features as keys and ranges as values, False to get ranges in a list. If n is given and asDict is False, returns a number.

C.median(n) #Returns the nth column's median, give None to get all columns' medians

C.freq(n) #Returns the nth column's elements frequency as a dictionary where elements are keys and how often they repeat as values. If called without arguments, returns every column"s frequencies 

C.mode(n) #Returns the nth column's mode, give None to get all columns' modes

C.iqr(n,as_quartiles,asDict) #Returns the nth column's iqr, give None to get all columns' iqr values. If first,second and third quartiles is desired, give as_quartiles parameter bool(True); asDict: True to get return a dictionary of features as keys and iqr's as values, False to get iqr's in a list. If n is given and asDict is False, returns a number(or a list dependent on as_quartiles).

C.sdev(n,population,asDict) #Returns the nth column's standard deviation, if None is given as an argument returns all columns' standard deviations. Give population parameter 1 if calculation is not for samples, 0 otherwise; asDict: True to get return a dictionary of features as keys and standard deviations as values, False to get standard deviations in a list. If n is given and asDict is False, returns a number.

C.var(n,population,asDict) #Returns the nth column's variance, if None is given as an argument returns all columns' variance. Give population parameter 1 if calculation is not for samples, 0 otherwise; asDict: True to get return a dictionary of features as keys and variances as values, False to get variances in a list. If n is given and asDict is False, returns a number.

C.cov(col1,col2,population) #Returns the col1 and col2's covariance. Give population parameter True if calculation is not for samples

C.z(row,col,population) #Returns the z-scores of the desired row and/or column, call without arguments to get the all z-scores as a matrix. If both row and column given, returns a number. Give population parameter 1 if calculation is not for samples, 0 otherwise.

C.corr(column_1,column_2,population) #Returns linear correlation of 2 columns chosen from the matrix. If no argument given, returns the correlation matrix. Give population parameter 1 if calculation is not for samples, 0 otherwise

C.normalize(column,inplace) #Normalize the data in the desired column, None to normalize all columns. Give inplace parameter "True" boolean value to make normalization in-place, "False" to return a new matrix with normalized data

C.stdize(column,inplace) #Standardize the data in the desired column, None to standardize all columns. Give inplace parameter "True" boolean value to make standardization in-place, "False" to return a new matrix with standardized data

C.features #Returns the column names if given, can also be used to set column names

C.coldtypes #Returns what type of data each column carries, can be used to set the values.

C.setFeatures() #Can be used to fix column naming issues, sets the column names to defaults

C.setcoldtypes(declare) #Can be used to fix column type related issues, sets the column types to what first row carries. If declare is True, individual dtypes are applied to every element in the matrix

```

----------------------------------------

##### All calculations below returns a matrix filled with 1's where the condition is True, otherwise 0
```python 
   A**2 == A*A
   
   A*2 == A+A
   
   A.t.t == A
   
   A.adj.matrix[2][0] == A.minor(1,3)
   
   #bool object can be called to get a boolean value of the matrix, if all elements are 1's then it will return True and False in any other case.
   bool(Matrix(10,fill=1)) == True

   #round call is currently required for the next examples due to <~%1e-5 error rate on some calculations
   round(A @ Matrix(listed=Identity(A.dim[0])),4) == round(A, 4) #A assumed to be a square matrix
   
   round(A.lowtri @ A.uptri, 4) == round(A, 4)
   
   round(A.inv.inv,4) == round(A, 4)
   
   round(A.Q @ A.R, 4) == round(A, 4)
   
   round(A @ A.inv)== Matrix(listed=Identity(A.dim[0]))
``` 
----------------------------------------

#### More examples can be found in [exampleMatrices.py](https://github.com/MathStuff/MatricesM/blob/master/MatricesM/exampleMatrices.py)
