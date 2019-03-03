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

# =============================================================================
# Valid Matrices
# =============================================================================
o=Matrix(8,randomFill=0)
b=Matrix(1)
c=Matrix(dim=[2,4],ranged=[-50,50])
d=FMatrix([4,3])
e=Matrix(8,randomFill=0)
f=FMatrix(dim=6,ranged=[-1250,1250])
g=Matrix(dim=[3,6],ranged=[2,10])
p=Matrix(5,ranged=[0,100])
q=FMatrix(4)
y=Matrix(3,listed=[3,5,7,8,3,4,5,2,5])
c1=CMatrix(5)
c2=CMatrix([7,3],ranged=[-10,10])
# =============================================================================
# String inputs Matrices
# =============================================================================
proj=Matrix(20,listed=projectGrid)
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
""",features=["Height","Weight","Age"])

# =============================================================================
# InvalidMatrices
# =============================================================================
#You have to give the matrix a valid dimension, or a list to get a dimension, or it won't be a valid matrix

#a=Matrix(0)
#v=Matrix()
#k=Matrix(dim=-1)
#l=Matrix(ranged=[0])
#m=Matrix(randomFill=1)

# =============================================================================
# Identity Matrices
# =============================================================================
id1=Identity()
id2=Identity(5)
id3=id2.subM(3,3)
id4=Identity(6)

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
l=[proj,o,b,c,d,e,f,g,p,q,y,c1,c2]
for matrix in l:
    print(matrix)
print('################################')     
# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving strings or a directory")
for matrix in [validStr1,validStr2,validStr3,validStr4]:
    print(matrix)
print('################################') 
# =============================================================================
"""PRINT THE IDENTITY MATRICES """
# =============================================================================
print('################################') 
print("Identity matrices")
for i in [id1,id2,id3,id4]:
    print(i)
print('################################')     
# =============================================================================
"""PROPERTIES, METHODS CALLS"""   
# =============================================================================
print('################################')  
print("Attribute call outputs\n")
print('################\n')
      
print("d:")
print(d)
print("d.matrix:\n")
print(d.matrix)

print('\n################\n')
      
print("f.subM(1,4,2,3):\n",f.subM(1,4,2,3),"\n")
print(f)
print("f.delDim(4)")
print(f)
print("f.uptri.p")
f.uptri.p
print("f.lowtri.p")
f.lowtri.p
print("f-(f.lowtri@f.uptri)")
print(f-(f.lowtri@f.uptri))
print('################')
      
print("g.dim:\n",g.dim)
print("g.ranged():\n",g.ranged())
print("g:",g)      
print("g.remove(3):")
g.remove(3)
print(g)

print('################')
      
h=proj.subM(12,18,5,11)
print("h=proj.subM(12,18,5,11):\n",h)
print("h.mean():",h.mean())
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.rrechelon:",h.rrechelon)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4):\n",h.minor(3,4),"\n")

print('################')
      
j=g.subM(1,2,1,4)
print("j=g.sub(1,2,1,4):\n",j,"\n")
print("j.summary:\n",j.summary)

print('\n################')
      
print("proj=proj.subM(5,15).copy:\n")
proj=proj.subM(5,15).copy
print(proj)

print('################')
      
print("p:",p)
print("p.det:\n",p.det)
print("\np.adj:\n",p.adj)
print("p.inv:\n")
print(p.inv)

print('################')
      
print("p:")
print(p)
print("p.remove(c=1) and p.remove(r=2)")
p.remove(c=1)
p.remove(r=2)
print(p)
print("p.add(col=2,lis=[55,55,55,55,55]):")
p.add(col=2,lis=[55,55,55,55])
print(p)
print("p.sdev()")
print(p.sdev())
print('################\n')
      
r=p.t
print("r:",r)
print("p==r.t:\n")
print(p==r.t)

print("################")
      
print("id2:\n",id2)
print("\nid2.addDim(2):",id2.addDim(2))
print("id2.matrix:\n",id2.matrix)

print('\n################')
      
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

# =============================================================================
"""OPERATIONS ON ELEMENTS"""    
# =============================================================================

print("################################")   
print("Operator examples")
print("################")
      
print("\nc.dim=",c.dim," d.dim:",d.dim)
print("\nmMulti=c@d:")
mMulti=c@d
print(mMulti)
print("\n((((mMulti)+125)**3)%2):")
print(((((mMulti)+125)**3)%2))

print("################\n")
      
print("f:\n",f)
print("f1=f.intForm")
f1=f.intForm
print(f1)
print("f2=f.roundForm(3)")
f2=f.roundForm(2)
print(f2)
print("f2-f1")
f3=f2-f1
print(f3)

print("################")
      
print("r.remove(r=2):")
r.remove(r=2)
print(r)
print("r.rank:",r.rank)
print("\nr[0]=r[1][:]")
r[0]=r[1][:]
print(r)
print("r.rank:",r.rank)    

print("################")
      
print("for i in range(len(e.matrix)): e[i][-i-1]=99")
for i in range(len(e.matrix)):e[i][i]=99
print(e)
print("\ne+=50:")
e+=50
print(e)
print("for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:\n")
for i in range(len(e.matrix)):e[i]=[b%2 for b in e[i]]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("\n(f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)")
print((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4))
# =============================================================================
""" STRING MATRICES' OUTPUTS"""
# =============================================================================
print("\n################################")
print("Strings' matrices:")
print("################\n")
      
