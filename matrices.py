# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

import random as rd

class Matrix(object):
    """Matrix object:
***Create matrices and print them as grids***
***Use this if and only if you are going to work with integers. Use FMatrix class to use float values***

-dim:dimension of the matrix;natural numbers as [rows,cols],if and integer given, matrix will be a square matrix 
-listed:(a list of integers | a string) with & dim**2 amount of integers
-inRange:list of 2 numbers
-rangeLock: wheter or not not to allow numbers out of given range
-randomFill: 
    ->1 to fill the matrix with random integers if no list is given
    ->0 to fill the matrix with 0s
    
-Giving ~300< elements may make grid look terrible, adjust your terminal size to display it better
-Can contain integers only (Unless it's a FMatrix class) 

-Elements/row can be changed in place ( Current not available on columns )
-Additional rows and columns can be added with add(row,col,lis)
-Rows and cols from right and bottom can be deleted with del
-Sub-matrices can be obtained with "subM" method
-Get specific items by using a[i][j] for the (i+1)th row and (j+1)th column   

-Average of the all given elements can be seen with "avg" property
-Determinant of the matrix can be calculated by "det" propery
-For the adjoint form of the matrix, use "adj" property
-To get the transposed matrix, use "t" property
-For the inverse of the matrix use "inv" property

-Use "summary" property to get the representation of the matrix
-Use "matrix" property to get the matrix in list format or just call the variable by itself

-You can use +,-,*,/,//,**,%,@,<,>,== operators:
    o Addition : +
    o Subtraction : -
    o Multiplication : *
    o True division : /
    o Floor division : //
    o Modular : %
    o Power : **
    o Matrix multiplication : @
    o Less than, greater than, equal to : <, >, ==
    
Check exampleMatrices.py for further explanation and examples
    """
    def __init__(self,dim=None,listed=[],inRange=[-125,125],rangeLock=0,randomFill=1):
        self._isIdentity=0
        self._fMat=0
        self._cMat=0
        if isinstance(self,FMatrix):
            self._fMat=1
        elif isinstance(self,CMatrix):
            self._cMat=1
        
        self._valid = 1
        self.__adjCalc=0
        self.__detCalc=0
        self.__invCalc=0
        self.__rankCalc=0
        
        if not self._isIdentity:
            if dim==None:
                self._dim = [0,0]
            else:
                self._dimSet(dim)
            self._matrix = []     
            self._inRange = inRange
            self._randomFill = randomFill
            self._rangeLock = rangeLock
            
        try:
            if len(inRange)!=2:
                self._valid=0
            elif inRange[0]==inRange[1]:
                self._valid=0
            
        except Exception as err:
            print(err)
            print(Matrix.__doc__)
            
        else:
            if isinstance(listed,str) and self._valid and not self._isIdentity :
                self._valid=1
                self._matrix=self._listify(listed)
                self._dim=self._declareDim()
                if not self._rangeLock:
                    self._inRange=self._declareRange(self._matrix)

               
            elif self._validateList(listed) and self._valid and not self._isIdentity :
                    self.__temp1=[a[:] for a in listed]
                    
                    if len(self.__temp1)>0:                        
                            self._matrix = self.__temp1.copy()  
                            if not self._rangeLock:
                                self._inRange=self._declareRange(self._matrix)
                            self._dim=self._declareDim()
                            self._string=self._stringfy(self._dim)     
                    elif len(self.__temp1)==0 and dim!=[0,0]:
                        
                        if not self._randomFill:
                            self._matrix=self._zeroFiller(self.__temp1)
                            if not self._rangeLock:
                                self._inRange=self._declareRange(self._matrix)
                            
                        elif self._randomFill:
                            self._matrix=self._randomFiller(self.__temp1)
                            if not self._rangeLock:
                                self._inRange=self._declareRange(self._matrix)
                            self._dim=self._declareDim() 
                            self._string=self._stringfy(self._dim) 
                        else:
                            self._valid=0
                            return None
                    else:
                        self._valid=0
                        return None
            else:
                self._valid=0
                return None
            
