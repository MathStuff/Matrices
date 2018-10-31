# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

import random as rd 

class Matrix(object):
    """Matrix object:
***Create matrices and print them as grids***
-dim:natural number, dimension of the matrix
-listed:(a list of integers | a string) with & dim**2 amount of integers
-inRange:list of 2 numbers
-rangeLock: wheter or not not to allow numbers out of given range
-randomFill: 
    ->1 to fill the matrix with random integers if no list is given
    ->0 to fill the matrix with empty lists 
-Works like square matrices
-Can contain integers only, dimension should be a squared integer:
    ->(dimension)**2==len(listofnumber | string of numbers)
    
-Additional rows and columns can be added with addRC(dimension amount),
    ->You can't add numbers out of the current range if rangeLock is enabled
    
    """
    def __init__(self,dim=[0,0],listed=[],inRange=[-125,125],rangeLock=0,randomFill=1):
        self.__dim=[0,0]
        self.__valid=1
        try:
                
            if isinstance(dim,list):
                self.__dim=dim[:]
                rows=dim[0]
                cols=dim[1]
                if rows<0 or cols<0: 
                    self.__valid=0  
                else:                              
                    self.__dim=[rows,cols]
                
            elif isinstance(dim,int):
                if dim<0:
                    self.__valid=0
                else:
                    self.__dim=[dim,dim]
    
                
            self.__inRange = inRange
            self.__randomFill = randomFill
            self.__rangeLock = rangeLock
            if len(inRange)!=2:
                self.__valid=0
            self.__listFill=0
                
        except Exception as err:
            print(err)
            print(Matrix.__doc__)
            
        else:
            if isinstance(listed,str):
                self.__valid=1
                self.__matrix=self.__listify(listed)
                self.__inRange=self.__declareRange(self.__matrix)
                self.__avg=self.__avg()
               
            elif self.__validateList(listed) and self.__valid:
                    self.__temp1=[a[:] for a in listed]
                    
                    if len(self.__temp1)>0:
                            self.__matrix = self.__temp1.copy()
                            self.__inRange=self.__declareRange(self.__matrix)
                            self.__dim=self.__declareDim() 
                            self.__string=self.__stringfy(self.__dim)     
                    elif len(self.__temp1)==0:
                        
                        if dim==0 or dim==[0,0] or not randomFill:
                            self.__matrix=self.__zeroFiller(self.__temp1)
                            self.__listFill=1
                            
                        elif randomFill:
                            self.__matrix=self.__randomFiller(self.__temp1)
                            self.__inRange=self.__declareRange(self.__matrix)
                            self.__dim=self.__declareDim() 
                            self.__string=self.__stringfy(self.__dim) 
                                      
                    self.__avg=self.__avg()

# =============================================================================
    def __declareDim(self):
        """
        Checks if the given number is a perfect square
        Returns the integer found, if none found returns 0
        """
        rows=0
        cols=0
        for row in self.__matrix:
            rows+=1
            cols=0
            for ele in row:
                cols+=1
        if rows!=cols:
            return [rows,cols]
        return [cols,cols]
    
    def __validateList(self,alist):
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
                
                self.__dim=l[0]
                return True
            else:
                return True
        return False
    
    def __declareRange(self,lis):
        """
        Finds and returns the range of the elements in a given list
        """
        try:
            low=0
            high=0
            looped=0
            for row in self.__matrix:
                for element in row:
                    if not looped:
                        low=element
                        looped=1
                    elif element<low:
                        low=element
                    elif element>high:
                        high=element
                        
        except Exception as err:
            print("range error")
            #print(Matrix.__doc__)
            return [self.inRange[0],self.inRange[1]]
        else:
            return [low,high]
   
# =============================================================================  
            
    def __listify(self,string,square=1):
        """
        Finds all the positive and negative numbers in the given string
        Tries to fit the numbers into a grid shape
        Returns a list in a form of a square matrix
        """
#        try:
        gridNum=""
        numbers=["0","1","2","3","4","5","6","7","8","9"]
        l=len(string)
        
        list1=list()
        negative=0
        
        for c in range(0,l):
            #print("c:{0} neg:{1} str:{2} num:{3}".format(c,negative,string[c],gridNum))
            #print("list:",list1)
            if string[c] in numbers:
                gridNum+=string[c]
                if c==l-1:
                    if negative:
                        list1.append(int(gridNum)*-1)
                        negative=0
                    else:
                        list1.append(int(gridNum))

            elif string[c]=="-":
                
                if len(gridNum)>0:
                    list1.append(int(gridNum))
                    gridNum=""
                negative=1  
            
            elif string[c]=="\n":
                if negative:
                    list1.append(int(gridNum)*-1)
                    negative=0
                else:
                    list1.append(int(gridNum))
                if not square:
                    list1.append("\n")
                gridNum=""
                    
            else:
                if len(gridNum)>0:
                    if negative:
                        list1.append(int(gridNum)*-1)
                        negative=0
                    else:
                        list1.append(int(gridNum))
                    gridNum=""
       
        l1=len(list1)
        l=l1**0.5
        d=0
        for integer in range(1,25):
            if integer==l:
                 d=integer

        if self.__dim==[0,0]:
            self.__dim=[d,d]
        assert l1==int((d)**2)

        self.__temp1=list1
        list2=list()
        list2=self.__zeroFiller(list2)
        temp=0
 
        if square:
            for rows in range(0,self.__dim[0]):
                
                for i in range(temp,self.__dim[1]+temp):
                    list2[rows].append(list1[i])
                temp+=self.__dim[1]  

            assert len(list2)==self.__dim[0]
        