for numb,strings in enumerate([validStr1,validStr2,validStr3,validStr4]):
    print("validStr"+str(numb+1)+":")
    print(strings)         
    print('################')
print("")
# =============================================================================
"""Basic statistical properties"""
# =============================================================================
print("validStr4.ranged()")
print(validStr4.ranged())
print("")

print("validStr4.mean()")
print(validStr4.mean())
print("")

print("validStr4.sdev()")
print(validStr4.sdev())
print("")

print("validStr4.median()")
print(validStr4.median())
print("")

print("validStr4.freq()")
print(validStr4.freq())
print("")

print("validStr4.mode()")
print(validStr4.mode())
print("")

print("validStr4.iqr()")
print(validStr4.iqr())
print("")

print("validStr4.iqr(as_quartiles=True)")
print(validStr4.iqr(as_quartiles=True))
print("")

print("validStr4.variance()")
print(validStr4.variance())
print("")

# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14', 'Col 15', 'Col 16', 'Col 17', 'Col 18', 'Col 19', 'Col 20']

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
 1 70 54 71 83 51 54 69 16 92 33 48 61 43 52  1 89 19 67 48 


Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 
0 0 0 0 0 0 0 0 


Square matrix
Dimension: 1x1
Features: ['Col 1']

0 


Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 19  15 -35 -27 
 -4  36 -28  42 


Float Matrix
Dimension: 4x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.1230 0.8669 0.3138 
0.9186 0.9908 0.4717 
0.8515 0.6386 0.3229 
0.1280 0.1708 0.5337 


Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

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
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117.7480  -558.8427  -638.5561 -1001.2593  -676.6451  1190.3722 
 -229.9265   -62.5781  -853.6014  1245.4437   738.8377  -565.5183 
 -332.0315  -602.3023   680.3777   234.9903    61.9303  1064.0573 
-1195.7894  -143.4261   890.3582  -744.5622   119.2386   790.4302 
  -70.3920  -345.1915  -586.3075   895.9533  -787.5995   197.9224 
 -786.2408   384.8959   815.4934   885.1350  -251.6598  1020.6173 


Dimension: 3x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

6 7 5 5 5 5 
8 4 7 8 1 6 
4 8 3 2 5 4 


Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

 1 47 31 22 95 
70 31 16 11 55 
18 94 96 13  4 
38  8 54 15 86 
39 82 78 77 92 


Float Matrix
Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

0.7087 0.8936 0.4755 0.5141 
1.0000 0.3854 0.1121 0.3202 
0.8894 0.0497 0.5637 0.2870 
0.1156 0.2626 0.3391 0.6626 


Square matrix
Dimension: 3x3
Features: ['Col 1', 'Col 2', 'Col 3']

3 5 7 
8 3 4 
5 2 5 


Complex Matrix
Square matrix
Dimension: 5x5

  0.6387+0.485j   0.8559+0.5201j   0.7376+0.0703j   0.3109+0.5153j   0.7801+0.4143j  
   0.73+0.2473j    0.553+0.3484j   0.6345+0.1421j   0.9168+0.0408j   0.7601+0.6701j  
 0.0463+0.7996j   0.5194+0.3735j    0.008+0.8176j    0.582+0.1993j   0.6091+0.1031j  
 0.9391+0.4046j   0.0373+0.3293j   0.7929+0.5407j   0.2081+0.3476j   0.5489+0.5409j  
  0.9672+0.845j   0.3358+0.1705j    0.052+0.9523j   0.2263+0.0526j    0.867+0.6606j  


