# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:26:48 2018

@author: Semih
"""

import random as rd
import re

class Matrix(object):
    """Matrix object for integers(Use FMatrix for float values):
-dim:dimension of the matrix;natural numbers as [rows,cols],if and integer given, matrix will be a square matrix 
-listed:string of integers,list of integers/floats or list of lists containing integers/floats ([[numbers],[given],[here]])
-randomFill(Doesn't matter if "listed" parament is provided): 
    ->1 to fill the matrix with random integers/floats
    ->0 to fill the matrix with 0s
-ranged: 2 numbers as a list, to determine the upper and lower bound of the random elements    
-Giving ~300< elements may make grid look terrible, adjust your terminal size to display it better
-Can contain integers only (Unless it's a FMatrix class) 

-Elements/row can be changed in place ( Current not available on columns )
-Additional rows and columns can be added with add(row,col,lis)
-Rows and cols from right and bottom can be deleted with del
-Sub-matrices can be obtained with "subM" method
-Get specific items by using a[i][j] for the (i+1)th row and (j+1)th column   

-Mean of the all colums can be seen with "mean" property
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
    def __init__(self,dim=None,listed=[],directory="",ranged=[-5,5],randomFill=1,header=None,features=[]):
        self._isIdentity=0
        self._fMat=0
        self._cMat=0
        self._valid = 1
        self._badDims= 0
        self.__temp1 = None
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
            self.__features=features
            self._header=header
        if self._valid:
##########################################################################################################                
            if isinstance(listed,str):
                try:
                    self._matrix=self._listify(listed)
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
                        self._matrix=self._listify(lis)
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
                    if self.__temp1==None:
                        self.__temp1=[a[:] for a in listed]
                    
                    if len(self.__temp1)>0 and dim!=[0,0]:                        
                            self._matrix = self.__temp1.copy() 
                            self.__dim=self._declareDim()
                            self._inRange=self._declareRange(self._matrix)
                            self._string=self._stringfy()   
                            
                    elif len(self.__temp1)==0 and dim!=[0,0]:
                        if not self._randomFill:
                            self._matrix=self._zeroFiller(self.__temp1)
                            self._inRange=self._declareRange(self._matrix)
                            
                        elif self._randomFill:
                            self._matrix=self._randomFiller(self.__temp1)
                            self.__dim=self._declareDim()
                            self._inRange=self._declareRange(self._matrix)
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
        try:
            if isinstance(alist,list):

                if isinstance(alist[0],int) or isinstance(alist[0],float) or isinstance(alist[0],str):
                    try:
                        if self.__dim==[0,0]:
                            self.__dim=[1,len(alist)]
                        else:
                            assert len(alist)==self.dim[0]*self.dim[1]
                        if isinstance(alist[0],str):
                            if "." in alist[0] or isinstance(self,FMatrix):
                                alist=[float(strs) for strs in alist]
                            else:
                                alist=[int(strs) for strs in alist]
                        t=[]
                        i=0
                        for rows in range(self.dim[0]):
                           t.append(list())
                           for cols in range(self.dim[1]):
                               t[rows].append(alist[i])
                               i+=1
                        self.__temp1=t
                    except AssertionError:
                        print("Given list is not valid")
                        self._valid=0
                        self._randomFill=0
                        return False
                    except ValueError:
                        print("List contain non-integer values, use FMatrix")
                        return False
                    else:
                        return True   
                if len(alist)>0:
                    l=[]
                    c=0
                    for row in alist:
                        c=0
                        for col in row:
                            c+=1
                        l.append(c)
                    return max(l)==min(l)
                return True
        except IndexError:
            if self.dim!=[0,0]:
                return True
            self._valid=0
            return False
        else:
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
                if len(self.__features)==0:
                    c["Col {}".format(i)]=[round(min(temp),4),round(max(temp),4)]
                else:
                    c[self.__features[i-1]]=[round(min(temp),4),round(max(temp),4)]
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
    def _listify(self,string):
        """
        Finds all the numbers in the given string
        """
        #Get the features from the first row if header exists
        if self._header:
            i=0
            for ch in string:
                if ch!="\n":
                    i+=1
                else:
                    if len(self.__features)!=0:
                        pattern=r"\w+"
                        self.__features=re.findall(pattern,string[:i])
                    string=string[i:]
                    break
        #Get all integer and float values       
        pattern=r"(?:\-?[0-9]+)(?:\.?[0-9]*)"
        found=re.findall(pattern,string)
        
        #String to number
        if not isinstance(self,FMatrix):
            found=[int(a) for a in found]
        elif isinstance(self,FMatrix):
            found=[float(a) for a in found] 
        #Fix dimensions to create a row matrix   
        if self.dim==[0,0]:
            self.__dim=[1,len(found)]
            self._badDims=1
        #Create the row matrix
        temp=[]
        e=0            
        for rows in range(self.dim[0]):
            temp.append(list())
            for cols in range(self.dim[1]):
                temp[rows].append(found[cols+e])
            e+=self.dim[1]
            
        return temp
            
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
                        round(cols,self._decimal)
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
            
    def add(self,feature="Col",lis=[],row=None,col=None):
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
            if col!=None and self.__features!=[]:
                self.__features.insert(col-1,feature)
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
                        if r<self.dim[0]:
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
            if c!=None and len(self.__features)>0:
                self.__features.pop(c-1)                    
            self._matrix=[a[:] for a in newM]
            self.__dim=self._declareDim()
            self._inRange=self._declareRange(self._matrix)
            self._string=self._stringfy()
            
    def delDim(self,num):
        """
Removes desired number of dimensions from bottom right corner
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
            if self.__features!=[]:
                self.__features=self.__features[:goal2]
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
                    return FMatrix(dim=[rowE-rowS,colE-colS+1],listed=temp2,features=self.__features[colS-1:colE])
                elif isinstance(self,CMatrix):
                    return CMatrix(dim=[rowE-rowS,colE-colS+1],listed=temp2,features=self.__features[colS-1:colE])
                else:
                    return Matrix(dim=[rowE-rowS,colE-colS+1],listed=temp2,features=self.__features[colS-1:colE])

# =============================================================================
    def _determinantByLUForm(self):
        try:
            if self.dim[0]==self.dim[1] and self.dim[0]==1:
                return self.matrix[0][0]
            if not self.__detCalc:
                self._det=self._LU()[1]
                self.__detCalc=1
        except Exception as e:
#            print("error ",e)
            return 0
        else:
            return self._det
# =============================================================================    
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
# =============================================================================                
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
            if temp.dim[0]==1 and temp.dim[1]==1:
                return temp            
            if not temp.dim[0]<1:   
                temp.remove(r=row)
            if not temp.dim[1]<1: 
                temp.remove(c=col)
            return temp
# =============================================================================    
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
# =============================================================================                           
    def _inverse(self):
        """
        Returns the inversed matrix
        O(n^3)
        Takes about a second to solve a 50x50 matrix
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
            id1=Identity(self.dim[0])
            temp=self.copy
            i=0
            while i <self.dim[0]:
                #Swap lines if diagonal is 0, stop when you find a non zero in the column
                if temp[i][i]==0:
                    i2=i
                    old=temp[i][:]
                    while temp[i2][i]==0 and i2<self.dim[0]:
                        i2+=1
                    temp[i]=temp[i2][:]
                    temp[i2]=old[:]
                    
                    old=id1[i][:]
                    id1[i]=id1[i2][:]
                    id1[i2]=old[:]
                
                co=temp[i][i]
                for j in range(self.dim[0]):
                    temp[i][j]/=co
                    id1[i][j]/=co

                for k in range(self.dim[0]):
                    if k!=i:
                        mult=temp[k][i]
                        for m in range(self.dim[1]):
                            num=temp[k][m]-temp[i][m]*mult
                            if num>=-0.0001 and num<=0.0001:
                                num=0
                            temp[k][m]=num
                            
                            num2=id1[k][m]-id1[i][m]*mult
                            if num2>=-0.0001 and num2<=0.0001:
                                num2=0
                            id1[k][m]=num2         
                i+=1
            
            self._inv=FMatrix(listed=id1.matrix)
            self.__invCalc=1
            return self._inv
# =============================================================================    
    def _Rank(self):
        """
        Returns the rank of the matrix
        """
        try:
            r=0
            temp=self._LU()[0]
            for rows in temp._matrix:
                if rows!=[0]*self.dim[1]:
                    r+=1
        except:
            #print("error getting rank")
            return self._echelon()[1]
        else:
            return r
# =============================================================================        

    def _echelon(self):
        """
        Returns reduced row echelon form of the matrix
        """
        temp=self.copy
        i=0
        zeros=[0]*self.dim[1]
        while i <min(self.dim):
            if zeros in temp.matrix:
                ind=0
                for rows in temp.matrix:
                    while temp.matrix[ind]!=zeros:
                        ind+=1
                del(temp.matrix[ind])
                temp.matrix.append(zeros)
                    
            if temp[i][i]==0:
                try:
                    i2=i
                    old=temp[i][:]
                    while temp[i2][i]==0 and i2<self.dim[0]:
                        i2+=1
                    temp[i]=temp[i2][:]
                    temp[i2]=old[:]
                except:
                    break
            co=temp[i][i]
            for j in range(self.dim[1]):
                temp[i][j]/=co

            for k in range(self.dim[0]):
                if k!=i:
                    mult=temp[k][i]
                    for m in range(self.dim[1]):
                        num=temp[k][m]-temp[i][m]*mult
                        if num>=-0.0001 and num<=0.0001:
                            num=0
                        temp[k][m]=round(num,4)
            i+=1
            
        z=0    
        for a in temp.matrix:
            if a==zeros:
                z+=1    
        return (FMatrix(listed=temp.matrix),self.dim[0]-z)
            
# =============================================================================            

    def _LU(self):
        """
        Returns L and U matrices of the matrix
        ***KNOWN ISSUE:Doesn't always work if determinant is 0 | linear system is inconsistant***
        ***STILL NEEDS CLEAN UP***
        """
        temp = FMatrix(listed=self._matrix)
        rowC=0
        prod=1
        dia=[]
        i=0
        L=FMatrix(self.dim,randomFill=0)
        #Set diagonal elements to 1
        for diags in range(self.dim[0]):
            L[diags][diags]=1
            
        while i <min(self.__dim):
            #Swap lines if diagonal has 0, stop when you find a non zero in the column
            if temp[i][i]==0:
                try:
                    i2=i
                    old=temp[i][:]
                    while temp[i2][i]==0 and i2<min(self.dim):
                        rowC+=1
                        i2+=1
                    temp[i]=temp[i2][:]
                    temp[i2]=old[:]
                except:
                    print("Determinant is 0, can't get lower/upper triangular matrices")
                    self.__detCalc=1
                    self._det=0
                    return [None,0,None]
                
            #Loop through the ith column find the coefficients to multiply the diagonal element with
            #to make the elements under [i][i] all zeros
            rowMulti=[]
            for j in range(i+1,self.dim[0]):
                co=temp[j][i]/temp[i][i]
                rowMulti.append(co)            
            #Loop to substitute ith row times the coefficient found from the i+n th row (n>0 & n<rows)
            k0=0
            for k in range(i+1,self.dim[0]):
                for m in range(self.dim[1]):
                    num=temp[k][m]-(rowMulti[k0]*temp[i][m])
                    if num>=-0.0001 and num<=0.0001:
                        num=0
                    temp[k][m]=num
                #Lower triangular matrix
                L[k][i]=rowMulti[k0]
                k0+=1   
            #Get the diagonal for determinant calculation
            dia.append(temp[i][i])
            i+=1

        for element in dia:
            prod*=element
        U=temp.copy
#        print(dia)
        return (U,((-1)**(rowC))*prod,L)
# =============================================================================

    def _mean(self,col=None):
        """
        Sets the "mean" attribute of the matrix as the mean of it's elements
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
                i=0
                new=dict()
                for key,value in colAvg.items():
                    if len(self.__features)==0:
                        colAvg[key]=round(value/self.dim[0],4)
                    else:
                        new[self.__features[i]]=round(value/self.dim[0],4)
                        i+=1
                if len(self.__features)==0:
                    return colAvg
                return new
                    
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
    
    def _sd(self,col=None,population=0):
        """
        Standard deviation of the columns
        col:integer>=1
        population: 1 for σ, 0 for s value (default 0)
        """
        try:
            assert self.dim[0]>1
            assert population==0 or population==1
        except:
            print("Bad arguments")
        else:
            if col==None:
                sd={}
                avgs=self._mean()
                for i in range(self.dim[1]):
                    e=0
                    if len(self.__features)==0:
                        for j in range(self.dim[0]):
                            e+=(self.matrix[j][i]-avgs["Col "+str(i+1)])**2
                        sd["Col "+str(i+1)]=(e/(self.dim[0]-1))**(1/2)
                    else:
                        for j in range(self.dim[0]):
                            e+=(self.matrix[j][i]-avgs[self.__features[i]])**2
                        sd[self.__features[i]]=(e/(self.dim[0]-1))**(1/2)
                return sd
            else:
                try:
                    assert col>0 and col<=self.dim[1]
                except AssertionError:
                    print("Col parameter is not valid")
                else:
                    sd={}
                    a=self._mean(col)
                    e=0
                    for i in range(self.dim[0]):
                        e+=(self.matrix[i][col-1]-a)**2
                    if len(self.__features)==0:
                        sd["Col "+str(col)]=(e/(self.dim[0]-1+population))**(1/2)
                    else:
                        sd[self.__features[col-1]]=(e/(self.dim[0]-1+population))**(1/2)
                    return sd
                
# =============================================================================
       
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
        return " ".join(self.__features)+self._stringfy()
    @property
    def directory(self):
        return self._dir
    
    @property
    def features(self):
        return self.__features
    @features.setter
    def features(self,li):
        if self._valid:
            try:
                assert isinstance(li,list)
                assert len(li)==self.dim[1]
            except AssertionError:
                print("Give the feature names as a list of strings with the right amount")
            else:
                temp=[str(i) for i in li]
                self.__features=temp
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
        return self._LU()[0]
    @property
    def lowtri(self):
        return self._LU()[2]
    @property
    def rank(self):
        if not self.__rankCalc:
            self._rank=self._Rank()
        return self._rank
    @property
    def rrechelon(self):
        """
        Reduced-Row-Echelon
        """
        return self._echelon()[0]
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
                return self._determinantByLUForm()       
    @property
    def highest(self):
        if not self._isIdentity:
            return max([max(a) for a in self.ranged().values()])
        else:
            return 1
    @property
    def lowest(self):
        if not self._isIdentity:
            return min([min(a) for a in self.ranged().values()])  
        else:
            return 0
        
    @property
    def summary(self):
        #ranged and randomFill arguments are NOT required to create the same matrix
        if self._valid and self._fMat:
            return "FMatrix(dim={0},listed={1},ranged={2},randomFill={3},features={4},header={5},directory='{6}')".format(self.__dim,self._matrix,self._initRange,self._randomFill,self.__features,self._header,self._dir)
        elif self._valid and not self._isIdentity:
            return "Matrix(dim={0},listed={1},ranged={2},randomFill={3},features={4},header={5},directory='{6}')".format(self.__dim,self._matrix,self._initRange,self._randomFill,self.__features,self._header,self._dir)
        elif self._valid and self._isIdentity:
            return "Identity(dim={0},listed={1},ranged=[0,1],randomFill=0)".format(self.__dim,self._matrix)
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
    
    def ranged(self,col=None):
        self._inRange=self._declareRange(self.matrix)
        if col==None:
            return self._inRange
        if len(self.__features)==0:
            return self._inRange["Col {}".format(col)]   
        return self._inRange[self.__features[col-1]]
    
    def mean(self,col=None):
        if self._mean(col)!=None:
            return self._mean(col)
        return None
    
    def sdev(self,col=None,population=0):
        if self._sd(col)!=None:
            return self._sd(col,population)
        return None
    
    def median(self,col=None):
        """
        Returns the median of the columns
        col:integer>=1 and <=column amount
        """
        try:
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                if len(self.__features)!=0:
                    feats=self.__features[col-1]
                else:
                    feats="Col "+str(col)
                    
            meds={}
            i=1
            for rows in temp.matrix:
                
                n=sorted(rows)[self.dim[0]//2]
                
                if len(feats)!=0 and isinstance(feats,list):
                    meds[feats[i-1]]=n
                elif len(feats)==0:
                    meds["Col "+str(i)]=n
                else:
                    meds[feats]=n
                i+=1
        except:
            print("Error getting median")
        else:
            return meds
    
    def mode(self,col=None):
        """
        Returns the most columns' most repeated elements
        col:integer>=1 and <=amount of columns
        """
        try:
            #Set feature name and the matrix to use dependent on the column desired
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                if len(self.__features)>0:
                    feats=self.features[col-1]
                else:
                    feats="Col "+str(col)
            #Set keys in the dictionary which will be returned at the end
            mods={}
            if len(feats)!=0 and isinstance(feats,list):
                for fs in feats:
                    mods[fs]=None
            elif len(feats)==0:
                for fs in range(self.dim[1]):
                    mods["Col "+str(fs+1)]=None
                   
            #Set column amount
            if col==None:
                r=self.dim[1]
            else:
                r=1
                
            #Loop through the transpozed matrices (From column to row matrices to make calculations easier)               
            for rows in range(r):
                #Variables to keep track of the frequency of the numbers
                a={}
                i=0
                
                #Loop through the column to get frequencies
                for els in temp[rows]:
                    if els not in a.keys():
                        a[els]=1
                    else:
                        a[els]+=1
                    i+=1
                
                #Get a list of the values from the frequency dictionary
                temp2=[]
                for k,v in a.items():
                    temp2.append(v)
                
                #Find the maximum repetation
                m=max(temp2)
                #Create a dictionary to store the most repated key(s) as keys and frequency as the value
                n={}
                s=""
                allSame=0
                #Check if there are multiple most repeated elements
                for k,v in a.items(): 
                    if v==m:
                        allSame+=1
                        if len(s)!=0:
                            s+=", "+str(k)
                        else:
                            s+=str(k)
                #If all the elements repeated same amount don't get all the numbers, just set the name to "All"          
                if allSame==len(temp2):
                    n["All"]=temp2[0]
                else:
                    n[s]=m
                
                #Set the final dictionary's key(s) and  value(s) calculated
                if len(feats)!=0 and isinstance(feats,list):
                    mods[feats[rows]]=n
                elif len(feats)==0:
                    mods["Col "+str(rows+1)]=n
                else:
                    mods[feats]=n
                #END
        except Exception as err:
            print("Bad arguments given to mode method\n",err)
        else:
            return mods
    
    def iqr(self,col=None,as_quartiles=False):
        """
        Returns the interquartile range(IQR)
        col:integer>=1 and <=column amount
        as_quartiles:
            True to return dictionary as:
                {Column1=[First_Quartile,Median,Third_Quartile],Column2=[First_Quartile,Median,Third_Quartile],...}
            False to get iqr values(default):
                {Column1=IQR_1,Column2=IQR_2,...}
        """
        
        try:
            if col==None:
                temp=self.t
                feats=self.__features[:]
            else:
                assert col>=1 and col<=self.dim[1]
                temp=self.subM(1,self.dim[0],col,col).t
                if len(self.__features)!=0:
                    feats=self.__features[col-1]
                else:
                    feats="Col "+str(col)
                    
            iqr={}
            qmeds={}
            i=1
            for rows in temp.matrix:
                low=sorted(rows)[:self.dim[0]//2]
                low=low[len(low)//2]
                
                up=sorted(rows)[self.dim[0]//2:]
                up=up[len(up)//2]
                
                if len(feats)!=0 and isinstance(feats,list):
                    iqr[feats[i-1]]=up-low
                    qmeds[feats[i-1]]=[low,self.median(col)[feats[i-1]],up]
                elif len(feats)==0:
                    iqr["Col "+str(i)]=up-low
                    qmeds["Col "+str(i)]=[low,self.median(col)["Col "+str(i)],up]
                else:
                    iqr[feats]=up-low
                    qmeds[feats]=[low,self.median(col)[feats],up]
                i+=1
        except Exception as err:
            print("Error getting median",err)
        else:
            if as_quartiles:
                return qmeds
            return iqr
        
    def variance(self,col=None,population=0):
        s=self.sdev(col,population)
        vs={}
        for k,v in s.items():
            vs[k]=v**2
        return vs
    
# =============================================================================
    def __contains__(self,val):
        """
        val:value to search for in the whole matrix
        Returns True or False
        syntax: "value" in a.matrix
        """
        inds=self.find(val)
        return bool(inds)
    
    def concat(self,b,concat_as="row"):
        """
        Concatenate matrices row or columns vice
        b:matrix to concatenate to self
        concat_as:"row" to concat b matrix as rows, "col" to add b matrix as columns
        Note: This method concatenates the matrix to self
        """
        try:
            assert isinstance(b,Matrix)
            if concat_as=="row":
                assert b.dim[1]==self.dim[1]
            elif concat_as=="col":
                assert b.dim[0]==self.dim[0]
        except AssertionError:
            print("Bad dimensions")
        else:
            if concat_as=="row":
                for rows in b.matrix:
                    self._matrix.append(rows)

            else:
                i=0
                for rows in self.matrix:
                    for cols in range(b.dim[1]):
                        rows.append(b[i][cols])
                    i+=1
                    
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0  
            self.__rankCalc=0  
            self.__dim=self._declareDim()
            self._inRange=self._declareRange(self._matrix)
            self._string=self._stringfy()
            return self
                  
# =============================================================================

    def __getitem__(self,pos):
        try:
            self.__rankCalc=0
            self.__adjCalc=0
            self.__detCalc=0
            self.__invCalc=0
            if isinstance(pos,slice) or isinstance(pos,int):
                return self.matrix[pos]
        except:
#            print("Bad indeces")
            return None
        
    def __setitem__(self,pos,item):
        try:
            if isinstance(pos,slice) and  isinstance(item,list):
                if len(item)>0:
                    if isinstance(item[0],list):
                        self._matrix[pos]=item
                    else:
                        self._matrix[pos]=[item]
                
            elif isinstance(pos,int) and isinstance(item,list):
                if len(item)==self.dim[1]: 
                    row=pos
                    self._matrix[row]=item[:]
                    self.__dim=self._declareDim()
                else:
                    print("Check the dimension of the given list")
        except:
            print(pos,item)
#            print("Bad indeces")
            return None
        else:
            self.__dim=self._declareDim()
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
            temp.append([int(a) for a in elements if isinstance(a,float) or isinstance(a,int)])
        return temp       
    
    def __ceil__(self):
        temp=[]
        for elements in self._matrix:
            temp.append([int(a)+1 for a in elements if isinstance(a,float) or isinstance(a,int)])
        return temp     
    
    def __repr__(self):
        return str(self.matrix)
    
    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        if self._badDims:
            print("You should give proper dimensions to work with the data\nExample dimension:[data_amount,feature_amount]")
        self._inRange=self._declareRange(self._matrix)
        if self._valid and self.mean()!=None:
            if self.dim[0]!=self.dim[1]:
                print("\nDimension: {0}x{1}\nRange: {2}\nMean: {3}".format(self.dim[0],self.dim[1],self._inRange,self.mean()))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nRange: {1}\nMean: {2}".format(self.dim[0],self._inRange,self.mean()))
            return self._stringfy()+"\n"
        else:
            return "Invalid matrix\n"
    
# =============================================================================

class Identity(Matrix):
    """
Identity matrix
    """
    def __init__(self,dim=1):     
        self._valid=1 
        try:
            assert isinstance(dim,int)
            assert dim>0
        except AssertionError:
            print("Give integer as the dimension")
            self._valid=0
            return None
        else:
            self._dim=[dim,dim]
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
            goal=self._dim[0]+num
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
            assert isinstance(num,int) and num>0 and self._dim[0]-num>=0
        except AssertionError:
            print("Enter a valid input")
        except Exception as err:
            print(err)
        else:
            goal=self._dim[0]-num
            if goal==0:
                print("All rows have been deleted")
            self.__dim=[goal,goal]
            self._matrix=self._zeroFiller(list())
            self._string=self._stringfy()
            return self
        
    @property
    def inv(self):
        return self
    @property    
    def det(self):
        return 1
    @property
    def adj(self):
        return self
    
    def __str__(self):
        if self._isIdentity:
            print("\nIdentity Matrix\nDimension: {0}x{0}".format(self._dim[0]))
            return self._stringfy()+"\n"
        
class FMatrix(Matrix):
    """
Matrix which contain float numbers
decimal: digits to round up to 
    """
    def __init__(self,*args,decimal=8,**kwargs):
        self._valid=1
        self._decimal=decimal
        self._fMat=1
        super().__init__(*args,**kwargs)

    def __str__(self): 
        """ 
        Prints the matrix's attributes and itself as a grid of numbers
        """
        if self._badDims:
            print("You should give proper dimensions to work with the data\nExample dimension:[data_amount,feature_amount]")

        self._inRange=self._declareRange(self._matrix)
        print("\nFloat Matrix",end="")
        if self._valid and self.mean()!=None:
            if self.dim[0]!=self.dim[1]:
                print("\nDimension: {0}x{1}\nRange: {2}\nMean: {3}".format(self.dim[0],self.dim[1],self._inRange,self.mean()))
            else:
                print("\nSquare matrix\nDimension: {0}x{0}\nRange: {1}\nMean: {2}".format(self.dim[0],self._inRange,self.mean()))
            return self._stringfy()+"\n"
        else:
            return "Invalid matrix\n"        
        
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
                print("\nDimension: {0}x{1}\nRange: {2}\nMean: {3}".format(self.dim[0],self.dim[1],self._inRange,self.mean()))
            else:
                print("Square matrix\nDimension: {0}x{0}\nRange: {1}\nMean: {2}".format(self.dim[0],self._inRange,self.mean()))            
                
            return self._stringfy()+"\n"
