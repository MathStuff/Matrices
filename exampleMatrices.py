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
d=FMatrix(dim=[4,3])
e=Matrix(8,randomFill=0)
f=FMatrix(dim=6,inRange=[-1250,1250])
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
"""PRINT THE MATRICES """
for matrix in [proj,v,o,a,b,validStr1,validStr2,validStr3,validStr4,c,d,e,f,g,p,q,k,l,m]:
    print(matrix)
    
"""PRINT THE IDENTITY MATRICES """
for i in [id1,id2,id3,id4]:
    print(i)
"""ATTRIBUTE CALL EXAMPLES"""    
print('################################')
print("Attribute call outputs\n")
print("d:")
print(d)
print("d.matrix:\n")
print(d.matrix)
print('################')
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print('################')
print("proj.dim:\n",proj.dim,"\n")
print('################')
print("validStr2.inRange:\n",validStr2.inRange,"\n")
print('################')
print("for i in range(len(e.matrix)): e[i][-i-1]=99")
for i in range(len(e.matrix)): e[i][-i-1]=99
print(e)
print('################')
print("f.avg:\n",f.avg,"\n")
print('################')
print("g:\n",g)
print('################')
print("g.remove(3):\n")
g.remove(3)
print(g)
print('################')
h=proj.subM(12,18,5,11)
print("h=proj.subM(12,18,5,11):",h,"\n")
print("h.det:\n")
print(h.det)
print("h.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")
print('################')
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary\n",j.summary)
print('################')
print("Only give 1 argument, row/column! Or it will return an error like so")
print("proj.remove(5,15):\n")
print(proj.remove(5,15))
print('################')
print("p:",p)
print("p.det:\n",p.det)
print("p.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)
print('################')
print("p:")
print(p)
print("p.remove(c=1):")
p.remove(c=1)
print("p.remove(r=2):")
p.remove(r=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55,55])
print(p)
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
Numbers' range: [-47, -47]
Average: -47.0000

-47 


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
Numbers' range: [-109, 101]
Average: -0.1250

  16 -109  -48  -90 
  31   66   32  101 


Float Matrix
Dimension: 4x3
Numbers' range: [-58.0456, 82.2626]
Average: 4.1980

-58.045600 -1.619500  11.660000 
 26.836600  33.807400 -16.396200 
 48.278800 -22.575900 -3.060700 
-4.828800 -45.942300  82.262600 


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


Float Matrix
Square matrix
Dimension: 6x6
Numbers' range: [-804.7608, 773.3867]
Average: 104.8343

 263.921800  101.629800  566.375200  119.477400  162.585500   26.487900 
 576.757100 -433.507400  124.668100  218.727800  0.758400  273.447800 
 460.272600 -325.165700 -157.651300   63.954800  260.381600 -310.987500 
-555.077700 -64.519900  174.499100 -53.258200 -149.905800 -804.760800 
   3.036000  -1.502700  230.429800  656.735400  361.003900  460.470600 
 773.386700  258.508300 -723.879800  575.630300  509.041200  132.064500 


Dimension: 3x6
Numbers' range: [-49, 121]
Average: 42.3889

 19 115  -5 -32  35 110 
-37  26  55  91  60  59 
 10 121  28  69 -49  88 


Square matrix
Dimension: 5x5
Numbers' range: [6, 95]
Average: 49.7600

47 15 23 49 52 
90 24 86 67 67 
25 52 41 38 95 
48  6 75 10 59 
74 60  7 49 85 


Float Matrix
Square matrix
Dimension: 4x4
Numbers' range: [-118.0753, 95.0637]
Average: -4.4878

  95.063700   18.914500  -7.333100  -7.943600 
   2.048400   90.969800   65.578000 -26.326200 
-24.306700 -74.045700    3.224300 -51.632300 
-46.370500 -118.075300    8.854300  -0.424200 

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

d:

Float Matrix
Dimension: 4x3
Numbers' range: [-58.0456, 82.2626]
Average: 4.1980

-58.045600 -1.619500  11.660000 
 26.836600  33.807400 -16.396200 
 48.278800 -22.575900 -3.060700 
-4.828800 -45.942300  82.262600 

d.matrix:

[[-58.0456, -1.6195, 11.66], [26.8366, 33.8074, -16.3962], [48.2788, -22.5759, -3.0607], [-4.8288, -45.9423, 82.2626]]
################
f.subM(1,4,2,3):
 
Float Matrix
Dimension: 4x2
Numbers' range: [-433.5074, 566.3752]
Average: -1.7090

 101.629800  566.375200 
-433.507400  124.668100 
-325.165700 -157.651300 
-64.519900  174.499100 
 

################
proj.dim:
 [20, 20] 

################
validStr2.inRange:
 [-5, 352] 

