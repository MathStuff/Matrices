# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from matrices import Matrix,FMatrix,CMatrix,Identity

# =============================================================================
"""Example Inputs"""      
# =============================================================================
projectGrid="""08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"""

#Valid Matrices
proj=Matrix(listed=projectGrid)
v=Matrix()
o=Matrix(dim=8,randomFill=0)
a=Matrix(0)
b=Matrix(1)
c=Matrix(dim=[2,4])
d=Matrix(dim=[4,3])
e=Matrix(8,randomFill=0)
f=Matrix(dim=6,inRange=[-1250,1250])
g=Matrix(dim=[3,6])
p=Matrix(5,inRange=[0,100])
q=FMatrix(4)
#String inputs Matrices
validStr1=Matrix(dim=[2,3],listed=" 34-52\n33a c9d88 hello\n--3-")
validStr2=Matrix(listed="312as45\ndid12,,,44\ncc352as45\ndid12,,,44\ncc3-5")
validStr3=Matrix(listed="\n\n\ndd34 5\n\n44\nn659")
validStr4=Matrix(dim=[22,3],listed="""ulke,boy,kilo,yas,cinsiyet
tr,130,30,10,e
tr,125,36,11,e
tr,135,34,10,k
tr,133,30,9,k
tr,129,38,12,e
tr,180,90,30,e
tr,190,80,25,e
tr,175,90,35,e
tr,177,60,22,k
us,185,105,33,e
us,165,55,27,k
us,155,50,44,k
us,160,58,39,k
us,162,59,41,k
us,167,62,55,k
fr,174,70,47,e
fr,193,90,23,e
fr,187,80,27,e
fr,183,88,28,e
fr,159,40,29,k
fr,164,66,32,k
fr,166,56,42,k
""")

#InvalidMatrices
k=Matrix(dim=-1)
l=Matrix(inRange=[0])
m=Matrix(inRange=[0,0],rangeLock=1)

#Identity Matrices
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
for matrix in [proj,v,o,a,b,validStr1,validStr2,validStr3,validStr4,c,d,e,f,g,p,q,k,l,m]:
    print(matrix)
 
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')
print("Attribute call outputs\n")
print("d.matix:\n",d.matrix,"\n")
print('################')
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print('################')
print("proj.dim:\n",proj.dim,"\n")
print('################')
print("validStr2.inRange:\n",validStr2.inRange,"\n")
print('################')
print("e.matrix:\n",e.matrix,"\n")
print('################')
print("f.avg:\n",f.avg,"\n")
print('################')
print("g:\n",g)
print('################')
print("g.delRC(3):\n")
g.delRC(3)
print(g)
print('################')
h=proj.subM(12,18,5,11)
print("h=proj.Msub(12,18,5,11):\n",h,"\n")
print("h.det:\n")
print(h.det)
print("\nh.inv:")
print(h.inv)
print('################')
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary\n",j.summary)
print('################')
print("Only give 1 argument, row/column! Or it will return an error like so")
print("proj.delRC(5,15):\n")
print(proj.delRC(5,15))
print('################')
print("p:",p)
print("p.det:\n",p.det)
print("p.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)
print('################')
r=p.t
print("r:",r)
print("p==r.t:\n")
print(p==r.t)
print("################")
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)
print('################')
print("id3:\n")
print(id3)
print('################')
print("id4:\n")
print(id4)
print("\nid4.delDim(6):\n")
print(id4.delDim(6))
print('################')
print("id4:",id4)
print("\nid4.addDim(10)):\n",id4.addDim(10))
print("################################")
print("Operator examples")
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("################")
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))
print("################")
print("\ne+50:")
print(e+50)
print("################")
print("\nc%j")
print(c%j)
print("################")
print("\na<b")
print(a<b)
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print('################')
    print("validStr",numb,":\n")
    print(strings)         
    print('################')