Complex Matrix
Dimension: 7x3

  6.7185-6.0631j   -8.3036+1.1578j   -0.5816+3.1495j  
 -0.7824-9.3388j     2.2122-6.217j   -4.1402+5.4784j  
 -2.1225+1.2082j     2.9757+5.354j   -2.9657-7.7466j  
 -0.8815+4.8111j    5.0208+1.2862j    4.4207-5.8869j  
  6.7543+3.7432j    4.9278+9.1271j   -3.9865-7.9569j  
  9.7393+5.5074j    1.2484+4.1435j   -8.8612-3.6594j  
 -1.0447-7.4864j    -2.7755+9.905j    2.7611-6.1739j  

################################
################################
Matrices created by giving strings or a directory

Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

 34 -52  33 
  9  88  -3 

You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x10
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10']

312  45  12  44 352  45  12  44   3  -5 

You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 34   5  44 659 


Dimension: 22x3
Features: ['Height', 'Weight', 'Age']

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

################################
################################
Identity matrices

Identity Matrix
Dimension: 1x1

 1 


Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 

################################
################################
Attribute call outputs

################

d:

Float Matrix
Dimension: 4x3
Features: ['Col 1', 'Col 2', 'Col 3']

0.1230 0.8669 0.3138 
0.9186 0.9908 0.4717 
0.8515 0.6386 0.3229 
0.1280 0.1708 0.5337 

d.matrix:

[[0.12303531479998275, 0.866892471614402, 0.3138418769128597], [0.918631959793716, 0.9908086226343842, 0.47171674931990926], [0.8515167994322641, 0.6386125652280791, 0.32292791450203273], [0.1280342046508044, 0.17080024791377146, 0.5336621617241152]]

################

f.subM(1,4,2,3):
 
Float Matrix
Dimension: 4x2
Features: ['Col 2', 'Col 3']

-558.8427 -638.5561 
 -62.5781 -853.6014 
-602.3023  680.3777 
-143.4261  890.3582 
 


Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117.7480  -558.8427  -638.5561 -1001.2593  -676.6451  1190.3722 
 -229.9265   -62.5781  -853.6014  1245.4437   738.8377  -565.5183 
 -332.0315  -602.3023   680.3777   234.9903    61.9303  1064.0573 
-1195.7894  -143.4261   890.3582  -744.5622   119.2386   790.4302 
  -70.3920  -345.1915  -586.3075   895.9533  -787.5995   197.9224 
 -786.2408   384.8959   815.4934   885.1350  -251.6598  1020.6173 

f.delDim(4)

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117.7480  -558.8427  -638.5561 -1001.2593  -676.6451  1190.3722 
 -229.9265   -62.5781  -853.6014  1245.4437   738.8377  -565.5183 
 -332.0315  -602.3023   680.3777   234.9903    61.9303  1064.0573 
-1195.7894  -143.4261   890.3582  -744.5622   119.2386   790.4302 
  -70.3920  -345.1915  -586.3075   895.9533  -787.5995   197.9224 
 -786.2408   384.8959   815.4934   885.1350  -251.6598  1020.6173 

f.uptri.p

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117.7480  -558.8427  -638.5561 -1001.2593  -676.6451  1190.3722 
    0.0000 -1153.8303 -2100.5100  -709.7155  -582.4474  1758.9217 
    0.0000     0.0000  2845.0038 -1248.6369  -746.5859  1100.3055 
    0.0000     0.0000     0.0000 -5140.0478 -2503.4873  2075.9200 
    0.0000     0.0000     0.0000     0.0000 -1184.4906   106.6332 
    0.0000     0.0000     0.0000    -0.0000     0.0000  1700.4626 

f.lowtri.p

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  1.0000   0.0000   0.0000   0.0000   0.0000   0.0000 
 -1.9527   1.0000   0.0000   0.0000   0.0000   0.0000 
 -2.8198   1.8878   1.0000   0.0000   0.0000   0.0000 
-10.1555   5.0430   1.7569   1.0000   0.0000   0.0000 
 -0.5978   0.5887   0.0944  -0.1621   1.0000   0.0000 
 -6.6773   2.9005   0.9294   0.5022   0.9533   1.0000 