################
for i in range(len(e.matrix)): e[i][-i-1]=99

Square matrix
Dimension: 8x8
Numbers' range: [0, 0]
Average: 12.3750

0 0 0 0 0 0 0 99 
0 0 0 0 0 0 99 0 
0 0 0 0 0 99 0 0 
0 0 0 0 99 0 0 0 
0 0 0 99 0 0 0 0 
0 0 99 0 0 0 0 0 
0 99 0 0 0 0 0 0 
99 0 0 0 0 0 0 0 

################
f.avg:
 104.8343 

################
g:
 
Dimension: 3x6
Numbers' range: [-49, 121]
Average: 42.3889

 19 115  -5 -32  35 110 
-37  26  55  91  60  59 
 10 121  28  69 -49  88 

################
g.remove(3):


Dimension: 2x6
Numbers' range: [-49, 121]
Average: 41.3333

 19 115  -5 -32  35 110 
-37  26  55  91  60  59 

################
h=proj.subM(12,18,5,11): 
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

Float Matrix
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

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Numbers' range: [3, 99]
Average: 52.1111

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Numbers' range: [-37, 115]
Average: 29.0000

 19 115  -5 -32 
-37  26  55  91 
 

j.summary
 Matrix(dim=[2, 4],listed=[[19, 115, -5, -32], [-37, 26, 55, 91]],inRange=[-37, 115],rangeLock=0,randomFill=1)
################
Only give 1 argument, row/column! Or it will return an error like so
proj.remove(5,15):

Bad arguments
None
################
p: 
Square matrix
Dimension: 5x5
Numbers' range: [6, 95]
Average: 49.7600

47 15 23 49 52 
90 24 86 67 67 
25 52 41 38 95 
48  6 75 10 59 
74 60  7 49 85 

p.det:
 -370634923
p.adj:
 
Square matrix
Dimension: 5x5
Numbers' range: [-10363478, 17565603]
Average: -26111.2800

  1168558    119852   6735591  -3635265  -5814066 
 17565603  -8423421  -4511239   7111614  -4000702 
  6835844  -5662011  -2948256    782976   3032701 
 -6272750  -4051064  -2858808   7674457   4898801 
-10363478   8643205   -788706  -6343723    451505 

p.inv:


Float Matrix
Square matrix
Dimension: 5x5
Numbers' range: [-0.04739327545774741, 0.027961417980032065]
Average: 0.0001

 -0.003153  -0.000323  -0.018173  0.009808  0.015687 
 -0.047393  0.022727  0.012172  -0.019188  0.010794 
 -0.018444  0.015277  0.007955  -0.002113  -0.008182 
 0.016924  0.010930  0.007713  -0.020706  -0.013217 
 0.027961  -0.023320  0.002128  0.017116  -0.001218 

################
p:

Square matrix
Dimension: 5x5
Numbers' range: [6, 95]
Average: 49.7600

47 15 23 49 52 
90 24 86 67 67 
25 52 41 38 95 
48  6 75 10 59 
74 60  7 49 85 

p.remove(c=1):
p.remove(r=2):

Square matrix
Dimension: 4x4
Numbers' range: [6, 95]
Average: 44.7500

15 23 49 52 
52 41 38 95 
 6 75 10 59 
60  7 49 85 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Numbers' range: [6, 95]
Average: 46.8000

15 55 23 49 52 
52 55 41 38 95 
 6 55 75 10 59 
60 55  7 49 85 

################
r: 
Dimension: 5x4
Numbers' range: [6, 95]
Average: 46.8000

15 52  6 60 
55 55 55 55 
23 41 75  7 
49 38 10 49 
52 95 59 85 

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

Float Matrix
Dimension: 2x3
Numbers' range: [-5736.709400000001, 7489.8910000000005]
Average: -695.7940

-5736.709400  1507.531600 -5282.974600 
 1029.014800 -3181.517200  7489.891000 

################

((((mMulti)+125)**3)%2):

Float Matrix
Dimension: 2x3
Numbers' range: [0.04218292236328125, 1.711090087890625]
Average: 0.6948

1.711090  0.347985  0.273499 
 0.948720  0.042183  0.845215 

################

e+50:

Square matrix
Dimension: 8x8
Numbers' range: [50, 149]
Average: 62.3750

 50  50  50  50  50  50  50 149 
 50  50  50  50  50  50 149  50 
 50  50  50  50  50 149  50  50 
 50  50  50  50 149  50  50  50 
 50  50  50 149  50  50  50  50 
 50  50 149  50  50  50  50  50 
 50 149  50  50  50  50  50  50 
149  50  50  50  50  50  50  50 

################

c%j

Dimension: 2x4
Numbers' range: [-26, 32]
Average: 5.3750

 16   6  -3 -26 
 -6  14  32  10 

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