print("")
# =============================================================================
""" Expected Outputs """
# =============================================================================
"""

Square matrix
Dimension: 20x20
Numbers' range: [0, 99]
Average: 47.2250

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 12 50 77 91  8 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48  4 56 62  0 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30  3 49 13 36 65 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 71 37  2 36 91 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80 
24 47 32 60 99  3 45  2 44 75 33 53 78 36 84 20 35 17 12 50 
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70 
67 26 20 68  2 62 12 20 95 63 94 39 63  8 40 91 66 49 94 21 
24 55 58  5 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72 
21 36 23  9 75  0 76 44 20 45 35 14  0 61 33 97 34 31 33 95 
78 17 53 28 22 75 31 67 15 94  3 80  4 62 16 14  9 53 56 92 
16 39  5 42 96 35 31 47 55 58 88 24  0 17 54 24 36 29 85 57 
86 56  0 48 35 71 89  7  5 44 44 37 44 60 21 58 51 54 17 58 
19 80 81 68  5 94 47 69 28 73 92 13 86 52 17 77  4 89 55 40 
 4 52  8 83 97 35 99 16  7 97 57 32 16 26 26 79 33 27 98 66 
88 36 68 87 57 62 20 72  3 46 33 67 46 55 12 32 63 93 53 69 
 4 42 16 73 38 25 39 11 24 94 72 18  8 46 29 32 40 62 76 36 
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74  4 36 16 
20 73 35 29 78 31 90  1 74 31 49 71 48 86 81 16 23 57  5 54 
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67  4 


Square matrix
Dimension: 0x0
Numbers' range: [0, 0]
Average: None



Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 0.0000

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 0x0
Numbers' range: [0, 0]
Average: None



Square matrix
Dimension: 1x1
Numbers' range: [118, 118]
Average: 118.0000

118 


Dimension: 2x3
Numbers' range: [-52, 88]
Average: 18.1667

 34 -52  33 
  9  88  -3 


Dimension: 1x10
Numbers' range: [-5, 352]
Average: 86.4000

312  45  12  44 352  45  12  44   3  -5 


Dimension: 4x1
Numbers' range: [5, 65]
Average: 37.0000

34 
 5 
44 
65 


Dimension: 22x3
Numbers' range: [9, 193]
Average: 84.7273

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 


Dimension: 2x4
Numbers' range: [-92, 68]
Average: -3.2500

 68  30 -54 -27 
 46 -92 -44  47 


Dimension: 4x3
Numbers' range: [-108, 124]
Average: 12.5833

   8   -1   44 
   5  112   27 
   6  -93  -44 
 124 -108   71 


Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 0.0000

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 6x6
Numbers' range: [-1231, 1203]
Average: 10.2500

 -288   113  -405  -610 -1165  -813 
 -732   125   193  1056 -1022  -701 
 -900   465    61    65  1049   925 
-1167  -672    20   681   853   -39 
  934   131   896   701   367   392 
  672  -428  -473 -1231  1203   113 


Dimension: 3x6
Numbers' range: [-85, 124]
Average: 33.0000

  8  87 -47 118 114 -35 
-29 -46  76  90  96 -22 
 27  75 -85  -9  52 124 


Square matrix
Dimension: 5x5
Numbers' range: [3, 89]
Average: 50.7200

25 62 47 83 54 
59 33 62 72 64 
51 69 32  3 24 
48 89 84 62 35 
89  4 19 77 21 


Float Matrix

Square matrix
Dimension: 4x4
Numbers' range: [-107.9473, 48.0011]
Average: -12.8543

 -0.777100 -107.947300 -61.729400   22.501900 
  21.518300 -44.893000 -61.568000   48.001100 
-31.185900   30.098800    9.070500  -3.188700 
  31.918700 -54.182800  0.000000  -3.306400 

Invalid matrix

Invalid matrix

Invalid matrix


Identity Matrix
Dimension: 1x1

1 


Identity Matrix
Dimension: 5x5

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 


Square matrix
Dimension: 3x3
Numbers' range: [0, 1]
Average: 0.3333

1 0 0 
0 1 0 
0 0 1 


Identity Matrix
Dimension: 6x6

1 0 0 0 0 0 
0 1 0 0 0 0 
0 0 1 0 0 0 
0 0 0 1 0 0 
0 0 0 0 1 0 
0 0 0 0 0 1 

################################
Attribute call outputs

d.matix:
 [[8, -1, 44], [5, 112, 27], [6, -93, -44], [124, -108, 71]] 

################
f.subM(1,4,2,3):
 
Dimension: 4x2
Numbers' range: [-672, 465]
Average: -12.5000

 113 -405 
 125  193 
 465   61 
-672   20 
 

################
proj.dim:
 [20, 20] 

################
validStr2.inRange:
 [-5, 352] 

################
e.matrix:
 [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]] 

################
f.avg:
 10.2500 

################
g:
 
Dimension: 3x6
Numbers' range: [-85, 124]
Average: 33.0000

  8  87 -47 118 114 -35 
-29 -46  76  90  96 -22 
 27  75 -85  -9  52 124 

################
g.delRC(3):


Dimension: 2x6
Numbers' range: [-85, 124]
Average: 34.1667

  8  87 -47 118 114 -35 
-29 -46  76  90  96 -22 

################
h=proj.Msub(12,18,5,11):
 
Square matrix
Dimension: 7x7
Numbers' range: [3, 99]
Average: 51.5306

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 
 

h.det:

1287494735580

h.inv:
Elements may look complicated

Complex Matrix

Square matrix
Dimension: 7x7
Numbers' range: [-0.07446221620223706, 0.0709854244777385]
Average: -0.0004

 0.001074  0.022869  -0.027872  -0.019598  0.015516  0.017542  0.008137 
 0.001470  0.026788  -0.017423  -0.027914  0.019661  0.021190  -0.002915 
 0.004775  -0.028187  0.033986  0.040659  -0.024137  -0.039954  -0.009606 
 0.002782  -0.040555  0.036255  0.038035  -0.012132  -0.039322  -0.007397 
 0.039757  -0.074462  0.070985  0.063009  -0.031733  -0.062179  -0.048690 
 0.001651  -0.027245  0.017814  0.019698  0.000651  -0.001122  -0.016656 
 -0.019497  0.060483  -0.050107  -0.054519  0.009640  0.047113  0.041026 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Numbers' range: [-47, 118]
Average: 32.1250

  8  87 -47 118 
-29 -46  76  90 
 

j.summary
 Matrix(dim=[2, 4],listed=[[8, 87, -47, 118], [-29, -46, 76, 90]],inRange=[-47, 118],rangeLock=0,randomFill=1)
################
Only give 1 argument, row/column! Or it will return an error like so
proj.delRC(5,15):

Bad arguments
None
################
p: 
Square matrix
Dimension: 5x5
Numbers' range: [3, 89]
Average: 50.7200

25 62 47 83 54 
59 33 62 72 64 
51 69 32  3 24 
48 89 84 62 35 
89  4 19 77 21 

p.det:
 871956833
p.adj:
 
Square matrix
Dimension: 5x5
Numbers' range: [-18094990, 17452413]
Average: 696026.3200

 -7213625   1901459   7602738  -1899043   7230627 
 10800231 -12406612   9536780   -520261      6529 
-17705358  11583066 -11832227  17452413  -5337519 
 10347824  -9136839  -8997483   2850582   6768782 
  6591955  17326426   9658462 -18094990  -9113259 

p.inv:

Elements may look complicated

Complex Matrix

Square matrix
Dimension: 5x5
Numbers' range: [-0.02075216262454589, 0.0200152259142856]
Average: 0.0008

 -0.008273  0.002181  0.008719  -0.002178  0.008292 
 0.012386  -0.014228  0.010937  -0.000597  0.000007 
 -0.020305  0.013284  -0.013570  0.020015  -0.006121 
 0.011867  -0.010479  -0.010319  0.003269  0.007763 
 0.007560  0.019871  0.011077  -0.020752  -0.010452 

################
r: 
Square matrix
Dimension: 5x5
Numbers' range: [3, 89]
Average: 50.7200

25 59 51 48 89 
62 33 69 89  4 
47 62 32 84 19 
83 72  3 62 77 
54 64 24 35 21 

p==r.t:

Same dimension
Same average
All the elements and their positions are same!
True
################
id2:
 
Identity Matrix
Dimension: 5x5

1 0 0 0 0 
0 1 0 0 0 
0 0 1 0 0 
0 0 0 1 0 
0 0 0 0 1 


id2.addDim(2): 
Identity Matrix
Dimension: 7x7

1 0 0 0 0 0 0 
0 1 0 0 0 0 0 
0 0 1 0 0 0 0 
0 0 0 1 0 0 0 
0 0 0 0 1 0 0 
0 0 0 0 0 1 0 
0 0 0 0 0 0 1 

id2.matrix:
 [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]
################
id3:


Square matrix
Dimension: 3x3
Numbers' range: [0, 1]
Average: 0.3333

1 0 0 
0 1 0 
0 0 1 

################
id4:


Identity Matrix
Dimension: 6x6

1 0 0 0 0 0 
0 1 0 0 0 0 
0 0 1 0 0 0 
0 0 0 1 0 0 
0 0 0 0 1 0 
0 0 0 0 0 1 


id4.delDim(6):

All rows have been deleted

Identity Matrix
Dimension: 0x0


################
id4: 
Identity Matrix
Dimension: 0x0



id4.addDim(10)):
 
Identity Matrix
Dimension: 10x10

1 0 0 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 0 0 
0 0 0 1 0 0 0 0 0 0 
0 0 0 0 1 0 0 0 0 0 
0 0 0 0 0 1 0 0 0 0 
0 0 0 0 0 0 1 0 0 0 
0 0 0 0 0 0 0 1 0 0 
0 0 0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 0 0 1 

################################
Operator examples

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Dimension: 2x3
Numbers' range: [-11334, 11230]
Average: 1910.6667

 -2978  11230   4261 
  5472 -11334   4813 

################

((((mMulti)+125)**3)%2):

Dimension: 2x3
Numbers' range: [0, 1]
Average: 0.6667

1 1 0 
1 1 0 

################

e+50:

Square matrix
Dimension: 8x8
Numbers' range: [50, 50]
Average: 50.0000

50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 
50 50 50 50 50 50 50 50 

################

c%j

Dimension: 2x4
Numbers' range: [-12, 91]
Average: 23.1250

  4  30  -7  91 
-12   0  32  47 

################

a<b
Lower dimension!
True
################
validStr 0 :


Dimension: 2x3
Numbers' range: [-52, 88]
Average: 18.1667

 34 -52  33 
  9  88  -3 

################
################
validStr 1 :


Dimension: 1x10
Numbers' range: [-5, 352]
Average: 86.4000

312  45  12  44 352  45  12  44   3  -5 

################
################
validStr 2 :


Dimension: 4x1
Numbers' range: [5, 65]
Average: 37.0000

34 
 5 
44 
65 

################
################
validStr 3 :


Dimension: 22x3
Numbers' range: [9, 193]
Average: 84.7273

130  30  10 
125  36  11 
135  34  10 
133  30   9 
129  38  12 
180  90  30 
190  80  25 
175  90  35 
177  60  22 
185 105  33 
165  55  27 
155  50  44 
160  58  39 
162  59  41 
167  62  55 
174  70  47 
193  90  23 
187  80  27 
183  88  28 
159  40  29 
164  66  32 
166  56  42 

################
"""
# =============================================================================