# =============================================================================
            
    def _dimSet(self,dim):        
        """
        Change the given dimension's format to a list if it's a valid integer.
        """
        if isinstance(dim,list):
            self._dim=dim[:]
            rows=dim[0]
            cols=dim[1]
            if rows<0 or cols<0: 
                self._valid=0  
            else:                              
                self._dim=[rows,cols]
            
        elif isinstance(dim,int):
            if dim<0:
                self._valid=0
            else:
                self._dim=[dim,dim]
            
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
            if rows!=cols:
                return [rows,cols]
            return [cols,cols]
    
    def _validateList(self,alist):
        """
        Validates the given matrix by checking if all the rows are the same length
        """
        if isinstance(alist,list):
            if len(alist)>0:

                r=0
                l=[]
                c=0
                for row in alist:
                    c=0
                    r+=1
                    for col in row:
                        c+=1
                    l.append(c)
                return max(l)==min(l)
            return True
        return False
    
    def _declareRange(self,lis):
        """
        Finds and returns the range of the elements in a given list
        """
        try:
            low=0
            high=0
            first=True
            for row in lis:
                m=max(row)
                n=min(row)
                if first:
                    low=n
                    high=m
                    first=False
                else:
                    temp=[low,high,n,m]
                    low=min(temp)
                    high=max(temp)
        except Exception as err:
            print("Can't declare range")
            #print(Matrix.__doc__)
            return [low,high]
        else:
            return [low,high]
   
# =============================================================================  
    def _listify(self,string,square=0):
        """
        Finds all the positive and negative numbers in the given string
        Tries to fit the numbers into a grid shape
        Returns a list in a form of a square matrix
        """
        try:
            gridNum=""
            numbers=["0","1","2","3","4","5","6","7","8","9"]
            l=len(string)
            
            list1=list()
            negative=0
            newRow=0
            rowadded=0
            
            if self._dim==[0,0]:
                square=0
            else:
                square=1
            
            for c in range(0,l):    
                #print("c:{0} neg:{1} str:{2} num:{3}".format(c,negative,string[c],gridNum))
                #print("list:",list1)
                if c==l-1 and len(gridNum)>0:
                    if negative:
                            list1.append(int(gridNum)*-1)
                    else:
                        list1.append(int(gridNum))
                    break
                if string[c] in numbers:
                    gridNum+=string[c]
                    if c==l-1:
                        if negative:
                            list1.append(int(gridNum)*-1)
                            rowadded=0
                            gridNum=""
                            negative=0
                        else:
                            list1.append(int(gridNum))
                            rowadded=0
                            gridNum=""
                elif string[c]=="-":
                    
                    if len(gridNum)>0:
                        list1.append(int(gridNum))
                        rowadded=0
                        gridNum=""
                    negative=1  
                
                elif string[c]=="\n":
                    if not square and not rowadded:
                            newRow+=1
                            rowadded=1
                    if len(gridNum)>0:
                        if negative:
                            list1.append(int(gridNum)*-1)
                            rowadded=0
                            gridNum=""
                            negative=0
                        else:
                            list1.append(int(gridNum))
                            rowadded=0
                            gridNum=""
