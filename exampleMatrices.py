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
for matrix in [proj,v,o,a,b,validStr1,validStr2,validStr3,validStr4,c,d,e,f,g,p,q,k,l,m]:
    print(matrix)
 
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')
print("Attribute call outputs\n")
print("d:\n")
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
print("e.matrix:\n",e.matrix,"\n")
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
Numbers' range: [-56, -56]
Average: -56.0000

-56 


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
Numbers' range: [-106, 55]
Average: -14.0000

-106  -10   15   55 
  25    7   -8  -90 


Float Matrix

Dimension: 4x3
Numbers' range: [-80.3815, 58.1863]
Average: -15.2444

 58.186300 -49.063500  14.934500 
-7.124800  47.541400 -51.917800 
-80.381500 -26.015900 -18.285100 
-13.844100 -29.545500 -27.416900 


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
Numbers' range: [-853.1011, 821.3486]
Average: 97.2878

-46.425100  643.452100 -223.126200  258.810800 -11.476300 -277.083300 
 452.486100  188.491600  498.730900  162.632400 -351.695600  197.506100 
 532.538000   97.604000 -91.835600    2.190500 -613.033300  292.662400 
-343.021300  550.323900  391.022200 -342.830400   22.295600   34.959900 
  34.310000 -19.141700 -506.401900 -853.101100  705.285800  821.348600 
 386.593000 -130.179800  437.507800  110.937300  433.379700   56.644000 


Dimension: 3x6
Numbers' range: [-118, 120]
Average: 15.8889

  57   88   13   30    1  120 
  20  -66   92 -118  -63  -89 
 -47   58  -59   57   75  117 


Square matrix
Dimension: 5x5
Numbers' range: [2, 100]
Average: 47.7600

 63  42  99  22   2 
100  72  31  81  65 
  8  50  56  66  45 
 37  15  19  60  61 
  8  66  42  46  38 


Float Matrix

Square matrix
Dimension: 4x4
Numbers' range: [-83.0492, 80.1419]
Average: -4.9059

-62.347100 -64.780700 -30.928700  55.561800 
 36.535200 -15.933000  47.481900 -72.170000 
 31.956200 -6.432700  80.141900 -36.710000 
  2.424800  31.215400   8.539800 -83.049200 

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
Numbers' range: [-80.3815, 58.1863]
Average: -15.2444

 58.186300 -49.063500  14.934500 
-7.124800  47.541400 -51.917800 
-80.381500 -26.015900 -18.285100 
-13.844100 -29.545500 -27.416900 

d.matrix:

[[58.1863, -49.0635, 14.9345], [-7.1248, 47.5414, -51.9178], [-80.3815, -26.0159, -18.2851], [-13.8441, -29.5455, -27.4169]]
################
f.subM(1,4,2,3):
 
Float Matrix

Dimension: 4x2
Numbers' range: [-223.1262, 643.4521]
Average: 256.8329

 643.452100 -223.126200 
 188.491600  498.730900 
  97.604000 -91.835600 
 550.323900  391.022200 
 

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
 97.2878 

################
g:
 
Dimension: 3x6
Numbers' range: [-118, 120]
Average: 15.8889

  57   88   13   30    1  120 
  20  -66   92 -118  -63  -89 
 -47   58  -59   57   75  117 

################
g.remove(3):


Dimension: 2x6
Numbers' range: [-118, 120]
Average: 7.0833

  57   88   13   30    1  120 
  20  -66   92 -118  -63  -89 

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
matrices
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
Numbers' range: [-118, 92]
Average: 14.5000

  57   88   13   30 
  20  -66   92 -118 
 

j.summary
 Matrix(dim=[2, 4],listed=[[57, 88, 13, 30], [20, -66, 92, -118]],inRange=[-118, 92],rangeLock=0,randomFill=1)
################
Only give 1 argument, row/column! Or it will return an error like so
proj.remove(5,15):

Bad arguments
None
################
p: 
Square matrix
Dimension: 5x5
Numbers' range: [2, 100]
Average: 47.7600

 63  42  99  22   2 
100  72  31  81  65 
  8  50  56  66  45 
 37  15  19  60  61 
  8  66  42  46  38 

p.det:
 388292764
p.adj:
 
Square matrix
Dimension: 5x5
Numbers' range: [-20982912, 24689286]
Average: 410187.0000

  1669378   3160806  -3155154    262758  -2179933 
 -1138728   2010676  -3835768  -4468328   8335818 
  4387454  -4403290  -1427490   4280486   2120167 
 -4952438   7708702  24689286 -13208110 -20960103 
  2772108  -8622452 -20982912  18963164  19228578 

p.inv:

matrices
Elements may look complicated

Complex Matrix

Square matrix
Dimension: 5x5
Numbers' range: [-0.05403889524966785, 0.06358420318128823]
Average: 0.0011

 0.004299  0.008140  -0.008126  0.000677  -0.005614 
 -0.002933  0.005178  -0.009879  -0.011508  0.021468 
 0.011299  -0.011340  -0.003676  0.011024  0.005460 
 -0.012754  0.019853  0.063584  -0.034016  -0.053980 
 0.007139  -0.022206  -0.054039  0.048837  0.049521 

################
p:

Square matrix
Dimension: 5x5
Numbers' range: [2, 100]
Average: 47.7600

 63  42  99  22   2 
100  72  31  81  65 
  8  50  56  66  45 
 37  15  19  60  61 
  8  66  42  46  38 

p.remove(c=1):
p.remove(r=2):

Square matrix
Dimension: 4x4
Numbers' range: [2, 100]
Average: 45.5625

 42  99  22   2 
 50  56  66  45 
 15  19  60  61 
 66  42  46  38 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Numbers' range: [2, 99]
Average: 47.4500

42 55 99 22  2 
50 55 56 66 45 
15 55 19 60 61 
66 55 42 46 38 

################
r: 
Dimension: 5x4
Numbers' range: [2, 99]
Average: 47.4500

42 50 15 66 
55 55 55 55 
99 56 19 42 
22 66 60 46 
 2 45 61 38 

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
Numbers' range: [-8063.647800000001, 3293.8049]
Average: -51.4480

-8063.647800  2710.076000 -2846.085000 
 3293.804900  1973.424500  2623.739700 

################

((((mMulti)+125)**3)%2):

Float Matrix

Dimension: 2x3
Numbers' range: [0.56671142578125, 1.6859283447265625]
Average: 1.1111

 0.676208 1.425308  0.566711 
1.361824  0.950876 1.685928 

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
Numbers' range: [-90, 84]
Average: 6.6250

  8  78   2  25 
  5 -59  84 -90 

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

