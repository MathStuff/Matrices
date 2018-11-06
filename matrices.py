# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

from random import randint 
from time import sleep

class Matrix(object):
    """Matrix object:
***Create matrices and print them as grids***
***Use this if and only if you are going to work with integers. Use fMatrix class to use float values***

-dim:dimension of the matrix;natural numbers as [rows,cols],if and integer given, matrix will be a square matrix 
-listed:(a list of integers | a string) with & dim**2 amount of integers
-inRange:list of 2 numbers
-rangeLock: wheter or not not to allow numbers out of given range
-randomFill: 
    ->1 to fill the matrix with random integers if no list is given
    ->0 to fill the matrix with 0s
    
-Giving ~300< elements may make grid look terrible, adjust your terminal size to display it better
-Can contain integers only 

-Additional rows and columns can be added with addRC(row,col)
-Rows and cols from right and bottom can be deleted with delRC
-Sub-matrices can be obtained with "sub" method
-Specific elements of the matrix can be obtained by using "get" method   

-Average of the all given elements can be seen with "avg" property
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
    """
    def __init__(self,dim=-1,listed=[],inRange=[-125,125],rangeLock=0,randomFill=1):
        
        self._valid = 1
        self._isIdentity=0
        
        if not self._isIdentity:
            if dim==-1:
                self._dim = [0,0]
            else:
                self._dim = dim
            self._matrix = []     
            self._inRange = inRange
            self._randomFill = randomFill
            self._rangeLock = rangeLock
            
        try:
            self._dimSet(dim)    
            if len(inRange)!=2:
                self._valid=0
            
                
        except Exception as err:
            print(err)
            print(Matrix.__doc__)
            
        else:
            if isinstance(listed,str) and not self._isIdentity:
                self._valid=1
                self._matrix=self._listify(listed)
                self._dim=self._declareDim()
                if not self._rangeLock:
                    self._inRange=self._declareRange(self._matrix)

               
            elif self._validateList(listed) and self._valid and not self._isIdentity:
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
            
            self._avg=self._average()
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
        Checks if the given number is a perfect square
        Returns the integer found, if none found returns 0
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
                    if max(l)!=min(l):
                        return False
                
                self._dim=l[0]
                return True
            else:
                return True
        return False
    
    def _declareRange(self,lis):
        """
        Finds and returns the range of the elements in a given list
        """
        try:
            low=0
            high=0
            looped=0
            for row in self._matrix:
                if isinstance(row,list):
                    for element in row:
                        if not looped:
                            low=element
                            high=element
                            looped=1
                        elif element<low:
                            low=element
                        elif element>high:
                            high=element
                else:
                    if not looped:
                        low=row
                        high=row
                        looped=1
                    elif row<low:
                        low=row
                    elif row>high:
                        high=row
                        
        except Exception as err:
            print("range error")
            #print(Matrix.__doc__)
            return [self.inRange[0],self.inRange[1]]
        else:
            return [low,high]
   
# =============================================================================  
    def _writeOver(self,clear):
        """
        Clears the terminal if clear is set to anything==bool(True)
        """
        if clear:
            print("\f","\n")
            
        print("\n")
        for i in range(6):
            for j in range(6):
                for k in range(6):
                    sleep(0.0001)
        print("\n")

        
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
            print("****List error****\nMake sure string:\n-Has positive integers only \n-Has a squared integer amount of numbers:(0-1-4-9...n^2)\n-Have 1 space splitting the elements")
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
                #print("Couldn't create a square matrix with given input ")
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
                    #print("using given dimension")
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
            num=int(num)
            dig=1
            
            if num<=0:
                num=num*-1
                dig+=1
                
            while num>0:
                dig+=1
                num=num//10
                
            return dig
    
        string=""
        if self._isIdentity:
            l=1
            h=1
        else:
            l=_digits(self._inRange[0])
            h=_digits(self._inRange[1])
        s=max([h,l])
        d=self._dim[:]
        if d[0]>0 and d[1]>0:
            for i in range(0,d[0]):
                string+="\n"
                for j in range(0,d[1]):
                    a=str(self._matrix[i][j])
                    f=_digits(a)
                    string += " "*(s-f)+a+" "             
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
                        lis[row].append(randint(n,m))

            return lis
        
