# <a href="https://pypi.org/project/MatricesM/">MatricesM</a>
#### Python(>=3.6) library for creating matrices and doing matrix operations related to statistics and algebra mathematics
#### [Join MathStuff's Slack workspace](https://join.slack.com/t/mathstuffm/shared_invite/enQtNjE1NzE4NjM2ODM0LTk3ODEyNDVhY2Y5OGU1ZjZmZDc0YjQwMmE2YTJkZTczMGI1ODdmZGY2ZTQ2ZGRiMTM3MmQ0NjczODdmMzBiYjI) for questions and discussions.
 
### Install using pip:
   
   <code>pip install MatricesM</code>
   
### Import by using:
   ```python 
   import MatricesM as mm #Use by calling : mm.Matrix(arguments)
   ```
   #### OR
   ```python 
   from MatricesM import * #Use matrices directly : Matrix(arguments)
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

                     fill=value, #Optional,Available distributions: uniform|triangular|gauss|gammavariate|betavariate|expovariate|lognormvariate; also accepts int|float|complex|str|list|range, fills the matrix with chosen distribution or number, None will force uniform distribution. Doesn't affect the matrix if "listed" or "directory" is given

                     ranged=[*args] | dict;"""
                              ->To apply all the elements give a list | tuple
                              ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
                              ->Arguments should follow one of the following rules:
                                   1)If 'fill' is uniform, interval to pick numbers from as [minimum,maximum]; 
                                   2)If 'fill' is gauss or lognormvariate mean and standard deviation are picked from this attribute as [mean,standard_deviation];
                                   3)If 'fill' is triangular, range of the numbers and the mode as [minimum,maximum,mode];
                                   4)If 'fill' is gammavariate or betavariate, alpha and beta values are picked as [alpha,beta]
                                   5)If 'fill' is expovariate, lambda value have to be given in a list as [lambda]"""                   

                     header=hasHeader, #Optional, boolean. Default is 0. Wheter or not the dataset in the "directory" has a header row

                     features=columnNames #Optional, list of strings. If no argument given, columns get named "Col {}".format(colNumber) 
                     
                     seed=randomSeed #Optional, int. Seed to generate the random numbers from, doesn't affect anything if numbers are provided.
                       
                     dtype=dataType #Optional, int|float|complex|dataframe. Data type the matrix will hold, default is float.
                     
                     coldtypes=listOfTypes #Requires dtype==dataframe to work. Contains the data types each column will hold. If nothing is passed, types get declared by the first row.
                     
                     implicit=False #Optional, boolean. If necessary parameters are given, this can be set to True to speed up the setup process. Don't change if you aren't sure what your matrix requires to work properly.
                     )
"""
Using *args = Pass arguments matching with the parameters in order : dim, listed, directory, fill, ranged, seed, header, features, decimal, dtype, coldtypes, implicit
Using **kwargs = Make sure to use given parameter names OR give a dictionary with keys being parameter names as strings, values being their values

 Example:
         Matrix(3,"1 3 5 2 4 6 3 5 7",dtype=int)                             --> Use both *args and **kwargs
         Matrix(directory='.../directory/file.csv',header=1,dtype=dataframe) --> Use **kwargs
         Matrix(kwargs={'dim':4,'fill':triangular,'ranged'=(0,10,6)})        --> Use **kwargs with a dictionary
         Matrix(kwargs=anotherMatrix.kwargs)                                 --> Same as anotherMatrix.copy OR eval(anotherMatrix.obj)
"""
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
E = Matrix(6,dtype=int) 

#Create a 200x5 matrix using Gauss distribution with mean=50 and standard deviation=10
F = Matrix([200,5],fill=gauss,ranged=[50,10]) 

#Create a 10x10 matrix filled with 1's
G = Matrix(10,fill=1)

#Create a 200x4 matrix filled with integer numbers using triangular distribution where the range is [0,20] and mode is around if not 18
H = Matrix((200,4),fill=triangular,ranged=[0,20,18],dtype=int) 

#Create a 50x50 matrix filled with complex numbers using beta distribution for both real and imaginary parts with alpha=2 and beta=5
C1 = Matrix(50,fill=betavariate,ranged=[2,5],dtype=complex)

#Create a 10x1 matrix filled with the given string
S = Matrix((10,1),fill="hello",dtype=dataframe)
```
----------------------------------------
##### Generate randomly filled matrices using special distributions
```python
#Create a 10000x3 matrix using a triangular distribution with integer values.
randomData1 = Matrix((10000,3),
                     fill=triangular,
                     ranged={"feature1":(0,100,50),"feature2":(-50,50,25),"feature3":(10,20,20)},
                     seed=32141,
                     dtype=int)

#Create a 10000x4 matrix using gamma distribution with float numbers.
randomData2 = Matrix([10000,4],
                     fill=gammavariate,
                     ranged={"feature1":[1,1.2],"feature2":[12,24],"feature3":[15,100],"feature4":[1.5,3]},
                     seed=39598)

#Create a 10000x4 matrix using normal(gauss) distribution with integer numbers.
randomData3 = Matrix([10000,4],
                     fill=gauss,
                     ranged={"feature1":[0,25],"feature2":[100,200],"feature3":[1000,10000],"feature4":[1,100]},
                     seed=4472142,
                     dtype=int)

#Create a 20000x4 matrix using exponential distribution with float numbers.
randomData4 = Matrix([20000,4],
                     fill=expovariate,
                     ranged={"feature1":[0.1],"feature2":[0.95],"feature3":[0.5],"feature4":[0.00025]},
                     seed=21751923)
```
----------------------------------------
##### Create special matrices
```python 
#3x3 identity matrix
id3 = Matrix(listed=Identity(3))

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
            dtype=dataframe,
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
                dtype=int) 

#Or as a dataframe
df = Matrix(dim=[10,4],
            listed=data,
            features=["id","age","num1","num2"],
            dtype=dataframe,
            coldtypes=[int]*4)

```
----------------------------------------
##### Read data from csv files 
###### If there is a header, set header to any boolean value == True . Float numbers considered to be using dot(.) to separate decimal places and cammas(,) are used to separate columns. Will be updated in the future for more options
```python 
data_directory = r"Example\Directory\DATAFILE"

data_matrix = Matrix(directory=data_directory,header=1,dtype=dataframe,coldtypes=[str,float,...]) #Create a dataframe matrix from a csv file

#If you're having issues with setting the dimension, try explicitly providing it as dim=[data_amount,feature_amount]
#More options for reading the file will be added in the future

#Example dataset: https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
winedata = Matrix(directory="...\Data\winequality-red.csv",header=1,dtype=dataframe,coldtypes=[float]*12)
```
----------------------------------------
##### Get specific parts of the matrix
```python
#All rows' second to forth columns as a matrix
Matrix[:,1:4] == Matrix.t[1:4,:].t

#Nineth column of every even numbered row as a matrix
Matrix[::2,8] == Matrix[::2,8:9] == Matrix.col(9)[::2] == Matrix["Col 9"][::2] == Matrix.select(("Col 9"))[::2]

#Forth to seventh rows as a matrix
Matrix[3:7] 

#Fifth row's eighth element (returns the value as it is, not a new matrix)
Matrix[4,7] == Matrix.matrix[4][7]

#Use column names
Matrix["Col 3","Col 1","Col 2"] == Matrix.select(("Col 3","Col 1","Col 2"))
```
----------------------------------------
##### Filter out depending on what you need
```python 
#Using example dataset, get the rows where the "quality" feature is higher or equal to 6 and pH in range (3,3.3)
#All statements should be properly closed with parentheses
wineOverSix = winedata.where("(quality>6) and ((pH<3.3) and (pH>3))")
#Alternative way (2x faster)
wineOverSix = winedata[(winedata["quality"]>6) & ((winedata["pH"]<3.3) & (winedata["pH"]>3))]

#Select the columns of pH and quality and assign them to another matrix
filtered = winedata.select(("pH","quality"))
#Alternative way (2x faster)
filtered = winedata["pH","quality"] 


#Set index column to reverse further actions
winedata.indexSet()

#Sort by given column and shuffle the data
winedata.sortBy("quality") #Data is sorted in increasing order, use reverse=True for decreasing order

#Shuffle the rows
winedata.shuffle()

#Get 20 samples from the data under desired conditions
winedata.sample(20,"(quality>5) and ((alcohol<11) or (density>0.95))")
#Alternative way (1.5x faster)
winedata[(winedata["quality"]>5) & ((winedata["alcohol"]<11) | (winedata["density"]>0.95))].sample(20)

#Return all the rows and select 'alcohol' and 'quality' columns where quality is higher than 6
winedata[winedata["quality"]>6,("alcohol", "quality")]

```
----------------------------------------
##### Apply arithmetic operations to individual rows and columns.
```python
#Create a 1000x2 dataframe filled using normal distribution with given arguments
marketData = Matrix((1000,2),fill=gauss,ranged={"Price":(250,60),"Discount":(8,2)},dtype=dataframe)

#Change invalid values in "Discount" column where it's less than 0 to 0
marketData[marketData["Discount"]<0,"Discount"] = 0

#Explore the data
marketData.describe

#Multiply 'Price' with 0.9 and subtract 5 also add 10 to 'Discount' under the conditions: Price>100 and Discount<5
marketData.apply( ("*0.9 -5","+10"), ("Price","Discount"), "(Price>100) and (Discount<5)" )
```
----------------------------------------
##### Replace values in the matrix
```python
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
             
#Change value of 'Feature5' to 0 in the rows where the 'Feature1' is lower than 0
data[data["Feature1"]<0,"Feature5"] = 0

#Create a matrix with a square filled with 0's in the middle, 5's outside
s = Matrix(10,fill=5,dtype=int)
s[3:7,3:7] = 0
#Matrices can also be used to do the same
s[3:7,3:7] = Matrix(4,fill=0)
```
----------------------------------------
##### Concatenate a matrix to your matrix.
```python
#Concatenate a new column named 'Discounted_Price' containing the product of the 'Price' and 'Discount' columns
marketData["Discounted_Price"] = marketData["Price"] - marketData["Price"]*(marketData["Discount"]/100)
```
----------------------------------------
#### Use your matrix's methods and properties
##### Basics
```python 
Matrix.grid #Prints ALL of the matrix's elements as a grid, if dtype is dataframe, column names also get printed

Matrix.p #Prints the dimensions, wheter or not the matrix is square and the grid. If dtype is dataframe, column names are also printed

Matrix.decimal #Returns the chosen amount of decimal digits to round while printing. Can be used to set it's value

Matrix.directory #Returns the directory of the matrix if there is any given

Matrix.matrix #Returns the matrix's rows as lists in a list

Matrix.dim #Returns the dimension of the matrix; can be used to change the dimensions, ex: [4,8] can be set to [1,32] where rows carry over as columns in order from left to right

Matrix.col(n,as_matrix) #Returns the nth column if n is an integer or returns the column named n, as a list or matrix, set as_matrix to True to get the list as a matrix

Matrix.row(n,as_matrix) #Returns nth row of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

Matrix.concat(matrix,concat_as) #Merges a matrix to itself. concat_as is set to "row" by default; if concatenation required is as columns, give "col" as the argument

Matrix.add(values,row,col,feature,dtype) #Adds list to given index in row or col, indeces start from 1. If a column is added, dtype and feature are used determine type and name.

Matrix.remove(row,col) #Removes the desired row and/or column

Matrix.copy #Returns a copy of the matrix

Matrix.obj #Returns the string form of the Matrix object which can be evaluated to create the same matrix

Matrix.seed #Returns the seed used to generate the random numbers in the matrix, returns None if matrix wasn't filled randomly. Can be used to refill the matrix inplace if set to a new value

Matrix.fill #Returns the value or distribution of which the matrix was filled with. Can be used to refill the matrix inplace if set to a new value

Matrix.initRange #Returns the value of 'ranged' used while creating the matrix. Can be used to refill the matrix inplace if set to a new value

Matrix.intForm #Returns integer form of the matrix

Matrix.floatForm #Returns float form of the matrix

Matrix.ceilForm #Returns a matrix of all the elements' ceiling values

Matrix.floorForm #Returns the same matrix as "intForm"

Matrix.roundForm(n) #Returns a matrix of elements' rounded up to n decimal digits. Same as round(Matrix,n)

Matrix.kwargs #Returns a dictionary of the matrix's basic attributes

Matrix.ROW_LIMIT #Attribute to determine the amount of rows to print while representing the matrix, default is 30.

Matrix.COL_LIMIT #Attribute to determine the amount of columns to print while representing the matrix, default is 12.

Matrix.EIGEN_ITERS #Attribute to determine how many iterations will be done in eigenvalue calculation with QR algorithm, default is 100 for even numbered dimensions, 500 for odd ones. Play around with this value if the values you get don't seem right.

#Available arithmetic operators : "@", "+", "-", "*", "/", "//", "**", "%"

#Available comparison operators : "<" ,"<=", ">", ">=", "==", "!=", "&", "|", "~"

```
##### Algebric properties
```python
Matrix.det #Returns the determinant of the matrix

Matrix.t #Returns the transposed matrix

Matrix.ht #Returns the hermitian-transpose of the matrix

Matrix.adj #Returns the adjoint matrix

Matrix.inv #Returns the inversed matrix

Matrix.pseudoinv #Returns the pseudo inverse of the matrix

Matrix.minor(m,n,returndet) #Returns the mth row's nth element's minor matrix's determinant, set returndet to False to get the matrix of which the determinant was calculated

Matrix.rank #Returns the rank of the matrix

Matrix.echelon #Returns the echelon form of the matrix

Matrix.rrechelon #Returns the reduced row echelon form of the matrix

Matrix.LU #Returns both L and U matrices from LU decomposition in a tuple

Matrix.lowtri #Returns the lower triangular form (L matrix from LU decomposition) of the matrix

Matrix.uptri #Returns the upper triangular form (U matrix from LU decomposition) of the matrix

Matrix.symdec #Returns both symmetrical and anti-symmetrical parts of the matrix

Matrix.sym #Returns the symmetric part of the matrix 

Matrix.anti #Returns the antisymmetric part of the matrix

Matrix.perma #Returns the permanent of the matrix

Matrix.conj #Returns the conjugated forms of the elements in a matrix

Matrix.QR #Returns both Q and R matrices from QR decomposition in a tuple

Matrix.Q #Returns the orthonormal matrix from the QR decomposition

Matrix.R #Returns the upper-triangular matrix from the QR decomposition

Matrix.trace #Returns the trace of the matrix

Matrix.nilpotency(limit) #Returns the nilpotency degree of the matrix, returns None if some elements diverge. Limit parameter is for iteration amount

Matrix.eigenvalues #Returns the eigenvalues #Doesn't work 100%, check issue #64

Matrix.isSquare #Returns True if the matrix is a square matrix

Matrix.isSymmetric #Returns True if the matrix is a symmetric matrix

Matrix.isAntiSymmetric #Returns True if the matrix is an antisymmetric matrix

Matrix.isPerSymmetric #Returns True if the matrix is a persymmetric matrix

Matrix.isHermitian #Returns True if the matrix is a hermitian matrix

Matrix.isTriangular #Returns True if the matrix is a triangular matrix

Matrix.isUpperTri #Returns True if the matrix is a upper-trianguar matrix

Matrix.isLowerTri #Returns True if the matrix is a lower-triangular matrix

Matrix.isDiagonal #Returns True if the matrix is a diagonal matrix

Matrix.isUpperBidiagonal #Returns True if the matrix is an upper-bidiagonal matrix

Matrix.isLowerBidiagonal #Returns True if the matrix is a lower-bidiagonal matrix

Matrix.isBidiagonal #Returns True if the matrix is an upper-bidiagonal or a lower-bidiagonal matrix

Matrix.isTridiagonal #Returns True if the matrix is a tridiagonal matrix

Matrix.isUpperHessenberg #Returns True if the matrix is an upper-Hessenberg matrix

Matrix.isLowerHessenberg #Returns True if the matrix is a lower-Hessenberg matrix

Matrix.isHessenberg #Returns True if the matrix is an upper-Hessenberg or a lower-Hessenberg matrix

Matrix.isToeplitz #Returns True if the matrix is a Toeplitz matrix

Matrix.isUnitary #Returns True if the matrix is a unitary matrix

Matrix.isIdempotent #Returns True if the matrix is an idempotent matrix

Matrix.isOrthogonal #Returns True if the matrix is an orthogonal matrix

Matrix.isCircular #Returns True if the matrix is a circular matrix

Matrix.isPositive #Returns True if the matrix is a positive valued matrix

Matrix.isNonNegative #Returns True if the matrix is a non-negative matrix

Matrix.isProjection #Returns True if the matrix is a projection matrix

Matrix.isZero #Returns True if the all the elements in the matrix is 0

```
##### Statistical properties 
```python 

Matrix.head(n) #Returns the first n rows (if there are less than n rows it returns all the rows)

Matrix.tail(n) #Returns the last n rows (if there are less than n rows it returns all the rows)

Matrix.describe #Returns a description matrix with columns describing the matrix holding column, count, dtype, mean, sdev, min, max, 25%, 50%, 75%.

Matrix.sum(n,asDict) #Returns the sum of the elements in the column with name/index 'n'. If 'n' is None, all column sums are returned. asDict to change wheter or not to return values in a dictionary or a list. If 'n' is given, asDict being False returns the value as it is, not in a list.

Matrix.prod(n,asDict) #Returns the product of the elements in the column with name/index 'n'. If 'n' is None, all column products are returned. asDict to change wheter or not to return values in a dictionary or a list. If 'n' is given, asDict being False returns the value as it is, not in a list.

Matrix.find(element,indexStart) #Returns a list of the element's indeces as tuples. Returns None if element not in matrix

Matrix.select(columns) #Returns a matrix where the desired columns are concatenated in order. Only works if 'columns' is a tuple or a list

Matrix.where(condition) #Returns a matrix where the given condition(s) are True. Example: Matrix.where("(Col 1>=0.5) and (Col 2!=0)") 

Matrix.match(regex,columns,as_row) #Return the rows or the values in the matrix depending on 'as_row', in the given column names/numbers in 'columns' as a list/tuple or str/int, matching given 'regex' regular expressions

Matrix.apply(expressions,columns,conditions,returnmat) #Apply given 'expression' to given 'columns' where the 'conditions' are True, set returnmat wheter or not to return self. If 'columns' is None, 'expressions' is applied to all columns. 

Matrix.replace(old,new,columns,conditions,returnmat) #Change 'old' values to 'new' in the 'columns' where the 'conditions' are True. Set returnmat wheter or not to return self.

Matrix.indexSet(name,start,returnmat) #Set an indexing column named 'name', starting from 'start' and return self if 'returnmat' is True

Matrix.sortBy(column,reverse,returnmat) #Sort the matrix by the desired 'column', do it in decreasing order if 'reverse'==True, and return self if 'returnmat'==True

Matrix.shuffle(iterations,returnmat) #Shuffle the rows 'iterations' times and return self if 'returnmat'==True

Matrix.sample(size,condition) #Get a sample sized 'size' where the 'condition' is True

Matrix.joint(matrix) #Returns a matrix of shared rows with given 'matrix'

Matrix.count(column,asDict) #Returns how many of the values are valid (same type as given in coldtypes) for each or desired column(s). asDict to change wheter or not to return values in a dictionary or a list.

Matrix.mean(n,asDict) #Returns the nth column or column named n's average, give None as argument to get the all columns' averages; asDict: True to get return a dictionary of features as keys and means as values, False to get means in a list. If n is given and asDict is False, returns a number.

Matrix.ranged(n,asDict) #Returns the nth column or column named n's range, give None as argument to get the all columns' ranges; asDict: True to get return a dictionary of features as keys and ranges as values, False to get ranges in a list. If n is given and asDict is False, returns a number.

Matrix.median(n,asDict) #Returns the nth column or column named n's median, give None to get all columns' medians; asDict: True to get return a dictionary of features as keys and ranges as values, False to get ranges in a list.

Matrix.freq(n,asDict) #Returns the nth column or column named n's elements frequency as a dictionary where elements are keys and how often they repeat as values. If called without arguments, returns every column"s frequencies; asDict: True to get return a dictionary of features as keys and ranges as values, False to get ranges in a list.

Matrix.mode(n,asDict) #Returns the nth column or column named n's mode, give None to get all columns' modes; asDict: True to get return a dictionary of features as keys and ranges as values, False to get ranges in a list.

Matrix.iqr(n,as_quartiles,asDict) #Returns the nth column or column named n's iqr, give None to get all columns' iqr values. If first,second and third quartiles is desired, give as_quartiles parameter bool(True); asDict: True to get return a dictionary of features as keys and iqr's as values, False to get iqr's in a list. If n is given and asDict is False, returns a number(or a list dependent on as_quartiles).

Matrix.sdev(n,population,asDict) #Returns the nth column or column named n's standard deviation, if None is given as an argument returns all columns' standard deviations. Give population parameter 1 if calculation is not for samples, 0 otherwise; asDict: True to get return a dictionary of features as keys and standard deviations as values, False to get standard deviations in a list. If n is given and asDict is False, returns a number.

Matrix.var(n,population,asDict) #Returns the nth column or column named n's variance, if None is given as an argument returns all columns' variance. Give population parameter 1 if calculation is not for samples, 0 otherwise; asDict: True to get return a dictionary of features as keys and variances as values, False to get variances in a list. If n is given and asDict is False, returns a number.

Matrix.cov(col1,col2,population) #Returns the col1 and col2's covariance. Give population parameter True if calculation is not for samples

Matrix.z(col,population) #Returns the z-scores of the desired  column, call without arguments to get the all z-scores as a matrix. Give population parameter 1 if calculation is not for samples, 0 otherwise.

Matrix.corr(column_1,column_2,population) #Returns linear correlation of 2 columns chosen from the matrix. If no argument given, returns the correlation matrix. Give population parameter 1 if calculation is not for samples, 0 otherwise

Matrix.normalize(column,inplace) #Normalize the data in the desired column, None to normalize all columns. Give inplace parameter "True" boolean value to make normalization in-place, "False" to return a new matrix with normalized data

Matrix.stdize(column,inplace) #Standardize the data in the desired column, None to standardize all columns. Give inplace parameter "True" boolean value to make standardization in-place, "False" to return a new matrix with standardized data

Matrix.features #Returns the column names if given, can also be used to set column names

Matrix.coldtypes #Returns what type of data each column carries, can be used to set the values.

```