f-(f.lowtri@f.uptri)

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 -0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 -0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 -0.0000 0.0000 -0.0000 -0.0000 0.0000 

################
g.dim:
 [3, 6]
g.ranged():
 {'Col 1': [4, 8], 'Col 2': [4, 8], 'Col 3': [3, 7], 'Col 4': [2, 8], 'Col 5': [1, 5], 'Col 6': [4, 6]}
g: 
Dimension: 3x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

6 7 5 5 5 5 
8 4 7 8 1 6 
4 8 3 2 5 4 

g.remove(3):

Dimension: 2x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

6 7 5 5 5 5 
8 4 7 8 1 6 

################
h=proj.subM(12,18,5,11):
 
Square matrix
Dimension: 7x7
Features: ['Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11']

96 35 31 47 55 58 88 
35 71 89  7  5 44 44 
 5 94 47 69 28 73 92 
97 35 99 16  7 97 57 
57 62 20 72  3 46 33 
38 25 39 11 24 94 72 
72 30 23 88 34 62 99 

h.mean(): {'Col 5': 57.142857142857146, 'Col 6': 50.285714285714285, 'Col 7': 49.714285714285715, 'Col 8': 44.285714285714285, 'Col 9': 22.285714285714285, 'Col 10': 67.71428571428571, 'Col 11': 69.28571428571429}

h.det: 1287494735579.9985

h.rank: 7

h.rrechelon: 
Float Matrix
Square matrix
Dimension: 7x7
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7']

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 


h.inv:

Float Matrix
Square matrix
Dimension: 7x7
Features: ['Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14']

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081 
 0.0015  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029 
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096 
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074 
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487 
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167 
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410 

h.minor(3,4):
 
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 5', 'Col 6', 'Col 7']

96 35 31 55 58 88 
35 71 89  5 44 44 
97 35 99  7 97 57 
57 62 20  3 46 33 
38 25 39 24 94 72 
72 30 23 34 62 99 
 

################
j=g.sub(1,2,1,4):
 
Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

6 7 5 5 
8 4 7 8 
 

j.summary:
 Matrix(dim=[2, 4],listed=[[6, 7, 5, 5], [8, 4, 7, 8]],ranged=[0, 1],randomFill=True,features=['Col 1', 'Col 2', 'Col 3', 'Col 4'],header=False,directory='')

################
proj=proj.subM(5,15).copy:


Dimension: 5x15
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10', 'Col 11', 'Col 12', 'Col 13', 'Col 14', 'Col 15']

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52 
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56 
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 

################
p: 
Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

 1 47 31 22 95 
70 31 16 11 55 
18 94 96 13  4 
38  8 54 15 86 
39 82 78 77 92 

p.det:
 2024686027.9999995

p.adj:
 
Float Matrix
Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

-19185784.0000  27399304.0000   -711796.0000   2398312.0000   1220436.0000 
 23084622.0000  16490688.0000  11368129.0000 -31513797.0000  -4731662.0000 
-16792792.0000 -19612380.0000  12757834.0000  31169462.0000   -626184.0000 
-22759900.0000 -12617120.0000 -17951318.0000  -7845150.0000  39158916.0000 
 20844094.0000    874724.0000  -5622675.0000   7211475.0000  -6535966.0000 

p.inv:


Float Matrix
Square matrix
Dimension: 5x5
Features: ['Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10']

-0.0095  0.0135 -0.0004  0.0012  0.0006 
 0.0114  0.0081  0.0056 -0.0156 -0.0023 
-0.0083 -0.0097  0.0063  0.0154 -0.0003 
-0.0112 -0.0062 -0.0089 -0.0039  0.0193 
 0.0103  0.0004 -0.0028  0.0036 -0.0032 

################
p:

Square matrix
Dimension: 5x5
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5']

 1 47 31 22 95 
70 31 16 11 55 
18 94 96 13  4 
38  8 54 15 86 
39 82 78 77 92 

p.remove(c=1) and p.remove(r=2)

Square matrix
Dimension: 4x4
Features: ['Col 2', 'Col 3', 'Col 4', 'Col 5']

47 31 22 95 
94 96 13  4 
 8 54 15 86 
82 78 77 92 

p.add(col=2,lis=[55,55,55,55,55]):

Dimension: 4x5
Features: ['Col 2', 'Col', 'Col 3', 'Col 4', 'Col 5']