# =============================================================================
            
    def addRC(self,row=None,col=None):
        """
        row: natural number <100
        col: natural number <100
        Add row amount of rows and col amount of cols to the matrix from user input one integer at a time
        Starts from the first row's last column
        """
        try:
            if self._isIdentity:
                print("Can't add to identity matrix.\nUse addDim instead!")
                return None
            ###############
            #Valide the matrix and determine wheter or not it has any elements
            ###############
            loop=1
            valid=1
            VAL=[len(ele) for ele in self._matrix]
            for lengths in VAL:
                if loop==1:
                    l=lengths
                elif l!=lengths:
                    valid=0
                    print("Not valid")
            a=self._dim>[0,0]
            ###############
            
            #Keep a copy of the old matrix
            temp=[a[:] for a in self._matrix]
            
            ###############
            #Validate and adjust given arguments
            ###############
            
            if row==None and col!=0:
                row=col
                goal=[self.dim[0]+row,self.dim[1]+col]
            elif col==None and row!=0:
                col=row
                goal=[self.dim[0]+row,self.dim[1]+col]
            elif (row,col)==(0,0):
                print("Nothing to add!")
                return None
            
            assert row>=0 and col>=0 and row<100 and col<100 and self._valid==1
            
            ###############  
            #Set hoal dimension and calculate how many integers will be needed
            ###############
            d=self._dim[:]
            goal = [d[0] + row,d[1] + col] 
            dif= goal[0]*goal[1]-d[0]*d[1]
            print("Current dim: ",self._dim,"\nGoal dim: ",goal)
            print("\nDimension: {0}x{1}\nNumbers' range: {2}".format(self._dim[0],self._dim[1],self._inRange))
            print("You have to enter {} integers to the matrix!".format(dif)) 
            ###############
            
            ###############
            #If matrix is not empty and valid
            ###############
            if a and valid:
                ###############
                #Start the loop from the first rows end
                ###############
                for Nrow in range(0,goal[0]):
                    column=self._dim[1]+1
                    print(self.matrix)
                    #print(goal)
                    #print(self.dim)
                    #If user completed adding to the existing rows
                    if Nrow>=self._dim[0]:
                        #Add a new row
                        self._matrix.append(list())
                        #Keep getting input until desired column dimension reached
                        gotFirstInput=0
                        for Ncol in range(0,goal[1]):
                            gettingInput=1
                            
                            while gettingInput:
                                
                                #Clear the terminal/console
                                self._writeOver(gotFirstInput)
                                if not gotFirstInput:
                                    print("You are entering a new row")
                                #If the input range is given strictly
                                if self._rangeLock:
                                    print("Enter an integer in range:[{}]".format(self._inRange))
                                #If range is (-NaN,NaN)
                                try:
                                    print(self._matrix)
                                    #Get input
                                    inp=int(input("Row:{}, Column:{} = ".format(Nrow+1,Ncol+1)))
                                    #If range is locked check validaty of the input
                                    if self._rangeLock:
                                        if inp<=self._inRange[1] and inp>=self._inRange[0]:
                                            self._matrix[Nrow].append(inp)
                                            gotFirstInput=1
                                            gettingInput=0
                                        else:
                                            print("Out of range!")
                                            
                                    else:
                                        #If input is valid add it to the end of the row
                                        self._matrix[Nrow].append(inp)
                                        gettingInput=0
                                        gotFirstInput=1
                                except:
                                    print("Bad input")
                                    
                    elif Nrow<self._dim[0]:
                        #Loop to get inputs for the existed rows
                        gettingInput=self._dim[1]
                       
                        while gettingInput<goal[1]:
                            #Clear the window
                            self._writeOver(1)
                            #If range is locked
                            if self._rangeLock:
                                print("Enter an integer in range:[{}]".format(self._inRange))
                            try:
                                print(self._matrix)
                                #Get input
                                inp=int(input("Row:{}, Column:{} = ".format(Nrow+1,column)))
                                #If range is locked check validaty of the input
                                if self._rangeLock:
                                    if inp<=self._inRange[1] and inp>=self._inRange[0]:
                                        self._matrix[Nrow].append(inp)
                                        gettingInput+=1
                                        column+=1
                                    else:
                                        print("Out of range!")
                                else:
                                    #If number is valid add it to the end of the row
                                    self._matrix[Nrow].append(inp)
                                    gettingInput+=1
                                    column+=1
                            except:
                                print("Bad input")
                                
            elif valid:
                #If there is no elements in the matrix create rows and get input
                for rows in range(0,goal[0]) :

                    column=self._dim[1]+1 
                    self._matrix.append(list())
                    
                    #Loop desired column dimension times and get input 
                    for cols in range(0,goal[1]):
                        gettingInput=1
                                  
                        while gettingInput:
                            #Clear the screen
                            self._writeOver(1)
                            
                            #If range is locked
                            if self._rangeLock:
                                print("Enter an integer in range:[{}]".format(self._inRange))
                            try:
                                print(self._matrix)
                                #Get input
                                inp=int(input("Row:{}, Column:{} = ".format(rows+1,column)))
                                #Check validaty if range is locked
                                if self._rangeLock:
                                    if inp<=self._inRange[1] and inp>=self._inRange[0]:
                                        self._matrix[rows].append(inp)
                                        gettingInput=0
                                        column+=1
                                    else:
                                        print("Out of range!")
                                else:
                                    #Add the input to the row if it's valid
                                    self._matrix[rows].append(inp)
                                    gettingInput=0
                                    column+=1
                            except:
                                print("Bad input")
        ##############
        #Handle errors
        ##############
        except Exception as err:
            print("error")
            print(Matrix.__doc__,"\n")
            #Return the saved matrix if something goes wrong
            if self._valid:
                self._matrix=temp
                print("Current grid:\n",self._matrix)
                print(err)   
            else:
                return "Invalid matrix"
                
            
        else:
            #If nothing was added
            if row==0 and col==0:
                print("Nothing was added!")
            else:
            #If everything goes right change attributes to new ones
                self._dim=goal[:]
                self._valid=1
                if not self._rangeLock:
                    self._inRange=self._declareRange(self._matrix)   
                print("Addition was successfully completed!\n")
                print("Old grid:\n",self._stringfy(d))
                print("\nNew grid:\n",self._stringfy(self._dim))
                self._string=self._stringfy(self._dim) 
            return self._matrix
        
    def delRC(self,r=None,c=None):
        """
Deletes rows and columns from the right and bottom side
Removes r amount of rows and c amount of columns
If only 1 argument "n" is given:
    ->IF n==rows XOR n==columns:
        ~Subtracts a nxn dimension matrix from the left(if n==rows) or bottom(if n==columns)
    ->IF n<rows and n<colums:
        ~Deletes n amount of rows and columns from right and bottom
    ->IF n==rows==cols:
        ~Deleted all the elements
Applies changes on the current matrix also returns the new matrix created 
Use sub method if you want to get a new matrix
        """
        
        try:
            if self._isIdentity:
                print("Can't delete from the identity matrix.\nUse delDim instead!")
                return None
            ###############
            if r==None and c!=0:
                r=c
            elif c==None and r!=0:
                c=r
            elif (r,c)==(0,0) or (r,c)==(None,None):
                print("Nothing to delete!")
                return None
            dim=self._dim[:]
            temp=[a[:] for a in self._matrix]
            assert (r>=0 or r==None) and (c>=0 or c==None) and r<=dim[0] and c<=dim[1] and self._valid==1
            goal=[dim[0] - r,dim[1] - c]
            if goal[0]==0 and goal[1]!=0:
                goal[0]=r
                r*=-1
            elif goal[1]==0 and goal[0]!=0:
                goal[1]=c
                c*=-1
            print("Current dimension: ",dim)
            print("Goal dimension: ",goal)
            ############### 
        except Exception as err:
            self._matrix=temp
            print(err)
            print(self.delRC.__doc__)
        else:   
            if goal==[0,0]:
                print("All elements have been deleted")
                self._matrix=[]
                
            else:
                tempMat=[]
                for rows in self._matrix[:-r]:
                    tempMat.append(rows[:-c])
                print("Old grid:\n",self._stringfy(dim))    
                self._matrix=[a[:] for a in tempMat]
                self._inRange=self._declareRange(self._matrix)
                self._dim=goal[:]
                print("\nNew grid:")
                self._string=self._stringfy(self._dim) 
            return self
        
    def determinant(self):
        pass
    
    def get(self,r,c):
        """
        Returns the desired element
        r:row of the element
        c:column of the element
        r and c can be ranged from 1 to the matrix's dimension
        """
        try:
            r=int(r)
            c=int(c)
            assert r<=self._dim[0] and c<=self._dim[1] and r>0 and c>0
        except AssertionError:
            print("\tBad arguments!\n",self.get.__doc__)
        else:
            return self._matrix[r-1][c-1]
        
    def operateOver(self,operate="mul",result=0,row=0,column=0,direction=0,adjlen=0):
        """
        Do calculations over the elements without changing them
        
        operate:
            ->add=addition
            ->mul=multiplication
        result:
            (default)->0=get all the results calculated
            ->"mn"=get the lowest of results
            ->"mx"=get the highest of results
            ->"avg"=get the average of results
            ->"pos"=get the results which are negative
            ->"neg"=get the results which are negative
        
        Change row,column parameters only to operate over sub matrices
        row:list of which rows to operate on
        
            *Ranged in [1,dimension]    
            (default)->0=all rows
        column:list of which columns to operate on
            *Ranged in [1,dimension]
            (default)->0=all columns
            
        direction:lists of which direction to iterate through
            ->"hor"=horizontally
            ->"ver"=vertically
            *Diagonally(Requires row|col>=2)
                ->"ltrb"=diagonally LeftTop-RightBottom
                ->"lbrt"=diagonally LeftBottom-RightTop
                ->"dia"=both ways
            (default)->0=all directions possible(diagonal,vertical,horizontal)
            
        adjlen:how many elements to operate together at once=
            (default)->0=Highest possible
            ->"a"=all possible lengths [1-dimension]
        
        EXAMPLE: a.operateOver(operate="add",result="mx",row[1,2])
        
        Returns a number or a list,depends on input
        """