#        except Exception as err:
#            print("****List error****\nMake sure string:\n-Has positive integers only \n-Has a squared integer amount of numbers:(0-1-4-9...n^2)\n-Have 1 space splitting the elements")
#            print(Matrix.__doc__)
#        else:
        return list2
    
    def __stringfy(self,dm):
        """
        Turns a square matrix shaped list into a grid-like form that is printable
        Returns a string
        """
        def __digits(num):
            num=int(num)
            dig=1
            
            if num<=0:
                num=num*-1
                dig+=1
                
            while num>0:
                dig+=1
                num=num//10
                
            return dig
        
        if self.__randomFill==0 and self.__listFill==1:
            print(repr(self))
            return ""
        else:
            string=""
            l=__digits(self.__inRange[0])
            h=__digits(self.__inRange[1])
            s=max([h,l])
            d=dm[:]
            
            if d[0]>0 and d[1]>0:
                for i in range(0,d[0]):
                    string+="\n"
                    for j in range(0,d[1]):
                        a=str(self.__matrix[i][j])
                        f=__digits(a)
                        string += " "*(s-f)+a+" "             
            return string
# =============================================================================

    def __zeroFiller(self,lis):
        """
        Fills the matrix with empty lists
        """
        if self.__dim[0]>0:
            for rowfill in range(0,self.__dim[0]):
                lis.append(list())

        return lis
    
    def __randomFiller(self,lis):
        """
        Fill the matrix with random integers from given range
        """
        try:
            assert len(self.__inRange)==2 and self.__inRange[0]!=self.__inRange[1]
        except AssertionError:
            print("Bad argument for inRange parameter!")
            print(Matrix.__doc__)
        except Exception as err:
            print(err)
            print(Matrix.__doc__)
        else:
            
            if  self.__randomFill:
                
                lis=self.__zeroFiller(lis)
                m,n=max(self.__inRange),min(self.__inRange)
                d=self.__dim[:]
                for row in range(0,d[0]):
                    for column in range(0,d[1]):
                        lis[row].append(rd.randint(n,m))

            return lis
        
