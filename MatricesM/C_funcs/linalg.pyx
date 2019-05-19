cpdef list Crrechelon(list copy,obj,int cm,list dim):
  """
  Returns reduced row echelon form of the matrix
  """
  
  cdef int cmat = cm
  cdef int i
  cdef int i2
  cdef int i3
  cdef int k
  cdef int m
  cdef int z
  cdef int d0 = dim[0]
  cdef int d1 = dim[1]
  cdef int mn = min(dim)
  cdef double boundary = 1e-10
  cdef complex complx_n
  
  cdef list old
  cdef list zeros = []
  cdef list row1 = []
  cdef list row2 = []
  cdef list temp = copy

  if cmat:
    for i3 in range(d1):
      zeros.append(0j)
  else:
    for i3 in range(d1):
      zeros.append(0)

  for i in range(mn):
    #Find any zero-filled rows and make sure they are on the last row
    if zeros in temp:
      del(temp[temp.index(zeros)])
      temp.append(zeros)
        
    #Swap rows if diagonal is 0       
    if temp[i][i]==0:
      try:
        i2=i
        old=temp[i][:]
        while temp[i2][i]==0 and i2<d0:
          i2+=1
        temp[i]=temp[i2][:]
        temp[i2]=old[:]
      except:
        break 
    #Do the calculations to reduce rows

    row1 = []
    for j in range(d1):
      row1.append(temp[i][j]/temp[i][i])

    temp[i] = row1[:]
    if cmat:
      for k in range(d0):
        if k!=i:
          row2 = []
          for m in range(d1):
            complx_n = temp[k][m]-temp[i][m]*temp[k][i]
            row2.append(complex(round(complx_n.real,12),round(complx_n.imag,12)))
          temp[k] = row2[:]
        else:
          temp[k] = temp[i][:]
    else:
      for k in range(d0):
        if k!=i:
          row2 = [] 
          for m in range(d1):
            row2.append(round(temp[k][m]-temp[i][m]*temp[k][i],12))
          temp[k] = row2[:]
        else:
          temp[k] = temp[i][:]
  #Fix -0.0 issue
  if cmat:
    for i in range(d0):
      for j in range(d1):
        num=temp[i][j]
        if isinstance(num,complex):
          if num.real<boundary and num.real>-boundary:
            num=complex(0,num.imag)
          if num.imag<boundary and num.imag>-boundary:
            num=complex(num.real,0)
        else:
          if str(num)=="-0.0":
            num=0
        
        temp[i][j]=num
  else:
    for i in range(d0):
      for j in range(d1):
        if (temp[i][j]<boundary and temp[i][j]>-boundary):
          temp[i][j] = 0

  z = temp.count(zeros)
  if cmat:
    dt = "complex"
  else:
    dt = "float"
  return [obj((d0,d1),temp,dtype=dt),d0-z]

cpdef list Ctranspose(int m,int n,list arr):			
  cdef int i
  cdef int j
  cdef list lst=[]

  for i in range(n):
    lst.append([])
    for j in range(m):
      lst[i].append(arr[j][i])

  return lst

cpdef list CLU(list dim,list z,list copy,int isComp):

  cdef int i = 0
  cdef int rowC = 0
  cdef int mn = min(dim)
  cdef int d0 = dim[0]
  cdef int d1 = dim[1]
  cdef complex cprod = 1
  cdef double prod = 1
  cdef int i2,k,k0,m,j

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