----------------------------------------
##### Printing options
```python
#All the values + column names if it's a dataframe

myMatrix.grid 

#Dimensions + wheter its square or not + the string printed in 'grid' property

myMatrix.p #Same as print(myMatrix)

#Similar to 'grid' but rows and columns are limited by myMatrix.ROW_LIMIT and myMatrix.COL_LIMIT

myMatrix

#Issues about dtypes not matching and/or missing data can be solved by using 'replace' method
```
----------------------------------------
##### Copying the matrix
```python
#Using 'copy' property (Fastest)

newMatrix = oldMatrix.copy

#Using 'kwargs' property, 'copy' uses this one so it's as fast as 'copy' is

newMatrix = Matrix(kwargs=oldMatrix.kwargs)

#Using 'obj' property (Slowest)

newMatrix = eval(oldMatrix.obj)

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
   
   round(A @ A.inv)== Matrix(listed=Identity(A.dim[0]))
   
   round(A,4) == round(A.sym + A.anti,4)
   
   round(A.inv.inv,4) == round(A, 4)
   
   round(A.lowtri @ A.uptri, 4) == round(A, 4)
   
   round(A.Q @ A.R, 4) == round(A, 4)
   
   
``` 
----------------------------------------

#### More examples can be found in [exampleMatrices.py](https://github.com/MathStuff/MatricesM/blob/master/MatricesM/exampleMatrices.py)
