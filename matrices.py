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
-randomFill: 
    ->1 to fill the matrix with random integers if no list is given
    ->0 to fill the matrix with 0s
-ranged: 2 numbers as a list, to determine the upper and lower bound of the random elements    
-Giving ~300< elements may make grid look terrible, adjust your terminal size to display it better
-Can contain integers only (Unless it's a FMatrix class) 

-Elements/row can be changed in place ( Current not available on columns )
-Additional rows and columns can be added with add(row,col,lis)
-Rows and cols from right and bottom can be deleted with del
-Sub-matrices can be obtained with "subM" method
-Get specific items by using a[i][j] for the (i+1)th row and (j+1)th column   

-Average of the all colums can be seen with "avg" property
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
    def __init__(self,dim=None,listed=[],directory="",header=0,ranged=[-5,5],randomFill=1):
        self._isIdentity=0
        self._fMat=0
        self._cMat=0
        self._valid = 1
        
        if isinstance(self,FMatrix):
            self._fMat=1
        elif isinstance(self,CMatrix):
            self._cMat=1
        elif isinstance(self,Identity):
            self._isIdentity=1
            return self

        if not self._isIdentity:
            if dim==None:
                self.__dim=[0,0]
            else:
                self._dimSet(dim)             
            #Attributes    
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            self.__rankCalc=0    
            self._matrix = []     
            self._initRange = ranged
            self._randomFill = randomFill
            self._string=""
            self._dir=directory
            self._header=header
        if self._valid:
##########################################################################################################                
            if isinstance(listed,str):
                try:
                    self._matrix=self._listify(listed,self._header)
                    self.__dim=self._declareDim()
                    self._inRange=self._declareRange(self._matrix)
                    self._string=self._stringfy()
                except Exception as err:
                    print(err)
                    self._valid=0
                    return None
                else:
                    self._valid=1
##########################################################################################################                        
            elif len(directory)>0:
                try:
                    lis=self.__fromFile(directory)
                    if not lis==None:
                        self._matrix=self._listify(lis,self._header)
                        self.__dim=self._declareDim()
                        self._inRange=self._declareRange(self._matrix)
                        self._string=self._stringfy()
                    else:
                        raise Exception
                except Exception as err:
                    print(err)
                    self._valid=0
                    return None
                else:
                    self._valid=1
##########################################################################################################                    
            elif self._validateList(listed):
                try:
                    self.__temp1=[a[:] for a in listed]
                    
                    if len(self.__temp1)>0:                        
                            self._matrix = self.__temp1.copy()  
                            self._inRange=self._declareRange(self._matrix)
                            self.__dim=self._declareDim()
                            self._string=self._stringfy()   
                            
                    elif len(self.__temp1)==0 and dim!=[0,0]:
                        if not self._randomFill:
                            self._matrix=self._zeroFiller(self.__temp1)
                            self._inRange=self._declareRange(self._matrix)
                            
                        elif self._randomFill:
                            self._matrix=self._randomFiller(self.__temp1)
                            self._inRange=self._declareRange(self._matrix)
                            self.__dim=self._declareDim() 
                            self._string=self._stringfy()
                    else:
                        self._valid=0
                        return None
                except Exception as err:
                    print(err)
                    self._valid=0
                    
                else:
                    self._valid=1

##########################################################################################################
            else:
                self._valid=0
                return None
        else:
            return None
        
# =============================================================================
            
    def _dimSet(self,dim):        
        """
        Change the given dimension's format to a list if it's a valid integer.
        """
        if isinstance(dim,list):
            if len(dim)!=2:
                self._valid=0
                self.__dim=[0,0]
                print("Bad dimension argument")
                return None
            self.__dim=dim[:]
            rows=dim[0]
            cols=dim[1]
            if rows<=0 or cols<=0: 
                self._valid=0
                self.__dim=[0,0]
            else:                              
                self.__dim=[rows,cols]
            
        elif isinstance(dim,int):
            if dim<=0:
                self._valid=0
                self.__dim=[0,0]
            else:
                self.__dim=[dim,dim]
            
    def _declareDim(self):
        """
        Set new dimension 
        """
        try:
            if self._isIdentity:
                return self.dim
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
            assert self._valid==1
            c={}
            i=0
            for cols in range(len(lis[0])):
                i+=1
                temp=[]
                for rows in range(len(lis)):
                    temp.append(lis[rows][cols])
                c["Col {}".format(i)]=[round(min(temp),4),round(max(temp),4)]
        except AssertionError:
            return None
        except Exception as err:
            print("Can't declare range: ",err)
            #print(Matrix.__doc__)
            return None
        else:
            
            return c
        
    def __fromFile(self,d):
        try:
            data="" 
            with open(d,"r") as f:
                for lines in f:
                    data+=lines
        except FileNotFoundError:
            try:
                f.close()
            except:
                pass
            print("No such file or directory")
            self._valid=0
            return None
        else:
            f.close()
            return data
# =============================================================================  
    def _listify(self,string,header=0):
        """
        Finds all the positive and negative numbers in the given string
        Tries to fit the numbers into a grid shape

        """
        try:
            gridNum=""
            numbers=[str(i) for i in range(10)]
            
            l=len(string)
            list1=list()
            negative=0
            newRow=1
            rowadded=None
            
            for c in range(0,l):    
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
                    if rowadded==0:
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
            print("Bad stirng")
            print(Matrix.__doc__)
        else:          
            try:
                if self.__dim!=[0,0]:
                    try:
                        assert self.dim[0]*self.dim[1]==len(list1)
                    except AssertionError:
                        print("Can't create a matrix in given dimensions")
                        return None
                    else:
                        list2=[]
                        ind=0
                        for i in range(self.dim[0]):
                            list2.append(list())
                            for j in range(self.dim[1]):
                                list2[i].append(list1[ind])
                                ind+=1
                        return list2
                else:
                    try:
                        if header:
                            newRow-=1
                        l2=len(list1)/newRow
                        if int(l2)<l2 or int(l2)>l2:
                            #print("New rows couldn't be created")
                            return [list1]
                        list2=[]
                        ind=0
                        for i in range(newRow):
                            list2.append(list())
                            for j in range(int(l2)):
                                list2[i].append(list1[ind])
                                ind+=1
                    except ZeroDivisionError:
                        return [list1]
                    else:
                        return list2
            except Exception as err:
                print(err)
                self._valid=0
            else:
                return list2
    
    def _stringfy(self):
        """
        Turns a square matrix shaped list into a grid-like form that is printable
        Returns a string
        """
        def __digits(num):
            dig=0
            if num==0:
                return 1
            if num<0:
                dig+=1
                num*=-1
            while num!=0:
                num=num//10
                dig+=1
            return dig
        try:
            assert self._valid==1
            string=""
            if not self._isIdentity:
                i=min([min(a) for a in self._inRange.values()])
                j=max([max(a) for a in self._inRange.values()])
                b1=__digits(i)
                b2=__digits(j)
                bound=max([b1,b2])
            else:
                bound=2
        except Exception as e:
            print(e)
            return None
        else:
            for rows in self._matrix:
                string+="\n"
                for cols in rows:
                    s=__digits(cols)
                    if self._fMat:
                        round(cols,4)
                        item="{0:.4f}".format(cols)
                    else:
                        item=str(cols)
                    string += " "*(bound-s)+item+" "
        
            return string
# =============================================================================

    def _zeroFiller(self,lis):
        """
        Fills the matrix with zeros
        """
          
        for rows in range(0,self.dim[0]):
            lis.append(list())
            if not self._randomFill: 
                for cols in range(0,self.dim[1]):
                    lis[rows].append(0)
            else:
                pass
                #print("Try turning on randomFill if you're having issues")
        if self._isIdentity:            
            for row in range(0,self.dim[0]):
                lis[row][row]=1  
                
        return lis

    def _randomFiller(self,lis):
        """
        Fill the matrix with random integers from given range
        """
        try:
            if  self._randomFill:
                
                lis=self._zeroFiller(lis)
                m,n=max(self._initRange),min(self._initRange)
                d=self.__dim[:]
                for row in range(0,d[0]):
                    for column in range(0,d[1]):
                        if not self._fMat:
                            lis[row].append(rd.randint(n,m))
                        else:
                            new=rd.uniform(n,m)
                            ele="{0:.4f}".format(new)
                            lis[row].append(float(ele))
        
        except AssertionError:
            print("Bad argument for inRange parameter!")
        except Exception as err:
            print(err)
            print(Matrix.__doc__)
        else:
            return lis
        
    def __floatFix(self):    
        pass
# =============================================================================
            
    def add(self,lis=[],row=None,col=None):
        """
        Add a row or a column of numbers
        lis: list of numbers desired to be added to the matrix
        row: natural number
        col: natural number 
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
            self.__dim=self._declareDim()
            self._inRange=self._declareRange(self._matrix)
            self._string=self._stringfy()
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
            self.__dim=self._declareDim()
            self._string=self._stringfy()
            
    def delDim(self,num):
        """
Removes desired number of dimensions from bottom left corner
        """        
        try:
            if self.matrix==[]:
                return "Empty matrix"
            assert isinstance(num,int) and num>0 and self.dim[0]-num>=0 and self.dim[1]-num>=0
            goal1=self.dim[0]-num
            goal2=self.dim[1]-num
            if goal1==0 and goal2==0:
                print("All rows have been deleted")
            self.__dim=[goal1,goal2]
            temp=[]
            for i in range(goal1):
                temp.append(self._matrix[i][:goal2])
            self._matrix=temp
            self._string=self._stringfy()
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
            except ValueError:
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
            assert rowS<=self.dim[0] and rowE<=self.dim[0] and colS<=self.dim[1] and colE<=self.dim[1]
            
        except AssertionError:
            print("Bad arguments")
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
                if isinstance(self,Identity):
                    return Identity(dim=len(temp2))
                elif isinstance(self,FMatrix):
                    return FMatrix(dim=[rowE-rowS,colE-colS],listed=temp2)
                elif isinstance(self,CMatrix):
                    return CMatrix(dim=[rowE-rowS,colE-colS],listed=temp2)
                else:
                    return Matrix(dim=[rowE-rowS,colE-colS],listed=temp2)

# =============================================================================
    def _determinantByUpperTriangulerForm(self):
        try:
            if not self.__detCalc:
                self._det=self._UpperTrianguler()[1]
                self.__detCalc=1
        except:
            print("error")
        else:
            return self._det

    def _transpose(self):
        try:
            assert self._valid==1
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
            assert self._valid==1
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
            assert self._valid==1
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
                    adjL[rows].append(round(res,4))
                    
            adjM=FMatrix(dim=self.__dim,listed=adjL)
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
            assert self.dim[0]== self.dim[1]
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
            for rows in i._matrix:
                for cols in rows:
                    if cols<=0.0001 and cols>=-0.0001:
                        cols=0
            new=FMatrix(listed=i.matrix)
            self._inv=new
            return self._inv

    def _Rank(self):
        """
        Returns the rank of the matrix
        """
        #If matrix is not a square matrix
        if self.dim[0]!=self.dim[1]:
            m=min(self.__dim)
            dimsOf=[]
            #Get square matrices from mxn dimension matrix (m!=n)
            if self.dim[0]<2 or self.dim[1]<2:
                return 1
            if self.dim[0]!=self.dim[1]:
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
            
        #If matrix is a square matrix
        else:
            try:
                r=0
                temp=self._UpperTrianguler()[0]
                for rows in temp._matrix:
                    if rows!=[0]*self.dim[1]:
                        r+=1
            except:
                print("error getting rank")
            else:
                return r
    def _UpperTrianguler(self):
        """
        ### NEEDS SOME CLEAN UP###
        ### DETERMINANT CALCULATION DONE BY ERROR RATE OF 0.0001% ###
        Returns the not reduced upper trianguler form of the matrix
        """
        temp = FMatrix(listed=self._matrix)
        i=0
        rowC=0
        prod=1
        dia=[]
        while i <min(self.__dim):
            try:
                temp2 = [a/temp._matrix[i][i] for a in temp._matrix[i]]
                for nums in temp2:
                    if nums<=0.0000 and nums>-0.0001:
                        temp2[temp2.index(nums)]=0
            except ZeroDivisionError:
                try:
                    rowC+=1
                    """Note to self : Try using pop and push"""
                    if temp._matrix[i+1]==[0]*self.dim[1]:
                        m=temp._matrix[-1]
                        temp._matrix[-1]=temp._matrix[i+1]
                        temp._matrix[i+1]=m
                        i+=1
                        continue
                    rowN=temp._matrix[i]
                    temp._matrix[i]=temp._matrix[i+1]
                    temp._matrix[i+1]=rowN
                except IndexError:
                    m=temp._matrix[-1]
                    temp._matrix[-1]=temp._matrix[i]
                    temp._matrix[i]=m
                    i+=1
                    continue
            else:
                dia.append(temp[i][i])
                temp[i]=temp2
                for j in range(i+1,self.dim[0]):
                    temp3=[]
                    co=temp[j][i]
                    for k in range(self.dim[1]):
                        num=temp[j][k]-co*temp[i][k]
                        if round(num,4)<=0.0001 and round(num,4)>=-0.0001:
                            num=0
                        temp3.append(round(num,4))
                    temp[j]=temp3
                
                temp[i]=[round(a*dia[i],4) for a in temp[i]]
                i+=1
        
        t=[]
        ind=0
        for items in dia:
            prod*=items

            
        for rows in temp._matrix:
            t.append(list())
            for els in rows:
                if els<=0.0000 and els>-0.0001:
                    els=0
                t[ind].append(els)
            ind+=1
            
        t1=[]
        zeroRow=0
        for r in t:
            if r==[0]*self.dim[1]:
               zeroRow+=1
            else:
                t1.append(r)
        
        for j in range(zeroRow):
            t1.append([0]*self.dim[1])
        if zeroRow>0:
            prod=0
        self._det=prod
        self.__detCalc=1
        return (FMatrix(listed=t1),((-1)**(rowC))*prod)
# =============================================================================

    def _average(self,col=None):
        """
        Sets the avg attribute of the matrix as the average of it's elements
        """
        try:
            d=self.__dim[:]
            if d[0]==0 or d[1]==0:
                return None
            
            if col==None:
                colAvg={}
                for rows in self._matrix:
                    nth=1
                    for cols in rows:
                        if "Col "+str(nth) not in colAvg.keys():
                            colAvg["Col "+str(nth)]=cols
                        else:
                            colAvg["Col "+str(nth)]+=cols
                        nth+=1
                for key,value in colAvg.items():
                    colAvg[key]=round(value/self.dim[0],4)
                return colAvg
                    
            else:
                try:
                    assert col>0 and col<=self.dim[1]
                except AssertionError:
                    print("Col parameter should be in range [1,amount of columns]")
                else:
                    total=0
                    for rows in self._matrix:
                        total+=rows[col-1]
                    avg=total/self.dim[0]
                    return avg
            
        except Exception as err:
            print("Bad matrix and/or dimension")
            print(err)
            return None
        else:
            new=total/(d[0]*d[1])
            return new
        
    def col(self,column=None):
        """
        Get a specific column of the matrix
        Starts from 1
        Returns an ordered list 
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
            return temp
    def row(self,row=None):
        """
        Get a specific row of the matrix
        Starts from 1
        You can also use self._matrix[row-1]
        """
        try:
            assert isinstance(row,int)
            assert row>0 and row<=self.dim[0]
        except:
            print("Bad arguments")
            return None
        else:
            return self._matrix[row-1]
            
# =============================================================================
    """Properties available for public"""               
# =============================================================================
    @property
    def p(self):
        print(self)
    @property
    def grid(self):
        print(self._stringfy())
    @property
    def copy(self):
        if self._isIdentity:
            return Identity(dim=self.__dim)
        elif self._fMat:
            return FMatrix(dim=self.__dim,listed=self._matrix,randomFill=self._randomFill)
        else:
            return Matrix(dim=self.__dim,listed=self._matrix,randomFill=self._randomFill)
    @property
    def string(self):
        return self._stringfy()
    @property
    def directory(self):
        return self._dir
    
    @property
    def dim(self):
        return self.__dim
    @dim.setter
    def dim(self,val):
        if self._valid:
            try:
                a=self.dim[0]*self.dim[1]
                if isinstance(val,int):
                    assert val>0
                    val=[val,val]
                elif isinstance(val,list):
                    assert len(val)==2
                else:
                    return None
                assert val[0]*val[1]==a
            except:
                return None
            else:
                els=[]
                for rows in self.matrix:
                    for cols in rows:
                        els.append(cols)
                new=[]
                i=-1
                for r in range(val[0]):
                    i+=1
                    new.append([])
                    for c in range(val[1]):
                        new[i].append(els[c+val[1]*r])
                self.__init__(dim=val,listed=new)
            
        
    @property
    def uptri(self):
        return self._UpperTrianguler()[0]
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
    def matrix(self):
       return self._matrix
    @property
    def det(self):
        try:
            assert self.dim[0]==self.dim[1]
        except AssertionError:
            print("Not a square matrix")
        else:
            if self.__detCalc:
                return self._det
            else:
                return self._determinantByUpperTriangulerForm()       
    @property
    def highest(self):
        if not self._isIdentity:
            return self._initRange[1]
        else:
            return 1
    @property
    def lowest(self):
        if not self._isIdentity:
            return self._initRange[0]   
        else:
            return 0
    @property
    def summary(self):
        if self._valid and self._fMat:
            return "FMatrix(dim={0},listed={1},inRange={2},randomFill={3})".format(self.__dim,self._matrix,self._inRange,self._randomFill)
        elif self._valid and not self._isIdentity:
            return "Matrix(dim={0},listed={1},inRange={2},randomFill={3})".format(self.__dim,self._matrix,self._inRange,self._randomFill)
        elif self._valid and self._isIdentity:
            return "Identity(dim={0},listed={1},inRange=[0,1],randomFill=0)".format(self.__dim,self._matrix)
        else:
            return None
        
    @property
    def floorForm(self):
        return Matrix(listed=self.__floor__())  
    
    @property
    def ceilForm(self):
        return Matrix(listed=self.__ceil__())   
    
    @property   
    def intForm(self):
        return Matrix(listed=self.__floor__())
    
    @property   
    def floatForm(self):
        t=[]
        for a in self._matrix:
            t.append([float(b) for b in a])            
        return FMatrix(listed=t)
    
    def roundForm(self,decimal=1):
        if decimal==0:
            return Matrix(listed=round(self,decimal).matrix)
        return FMatrix(listed=round(self,decimal).matrix)
    
    def minor(self,r=None,c=None):
        return self._minor(row=r,col=c)
    
    def inRange(self,col=None):
        if col==None:
            return self._inRange
        return self._inRange["Col {}".format(col)]   

    def avg(self,col=None):
        if self._average(col)!=None:
            return self._average(col)
        return None
# =============================================================================
    """ Setters to secure some attributes """
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

    def __setitem__(self,pos,item):
        try:
            if isinstance(pos,tuple) and (isinstance(item,complex) or isinstance(item,float) or isinstance(item,int)):           
                row,col=pos
                self._matrix[row][col]=item
                self._inRange=self._declareRange(self._matrix)
                
            elif isinstance(pos,int) and isinstance(item,list):
                if len(item)==self.dim[1]: 
                    row=pos
                    self._matrix[row]=item[:]
                    self.__dim=self._declareDim()
                    self._inRange=self._declareRange(self._matrix)
                else:
                    print("Check the dimension of the given list")
        except:
            print(pos,item)
            print("Bad indeces")
            return None
        else:
            self._string=self._stringfy()
            self.__rankCalc=0
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            return self
        

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
                        if num<=0.0001 and num>=-0.0001:
                            num=0
                        total+=num
                    temp[r][rs]=round(total,4)
            if isinstance(self,FMatrix) or isinstance(other,FMatrix):
                return FMatrix(dim=[self.dim[0],other.dim[1]],listed=temp)
            return Matrix(dim=[self.dim[0],other.dim[1]],listed=temp)
################################################################################    
    def __add__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]+other.matrix[rows][cols])
            except:
                print("Can't add")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
            
                return Matrix(dim=self.__dim,listed=temp)    
            
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                
           
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                            
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
        else:
            print("Can't add")
