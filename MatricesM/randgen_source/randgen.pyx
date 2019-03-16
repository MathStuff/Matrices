from random import random
from random import uniform

cpdef list getzeros(int m,int n):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(0)
	return lst
	

cpdef list getrand(int m,int n):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(random())
	return lst
	
cpdef list rgetrand(int m,int n):			
	cdef int i
	cdef int j
	cdef list lst=[]
	for i in range(m):
		lst.append([])
		for j in range(n):
			lst[i].append(round(random()))
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
			lst[i].append(int(uniform(k,l)))
	return lst