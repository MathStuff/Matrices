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
Numbers' range: [56, 56]
Average: 56.0000

56 


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
Numbers' range: [-106, 105]
Average: -16.6250

 -47 -106  -27   15 
 -12  105  -52   -9 


Float Matrix

Dimension: 4x3
Numbers' range: [-96.7717, 42.4135]
Average: -13.6979

 22.521700 -96.631000   9.836400 
-96.771700 -21.585100  42.413500 
-27.725700 -4.269200 -2.858100 
 37.969800 -20.493600 -6.781500 


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
Numbers' range: [-728.876, 1085.2446]
Average: 94.2070

-162.363600  374.992200  512.597300   33.510900 -143.956600  317.618800 
-728.876000 1085.244600   12.697100 -363.382900 -343.855300  464.152300 
 115.587500   29.331300 -22.719000 -66.132000  388.409800  150.804000 
-84.107400 -101.124800  849.435700 -105.369100  221.562600  0.119200 
  67.518200   20.564300  114.280000 -124.785500  266.965900   62.840800 
  77.325000  172.828200 -181.247600  347.391800  -6.678800  140.272200 


Dimension: 3x6
Numbers' range: [-118, 118]
Average: 9.7778

  84  -34   -6    9   13  118 
 -44  -34   46   11   54  104 
 -82  102  -10 -118  -39    2 


Square matrix
Dimension: 5x5
Numbers' range: [1, 85]
Average: 51.7200

36  1 57 17 66 
24 44 61 66 85 
78 70 71  3 72 
18 52 72 60 58 
50 61 75 53 43 


Float Matrix

Square matrix
Dimension: 4x4
Numbers' range: [-77.4535, 103.7732]
Average: 3.3176

-28.187400 -77.453500  11.760600 -37.019100 
-11.295800 -9.785300 -5.843800 103.773200 
 11.657200 -59.210900  11.632600 -2.794600 
 31.511900  94.109100 -11.101400  31.329300 

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
Numbers' range: [-96.7717, 42.4135]
Average: -13.6979

 22.521700 -96.631000   9.836400 
-96.771700 -21.585100  42.413500 
-27.725700 -4.269200 -2.858100 
 37.969800 -20.493600 -6.781500 

d.matrix:

[[22.5217, -96.631, 9.8364], [-96.7717, -21.5851, 42.4135], [-27.7257, -4.2692, -2.8581], [37.9698, -20.4936, -6.7815]]
################
f.subM(1,4,2,3):
 
Float Matrix

Dimension: 4x2
Numbers' range: [-101.1248, 1085.2446]
Average: 342.5568

 374.992200  512.597300 
1085.244600   12.697100 
  29.331300 -22.719000 
-101.124800  849.435700 
 

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
 94.2070 

################
g:
 
Dimension: 3x6
Numbers' range: [-118, 118]
Average: 9.7778

  84  -34   -6    9   13  118 
 -44  -34   46   11   54  104 
 -82  102  -10 -118  -39    2 

################
g.remove(3):


Dimension: 2x6
Numbers' range: [-118, 118]
Average: 26.7500

  84  -34   -6    9   13  118 
 -44  -34   46   11   54  104 

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

Complex matrix, Square matrix
Dimension: 7x7
Numbers' range: [-0.07446221620223706, 0.0709854244777385]
Average: -0.0004

 0.00107353  0.02286871  -0.02787239  -0.01959816  0.01551642  0.01754200  0.00813732 
 0.00147009  0.02678839  -0.01742267  -0.02791370  0.01966099  0.02118985  -0.00291488 
 0.00477520  -0.02818736  0.03398555  0.04065869  -0.02413709  -0.03995425  -0.00960566 
 0.00278229  -0.04055486  0.03625478  0.03803534  -0.01213229  -0.03932200  -0.00739729 
 0.03975700  -0.07446222  0.07098542  0.06300893  -0.03173261  -0.06217939  -0.04869045 
 0.00165125  -0.02724464  0.01781397  0.01969845  0.00065067  -0.00112152  -0.01665621 
 -0.01949681  0.06048304  -0.05010673  -0.05451908  0.00963990  0.04711311  0.04102638 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Numbers' range: [-44, 84]
Average: 4.0000

 84 -34  -6   9 
-44 -34  46  11 
 

j.summary
 Matrix(dim=[2, 4],listed=[[84, -34, -6, 9], [-44, -34, 46, 11]],inRange=[-44, 84],rangeLock=0,randomFill=1)
################
Only give 1 argument, row/column! Or it will return an error like so
proj.remove(5,15):

Bad arguments
None
################
p: 
Square matrix
Dimension: 5x5
Numbers' range: [1, 85]
Average: 51.7200

36  1 57 17 66 
24 44 61 66 85 
78 70 71  3 72 
18 52 72 60 58 
50 61 75 53 43 

p.det:
 -262069574
p.adj:
 
Square matrix
Dimension: 5x5
Numbers' range: [-9910538, 11881959]
Average: -157321.4800

 -993830 -3876272   906424 11881959 -8356750 
 5410110  -142144 -3481330 -3840398  2986368 
-4217034  8804258   511972 -9910538  1579338 
  722834 -5292538  3974942  6955384 -6684870 
  -54834 -4123964 -1907672   344682  4870866 

p.inv:


Complex matrix, Square matrix
Dimension: 5x5
Numbers' range: [-0.04533894880906701, 0.03781643877514755]
Average: 0.0006

 0.00379224  0.01479100  -0.00345872  -0.04533895  0.03188752 
 -0.02064379  0.00054239  0.01328399  0.01465412  -0.01139533 
 0.01609128  -0.03359512  -0.00195357  0.03781644  -0.00602641 
 -0.00275818  0.02019516  -0.01516751  -0.02654022  0.02550800 
 0.00020923  0.01573614  0.00727926  -0.00131523  -0.01858616 

################
p:

Square matrix
Dimension: 5x5
Numbers' range: [1, 85]
Average: 51.7200

36  1 57 17 66 
24 44 61 66 85 
78 70 71  3 72 
18 52 72 60 58 
50 61 75 53 43 

p.remove(c=1):
p.remove(r=2):

Square matrix
Dimension: 4x4
Numbers' range: [1, 85]
Average: 51.9375

 1 57 17 66 
70 71  3 72 
52 72 60 58 
61 75 53 43 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Numbers' range: [1, 75]
Average: 52.5500

 1 55 57 17 66 
70 55 71  3 72 
52 55 72 60 58 
61 55 75 53 43 

################
r: 
Dimension: 5x4
Numbers' range: [1, 75]
Average: 52.5500

 1 70 52 61 
55 55 55 55 
57 71 72 75 
17  3 60 53 
66 72 58 43 

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
Numbers' range: [-9331.2807, 10517.4212]
Average: 1114.2666

10517.421200  6637.542000 -4982.695600 
-9331.280700 -700.422700  4545.035400 

################

((((mMulti)+125)**3)%2):

Float Matrix

Dimension: 2x3
Numbers' range: [0.479248046875, 1.7314453125]
Average: 1.0117

 0.479248  0.599915 1.375488 
1.731445 1.147099  0.736740 

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
Numbers' range: [-31, 40]
Average: 4.3750

 37  -4  -3   6 
-12 -31  40   2 

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