################################################################################            
    def __sub__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]-other.matrix[rows][cols])
            except:
                print("Can't subtract")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
            
                return Matrix(dim=self.__dim,listed=temp)    
            
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                
           
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                    
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
        else:
            print("Can't subtract")
################################################################################     
    def __mul__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]*other.matrix[rows][cols])
            except:
                print("Can't multiply")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
            
                return Matrix(dim=self.__dim,listed=temp)    
            
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                 
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
            
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
        else:
            print("Can't multiply")
################################################################################
    def __floordiv__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]//other.matrix[rows][cols])
            except ZeroDivisionError:
                print("Division by 0")
            except:
                print("Can't divide")
            else:
                return Matrix(dim=self.__dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]//other)
            except ZeroDivisionError:
                print("Division by 0")
            except:
                print("Can't divide") 
            else:
                return Matrix(dim=self.__dim,listed=temp)
                
           
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]//other)
            except ZeroDivisionError:
                print("Division by 0")
            except:
                print("Can't divide") 
            else:
                return Matrix(dim=self.__dim,listed=temp)
            
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
                return Matrix(dim=self.__dim,listed=temp)
            
        else:
            print("Can't divide")
################################################################################            
    def __truediv__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]/other.matrix[rows][cols])
            except ZeroDivisionError:
                print("Division by 0")
            except:
                print("Can't divide")
            else:
                return FMatrix(dim=self.__dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]/other)
            except ZeroDivisionError:
                print("Division by 0")
            except:
                print("Can't divide") 
            else:
                return FMatrix(dim=self.__dim,listed=temp)
                         
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]/other)
            except ZeroDivisionError:
                print("Division by 0")
            except:
                print("Can't divide") 
            else:
                return FMatrix(dim=self.__dim,listed=temp)
            
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
                return FMatrix(dim=self.__dim,listed=temp)
            
        else:
            print("Can't divide")
