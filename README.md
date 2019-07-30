# <a href="https://pypi.org/project/MatricesM/">MatricesM</a>
#### A stand-alone library for Python 3.6 and higher to create and manipulate matrices used in linear algebra and dataframes in statistics
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

Matrix(dim=dimensions,#Required(UNLESS 'data' is given), int | list/tuple as [rows,cols]

       data=data, #Optional, list of numbers | list of lists containing numbers | string | dictionary. If no argument is passed matrix is filled depending on the 'fill' and 'ranged' 

       fill=value, #Optional,Available distributions: uniform|triangular|gauss|gammavariate|betavariate|expovariate|lognormvariate; also accepts int|float|complex|str|list|range, fills the matrix with chosen distribution or number, None will force uniform distribution. Doesn't affect the matrix if "data" is given

       ranged=[*args] | dict;"""
                        ->To apply all the elements give a list | tuple
                        ->To apply every column individually give a dictionary as {"Column_name":[*args], ...}
                        ->Arguments should follow one of the following rules:
                              1)If 'fill' is uniform, interval to pick numbers from as [minimum,maximum]; 
                              2)If 'fill' is gauss or lognormvariate mean and standard deviation are picked from this attribute as [mean,standard_deviation];
                              3)If 'fill' is triangular, range of the numbers and the mode as [minimum,maximum,mode];
                              4)If 'fill' is gammavariate or betavariate, alpha and beta values are picked as [alpha,beta]
                              5)If 'fill' is expovariate, lambda value have to be given in a list as [lambda]"""                   

       features=column_names #Optional, list of strings. If no argument given, columns get named "col_1","col_2" and so on
      
       seed=integer_seed #Optional, int. Seed to generate the random numbers from, doesn't affect anything if numbers are provided.
         
       dtype=matrix_dtype #Optional, int|float|complex|dataframe. Data type the matrix will hold, default is float.
      
       coldtypes=column_dtypes #Requires dtype==dataframe to work. Contains the data types each column will hold. If nothing is passed, types get declared by the first row.
      
       decimal=decimals_to_round #Optional, int (default is 4). Decimal digits to round to while printing

       index=index_column #Optional, Matrix|list|tuple; indices to use for rows. Only works if dtype is set to dataframe

       indexname=index_col_name #Optional, str; name of the index column

       implicit=False #Optional, boolean. If necessary parameters are given, this can be set to True to speed up the setup process. Don't change if you aren't sure what your matrix requires to work properly.
      )

