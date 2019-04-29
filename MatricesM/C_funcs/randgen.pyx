from libc.stdlib cimport rand,RAND_MAX
from random import uniform

cpdef list getfill(int m,int n,num):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(num)
	return lst
	
cpdef list igetrand(int m,int n):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(round(<float>rand()/RAND_MAX))
	return lst

cpdef list getuni(int m,int n,int k,int l):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(uniform(k,l))
	return lst
	
cpdef list igetuni(int m,int n,int k,int l):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(<int>uniform(k,l))
	return lst