################################################################################
    def __mod__ (self, other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]%other.matrix[rows][cols])
            except ZeroDivisionError:
                print("Division by zero! Can't get modular")
            except AssertionError:
                print("Dimensions doesn't match")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
            
                return Matrix(dim=self.__dim,listed=temp)    
            
        elif isinstance(self,Matrix) and (isinstance(other,int) or isinstance(other,float)):
            try:
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]%other)
            except ZeroDivisionError:
                print("Division by zero! Can't get modular")
            except:
                print("Can't get modular")
            else:
                if isinstance(self,FMatrix) or isinstance(other,float):                
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                
           
        elif (isinstance(self,int) or isinstance(self,float)) and isinstance(other,Matrix):
            try:
                temp=[]
                for rows in range(other.dim[0]):
                    temp.append(list())
                    for cols in range(other.dim[1]):
                        temp[rows].append(other.matrix[rows][cols]%other)
            except ZeroDivisionError:
                print("Division by zero! Can't get modular")
            except:
                print("Can't get modular")
            else:
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                    
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't get modular")
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]%other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
        else:
            print("Can't get modular")
################################################################################         
    def __pow__(self,other):
        if isinstance(self,Matrix) and isinstance(other,Matrix):
            try:
                assert self.__dim==other.dim                
                temp=[]
                for rows in range(self.dim[0]):
                    temp.append(list())
                    for cols in range(self.dim[1]):
                        temp[rows].append(self.matrix[rows][cols]**other.matrix[rows][cols])
            except:
                print("Can't raise to the given power")
            else:
                if isinstance(self,FMatrix) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
            
                return Matrix(dim=self.__dim,listed=temp)    
            
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
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
                
        elif isinstance(other,list):
            if len(other)!=len(self.matrix[0]):
                print("Can't raise to the given power") 
                return None
            else:
                temp=[]
                s=0
                for rows in self._matrix:
                    temp.append(list())
                    for d in range(len(other)):
                        temp[s].append(rows[d]**other[d])
                    s+=1
                if isinstance(self,float) or isinstance(other,FMatrix):                
                    return FMatrix(dim=self.__dim,listed=temp)
                return Matrix(dim=self.__dim,listed=temp)
        else:
            print("Can't raise to the given power")
