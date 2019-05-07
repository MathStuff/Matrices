# <a href="https://pypi.org/project/MatricesM/">MatricesM (Alpha)</a>
#### Python(>=3.5) library for creating matrices and doing matrix operations related to statistics and algebra mathematics
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

matrix_name = Matrix(dim=dimension,#Required(UNLESS 'listed' is given), int | list as [rows,cols]

                     listed=elements, #Optional, list of numbers | list of lists containing numbers | string. If no argument is passed matrix is filled depending on the 'fill' and 'ranged' 

                     directory=directory, #Optional, string. Path to the dataset. listed parameter shouldn't get any value if directory is given

                     fill=distribution | number, #Optional,  'uniform'|'triangular'|'gauss' or integer | float | complex or None; fills the matrix with chosen distribution or number, None will force 'uniform' distribution. Doesn't affect the matrix if "listed" or "directory" is given

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
                       
                     dtype=dataType #Optional, 'integer'|'float'|'complex' . Data type the matrix will hold, default is 'float'.
                     )

```         
   ##### -<a href=https://github.com/MathStuff/MatricesM/blob/master/MatricesM/matrix.py>matrix.py</a> contains the main Matrix class.
   
   ##### -<a href=https://github.com/MathStuff/MatricesM/blob/master/MatricesM/constructors/matrices.py>matrices.py</a> contains functions to create special matrices.
   
   ##### -<a href=https://github.com/MathStuff/MatricesM/blob/master/MatricesM/exampleMatrices.py>exampleMatrices.py</a> contains example matrices.
   
   ##### -Check the <a href="https://github.com/semihM/Matrices/projects">project tab</a> to see the progress
-------------- 
Some examples:
--------------
##### Create matrices filled with random numbers
```python 
#Creates a 4x4 matrix filled with random integers from the default range which is [0,1]
A = Matrix(4) 

#Creates a 3x5 matrix with elements uniformly distributed in the range from 10 to 25
B = Matrix([3,5],ranged=[10,25]) 

#Create a 6x6 square matrix filled with random float values in the default range
E = Matrix(6) 

#Create a 200x5 matrix using Gauss distribution with mean=50 and standard deviation=10
F = Matrix([200,5],fill='gauss',ranged=[50,10]) 

#Create a 10x10 matrix filled with 1's
G = Matrix(10,fill=1)

#Create a 200x4 matrix filled with integer numbers using triangular distribution where the range is [0,20] and mode is around if not 18
H = Matrix((200,4),fill='triangular',ranged=[0,20,18],dtype="integer") 

#Create a 9x9 matrix filled with complex numbers using gauss distribution for both real and imaginary parts with mean=5 and sdev=2
C1 = Matrix(9,fill="gauss",ranged=[5,2],dtype="complex")
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
filled_rows = [[1,2,3],[4,5,6],[7,8,9]]

#Creates a matrix with the given list of numbers
C = Matrix(listed=filled_rows) 

#Creates a 3x3 matrix from the given string
C1 = Matrix(3,"1 0 -1 4 5 5 1 2 2") 

#Creates a 2x4 matrix from the given string
C2 = Matrix([2,4],"5 -2 -3 2 1 0 0 4") 
``` 
----------------------------------------
##### Generate randomly filled matrices
```python
#Create a 10000x3 matrix using a triangular distribution that is symmetrical by the modes 50,25 and 20 for each column limited by [0,100], [-50,50] and [10,20] in order with the seed 32141. Column names are selected from ranged.keys()
randomData1 = Matrix((10000,3),
                     fill='triangular',
                     ranged={"Feature_1":(0,100,50),"Feature_2":(-50,50,25),"Feature_3":(10,20,20)},
                     seed=32141,
                     dtype="integer"
                    )

randomData2 = Matrix([10000,4],
                     ranged={"height":[10,100],"weight":[200,500],"cost":[200,1000],"quality":[0,10]},
                     seed=39598
                    )

randomData3 = Matrix([10000,4],
                     fill='gauss',
                     ranged={"feature1":[0,25],"feature2":[100,200],"feature3":[1000,10000],"feature4":[1,100]},
                     seed=4472142,
                    )

```
----------------------------------------
##### Give a string filled with data and use the numbers in it to create a matrix
```python 
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

#Create a matrix from the given string, dimension is *required* as [dataAmount,features]

D = Matrix(dim=[10,4],
           listed=data,
           features=["id","age","num1","num2"],
           dtype="integer"
          ) 

