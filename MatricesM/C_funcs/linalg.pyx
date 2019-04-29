
cpdef list Ctranspose(int m,int n,list arr):			
  cdef int i
  cdef int j
  cdef list lst=[]

  for i in range(n):
    lst.append([])
    for j in range(m):
      lst[i].append(arr[j][i])

  return lst