################################################################################                    
    def __lt__(self,other):
        if self._valid==1 and other._valid==1:
            if self.__dim==other.dim:
                if self.matrix==other.matrix:
                    return False
                elif self.dim[0]==self.dim[1]:
                    return self.det<other.det
                else:
                    return None
            elif self.dim[0]==self.dim[1] and other._dim[0]==other._dim[1] :   
                return self.det<other.det
            else:
                return None
        print("Invalid")        
        return None
    
    def __eq__(self,other):
        if self._valid==1 and other._valid==1:
            if self.__dim==other.dim:
                if self.matrix==other.matrix:
                    return True
                return False
            else:   
                return False
        print("Invalid")        
        return None
    
    def __gt__(self,other):
        if self._valid==1 and other._valid==1:
            if self.__dim==other.dim:
                if self.matrix==other.matrix:
                    return False
                elif self.dim[0]==self.dim[1]:
                    return self.det>other.det
                else:
                    return None
            elif self.dim[0]==self.dim[1] and other._dim[0]==other._dim[1] :   
                return self.det>other.det
            else:
                return None
        print("Invalid")
        return None
# =============================================================================
    
    def __round__(self,n=-1):
        if self._fMat and n<0:
            n=1
        temp=[]
        for elements in self._matrix:
            temp.append([round(a,n) for a in elements])
        return Matrix(listed=temp)
    
    def __floor__(self):
        temp=[]
        for elements in self._matrix:
            temp.append([int(a) for a in elements if isinstance(a,float)])
        return temp       
    
    def __ceil__(self):
        temp=[]
        for elements in self._matrix:
            temp.append([int(a)+1 for a in elements if isinstance(a,float)])
        return temp     
    
    def __repr__(self):
        return str(self.matrix)
    
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        if self._fMat:
            print("\nFloat Matrix",end="")
        if self._valid and not self._cMat and not self._isIdentity and self.avg()!=None:
            if self.dim[0]!=self.dim[1]:
                print("\nDimension: {0}x{1}\nNumbers' range: {2}\nAverages: {3}".format(self.dim[0],self.dim[1],self._inRange,self.avg()))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nNumbers' range: {1}\nAverages: {2}".format(self.dim[0],self._inRange,self.avg()))
            return self._stringfy()+"\n"
        else:
            return "Invalid matrix\n"
    
