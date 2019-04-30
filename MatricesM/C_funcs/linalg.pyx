
cpdef list Ctranspose(int m,int n,list arr):			
  cdef int i
  cdef int j
  cdef list lst=[]

  for i in range(n):
    lst.append([])
    for j in range(m):
      lst[i].append(arr[j][i])

  return lst

cpdef list CLU(list dim,list z,list copy,int isComp ):

  cdef int i = 0
  cdef int rowC = 0
  cdef int mn = min(dim)
  cdef int d0 = dim[0]
  cdef int d1 = dim[1]
  cdef complex cprod = 1
  cdef double prod = 1
  cdef int i2
  cpdef k,k0,m,j

  cdef list temp = copy
  cdef list L = z
  cdef list rowMulti = []
  cdef list old = []
  cdef list dia = []

  while i <mn:
    #Swap lines if diagonal has 0, stop when you find a non zero in the column
    if temp[i][i]==0:
      try:
          i2=i
          old=temp[i][:]
          while temp[i2][i]==0 and i2<mn:
              rowC+=1
              i2+=1
          temp[i]=temp[i2][:]
          temp[i2]=old[:]
      except:
          return [None,0,None]
        
    #Loop through the ith column find the coefficients to multiply the diagonal element with
    #to make the elements under [i][i] all zeros
    rowMulti = []
    if isComp:
      for j in range(i+1,d0):
        rowMulti.append(complex(round((temp[j][i]/temp[i][i]).real,8),round((temp[j][i]/temp[i][i]).real,8)))
    else:
      for j in range(i+1,d0):
        rowMulti.append(round(temp[j][i]/temp[i][i],8))
    #Loop to substitute ith row times the coefficient found from the i+n th row (n>0 & n<rows)
    k0=0
    for k in range(i+1,d0):
      for m in range(d1):
        temp[k][m]-=rowMulti[k0]*temp[i][m]
      #Lower triangular matrix
      L[k][i]=rowMulti[k0]
      k0+=1
    #Get the diagonal for determinant calculation  
    dia.append(temp[i][i])
    i+=1
  
  if isComp:
    for i in range(mn):
      cprod*=dia[i]
    return [temp,((-1)**(rowC))*cprod,L]

  for i in range(mn):
    prod*=dia[i]
  return [temp,((-1)**(rowC))*prod,L]