# =============================================================================
            
    def addRC(self,row,col):
        """
        row: natural number <100
        col: natural number <100
        Add row amount of rows and col amount of cols to the matrix from user input one integer at a time
        Starts from the first row's last column
        """
        try:
            #Keep a copy of the old matrix
            temp=[a[:] for a in self.__matrix]
            assert row>0 and col>0 and row<100 and col<100 and self.__valid==1
            d=self.__dim[:]
            goal = [d[0] + row,d[1] + col]
            dif= goal[0]*goal[1]-d[0]*d[1]
            
            print("\nDimension: {0}x{1}\nNumbers' range: {2}".format(self.__dim[0],self.__dim[1],self.__inRange))
            print("You have to enter {} integers to the matrix!".format(dif)) 
            
            a=self.__dim>[0,0]
            
            if a:
                column=self.__dim[1]+1
                for row in range(0,goal[0]):
                    if row>=self.__dim[0]:
                        print("You are entering a new row")
                        self.__matrix.append(list())
                        
                        for col in range(0,goal[1]):
                            print(row,col)
                            gettingInput=1
                            print(self.__matrix)
                            print("Enter an integer in range:[{}]".format(self.__inRange))
                            
                            while gettingInput:
                                
                                inp=int(input("Row:{}, Column:{} = ".format(row+1,col+1)))
                                if self.__rangeLock:
                                    
                                    if inp<=self.__inRange[1] and inp>=self.__inRange[0]:
                                        self.__matrix[row].append(inp)
                                        gettingInput=0
                                    else:
                                        print("Out of range!")
                                        
                                else:
                                    self.__matrix[row].append(inp)
                                    print(self.__matrix)
                                    gettingInput=0
                            
                    elif row<self.__dim[0]:
                        gettingInput=self.__dim[1]
                       
                        while gettingInput<goal[1]:
                            print(self.__matrix)
                            print("Enter an integer in range:[{}]".format(self.__inRange))
                            inp=int(input("Row:{}, Column:{} = ".format(row+1,column)))
                            if self.__rangeLock:
                                if inp<=self.__inRange[1] and inp>=self.__inRange[0]:
                                    self.__matrix[row].append(inp)
                                    gettingInput+=1
                                    column+=1
                                else:
                                    print("Out of range!")
                            else:
                                self.__matrix[row].append(inp)
                                gettingInput+=1
                                column+=1
                                
            else:
                
                for row in range(0,goal[0]) :

                    column=self.__dim[1]+1 
                    self.__matrix.append(list())
                    
                    for col in range(0,goal):
                        gettingInput=1
                        print(self.__matrix)
                        print("Enter an integer in range:[{}]".format(self.__inRange))
                        
                        while gettingInput:
                            inp=int(input("Row:{}, Column:{} = ".format(row+1,column)))
                            if self.__rangeLock:
                                if inp<=self.__inRange[1] and inp>=self.__inRange[0]:
                                    self.__matrix[row].append(inp)
                                    gettingInput=0
                                    column+=1
                                else:
                                    print("Out of range!")
                            else:
                                self.__matrix[row].append(inp)
                                gettingInput=0
                                column+=1
                                
        except Exception as err:
            print("error")
            print(Matrix.__doc__,"\n")
            if self.__valid:
                self.__matrix=temp
                print("Current grid:\n",self.__matrix)
                print(err)   
            else:
                return "Invalid matrix"
                
            
        else:
            print("Addition was successfully completed!\n")
            print("Old grid:\n",temp)
            self.__dim=goal[:]
            self.__valid=1
            self.__stringfy(self.__dim)
            self.__inRange=self.__declareRange(self.__matrix)   
            print("\nNew grid:\n",self.__matrix)
            
    def delRC(self,r,c):
        pass

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
            assert r<=self.__dim[0] and c<=self.__dim[1] and r>0 and c>0
        except AssertionError:
            print("\tBad arguments!\n",self.get.__doc__)
        else:
            return self.__matrix[r-1][c-1]
        
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
#         if self.__valid:
#             tempM=[a[:] for a in self.__matrix]
#             if row==0:
#                 row=[0,self.__dim]
#             if column==0:
#                 column=[0,self.__dim]
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
    
    def sub(self,rowStart=1,rowEnd=1,colStart=1,colEnd=1):
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
            ->a.sub(1,1)==
        ***Returns a new grid class/matrix***
        """
        try:
            assert (rowStart,rowEnd,colStart,colEnd)>(0,0,0,0)
            if rowStart+rowEnd+colStart+colEnd-2==rowStart+colStart:
                pass
            temp=self.__matrix[rowStart-1:rowEnd]
            temp2=[]
            for cols in range(len(temp)):
                temp2.append(temp[cols][colStart-1:colEnd])
        except AssertionError:
            print("Enter a number in range and higher than 0")
        except Exception as err:
            print(err)
        else:
            return Matrix(listed=temp2)
    
    def __avg(self):
        """
        Sets the avg attribute of the matrix as the average of it's elements
        """
        d=self.__dim
        if d==0 or d==[0,0] or self.__listFill:
            return "None"
        total=0
        for row in self.__matrix:
            for ele in row:
                total+=ele
                
        return total//(d[0]*d[1])
# =============================================================================
    """Properties available for public"""               
# =============================================================================
    @property
    def string(self):
        return self.__string
    @property
    def dim(self):
        return self.__dim
    @property
    def inRange(self):
        return self.__inRange
    @property
    def matrix(self):
       return self.__matrix
    @property
    def avg(self):
        return self.__avg
    @property
    def highest(self):
        return self.__inRange[1]
    @property
    def lowest(self):
        return self.__inRange[0]      
        
    def rangeLock(self):
        try:
            state=["off","on"]
            print("Range lock is {}. 0=Turn off / 1=Turn on".format(state[self.__rangeLock]))
            i=input()
            assert i=="1" or i=="0"
        except Exception as err:
            print(err)
        else:
            if int(i):
                self.__rangeLock=1
            else:
                self.__rangeLock=0
            print("Range lock is {}".format(state[self.__rangeLock]))
            
# =============================================================================
    def __lt__(self,other):
        
        if self.__valid:
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
                
            if self.__dim>other.dim:   
                print("Higher dimension!")    
                return False
            else:
                print("Lower dimension!")
                return False
        print("Invalid")        
        return None
    
    def __eq__(self,other):
        
        if self.__valid:
            if self.__dim==other.dim:
                print("Same dimension")
                if self.avg==other.avg:
                    print("And same average!")
                    if self.matrix==other.matrix:
                        print("All the elements and their positions are same!")
                return True
            else:   
                print("Different dimensions!") 
                return False
        print("Invalid")        
        return None
    
    def __gt__(self,other):
        
        if self.__valid:
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
                
            if self.__dim>other.dim:   
                print("Higher dimension!")    
                return True
            else:
                print("Lower dimension!")
                return False
        print("Invalid")
        return None
    
    def __repr__(self):
        if self.__valid:
            return """Matrix(
dim={0},
listed={1},
inRange={2},
rangeLock={3},
randomFill={4}
)""".format(self.__dim,self.__matrix,self.__inRange,self.__rangeLock,self.__randomFill)
        else:
            return "Invalid matrix"
        
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        if self.__valid:
            print("\nDimension: {0}x{1}\nNumbers' range: {2}".format(self.__dim[0],self.__dim[1],self.__inRange))

            if self.__listFill==0:
                return self.__stringfy(self.__dim)+"\n"
            else:
                return str(self.__matrix)+"\n"
        else:
            return "Invalid matrix\n"
    
# =============================================================================