# =============================================================================

class Identity(Matrix):
    """
Identity matrix
    """
    def __init__(self,dim=[1,1]):     
        self._valid=1 
        self.__dim=self._dimSet(dim)
        if self.dim[0]!=self.dim[1]:
            self._valid=0
            return None

        self._randomFill=0
        self._inRange=[0,1]
        self._initRange=[0,1]
        
        self._fMat=0
        self._cMat=0
        self._isIdentity=1       
        self.__adjCalc=1
        self.__detCalc=1
        self.__invCalc=1

        self._dimSet(dim)
        self._matrix=list()
        self._matrix=self._zeroFiller(self._matrix)
        self._string=self._stringfy()
                    
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
            goal=self.dim[0]+num
            self.__dim=[goal,goal]
            self._matrix=self._zeroFiller(list())
            self._string=self._stringfy()
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
            goal=self.dim[0]-num
            if goal==0:
                print("All rows have been deleted")
            self.__dim=[goal,goal]
            self._matrix=self._zeroFiller(list())
            self._string=self._stringfy()
            return self
        
    @property
    def inv(self):
        return Identity(dim=self.__dim)
    @property    
    def det(self):
        return 1
    @property
    def adj(self):
        return Identity(dim=self.__dim)
    
    def __str__(self):
        if self._isIdentity:
            print("\nIdentity Matrix\nDimension: {0}x{0}".format(self.dim[0]))
            return self._stringfy()+"\n"
        
class FMatrix(Matrix):
    """
Matrix which contain float numbers
    """
    def __init__(self,*args,decimal=None,**kwargs):
        super().__init__(*args,**kwargs)
        self._valid=1
        self._decimal=decimal
        self._fMat=1
        
class CMatrix(FMatrix):
    """
######This class requires extra work, it doesn't work as intended yet######
Matrix which contain complex numbers
    """
    def __init__(self,*args,**a):
        super().__init__(*args,**a)
        self._valid=1
        self._cMat=1

    def __str__(self):
        if self._cMat:
            print("\nComplex matrix, ",end="")
            if self.dim[0]!=self.dim[1]:
                print("\nDimension: {0}x{1}\nNumbers' range: {2}\nAverages: {3}".format(self.dim[0],self.dim[1],self._inRange,self.avg()))
            else:
                print("Square matrix\nDimension: {0}x{0}\nNumbers' range: {1}\nAverages: {2}".format(self.dim[0],self._inRange,self.avg()))            
                
            return self._stringfy()+"\n"