47 55 31 22 95 
94 55 96 13  4 
 8 55 54 15 86 
82 55 78 77 92 

p.sdev()
{'Col 2': 38.69862185315303, 'Col': 0.0, 'Col 3': 28.324018076537094, 'Col 4': 30.412442629073166, 'Col 5': 43.660622991432454}
################

r: 
Dimension: 5x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

47 94  8 82 
55 55 55 55 
31 96 54 78 
22 13 15 77 
95  4 86 92 

p==r.t:

True
################
id2:
 
Identity Matrix
Dimension: 5x5

 1  0  0  0  0 
 0  1  0  0  0 
 0  0  1  0  0 
 0  0  0  1  0 
 0  0  0  0  1 


id2.addDim(2): 
Identity Matrix
Dimension: 7x7

 1  0  0  0  0  0  0 
 0  1  0  0  0  0  0 
 0  0  1  0  0  0  0 
 0  0  0  1  0  0  0 
 0  0  0  0  1  0  0 
 0  0  0  0  0  1  0 
 0  0  0  0  0  0  1 

id2.matrix:
 [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 1]]

################
id3:


Identity Matrix
Dimension: 3x3

 1  0  0 
 0  1  0 
 0  0  1 

################
id4:


Identity Matrix
Dimension: 6x6

 1  0  0  0  0  0 
 0  1  0  0  0  0 
 0  0  1  0  0  0 
 0  0  0  1  0  0 
 0  0  0  0  1  0 
 0  0  0  0  0  1 


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

 1  0  0  0  0  0  0  0  0  0 
 0  1  0  0  0  0  0  0  0  0 
 0  0  1  0  0  0  0  0  0  0 
 0  0  0  1  0  0  0  0  0  0 
 0  0  0  0  1  0  0  0  0  0 
 0  0  0  0  0  1  0  0  0  0 
 0  0  0  0  0  0  1  0  0  0 
 0  0  0  0  0  0  0  1  0  0 
 0  0  0  0  0  0  0  0  1  0 
 0  0  0  0  0  0  0  0  0  1 

################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Float Matrix
Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

-17.1429   4.3700 -12.6726 
 14.1136  21.4940  29.0983 


((((mMulti)+125)**3)%2):

Float Matrix
Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

1.6131 1.5405 0.4473 
1.5575 1.2633 1.7956 

################

f:
 
Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117.7480  -558.8427  -638.5561 -1001.2593  -676.6451  1190.3722 
 -229.9265   -62.5781  -853.6014  1245.4437   738.8377  -565.5183 
 -332.0315  -602.3023   680.3777   234.9903    61.9303  1064.0573 
-1195.7894  -143.4261   890.3582  -744.5622   119.2386   790.4302 
  -70.3920  -345.1915  -586.3075   895.9533  -787.5995   197.9224 
 -786.2408   384.8959   815.4934   885.1350  -251.6598  1020.6173 

f1=f.intForm

Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117  -558  -638 -1001  -676  1190 
 -229   -62  -853  1245   738  -565 
 -332  -602   680   234    61  1064 
-1195  -143   890  -744   119   790 
  -70  -345  -586   895  -787   197 
 -786   384   815   885  -251  1020 

f2=f.roundForm(3)

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

  117.7500  -558.8400  -638.5600 -1001.2600  -676.6500  1190.3700 
 -229.9300   -62.5800  -853.6000  1245.4400   738.8400  -565.5200 
 -332.0300  -602.3000   680.3800   234.9900    61.9300  1064.0600 
-1195.7900  -143.4300   890.3600  -744.5600   119.2400   790.4300 
  -70.3900  -345.1900  -586.3100   895.9500  -787.6000   197.9200 
 -786.2400   384.9000   815.4900   885.1400  -251.6600  1020.6200 

f2-f1

Float Matrix
Square matrix
Dimension: 6x6
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6']

 0.7500 -0.8400 -0.5600 -0.2600 -0.6500  0.3700 
-0.9300 -0.5800 -0.6000  0.4400  0.8400 -0.5200 
-0.0300 -0.3000  0.3800  0.9900  0.9300  0.0600 
-0.7900 -0.4300  0.3600 -0.5600  0.2400  0.4300 
-0.3900 -0.1900 -0.3100  0.9500 -0.6000  0.9200 
-0.2400  0.9000  0.4900  0.1400 -0.6600  0.6200 

################
r.remove(r=2):

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