# =============================================================================
#         if self._valid:
#             tempM=[a[:] for a in self._matrix]
#             if row==0:
#                 row=[0,self._dim]
#             if column==0:
#                 column=[0,self._dim]
#             if direction==0:
#                 dirs=[""]
#         
# =============================================================================
        pass
        
    def operateOn(self):
        """
        Do changes on elements
        """
        pass
    
    def sub(self,rowS=None,rowE=None,colS=None,colE=None):
        """
Get a sub matrix from the current matrix
rowStart:Desired matrix's starting row (starts from 1)
rowEnd:Last row(included)
colStart:First column
colEnd:Last column(included)
    |col1 col2 col3
    |---------------
row1|1    2    3
row2|4    5    6
row3|7    8    9

EXAMPLES:
    ->a.sub(1)==gets the first element of the first row
    ->a.sub(2,2)==2by2 square matrix from top left as starting point
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
            print(self.sub.__doc__)
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
                return Matrix(listed=temp2)

    
    def _average(self):
        """
        Sets the avg attribute of the matrix as the average of it's elements
        """
        try:
            d=self._dim[:]
            if d==[0,0]:
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
            return total//(d[0]*d[1])
# =============================================================================
    """Properties available for public"""               
# =============================================================================
    @property
    def string(self):
        return self._string
    @property
    def dim(self):
        return self._dim
    @property
    def inRange(self):
        if not self._isIdentity:
            return self._inRange
        else:
            return [0,1]
    @property
    def matrix(self):
       return self._matrix
    @property
    def avg(self):
        if not self._isIdentity:
            return self._average()
        else:
            return 0
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
        if self._valid and not self._isIdentity:
            return "Matrix(dim={0},listed={1},inRange={2},rangeLock={3},randomFill={4})".format(self._dim,self._matrix,self._inRange,self._rangeLock,self._randomFill)
        elif self._valid and self._isIdentity:
            return "Identity(dim={0},listed={1},inRange=[0,1],rangeLock=1,randomFill=0)".format(self._dim,self._matrix)
        else:
            return None
        
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
            return temp
################################################################################        
    def __add__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]+other.matrix[rows][cols])
                return temp
                
            except:
                print("Can't add")
        elif isinstance(self,Matrix) and isinstance(other,int):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]+other)
                return temp
                
            except:
                print("Can't add")            
        elif isinstance(self,int) and isinstance(other,matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]+other)
                return temp
            except:
                print("Can't add")
        else:
            print("Can't add")
################################################################################            
    def __sub__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]-other.matrix[rows][cols])
                return temp
                
            except:
                print("Can't subtract")
        elif isinstance(self,Matrix) and isinstance(other,int):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]-other)
                return temp
                
            except:
                print("Can't subtract")            
        elif isinstance(self,int) and isinstance(other,matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]-other)
                return temp
            except:
                print("Can't subtract")
        else:
            print("Can't subtract")
            
################################################################################     
    def __mul__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]*other.matrix[rows][cols])
                return temp
                
            except:
                print("Can't multiply")
        elif isinstance(self,Matrix) and isinstance(other,int):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]*other)
                return temp
                
            except:
                print("Can't multiply")            
        elif isinstance(self,int) and isinstance(other,matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]*other)
                return temp
            except:
                print("Can't multiply")
        else:
            print("Can't multiply")
            
################################################################################
    def __floordiv__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]//other.matrix[rows][cols])
                return temp
                
            except:
                print("Can't divide")
        elif isinstance(self,Matrix) and isinstance(other,int):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]//other)
                return temp
                
            except:
                print("Can't divide")            
        elif isinstance(self,int) and isinstance(other,matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]//other)
                return temp
            except:
                print("Can't divide")
        else:
            print("Can't divide")
################################################################################            
    def __truediv__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]/other.matrix[rows][cols])
                return temp
                
            except:
                print("Can't divide")
        elif isinstance(self,Matrix) and isinstance(other,int):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]/other)
                return temp
                
            except:
                print("Can't divide")            
        elif isinstance(self,int) and isinstance(other,matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]/other)
                return temp
            except:
                print("Can't divide")
        else:
            print("Can't divide")
################################################################################
    def __mod__ (self, other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]%other.matrix[rows][cols])
                return temp
                
            except:
                print("Can't get modular")
        elif isinstance(self,Matrix) and isinstance(other,int):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]%other)
                return temp
                
            except:
                print("Can't get modular")            
        elif isinstance(self,int) and isinstance(other,matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]%other)
                return temp
            except:
                print("Can't get modular")
        else:
            print("Can't get modular")
################################################################################         
    def __pow__(self,other):
        try:
            assert self.dim==other.dim
        except:
            print("Can't divide")
        else:
            temp=[]
            for rows in range(self.dim[0]):
                temp.append(list())
                for cols in range(self.dim[1]):
                    temp[rows].append(self.matrix[rows][cols]**other.matrix[rows][cols])
            return temp
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
        if self._valid and not self._isIdentity:
            if self._dim[0]!=self._dim[1]:
                print("\nDimension: {0}x{1}\nNumbers' range: {2}\nAverage: {3}".format(self._dim[0],self._dim[1],self._inRange,self.avg))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nNumbers' range: {1}\nAverage: {2}".format(self._dim[0],self._inRange,self.avg))
            return self._stringfy(self._dim)+"\n"
        elif self._isIdentity:
            print("\nIdentity Matrix\nDimension: {0}x{0}".format(self._dim[0]))
            return self._stringfy(self._dim)+"\n"
        else:
            return "Invalid matrix\n"
    
# =============================================================================

class Identity(Matrix):
    def __init__(self,dim=[1,1]):
        self._dim=dim
        self._dimSet(self._dim)
        self._valid=1
        self._matrix=list()
        self._randomFill=0
        if self.dim[0]==self.dim[1]:
            if self.dim[0]>0:
                self._isIdentity=1
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
            