# =============================================================================
#             elif string[c]=="," and len(gridNum)>0:
#                 loop=1
#                 print(c,l)
#                 while c<l:
#                     print(string[c],string[c+1])
#                     if string[c+1] in numbers:
#                         gridNum=int(gridNum)
#                         gridNum+=int(string[c+1])*(10**(-1*loop))
#                         c+=1
#                         loop+=1
#                     else:
#                         list1.append(gridNum)
#                         rowadded=0
#                         gridNum=""
#                         break
#                 
# =============================================================================
                else:
                    if len(gridNum)>0:
                        if negative:
                            list1.append(int(gridNum)*-1)
                            rowadded=0
                            negative=0
                            gridNum=""
                        else:
                            list1.append(int(gridNum))
                            rowadded=0
                            gridNum=""
                            
        except Exception as err:
            print("****List error****\nMake sure string:\n-Has positive integers only \n-Have 1 space splitting the elements")
            print(Matrix.__doc__)
        else:
            l1=len(list1)
            l=l1**0.5
            d=0
            list2=list()
            list2=self._zeroFiller(list2)
            for integer in range(1,30):
                if integer==l:
                     d=integer

            if l1==0:
                self._dim=[0,0]
                self._valid=1
                return []
            
            if l1>0 and d==0:
                square=0
                if self._dim==[0,0]:
                    self._dim=[1,l1]
                    list2=[list1]
                    return list2
                
            elif l1>0 and d>0 and newRow>=0:
                square=1
                if self.dim==[0,0]:
                    self._dim=[d,d]

            self.__temp1=list1[:]

            temp=0
            
            try:

                if newRow>0 and l1%(newRow+1)==0:
                    for rows in range(0,newRow+1):
                        list2.append(list())
                        for i in range(temp,(l1//(newRow+1))+temp):
                            list2[rows].append(list1[i])
                        temp+=(l1//(newRow+1))
                        
                elif square and self.dim==[d,d]:
                    for rows in range(0,d):
                        list2.append(list())
                        for i in range(temp,d + temp):
                            list2[rows].append(list1[i])
                        temp+=d

                        
                elif self.dim!=[0,0]:
                    for rows in range(0,self.dim[0]):
                        for i in range(temp,self.dim[1] + temp):
                            list2[rows].append(list1[i])
                        temp+=self.dim[1]

                else:
                    print("Invalid string")
                    self._valid=0
                    return None
                
            except Exception as err:
                print(err)
                self._valid=0
            else:
                return list2
    
    def _stringfy(self,dm):
        """
        Turns a square matrix shaped list into a grid-like form that is printable
        Returns a string
        """
        def _digits(num):
                try:
                    num=int(float(num))
                    dig=1
                except TypeError:
                    print("Digits are too much of a mess to handle! Returning none")
                    return None
                else:
                    if num<=0:
                        num=num*-1
                        dig+=1
                        
                    while num>0:
                        dig+=1
                        num=num//10
                        
                    return dig
        while True:
            try:     
                string=""
                if self._isIdentity:
                    l=1
                    h=1
                else:
                    l=_digits(self._inRange[0])
                    h=_digits(self._inRange[1])
                    
                d=self._dim[:]
                s=max([h,l])
                for i in range(d[0]):
                    string+="\n"
                    for j in range(d[1]):
                        if isinstance(self._matrix[i][j],complex) or self._cMat:
                            a="{0:.8f}".format(self._matrix[i][j])
                            string += " "+a+" " 
                            
                        elif self._fMat and not self._cMat:
                            n=self._matrix[i][j]
                            a="{:.4f}".format(n)
                            f=_digits(n)
                            if n>-1 and n<1:
                                string += " "+a+" "
                                continue
                            if n>1:
                                string += " "*(s-f)+a+" "
                            else:
                                string += " "*(s-f-1)+a+" "
                                
                        else:
                            a=str(self._matrix[i][j])
                            f=_digits(a)
                            string += " "*(s-f)+a+" "      
            except Exception as err:
                print("Elements may look complicated ",end="")
                print(err)
                break
            else:   
                return string
# =============================================================================

    def _zeroFiller(self,lis):
        """
        Fills the matrix with zeros
        """
          
        for rows in range(0,self._dim[0]):
            lis.append(list())
            if not self._randomFill: 
                for cols in range(0,self._dim[1]):
                    lis[rows].append(0)
            else:
                pass
                #print("Try turning on randomFill if you're having issues")
        if self._isIdentity:            
            for row in range(0,self._dim[0]):
                lis[row][row]=1  
                
        return lis

    def _randomFiller(self,lis):
        """
        Fill the matrix with random integers from given range
        """
        try:
            assert len(self._inRange)==2 and self._inRange[0]!=self._inRange[1]
        except AssertionError:
            print("Bad argument for inRange parameter!")
            print(Matrix.__doc__)
        except Exception as err:
            print(err)
            print(Matrix.__doc__)
        else:
            
            if  self._randomFill:
                
                lis=self._zeroFiller(lis)
                m,n=max(self._inRange),min(self._inRange)
                d=self._dim[:]
                for row in range(0,d[0]):
                    for column in range(0,d[1]):
                        if not self._fMat:
                            lis[row].append(rd.randint(n,m))
                        else:
                            new=rd.randint(n,m)*rd.random()
                            ele="{0:.4f}".format(new)
                            lis[row].append(float(ele))

            return lis
        
# =============================================================================
            
    def add(self,row=None,col=None,lis=[]):
        """
        Add a row or a column of numbers
        FIRST ROW | COLUMN : row | col = 1
        row: natural number
        col: natural number 
        lis: list of numbers desired to be added to the matrix
        row>=1 and col>=1
        
        To append a row, only give the list of numbers, no other arguments
        To append a column, you need to use col = self.dim[1]
        """
        try:
            if self._isIdentity:
                print("Can't add to identity matrix.\nUse addDim instead!")
                return None
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
            self._dim=self._declareDim()
            if not self._rangeLock:
                self._inRange=self._declareRange(self._matrix)
            self._string=self._stringfy(self._dim) 
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0     
            return self._matrix
        
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
                        if r<self.dim[1]:
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
            self._matrix=[a[:] for a in newM]
            self._dim=self._declareDim()
            self._string=self._stringfy(self._dim)
            
    def delDim(self,num):
        """
Removes desired number of dimensions from bottom left corner
        """        
        try:
            if self.matrix==[]:
                return "Empty matrix"
            assert isinstance(num,int) and num>0 and self.dim[0]-num>=0 and self.dim[1]-num>=0
            goal1=self._dim[0]-num
            goal2=self._dim[1]-num
            if goal1==0 and goal2==0:
                print("All rows have been deleted")
            self._dim=[goal1,goal2]
            temp=[]
            for i in range(goal1):
                temp.append(self._matrix[i][:goal2])
            self._matrix=temp
            self._string=self._stringfy(self.dim)
        except AssertionError:
            print("Enter a valid input")
        except Exception as err:
            print(err)
        else:
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0  
            return self
        
    def find(self,element):
        """
        element: Real number
        Returns the indeces of the given elements, multiple occurances are returned in a list
        """
        indeces=[]
        r=0
        for row in self._matrix:
            try:
                if element in row:
                    i=row.index(element)
                    indeces.append((r+1,i+1))
                    while element in row[i+1:]:
                        indeces.append((r+1,self._matrix[i+1:].index(element)+1))
            except IndexError:
                r+=1
                continue
            else:
                r+=1
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
            valid=0
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
            assert rowS<=self._dim[0] and rowE<=self._dim[0] and colS<=self._dim[1] and colE<=self._dim[1]
            
        except AssertionError:
            print("Bad arguments")
            print(rowS,rowE,colS,colE)
            print(self.subM.__doc__)
            return ""
        except Exception as err:
            print(err)
            return ""
        else:
            temp=self._matrix[rowS-1:rowE]
            for column in range(len(temp)):
                valid=1
                temp2.append(temp[column][colS-1:colE])
            if valid:
                if isinstance(self,FMatrix):
                    return FMatrix(dim=[rowE-rowS,colE-colS],listed=temp2)
                elif isinstance(self,CMatrix):
                    return CMatrix(dim=[rowE-rowS,colE-colS],listed=temp2)
                else:
                    return Matrix(dim=[rowE-rowS,colE-colS],listed=temp2)

# =============================================================================
                    
    def _determinant(self):
        """
        Leibniz formula for determinants
             
        """

        def __zerochecker(m):
            """
            Speed up the process by checking the linear dependencies
            """
            for i in range(len(m)):
                for rows in m:
                    n=m[i+1:]
                    if rows in n:
                        self._det=0
                        self.__detCalc=1
                        return self._det
                    else:
                        break
        def __factorial(num1,dict1={0:1,1:1}):
            if num1 not in dict1.keys():
                dict1[num1]=num1*__factorial(num1-1,dict1)    
            return dict1[num1]
        
        def __findPermutations(num):  
            """
            Find all the permutations of the given string or list
            """
            def __permutations(s,e='',l=[]):
    
                if isinstance(s,list):
                    s="".join(str(element) for element in s)
                    
                if len(s)==0:
                    if e not in l:
                        p=[int(letter) for letter in e]
                        l.append(p)
                else:
                    for i in range(len(s)):
                        __permutations(s[:i] + s[i+1:], e+s[i])
                
                return l
            
            allPermutations=__permutations(allNums)
            for permutation in allPermutations:
                yield permutation  
        
        def __signature(perm1,perm2):
            """
            Determine the signature of the product
            """
            def __orderChangeSteps(p1,p2):
                mirrorDict={}
                looping=True
                l=0
                for items in p1:
                    mirrorDict[items]=p2[l]
                    l+=1

                while looping:
                    try:                        
                        d=0
                        for k,v in mirrorDict.items():
                            if k!=v: 
                                d+=1
                                for keys,values in mirrorDict.items():
                                    if  values==k:
                                        mirrorDict[k]=values
                                        mirrorDict[keys]=v
                                    
                    except RuntimeError:
                        continue
                    except Exception as err:
                        print(err)
                    else:
                        looping=False
                        if d==len(perm1):
                            return d-1
                        return d
            
            dif=__orderChangeSteps(perm1,perm2)

            if dif%2==1:
                return -1
            else:
                return 1
            
        __zerochecker(self._matrix) 
        
        if not self.__detCalc:  
            try:
                assert self.dim[0]==self.dim[1]
                d0=self.dim[0]
                if d0>=8:
                    print("Press CTRL+C to quit, current runtime is too inefficient for dimensions beyond 8")
                if d0<2:
                    return self._matrix[0][0]
    
            except AssertionError:
                print("Not a square matrix")
            else:
                permPossible=__factorial(d0)
                allNums=[n for n in range(1,d0+1)]
                permGen=__findPermutations(d0)  
                
                det=0
                for sums in range(permPossible):
                    s=1
                    perms=next(permGen)
                    
                    for p in range(d0):
                        s*=self.matrix[p][perms[p]-1]                    
                    
                    sign=__signature(allNums,perms)
                    det+=s*sign
                self.__detCalc=1
                if not self._fMat:                        
                    self._det=int(det)
                    return self._det
                else:
                    a="{0:.4f}".format(det)
                    self._det=float(a)
                    return self._det
        else:
            return self._det
        
    def _transpose(self):
        try:
            if self._isIdentity:
                return self
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
                return FMatrix(listed=transposed)
            else:
                return Matrix(listed=transposed)
            
    def _minor(self,row=None,col=None):
        try:
            assert row!=None and col!=None
            assert row<=self.dim[0] and col<=self.dim[1]
            assert row>0 and col>0
        except AssertionError:
            print("Bad arguments")
        else:
            temp=self.copy
            temp.remove(r=row)
            temp.remove(c=col)
            return temp

    def _adjoint(self):
        def __sign(pos):
            return (-1)**(pos[0]+pos[1])   
        try:
            assert self.dim[0]==self.dim[1]
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

            if not self._fMat:
                adjM=Matrix(dim=self.dim,listed=adjL)
            else:
                adjM=FMatrix(dim=self.dim,listed=adjL)
            self._adj=adjM.t
            self.__adjCalc=1
            return self._adj
                       
    def _inverse(self):
        """
        Uses the formula:
            
                inv(A)=(1/det(A))*adj(A)
            
        Finds the inverse of the given square matrix
        Sets the inverse form in float numbers format
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
            if self.__adjCalc:
                a=self._adj
            else:
                a=self._adjoint()
            d=self.det
            i=a/d
            new=FMatrix(listed=i.matrix)
            self._inv=new
            return self._inv

    def _Rank(self):
        m=min(self.dim)
        dimsOf=[]
        #Get square matrices from mxn dimension matrix (m!=n)
        if self._dim[0]<2 or self._dim[1]<2:
            return 1
        if self._dim[0]!=self._dim[1]:
            if m==self.dim[0]:
                for i in range(1,m+2):    
                    temp=self.subM(1,m,i,i+m-1)
                    if temp.det!=0 and temp.det!=None:
                        return m
                    else:
                        dimsOf.append(temp.rank)
            elif m==self.dim[1]:
                for i in range(1,m+2):    
                    temp=self.subM(i,i+m-1,1,m)
                    if temp.det!=0 and temp.det!=None:
                        return m
                    else:
                        dimsOf.append(temp.rank)
            return max(dimsOf)
        else:
            topLeft=self.minor(1,1)
            topRight=self.minor(1,m)
            bottomLeft=self.minor(m,1)
            bottomRight=self.minor(m,m)
            a=[topLeft,topRight,bottomLeft,bottomRight]
            for items in [self,topLeft,topRight,bottomLeft,bottomRight]:
                if items.det!=0 and items.det!=None:
                    return items.dim[0]
            else:
                for jj in range(len(a)):
                    dimsOf.append(a[jj].rank)
            self.__rankCalc=1
            return max(dimsOf)
# =============================================================================

    def _average(self):
        """
        Sets the avg attribute of the matrix as the average of it's elements
        """
        try:
            d=self._dim[:]
            if d[0]==0 or d[1]==0:
                return "None"
            total=0
            for row in self._matrix:
                if isinstance(row,list):
                    for ele in row:
                        total+=ele
                else:
                    total+=row
        except Exception as err:
            print("Bad matrix and/or dimension")
            print(err)
            return None
        else:
            new=total/(d[0]*d[1])
            return new

# =============================================================================
    """Properties available for public"""               
# =============================================================================
    @property
    def grid(self):
        print(self._stringfy(self._dim))
    @property
    def copy(self):
        if self._isIdentity:
            return Identity(dim=self._dim)
        elif self._fMat:
            return FMatrix(dim=self._dim,listed=self._matrix,inRange=self._inRange,rangeLock=self._rangeLock,randomFill=self._randomFill)
        else:
            return Matrix(dim=self._dim,listed=self._matrix,inRange=self._inRange,rangeLock=self._rangeLock,randomFill=self._randomFill)
    @property
    def string(self):
        return self._string
    @property
    def dim(self):
        return self._dim
    @property
    def rank(self):
        if not self.__rankCalc:
            self._rank=self._Rank()
        return self._rank
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
    def inRange(self):
        self._inRange=self._declareRange(self._matrix)[:]
        return self._inRange
    @property
    def matrix(self):
       return self._matrix
    @property
    def det(self):
        if self.__detCalc:
            return self._det
        return self._determinant()
    @property
    def avg(self):
        if self._average()!="None":
            return float(self._average())
        else:
            return None
    @property
    def highest(self):
        if not self._isIdentity:
            return self._inRange[1]
        else:
            return 1
    @property
    def lowest(self):
        if not self._isIdentity:
            return self._inRange[0]   
        else:
            return 0
    @property
    def summary(self):
        if self._valid and self._fMat:
            return "FMatrix(dim={0},listed={1},inRange={2},rangeLock={3},randomFill={4})".format(self._dim,self._matrix,self._inRange,self._rangeLock,self._randomFill)
        elif self._valid and not self._isIdentity:
            return "Matrix(dim={0},listed={1},inRange={2},rangeLock={3},randomFill={4})".format(self._dim,self._matrix,self._inRange,self._rangeLock,self._randomFill)
        elif self._valid and self._isIdentity:
            return "Identity(dim={0},listed={1},inRange=[0,1],rangeLock=1,randomFill=0)".format(self._dim,self._matrix)
        else:
            return None
        
    def minor(self,r=None,c=None):
        return self._minor(row=r,col=c)  
    
    def rangeLock(self):
        try:
            state=["off","on"]
            print("Range lock is {}. 0=Turn off / 1=Turn on".format(state[self._rangeLock]))
            i=input()
            assert i=="1" or i=="0"
        except Exception as err:
            print(err)
        else:
            if int(i):
                self._rangeLock=1
            else:
                self._rangeLock=0
            print("Range lock is {}".format(state[self._rangeLock]))
            
# =============================================================================
    def __getitem__(self,pos):
        try:
            if isinstance(pos,tuple):
                row,col=pos
                return self.matrix[row][col]
            elif isinstance(pos,int):
                return self.matrix[pos]
        except:
            print("Bad indeces")
            return None
        else:
            self.__rankCalc=0
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            
    def __setitem__(self,pos,item):
        try:
            if isinstance(pos,tuple) and (isinstance(item,complex) or isinstance(item,float) or isinstance(item,int)):
               
                if self._rangeLock and (item>self._inRange[1] or item<self._inRange[0]):
                    print("Out of the range given, unlock the rangeLock first")
                    return None
                
                row,col=pos
                self._matrix[row][col]=item
                self._inRange=self._declareRange(self._matrix)
                
            elif isinstance(pos,int) and isinstance(item,list):
                if len(item)==self.dim[1]:
                    
                    if self._rangeLock:
                        for items in item:
                            if items>self._inRange[1] or items<self._inRange[0]:
                                print("Out of the range given, unlock the rangeLock first")
                                return None
                    
                    row=pos
                    self._matrix[row]=item[:]
                    self._dim=self._declareDim()
                    self._inRange=self._declareRange(self._matrix)
                    
                else:
                    print("Check the dimension of the given list")
        except:
            print(pos,item)
            print("Bad indeces")
            return None
        else:
            self.__rankCalc=0
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            if __name__=="__main__":
                print(self)
            return self.matrix
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
                        total+=(self.matrix[r][cs]*other.matrix[cs][rs])
                    temp[r][rs]=total
            if isinstance(self,FMatrix) or isinstance(other,FMatrix):
                return FMatrix(dim=[self.dim[0],other.dim[1]],listed=temp)
            return Matrix(dim=[self.dim[0],other.dim[1]],listed=temp)
################################################################################    
    def __add__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]+other.matrix[rows][cols])
            except:
                print("Can't add")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
            
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]+other)
            except:
                print("Can't add") 
            else:
                if isinstance(self,FMatrix) or isinstance(other,float):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                
           
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]+other)
            except:
                print("Can't add") 
            else:
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                            
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]+other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't add")
################################################################################            
    def __sub__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]-other.matrix[rows][cols])
            except:
                print("Can't subtract")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
            
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]-other)
            except:
                print("Can't subtract") 
            else:
                if isinstance(self,FMatrix) or isinstance(other,float):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                
           
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]-other)
            except:
                print("Can't subtract") 
            else:
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                    
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]-other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't subtract")
################################################################################     
    def __mul__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]*other.matrix[rows][cols])
            except:
                print("Can't multiply")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
            
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]*other)
            except:
                print("Can't multiply") 
            else:
                if isinstance(self,FMatrix) or isinstance(other,float):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                 
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]*other)
            except:
                print("Can't multiply") 
            else:
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
            
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]*other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't multiply")
################################################################################
    def __floordiv__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]//other.matrix[rows][cols])
            except:
                print("Can't divide")
            else:
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]//other)
            except:
                print("Can't divide") 
            else:
                return Matrix(dim=self.dim,listed=temp)
                
           
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]//other)
            except:
                print("Can't divide") 
            else:
                return Matrix(dim=self.dim,listed=temp)
            
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]//other[d])
                    s+=1
                return Matrix(dim=self.dim,listed=temp)
            
        else:
            print("Can't divide")
################################################################################            
    def __truediv__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]/other.matrix[rows][cols])
            except:
                print("Can't divide")
            else:
                return FMatrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]/other)
            except:
                print("Can't divide") 
            else:
                return FMatrix(dim=self.dim,listed=temp)
                         
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]/other)
            except:
                print("Can't divide") 
            else:
                return FMatrix(dim=self.dim,listed=temp)
            
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]/other[d])
                    s+=1
                return FMatrix(dim=self.dim,listed=temp)
            
        else:
            print("Can't divide")
################################################################################
    def __mod__ (self, other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]%other.matrix[rows][cols])
            except:
                print("Can't modular")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
            
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]%other)
            except:
                print("Can't modular") 
            else:
                if isinstance(self,FMatrix) or isinstance(other,float):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                
           
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]%other)
            except:
                print("Can't modular") 
            else:
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                    
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]/other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't get modular")
################################################################################         
    def __pow__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]**other.matrix[rows][cols])
            except:
                print("Can't raise to the given power")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
            
                return Matrix(dim=self.dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]**other)
            except:
                print("Can't raise to the given power") 
            else:
                if isinstance(self,FMatrix) or isinstance(other,float):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
                
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't divide")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]/other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.dim,listed=temp)
                return Matrix(dim=self.dim,listed=temp)
        else:
            print("Can't raise to the given power")
################################################################################                    
    def __lt__(self,other):
        
        if self._valid:
            if self.dim==other.dim:
                print("Same dimension")
                if self.avg>other.avg:
                    print("Higher average!")
                    return False
                elif self.avg==other.avg:
                    print("Same matrices!")
                    return "Equal"
                else:
                    print("Lower average!")
                    return True
                
            elif self.dim[0]<other.dim[0] and self.dim[1]<other.dim[1]:   
                print("Lower dimension!")    
                return True
            else:
                print("Higher dimension!")
                return False
        print("Invalid")        
        return None
    
    def __eq__(self,other):
        
        if self._valid:
            if self._dim==other.dim:
                print("Same dimension")
                if self.avg==other.avg:
                    print("Same average")
                    if self.matrix==other.matrix:
                        print("All the elements and their positions are same!")
                        return True
                elif self.avg<other.avg:
                    print("Lower average!")
                    return False
                else:
                    print("Higher average!")
                    return False
            else:   
                print("Different dimensions!") 
                return False
        print("Invalid")        
        return None
    
    def __gt__(self,other):
        
        if self._valid:
            if self.dim==other.dim:
                print("Same dimension")
                if self.avg>other.avg:
                    print("Higher average!")
                    return True
                elif self.avg==other.avg:
                    print("Same matrices!")
                    return "Equal"
                else:
                    print("Lower average!")
                    return False
                
            elif self.dim[0]>other.dim[0] and self.dim[1]>other.dim[1]:   
                print("Higher dimension!")    
                return True
            else:
                print("Lower dimension!")
                return False
        print("Invalid")
        return None
    
    def __repr__(self):
        return str(self.matrix)
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        if self._valid and not self._fMat and not self._cMat and not self._isIdentity and self.avg!=None:
            if self._dim[0]!=self._dim[1]:
                print("\nDimension: {0}x{1}\nNumbers' range: {2}\nAverage: {3:.4f}".format(self._dim[0],self._dim[1],self.inRange,self.avg))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nNumbers' range: {1}\nAverage: {2:.4f}".format(self._dim[0],self.inRange,self.avg))
            return self._stringfy(self._dim)+"\n"
        else:
            return "Invalid matrix\n"
    
# =============================================================================

class Identity(Matrix):
    """
Identity matrix
    """
    def __init__(self,dim=[1,1]):
        self._dim=dim
        self._dimSet(self._dim)
        self._matrix=list()
        self._randomFill=0
        self._inRange=[0,1]
        self._valid=1
        self._fMat=0
        self._cMat=0
        
        self.__adjCalc=1
        self.__detCalc=1
        self.__invCalc=1
        
        if self.dim[0]==self.dim[1]:
            if self.dim[0]>0:
                self._isIdentity=1
        else:
            self._valid=0
            return None
        if self._isIdentity:
            self._matrix=self._zeroFiller(self._matrix)
            self._string=self._stringfy(self.dim)
                    
    def addDim(self,num):
        """
        Add dimensions to identity matrix
        """
        try:
            assert isinstance(num,int) and num>0
        except AssertionError:
            print("Enter a positive integer")
        except Exception as err:
            print(err)
        else:
            goal=self._dim[0]+num
            self._dim=[goal,goal]
            self._matrix=self._zeroFiller(list())
            self._string=self._stringfy(self.dim)
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
            print("Enter a valid input")
        except Exception as err:
            print(err)
        else:
            goal=self._dim[0]-num
            if goal==0:
                print("All rows have been deleted")
            self._dim=[goal,goal]
            self._matrix=self._zeroFiller(list())
            self._string=self._stringfy(self.dim)
            return self
        
    @property
    def inv(self):
        return Identity(dim=self._dim)
    @property    
    def det(self):
        return 1
    @property
    def adj(self):
        return Identity(dim=self._dim)
    
    def __str__(self):
        if self._isIdentity:
            print("\nIdentity Matrix\nDimension: {0}x{0}".format(self._dim[0]))
            return self._stringfy(self._dim)+"\n"
        
class FMatrix(Matrix):
    """
Matrix which contain float numbers
    """
    def __init__(self,*args,**a):
        super().__init__(*args,**a)
        self._valid=1
        self._fMat=1
        
    def __str__(self):
        if self._fMat:
            print("\nFloat Matrix",end="")
            if self._dim[0]!=self._dim[1]:
                print("\nDimension: {0}x{1}\nNumbers' range: {2}\nAverage: {3}".format(self._dim[0],self._dim[1],self._inRange,self.avg))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nNumbers' range: {1}\nAverage: {2}".format(self._dim[0],self._inRange,self.avg))
            
            return self._stringfy(self._dim)+"\n"
        
class CMatrix(FMatrix):
    """
Matrix which contain complex numbers
    """
    def __init__(self,*args,**a):
        super().__init__(*args,**a)
        self._valid=1
        self._cMat=1

    def __str__(self):
        if self._cMat:
            print("\nComplex matrix, ",end="")
            if self._dim[0]!=self._dim[1]:
                print("\nDimension: {0}x{1}\nNumbers' range: {2}\nAverage: {3}".format(self._dim[0],self._dim[1],self._inRange,self.avg))
            else:
                print("Square matrix\nDimension: {0}x{0}\nNumbers' range: {1}\nAverage: {2}".format(self._dim[0],self._inRange,self.avg))            
                
            return self._stringfy(self._dim)+"\n"