47 94  8 82 
31 96 54 78 
22 13 15 77 
95  4 86 92 

r.rank: 4

r[0]=r[1][:]

Square matrix
Dimension: 4x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

31 96 54 78 
31 96 54 78 
22 13 15 77 
95  4 86 92 

Determinant is 0, can't get lower/upper triangular matrices
r.rank: 3
################
for i in range(len(e.matrix)): e[i][-i-1]=99

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

99  0  0  0  0  0  0  0 
 0 99  0  0  0  0  0  0 
 0  0 99  0  0  0  0  0 
 0  0  0 99  0  0  0  0 
 0  0  0  0 99  0  0  0 
 0  0  0  0  0 99  0  0 
 0  0  0  0  0  0 99  0 
 0  0  0  0  0  0  0 99 


e+=50:

Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

149  50  50  50  50  50  50  50 
 50 149  50  50  50  50  50  50 
 50  50 149  50  50  50  50  50 
 50  50  50 149  50  50  50  50 
 50  50  50  50 149  50  50  50 
 50  50  50  50  50 149  50  50 
 50  50  50  50  50  50 149  50 
 50  50  50  50  50  50  50 149 

for i in range(len(e.matrixiid)):e[i]=[b%2 for b in e[i]]:


Square matrix
Dimension: 8x8
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8']

1 0 0 0 0 0 0 0 
0 1 0 0 0 0 0 0 
0 0 1 0 0 0 0 0 
0 0 0 1 0 0 0 0 
0 0 0 0 1 0 0 0 
0 0 0 0 0 1 0 0 
0 0 0 0 0 0 1 0 
0 0 0 0 0 0 0 1 

################

c%j

Dimension: 2x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

1 1 0 3 
4 0 0 2 


(f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)
True

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3
Features: ['Col 1', 'Col 2', 'Col 3']

 34 -52  33 
  9  88  -3 

################
validStr2:
You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x10
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4', 'Col 5', 'Col 6', 'Col 7', 'Col 8', 'Col 9', 'Col 10']

312  45  12  44 352  45  12  44   3  -5 

################
validStr3:
You should give proper dimensions to work with the data
Example dimension:[data_amount,feature_amount]

Dimension: 1x4
Features: ['Col 1', 'Col 2', 'Col 3', 'Col 4']

 34   5  44 659 

################
validStr4:

Dimension: 22x3
Features: ['Height', 'Weight', 'Age']

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

validStr4.ranged()
{'Height': [125, 193], 'Weight': [30, 105], 'Age': [9, 55]}

validStr4.mean()
{'Height': 163.36363636363637, 'Weight': 62.13636363636363, 'Age': 28.681818181818183}

validStr4.sdev()
{'Height': 21.077059193407987, 'Weight': 22.286650829472002, 'Age': 12.98858973112413}

validStr4.median()
{'Height': 166, 'Weight': 60, 'Age': 29}

validStr4.freq()
{'Height': {130: 1, 125: 1, 135: 1, 133: 1, 129: 1, 180: 1, 190: 1, 175: 1, 177: 1, 185: 1, 165: 1, 155: 1, 160: 1, 162: 1, 167: 1, 174: 1, 193: 1, 187: 1, 183: 1, 159: 1, 164: 1, 166: 1}, 'Weight': {30: 2, 36: 1, 34: 1, 38: 1, 90: 3, 80: 2, 60: 1, 105: 1, 55: 1, 50: 1, 58: 1, 59: 1, 62: 1, 70: 1, 88: 1, 40: 1, 66: 1, 56: 1}, 'Age': {10: 2, 11: 1, 9: 1, 12: 1, 30: 1, 25: 1, 35: 1, 22: 1, 33: 1, 27: 2, 44: 1, 39: 1, 41: 1, 55: 1, 47: 1, 23: 1, 28: 1, 29: 1, 32: 1, 42: 1}}

validStr4.mode()
{'Height': {'All': 1}, 'Weight': {'90': 3}, 'Age': {'10, 27': 2}}

validStr4.iqr()
{'Height': 25, 'Weight': 40, 'Age': 17}

validStr4.iqr(as_quartiles=True)
{'Height': [155, 166, 180], 'Weight': [40, 60, 80], 'Age': [22, 29, 39]}

validStr4.variance()
{'Height': 444.24242424242414, 'Weight': 496.6948051948051, 'Age': 168.70346320346317}

"""
# =============================================================================