#Alternative way for creating dataframes, inherits from Matrix class, dtype is passed as dataframe to Matrix
dataframe(data=data,
          features=column_names,
          coldtypes=column_dtypes,
          decimal=decimals_to_round, #Decimal defaults to 3
          index=index_column,
          indexname=index_col_name, 
          **kwargs #Rest of the arguments passed to Matrix's __init__
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
id3 = Matrix(data=Identity(3))

#A 8x8 symmetrical matrix filled with numbers in range from 0 to 1 with uniform distribution 
sym1 = Matrix(data=Symmetrical(8))

``` 
----------------------------------------
##### Give list of numbers to create matrices
```python 
#Creates a matrix with the given list of numbers
filled_rows = [[1,2,3],[4,5,6],[7,8,9]]

C = Matrix(data=filled_rows) 

#Create a dataframe from a list
data = [["James",180.4,85],
        ["Tom",172,73],
        ["Sophia",168.25,65]]

df = dataframe(data=data,
               features=["Name","Height","Weight"],
               decimal=1)
               
#Same as:        
df = Matrix(data=data,
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
                data=data,
                features=["id","age","num1","num2"],
                dtype=int) 

#Or as a dataframe
df = Matrix(dim=[10,4],
            data=data,
            features=["id","age","num1","num2"],
            dtype=dataframe,
            coldtypes=[int]*4)

```
----------------------------------------
##### Read data from files 
```python 
#Create a dataframe matrix from a csv file. read_file accepts 2 optional parameters: encoding, delimiter
data_matrix = read_file(data_directory) 

#Example dataset: https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009
wine = read_file(".../Data/winequality-red.csv")
```
----------------------------------------
##### Get specific parts of the matrix (Assuming default column names)
```python
#All rows' second to forth columns as a matrix
Matrix[:,1:4] == Matrix.t[1:4,:].t

#Nineth column of every even numbered row as a matrix
Matrix[::2,8] == Matrix[::2,8:9] == Matrix["col_9"][::2] == Matrix.col_9[::2] 
#Using methods
Matrix.select(("col_9"))[::2] == Matrix.col(9)[::2]

#Forth to seventh rows as a matrix
Matrix[3:7] 

#Fifth row's eighth element (returns the value as it is, not a new matrix)
Matrix[4,7] == Matrix.matrix[4][7]

#Use column names
Matrix["col_3","col_1","col_2"] == Matrix.select(("col_3","col_1","col_2"))

#Use index column for row indices
#Return the rows where the index matches the 'value'
Matrix.ind[value]

#Return the rows from val1's first appearance until val2's first appearance with only 'col_4' column
Matrix.ind[val1:val2,"col_4"]
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

#Use 'quality' column as indices
winedata.index = winedata.quality

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

#Return the rows of all email adresses using gmail.com domain in the column 'mail'
Matrix.match(expression=r"\w+@gmail.com",
             columns="mail",
             as_row=True)
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
              new=data.mean("Length",get=0),
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
s = Matrix(5,fill=5,dtype=int)
s[1:4,1:4] = 0 #Same as using Matrix(3,fill=0)
#Visually:
"""
5 5 5 5 5              5 5 5 5 5
5 5 5 5 5  Changes to  5 0 0 0 5
5 5 5 5 5     ---->    5 0 0 0 5
5 5 5 5 5              5 0 0 0 5
5 5 5 5 5              5 5 5 5 5
"""

#Change the values in the 2nd to 4th rows' 1st and 3rd columns to 0 and 99 
Matrix[1:4,("col_1","col_3")] = [0,9]
#Visually:
"""
3 9 6 10               3 9  6  10
5 0 4  2   Changes to  0 0 99   2
5 8 2  2      ---->    0 8 99   2
6 1 7  0               0 1 99   0
"""

#Change all values in the 2nd column to 7's
Matrix.col_2 = 7
#Visually:
"""
3 9 6 10               3 7 6 10
5 0 4  2   Changes to  5 7 4  2
5 8 2  2      ---->    5 7 2  2
6 1 7  0               6 7 7  0
"""

#Change odd numbered rows' even numbered columns to the values in the given matrix
Matrix[0::2,1::2] = Matrix(2,fill=999)
#Visually:
"""
3 9 6 10               3 999 6 999
5 0 4  2   Changes to  5   7 4   2
5 8 2  2      ---->    5 999 2 999
6 1 7  0               6   7 7   0
"""
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

Matrix.matrix #Returns the matrix's rows as lists in a list. >>> dataframe.data Returns the same thing if dataframe was used instead of Matrix

Matrix.dim #Returns the dimension of the matrix; can be used to change the dimensions, ex: [4,8] can be set to [1,32] where rows carry over as columns in order from left to right

Matrix.d0 #Returns the amount of rows

Matrix.d1 #Returns the amount of columns

Matrix.col(n,as_matrix) #Returns the nth column if n is an integer or returns the column named n, as a list or matrix, set as_matrix to True to get the list as a matrix

Matrix.row(n,as_matrix) #Returns nth row of the matrix as a list or matrix, set as_matrix to True to get the list as a matrix

Matrix.concat(matrix,axis) #Concatenate a matrix to self. Set 'axis' to 0 to concatenate as rows, 1(default) to concatenate as columns

Matrix.add(values,row,col,feature,dtype) #Adds list to given index in row or col, indeces start from 1. If a column is added, dtype and feature are used determine type and name.

Matrix.remove(row,col) #Removes the desired row and/or column

Matrix.copy #Returns a copy of the matrix

Matrix.obj #Returns the string form of the Matrix object which can be evaluated to create the same matrix

Matrix.seed #Returns the seed used to generate the random numbers in the matrix, returns None if matrix wasn't filled randomly. Can be used to refill the matrix inplace if set to a new value

Matrix.fill #Returns the value or distribution of which the matrix was filled with. Can be used to refill the matrix inplace if set to a new value

Matrix.initRange #Returns the value of 'ranged' used while creating the matrix. Can be used to refill the matrix inplace if set to a new value

Matrix.index #Returns the values in the index column in a list, can bu used to set new indices

Matrix.indexname #Returns the index column's name

Matrix.intForm #Returns integer form of the matrix

Matrix.floatForm #Returns float form of the matrix

Matrix.ceilForm #Returns a matrix of all the elements' ceiling values

Matrix.floorForm #Returns the same matrix as "intForm"

Matrix.roundForm(n) #Returns a matrix of elements' rounded up to n decimal digits. Same as round(Matrix,n)

Matrix.kwargs #Returns a dictionary of the matrix's basic attributes

Matrix.ROW_LIMIT #Attribute to determine the amount of rows to print while representing the matrix, default is 30.

Matrix.COL_LIMIT #Attribute to determine the amount of columns to print while representing the matrix, default is 12.

Matrix.EIGEN_ITERS #Attribute to determine how many iterations will be done in eigenvalue calculation with QR algorithm, default is 100 for even numbered dimensions, 500 for odd ones. Play around with this value if the values you get don't seem right.

Matrix.col_1, Matrix.col_2, ... #Returns the column named col_1,col_2 ...

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

Matrix.describe #Returns a description matrix with columns describing the matrix holding column, count, dtype, mean, sdev, min, 25%, 50%, 75%, max.

Matrix.info #Returns information about columns: Dtype, Valid data amount, Invalid data amount, Unique data amount

Matrix.uniques(column) #Returns the unique set of the 'column'; If 'column' is None, all columns' unique values are returned in a list of lists 

Matrix.groupBy(columns) #Return a 'Group' object containing the Matrix grouped by given 'columns'.

Matrix.sum(n,get) #Returns the sum of the elements in the column with name/index 'n'. If 'n' is None, all column sums are returned. Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.prod(n,get) #Returns the product of the elements in the column with name/index 'n'. If 'n' is None, all column products are returned. Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.find(element,indexStart) #Returns a list of the element's indeces as tuples. Returns None if element not in matrix

Matrix.select(columns) #Returns a matrix where the desired columns are concatenated in order. Only works if 'columns' is a tuple or a list

Matrix.where(condition) #Returns a matrix where the given condition(s) are True. Example: Matrix.where("(col_1>=0.5) and (col_2!=0)") 

Matrix.match(regex,columns,as_row) #Return the rows or the values in the matrix depending on 'as_row', in the given column names/numbers in 'columns' as a list/tuple or str/int, matching given 'regex' regular expressions

Matrix.apply(expressions,columns,conditions,returnmat) #Apply given 'expression' to given 'columns' where the 'conditions' are True, set returnmat wheter or not to return self. If 'columns' is None, 'expressions' is applied to all columns. Executed as: value=eval('value'+operation)

Matrix.transform(function,columns,conditions,returnmat #Pass values into the given 'function' and change them to what it outputs. Rest of the parameters works same as 'apply' method. Executed as: value = function(value)

Matrix.replace(old,new,columns,conditions,returnmat) #Change 'old' values to 'new' in the 'columns' where the 'conditions' are True. Set returnmat wheter or not to return self.

Matrix.indexreset(start) #Reset index column to range(start,Matrix.d0+start)

Matrix.namereset() #Reset column names to 'col_1','col_2', ...

Matrix.sortBy(column,reverse,returnmat) #Sort the matrix by the desired 'column', do it in decreasing order if 'reverse'==True, and return self if 'returnmat'==True

Matrix.shuffle(iterations,returnmat) #Shuffle the rows 'iterations' times and return self if 'returnmat'==True

Matrix.sample(size,condition) #Get a sample sized 'size' where the 'condition' is True

Matrix.joint(matrix) #Returns a matrix of shared rows with given 'matrix'

Matrix.count(column,get) #Returns how many of the values are valid (same type as given in coldtypes) for each or desired column(s).  Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.mean(n,get) #Returns the nth column or column named n's average, give None as argument to get the all columns' averages;  Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.ranged(n,get) #Returns the nth column or column named n's range, give None as argument to get the all columns' ranges; Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.median(n,get) #Returns the nth column or column named n's median, give None to get all columns' medians;  Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.freq(n,get) #Returns the nth column or column named n's elements frequency as a dictionary where elements are keys and how often they repeat as values. If called without arguments, returns every column"s frequencies; Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a list of Matrix object for each column.

Matrix.mode(n,get) #Returns the nth column or column named n's mode, give None to get all columns' modes;  Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a list of Matrix object for each column.

Matrix.ranked(n,reverse,key,get) #Returns the nth column or column named n's ranks(that are the indices the values would get if they were sorted) give None to get all columns' modes;  Use 'get' to choose what to return,-1 for ranks in-place, 0 for a list, 1 for a dictionary(default), 2 for a list of Matrix object for each column.

Matrix.iqr(n,as_quartiles,get) #Returns the nth column or column named n's iqr, give None to get all columns' iqr values. If first,second and third quartiles is desired, give as_quartiles parameter bool(True);  Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.sdev(n,population,get) #Returns the nth column or column named n's standard deviation, if None is given as an argument returns all columns' standard deviations. Give population parameter 1 if calculation is not for samples, 0 otherwise; Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.var(n,population,get) #Returns the nth column or column named n's variance, if None is given as an argument returns all columns' variance. Give population parameter 1 if calculation is not for samples, 0 otherwise;  Use 'get' to choose what to return, 0 for a list, 1 for a dictionary(default), 2 for a Matrix.

Matrix.cov(col1,col2,population) #Returns the col1 and col2's covariance. Give population parameter True if calculation is not for samples

Matrix.z(col,population) #Returns the z-scores of the desired  column, call without arguments to get the all z-scores as a matrix. Give population parameter 1 if calculation is not for samples, 0 otherwise.

Matrix.corr(column_1,column_2,population,method) #Returns linear correlation of 2 columns chosen from the matrix. If no argument given, returns the correlation matrix. Give population parameter 1 if calculation is not for samples, 0 otherwise; methods available: 'pearson'(default), 'kandell', 'spearman'

Matrix.normalize(column,inplace) #Normalize the data in the desired column, None to normalize all columns. Give inplace parameter "True" boolean value to make normalization in-place, "False" to return a new matrix with normalized data

Matrix.stdize(column,inplace) #Standardize the data in the desired column, None to standardize all columns. Give inplace parameter "True" boolean value to make standardization in-place, "False" to return a new matrix with standardized data

Matrix.features #Returns the column names if given, can also be used to set column names

Matrix.rename(old_names,new_names) #Rename columns. Multiple names should be given in a list or a tuple

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
   
   round(A @ Matrix(data=Identity(A.dim[0])),4) == round(A, 4) #A assumed to be a square matrix
   
   round(A @ A.inv)== Matrix(data=Identity(A.dim[0]))
   
   round(A,4) == round(A.sym + A.anti,4)
   
   round(A.inv.inv,4) == round(A, 4)
   
   round(A.lowtri @ A.uptri, 4) == round(A, 4)
   
   round(A.Q @ A.R, 4) == round(A, 4)
   
   
``` 
----------------------------------------

#### More examples can be found in [exampleMatrices.py](https://github.com/MathStuff/MatricesM/blob/master/MatricesM/exampleMatrices.py)