```
##### OR

##### Read data from files (Only tested on CSV and TXT files)
###### header: boolean value, **True** if data file has a header as the **first** row, default is **False**

###### If bool(header) is True, feature names automatically get picked up from the first row
```python 
data_directory = "Example\Directory\DATAFILE"

data_dim = [data_amount,feature_amount]

data_matrix = Matrix(dim=data_dim,directory=data_directory,header=1,dtype="float") #Create a float matrix from a table of data
```
----------------------------------------
##### Get specific parts of the matrix
```python
#All rows' second to forth columns as a matrix
C[:,1:4] == C.t[1:4,:].t

#Nineth column of every even numbered row as a matrix
C[::2,8] == C[::2,8:9] == C.col(9)[::2]

#Forth to seventh rows as a matrix
C[3:7] 

#Fifth row's eigth element (returns the value as it is, not a new matrix)
C[4,7] == C.matrix[4][7]

```
----------------------------------------
#### Use your matrix's methods and properties
##### Basics
```python 
C.grid #Prints the matrix's elements as a grid

C.p #Print the type, dimension, column names and the grid

C.decimal #Returns the chosen amount of decimals while printing. Can be used to set it's value

C.directory #Returns the directory of the matrix if there is any given

C.matrix #Returns the matrix's rows as lists in a list

C.dim #Returns the dimension of the matrix; can be used to change the dimensions, ex: [4,8] can be set to [1,32] where rows carry over as columns in order from left to right

C.string #Returns the string form of the matrix's elements

C.col(n,as_matrix) #Returns nth column of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

C.row(n,as_matrix) #Returns nth row of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

C.concat(matrix,concat_as) #Merges a matrix to itself. concat_as is set to "row" by default; if concatenation required is as columns, give "col" as the argument

C.copy #Returns a copy of the matrix

C.obj #Returns the string form of the object

C.seed #Returns the seed used to generate the random numbers in the matrix, returns None if matrix wasn't filled randomly. Seed can be changed to refill the matrix in-place

C.intForm #Returns integer form of the matrix

C.floatForm #Returns integer form of the matrix

C.ceilForm #Returns a matrix of all the elements' ceiling value

C.floorForm #Returns the same matrix as "intForm"

C.roundForm(n) #Returns a matrix of elements' rounded up to n decimal digits

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

C.minor(m,n) #Returns the mth row's nth element's minor matrix's determinant

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

C.find(element,indexStart) #Returns a list of the element's indeces as tuples. Returns None if element not in matrix

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

C.setFeatures() #Can be used to fix column naming issues, sets the column names to defaults

```

----------------------------------------

##### Add or remove rows/columns and operate on them
```python 
E.add(r=3,lis=[1.0 ,2.5 ,52,242 ,-9883,212, 0.000001, -555,554]) #Make the list given the 3rd row

A.remove(c=2) #Remove the second column 

F*=[2]+[1]*F.dim[1]-1 #Multiplies the first column with 2 and the rest with 1 

B @ B.t #Matrix multiplication example

```
----------------------------------------
##### Use bitwise operators 
```python
#Filter out and print the correlation matrix depending on the desired conditions
corrMat = (abs(data.corr())>0.5) & (data.corr()!=1)

#Get a matrix filled with the data matrix's first column, where elements' values are higher than 5000, put 0 otherwise (Will be updated soon)
limit = data.col(1) * (data.col(1)>5000)
```

##### All calculations below returns a matrix filled with 1's where the condition is True, otherwise 0
```python 
   A**2 == A*A
   
   A*2 == A+A
   
   A.t.t == A
   
   A.adj.matrix[2][0] == A.minor(1,3)
   
   #round call is currently required for the next examples due to <~%1e-5 error rate on some calculations
   
   round(A @ Matrix(listed=Identity(A.dim[0])),4) == round(A, 4) #A assumed to be a square matrix
   
   round(A.lowtri @ A.uptri, 4) == round(A, 4)
   
   round(A.inv.inv,4) == round(A, 4)
   
   round(A.Q @ A.R, 4) == round(A, 4)
   
   round(A @ A.inv)== Matrix(listed=Identity(A.dim[0]))
``` 
----------------------------------------

#### More examples can be found in <a href=https://github.com/MathStuff/MatricesM/blob/master/MatricesM/exampleMatrices.py>exampleMatrices.py</a>
