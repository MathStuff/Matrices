# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from MatricesM.matrix import Matrix
from MatricesM.constructors.matrices import Identity
try:
    plotting=bool(int(input("Enable plotting ?(0/1) (Requires matplotlib)")))
except:
    plotting=0
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
o=Matrix(8,fill=0)
b=Matrix(1)
c=Matrix(dim=[2,4],ranged=[-50,50])
d=Matrix([4,3],dtype="float")
e=Matrix(8,fill="gauss",ranged=[0,3])
f=Matrix(dim=6,ranged=[-1250,1250],dtype="float")
g=Matrix(dim=[3,6],ranged=[2,10])
p=Matrix(5,ranged=[0,100])
q=Matrix(4,dtype="float")
q1=Matrix(9,decimal=2,dtype="float")
q2=Matrix(6,decimal=6,dtype="float")
y=Matrix(3,listed=[3,5,7,8,3,4,5,2,5])
c1=Matrix(5,dtype="complex")
c2=Matrix([7,3],ranged=[-10,10],dtype="complex")
# =============================================================================
# String inputs Matrices
# =============================================================================
proj=Matrix(20,listed=projectGrid,dtype="integer")
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
""",features=["Height","Weight","Age"],dtype="dataframe",coldtypes=[int]*3)
# =============================================================================
# Identity Matrices
# =============================================================================
id1=Matrix(listed=Identity())
id2=Matrix(listed=Identity(5))
id3=id2[:3,:3]
id4=Matrix(listed=Identity(6))

# =============================================================================
"""PRINT THE MATRICES """
# =============================================================================
print('################################') 
print("Matrices created by giving dimensions")
l=[proj,o,b,c,d,e,f,g,p,q,q1,q2,y,c1,c2]
for matrix in l:
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
      
print("f[:4,1:3]:\n",f[:4,1:3],"\n")
print(f)
print("f.delDim(2)")
f.delDim(2)
print(f)
print("[L,U]=f.LU")
[L,U]=f.LU
print("L.p")
L.p
print("U.p")
U.p
print("f-(L@U)")
print(f-(L@U))
print("[Q,R]=f.QR")
[Q,R]=f.QR
print("Q.p")
Q.p
print("R.p")
R.p
print("f-(Q@R)")
print(f-(Q@R))
print('################')
      
print("g.dim:\n",g.dim)
print("g.ranged():\n",g.ranged())
print("g:",g)      
print("g.remove(3):")
g.remove(3)
print(g)

print('################')
print("q1.decimal",q1.decimal)
q1.p
print("q1.decimal=5")
q1.decimal=5
q1.p
print('################')      
h=proj[11:18,4:11]
print("h=proj[11:18,4:11]:\n",h)
print("h.mean():",h.mean())
print("\nh.det:",h.det)
print("\nh.rank:",h.rank)
print("\nh.rrechelon:",h.rrechelon)
print("\nh.inv:")
print(h.inv)
print("h.minor(3,4,returndet=False):\n",h.minor(3,4,returndet=False),"\n")
print("h.minor(3,4):\n",h.minor(3,4),"\n")
print('################')
      
j=g[:2,:4]
print("j=g.[:2,:4]:\n",j,"\n")
print("j.obj:\n",j.obj)

print('\n################')
      
print("proj=proj[:5,:15]:\n")
proj=proj[:5,:15]
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
print("p.remove(2,1)\np.p")
p.remove(2,1)
p.p
print("p.add(col=2,lis=[55]*4):")
p.add(col=2,lis=[55]*4)
print(p)
print("p.sdev()")
print(p.sdev())

print('################\n')

print("proj.find(40)")
print(proj.find(40))
print("\nproj.find(40,0)")
print(proj.find(40,0))
print("\nproj.find(111)")
proj.find(111)

print("################\n")

print("r=p.t")
r=p.t
print("r.remove(2):")
r.remove(2)
print(r)
print("r.rank:",r.rank)
print("\nr.matrix[0]=r.matrix[1][:]")
r.matrix[0]=r.matrix[1][:]
print(r)
print("r.rank:",r.rank)    

      
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
      
print("e+=Matrix(listed=Identity(e.dim[0]))*99")
e+=Matrix(listed=Identity(e.dim[0]))*99
print(e)
print("\ne-=33:")
e-=33
print(e)
print("\ne+=Matrix(e.dim):")
e+=Matrix(e.dim,dtype="float")
print(e)
print("\ne*=[2,1,1,0.5,0.2,0.0003,1,3]:")
e*=[2,1,1,0.5,0.2,0.0003,1,3]
print(e)
print("e%=[2,2,2,2,1,1,1,1]")
e%=[5,5,5,5,3,3,1,1]
print(e)

print("################")
      
print("\nc%j")
print(c%j)

print("\nbool((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)):")
print(bool((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)))
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

print("validStr4.var()")
print(validStr4.var())
print("")

print('################')
print("Linear model for validStr4:")
print("""
validStr4.corr().p #First and second columns have strong positive correlation. Let's choose first column to be predicted

var = validStr4["Weight"]
var.add([1]*22,col=1,feature="bias")

out = validStr4["Height"]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]

print("Height={0} + {1}*{2}".format(coefs[0,0],coefs[1,0],"Weight"))
print("Model range:",var.ranged()["Weight"])
print("Average error:",err.mean()["Difference"])

""")

validStr4.corr().p

var = validStr4["Weight"]
var.add([1]*22,col=1,feature="bias")

out = validStr4["Height"]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]

print("Height={0} + {1}*{2}".format(coefs[0,0],coefs[1,0],"Weight"))
print("\nModel range:",var.ranged()["Weight"])
print("\nAverage error:",err.mean()["Difference"])

if plotting:
    try:
        from matplotlib import pyplot as plt
    except ImportError:
        print("Couldn't import matplotlib")
    else:
        model = plt.figure()
        
        #Data in a scatter plot
        plt.scatter(var.col(2,0),out.col(1,0))
        
        #Linear model to predict
        plt.plot(var.col(2,0),preds.col(1,0),c="red")
        
        #Titles
        plt.xlabel(validStr4.features[1])
        plt.ylabel(validStr4.features[0])
        plt.legend(["Linear model","Data points"],loc=4)
        model.suptitle("Height prediction")
        plt.show()

# =============================================================================
""" Expected Outputs """
# =============================================================================
"""
################################
Matrices created by giving dimensions

Square matrix
Dimension: 20x20

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

0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000


Square matrix
Dimension: 1x1

0.8554


Dimension: 2x4

-38.2714 -17.6604 -45.9740 -5.9706
 35.1542  37.2449  39.9189 37.2432


Dimension: 4x3

0.1968 0.4906 0.5025
0.7183 0.0228 0.6342
0.5840 0.8060 0.1555
0.8709 0.5024 0.5658


Square matrix
Dimension: 8x8

-0.9497 -2.1571 -1.0395  0.9981  3.8667 -1.6761  0.1415 -0.7237
-4.7562  0.4283  1.1035 -4.8985 -5.4196  1.3044 -5.0751 -3.5036
 4.8267  3.8222  1.4003  3.4292 -4.4964  3.8328 -9.0298 -6.7511
 0.0964  0.6918  4.3948 -3.7930  1.0148  2.8540 -0.1247 -0.5862
 2.0764 -1.9198 -0.9033  4.0095  2.0821  4.1393  1.8200 -2.5762
-5.8804 -1.9794  0.4730 -2.3903 -1.3311 -1.0409 -0.7161 -2.6036
 2.5251 -0.3099  1.3486 -4.5777 -3.7435 -0.0652 -6.3998 -2.2195
 2.5618  4.7087  1.8311  0.0711 -5.5426  0.1459  6.9657 -2.6620


Square matrix
Dimension: 6x6

 271.8329 -719.4545   800.9249 -1058.2952   236.3437  707.3202
-483.9847  870.4989  -557.4067  -771.6552  1139.1099 1204.7894
 801.1412  683.5654  1070.4233  -883.5232 -1147.9864  -56.2430
-252.3416   61.3385   930.6123  -722.8897  -498.1111 1108.2689
 338.2435   96.9183 -1038.5434  -467.6239  -941.9333 1126.8197
 339.9659  950.4870   465.1454  1013.7930  1224.5803 -957.1393


Dimension: 3x6

6.7600 4.9043 6.4048 3.1729 6.8038 3.0413
4.5109 3.2520 8.5359 6.6479 9.6750 2.9970
5.5954 7.5136 4.5185 2.4375 5.2975 9.3888


Square matrix
Dimension: 5x5

27.2335 11.4441 14.3559 45.5002  4.0471
59.7826 43.2915 16.0596 51.8446 53.7991
 2.9315 93.7677 75.6139 44.6397 43.8224
53.2221 87.4442 79.5673  5.0092  2.6417
95.2866  4.9405 50.4917 80.9151  7.4889


Square matrix
Dimension: 4x4

0.1865 0.9242 0.0439 0.4147
0.4282 0.5619 0.4818 0.7299
0.5519 0.1188 0.6230 0.0833
0.5217 0.0350 0.6498 0.9210


Square matrix
Dimension: 9x9

0.32 0.07 0.50 0.08 0.57 0.49 0.90 0.57 0.06
0.86 0.86 0.50 0.76 0.82 0.54 0.74 0.35 0.72
0.09 0.71 0.41 0.79 0.28 0.19 0.09 0.87 0.56
0.56 0.35 0.01 0.14 0.35 0.66 0.32 0.87 0.20
0.04 0.23 0.31 0.21 0.32 0.50 0.03 0.76 0.63
0.31 0.35 0.81 0.84 0.52 0.66 0.66 0.11 0.73
0.48 0.33 0.16 0.00 0.37 0.47 0.53 0.86 0.99
0.84 0.26 0.66 0.23 0.50 0.45 0.71 0.82 0.59
0.08 0.36 0.39 0.90 0.43 0.39 0.24 0.04 0.65


Square matrix
Dimension: 6x6

0.978973 0.202246 0.898038 0.824610 0.170782 0.752129
0.655538 0.981262 0.462416 0.446181 0.306162 0.512528
0.374004 0.329783 0.396069 0.233711 0.598987 0.405194
0.170751 0.150975 0.390759 0.596240 0.306650 0.391736
0.396954 0.370769 0.668111 0.058718 0.721915 0.677999
0.120975 0.914274 0.499069 0.356182 0.934172 0.300729


Square matrix
Dimension: 3x3

3.0000 5.0000 7.0000
8.0000 3.0000 4.0000
5.0000 2.0000 5.0000


Square matrix
Dimension: 5x5

 0.8617+0.0445j   0.6896+0.2354j   0.1554+0.2367j   0.1212+0.8389j   0.2335+0.2552j
 0.6816+0.0043j   0.7161+0.5093j   0.7417+0.5502j   0.9207+0.9358j   0.8186+0.9227j
 0.6028+0.7709j   0.4328+0.3487j   0.8029+0.9331j   0.2991+0.9282j    0.855+0.4487j
 0.8108+0.1321j   0.0184+0.7958j   0.2506+0.1448j   0.7138+0.7805j   0.3964+0.5441j
  0.2861+0.647j   0.4792+0.5017j   0.4217+0.7373j   0.0263+0.7112j   0.1092+0.6021j


Dimension: 7x3

  3.8128+6.0303j    4.4233-5.4403j    9.7119+0.8273j
  5.4711+2.6051j    1.0855+9.4428j    1.0169-8.8426j
  9.5471+6.4287j    2.6032+3.9026j   -6.5096-0.0164j
  3.0477+9.0744j    8.1405-2.9541j    8.3798-2.0804j
 -3.3914-5.4714j   -7.4695+2.1098j     5.752+8.3838j
  0.0378+3.5002j    1.4538+9.3207j   -7.8542-3.8343j
 -7.9563-8.5474j   -2.7511-3.0013j    2.1127-2.2594j

################################
################################
Identity matrices

Square matrix
Dimension: 1x1

1.0000


Square matrix
Dimension: 5x5

1.0000 0.0000 0.0000 0.0000 0.0000
0.0000 1.0000 0.0000 0.0000 0.0000
0.0000 0.0000 1.0000 0.0000 0.0000
0.0000 0.0000 0.0000 1.0000 0.0000
0.0000 0.0000 0.0000 0.0000 1.0000


Square matrix
Dimension: 3x3

1.0000 0.0000 0.0000
0.0000 1.0000 0.0000
0.0000 0.0000 1.0000


Square matrix
Dimension: 6x6

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000

################################
################################
Attribute call outputs

################

d:

Dimension: 4x3

0.1968 0.4906 0.5025
0.7183 0.0228 0.6342
0.5840 0.8060 0.1555
0.8709 0.5024 0.5658

d.matrix:

[[0.1968138676107059, 0.49055452131717886, 0.5025177770317698], [0.7182531205175939, 0.022797326578569903, 0.6341746269112216], [0.5840327158421583, 0.8059633167516098, 0.15552232428968168], [0.8709067049165319, 0.5023651844843898, 0.565782647175512]]

################

f[:4,1:3]:

Dimension: 4x2

-719.4545  800.9249
 870.4989 -557.4067
 683.5654 1070.4233
  61.3385  930.6123



Square matrix
Dimension: 6x6

 271.8329 -719.4545   800.9249 -1058.2952   236.3437  707.3202
-483.9847  870.4989  -557.4067  -771.6552  1139.1099 1204.7894
 801.1412  683.5654  1070.4233  -883.5232 -1147.9864  -56.2430
-252.3416   61.3385   930.6123  -722.8897  -498.1111 1108.2689
 338.2435   96.9183 -1038.5434  -467.6239  -941.9333 1126.8197
 339.9659  950.4870   465.1454  1013.7930  1224.5803 -957.1393

f.delDim(2)

Square matrix
Dimension: 4x4

 271.8329 -719.4545  800.9249 -1058.2952
-483.9847  870.4989 -557.4067  -771.6552
 801.1412  683.5654 1070.4233  -883.5232
-252.3416   61.3385  930.6123  -722.8897

[L,U]=f.LU
L.p

Square matrix
Dimension: 4x4

 1.0000  0.0000 0.0000 0.0000
-1.7804  1.0000 0.0000 0.0000
 2.9472 -6.8313 1.0000 0.0000
-0.9283  1.4777 0.0841 1.0000

U.p

Square matrix
Dimension: 4x4

271.8329 -719.4545  800.9249  -1058.2952
  0.0000 -410.4535  868.5996  -2655.8965
  0.0000    0.0000 4643.6124 -15907.7489
  0.0000    0.0000    0.0000   3557.3311

f-(L@U)

Square matrix
Dimension: 4x4

0.0000  0.0000 0.0000  0.0000
0.0000  0.0000 0.0000  0.0000
0.0000  0.0000 0.0000  0.0000
0.0000  0.0000 0.0000  0.0000

[Q,R]=f.QR
Q.p

Square matrix
Dimension: 4x4

 0.2700 -0.5283 0.3278 -0.7352
-0.4807  0.6294 0.0445 -0.6089
 0.7957  0.5691 0.2057 -0.0250
-0.2506  0.0305 0.9210  0.2967

R.p

Square matrix
Dimension: 4x4

1006.7958  -84.1534 1102.7281  -436.6544
   0.0000 1318.8348 -136.3823  -451.4308
   0.0000    0.0000 1315.0737 -1228.8431
   0.0000    0.0000    0.0000  1055.5147

f-(Q@R)

Square matrix
Dimension: 4x4

 0.0000  0.0000  0.0000  0.0000
 0.0000  0.0000  0.0000  0.0000
 0.0000  0.0000  0.0000  0.0000
 0.0000  0.0000  0.0000  0.0000

################
g.dim:
 [3, 6]
g.ranged():
 {'Col 1': [4.510879979847405, 6.759998401691722], 'Col 2': [3.2519910141642585, 7.513553234149581], 'Col 3': [4.518503351033807, 8.535924109459824], 'Col 4': [2.437464623345365, 6.647879444325895], 'Col 5': [5.297472883106707, 9.675004861813733], 'Col 6': [2.9969911203796524, 9.388840095317265]}
g:
Dimension: 3x6

6.7600 4.9043 6.4048 3.1729 6.8038 3.0413
4.5109 3.2520 8.5359 6.6479 9.6750 2.9970
5.5954 7.5136 4.5185 2.4375 5.2975 9.3888

g.remove(3):

Dimension: 2x6

6.7600 4.9043 6.4048 3.1729 6.8038 3.0413
4.5109 3.2520 8.5359 6.6479 9.6750 2.9970

################
q1.decimal 2

Square matrix
Dimension: 9x9

0.32 0.07 0.50 0.08 0.57 0.49 0.90 0.57 0.06
0.86 0.86 0.50 0.76 0.82 0.54 0.74 0.35 0.72
0.09 0.71 0.41 0.79 0.28 0.19 0.09 0.87 0.56
0.56 0.35 0.01 0.14 0.35 0.66 0.32 0.87 0.20
0.04 0.23 0.31 0.21 0.32 0.50 0.03 0.76 0.63
0.31 0.35 0.81 0.84 0.52 0.66 0.66 0.11 0.73
0.48 0.33 0.16 0.00 0.37 0.47 0.53 0.86 0.99
0.84 0.26 0.66 0.23 0.50 0.45 0.71 0.82 0.59
0.08 0.36 0.39 0.90 0.43 0.39 0.24 0.04 0.65

q1.decimal=5

Square matrix
Dimension: 9x9

0.32395 0.07212 0.50319 0.07724 0.57115 0.48759 0.90472 0.57152 0.06433
0.86337 0.86181 0.49590 0.75750 0.82434 0.53926 0.73760 0.34510 0.71914
0.09482 0.71239 0.41227 0.79495 0.27955 0.18909 0.08658 0.86670 0.55559
0.56120 0.34846 0.01132 0.13770 0.34678 0.65557 0.31907 0.86514 0.19868
0.03830 0.23240 0.30952 0.20518 0.32215 0.50401 0.02551 0.76330 0.63298
0.30561 0.35029 0.80538 0.84210 0.51781 0.65804 0.66066 0.10691 0.73333
0.47569 0.33262 0.16352 0.00415 0.36650 0.47380 0.52748 0.86422 0.98730
0.83901 0.25913 0.65831 0.22562 0.49828 0.44951 0.70965 0.82363 0.59102
0.08322 0.35569 0.39412 0.90228 0.43471 0.38511 0.23579 0.04239 0.65368

################
h=proj[11:18,4:11]:

Square matrix
Dimension: 7x7

96 35 31 47 55 58 88
35 71 89  7  5 44 44
 5 94 47 69 28 73 92
97 35 99 16  7 97 57
57 62 20 72  3 46 33
38 25 39 11 24 94 72
72 30 23 88 34 62 99

h.mean(): {'Col 5': 57.142857142857146, 'Col 6': 50.285714285714285, 'Col 7': 49.714285714285715, 'Col 8': 44.285714285714285, 'Col 9': 22.285714285714285, 'Col 10': 67.71428571428571, 'Col 11': 69.28571428571429}

h.det: 1287494716522.8682

h.rank: 7

h.rrechelon:
Square matrix
Dimension: 7x7

1.0000 0.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 1.0000 0.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 1.0000 0.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 1.0000 0.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 1.0000 0.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 1.0000 0.0000
0.0000 0.0000 0.0000 0.0000 0.0000 0.0000 1.0000


h.inv:

Square matrix
Dimension: 7x7

 0.0011  0.0229 -0.0279 -0.0196  0.0155  0.0175  0.0081
 0.0015  0.0268 -0.0174 -0.0279  0.0197  0.0212 -0.0029
 0.0048 -0.0282  0.0340  0.0407 -0.0241 -0.0400 -0.0096
 0.0028 -0.0406  0.0363  0.0380 -0.0121 -0.0393 -0.0074
 0.0398 -0.0745  0.0710  0.0630 -0.0317 -0.0622 -0.0487
 0.0017 -0.0272  0.0178  0.0197  0.0007 -0.0011 -0.0167
-0.0195  0.0605 -0.0501 -0.0545  0.0096  0.0471  0.0410

h.minor(3,4,returndet=False):

Square matrix
Dimension: 6x6

96 35 31 55 58 88
35 71 89  5 44 44
97 35 99  7 97 57
57 62 20  3 46 33
38 25 39 24 94 72
72 30 23 34 62 99


h.minor(3,4):
 -46677834292.743515

################
j=g.[:2,:4]:

Dimension: 2x4

6.7600 4.9043 6.4048 3.1729
4.5109 3.2520 8.5359 6.6479


j.obj:
 Matrix(dim=[2, 4],listed=[[6.759998401691722, 4.904305902101776, 6.40479639909408, 3.172946127726555], [4.510879979847405, 3.2519910141642585, 8.535924109459824, 6.647879444325895]],ranged=[0, 1],fill='uniform',features=['Col 1', 'Col 2', 'Col 3', 'Col 4'],header=False,directory='',decimal=4,seed=None,dtype='float',coldtypes=[float, float, float, float])

################
proj=proj[:5,:15]:


Dimension: 5x15

 8  2 22 97 38 15  0 40  0 75  4  5  7 78 52
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30
52 70 95 23  4 60 11 42 69 24 68 56  1 32 56
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40

################
p:
Square matrix
Dimension: 5x5

27.2335 11.4441 14.3559 45.5002  4.0471
59.7826 43.2915 16.0596 51.8446 53.7991
 2.9315 93.7677 75.6139 44.6397 43.8224
53.2221 87.4442 79.5673  5.0092  2.6417
95.2866  4.9405 50.4917 80.9151  7.4889

p.det:
 -690030064.0210469

p.adj:

Square matrix
Dimension: 5x5

  2717980.2300 -5794621.1875   7461236.9201 -5397460.7027  -1597715.2667
-26322493.8969 -4070895.8586   5415528.5176 -9084555.8859  14984746.9467
 27447051.3878  8458288.3321 -10571428.3297  4420480.2191 -15295059.2577
-21566833.4940  2542747.2984  -1802598.9392  3340787.1106   2758081.1811
 30751194.0437 -8086426.9142  -7756078.8319  8769019.5622  -8374773.2727

p.inv:


Square matrix
Dimension: 5x5

-0.0039  0.0084 -0.0108  0.0078  0.0023
 0.0381  0.0059 -0.0078  0.0132 -0.0217
-0.0398 -0.0123  0.0153 -0.0064  0.0222
 0.0313 -0.0037  0.0026 -0.0048 -0.0040
-0.0446  0.0117  0.0112 -0.0127  0.0121

################
p:

Square matrix
Dimension: 5x5

27.2335 11.4441 14.3559 45.5002  4.0471
59.7826 43.2915 16.0596 51.8446 53.7991
 2.9315 93.7677 75.6139 44.6397 43.8224
53.2221 87.4442 79.5673  5.0092  2.6417
95.2866  4.9405 50.4917 80.9151  7.4889

p.remove(2,1)
p.p

Square matrix
Dimension: 4x4

11.4441 14.3559 45.5002  4.0471
93.7677 75.6139 44.6397 43.8224
87.4442 79.5673  5.0092  2.6417
 4.9405 50.4917 80.9151  7.4889

p.add(col=2,lis=[55]*4):

Dimension: 4x5

11.4441 55.0000 14.3559 45.5002  4.0471
93.7677 55.0000 75.6139 44.6397 43.8224
87.4442 55.0000 79.5673  5.0092  2.6417
 4.9405 55.0000 50.4917 80.9151  7.4889

p.sdev()
{'Col 2': 41.331461129583005, 'Col': 0.0, 'Col 3': 25.984387545720686, 'Col 4': 26.859176236652686, 'Col 5': 17.020853966870913}
################

proj.find(40)
[(1, 8), (2, 4), (2, 12), (3, 11), (5, 14), (5, 15)]

proj.find(40,0)
[(0, 7), (1, 3), (1, 11), (2, 10), (4, 13), (4, 14)]

proj.find(111)
################

r=p.t
r.remove(2):

Square matrix
Dimension: 4x4

11.4441 93.7677 87.4442  4.9405
14.3559 75.6139 79.5673 50.4917
45.5002 44.6397  5.0092 80.9151
 4.0471 43.8224  2.6417  7.4889

r.rank: 4

r.matrix[0]=r.matrix[1][:]

Square matrix
Dimension: 4x4

14.3559 75.6139 79.5673 50.4917
14.3559 75.6139 79.5673 50.4917
45.5002 44.6397  5.0092 80.9151
 4.0471 43.8224  2.6417  7.4889

r.rank: 3
################################
Operator examples
################

c.dim= [2, 4]  d.dim: [4, 3]

mMulti=c@d:

Dimension: 2x3

-52.2671 -59.2296 -40.9599
 89.4194  68.9770  68.5652


((((mMulti)+125)**3)%2):

Dimension: 2x3

0.1115 1.8220 1.7557
1.2913 0.5216 0.1900

################

f:

Square matrix
Dimension: 4x4

 271.8329 -719.4545  800.9249 -1058.2952
-483.9847  870.4989 -557.4067  -771.6552
 801.1412  683.5654 1070.4233  -883.5232
-252.3416   61.3385  930.6123  -722.8897

f1=f.intForm

Square matrix
Dimension: 4x4

 271 -719  800 -1058
-483  870 -557  -771
 801  683 1070  -883
-252   61  930  -722

f2=f.roundForm(3)

Square matrix
Dimension: 4x4

 271.8300 -719.4500  800.9200 -1058.3000
-483.9800  870.5000 -557.4100  -771.6600
 801.1400  683.5700 1070.4200  -883.5200
-252.3400   61.3400  930.6100  -722.8900

f2-f1

Square matrix
Dimension: 4x4

 0.8300 -0.4500  0.9200 -0.3000
-0.9800  0.5000 -0.4100 -0.6600
 0.1400  0.5700  0.4200 -0.5200
-0.3400  0.3400  0.6100 -0.8900

################
e+=Matrix(listed=Identity(e.dim[0]))*99

Square matrix
Dimension: 8x8

98.0503 -2.1571  -1.0395  0.9981   3.8667 -1.6761  0.1415 -0.7237
-4.7562 99.4283   1.1035 -4.8985  -5.4196  1.3044 -5.0751 -3.5036
 4.8267  3.8222 100.4003  3.4292  -4.4964  3.8328 -9.0298 -6.7511
 0.0964  0.6918   4.3948 95.2070   1.0148  2.8540 -0.1247 -0.5862
 2.0764 -1.9198  -0.9033  4.0095 101.0821  4.1393  1.8200 -2.5762
-5.8804 -1.9794   0.4730 -2.3903  -1.3311 97.9591 -0.7161 -2.6036
 2.5251 -0.3099   1.3486 -4.5777  -3.7435 -0.0652 92.6002 -2.2195
 2.5618  4.7087   1.8311  0.0711  -5.5426  0.1459  6.9657 96.3380


e-=33:

Square matrix
Dimension: 8x8

 65.0503 -35.1571 -34.0395 -32.0019 -29.1333 -34.6761 -32.8585 -33.7237
-37.7562  66.4283 -31.8965 -37.8985 -38.4196 -31.6956 -38.0751 -36.5036
-28.1733 -29.1778  67.4003 -29.5708 -37.4964 -29.1672 -42.0298 -39.7511
-32.9036 -32.3082 -28.6052  62.2070 -31.9852 -30.1460 -33.1247 -33.5862
-30.9236 -34.9198 -33.9033 -28.9905  68.0821 -28.8607 -31.1800 -35.5762
-38.8804 -34.9794 -32.5270 -35.3903 -34.3311  64.9591 -33.7161 -35.6036
-30.4749 -33.3099 -31.6514 -37.5777 -36.7435 -33.0652  59.6002 -35.2195
-30.4382 -28.2913 -31.1689 -32.9289 -38.5426 -32.8541 -26.0343  63.3380


e+=Matrix(e.dim):

Square matrix
Dimension: 8x8

 65.6406 -35.0519 -33.4148 -31.6034 -29.1279 -34.5519 -32.5815 -32.9154
-37.5622  67.1805 -31.4264 -37.8763 -38.3231 -31.0548 -37.7444 -35.5851
-27.3706 -28.3326  67.6186 -29.2297 -36.9816 -29.1063 -41.3871 -39.2787
-32.8531 -32.0716 -28.5555  62.8072 -31.8145 -29.4262 -33.1166 -32.9042
-30.4154 -34.3269 -33.0750 -28.3743  68.4648 -28.5066 -31.0373 -34.9535
-38.5990 -34.3785 -32.0452 -34.7481 -34.0443  65.8306 -33.3420 -35.4444
-30.2419 -33.0095 -31.6468 -37.2229 -35.8711 -32.8199  60.5587 -34.2234
-29.6066 -27.7508 -31.0818 -31.9610 -37.9003 -32.3203 -26.0127  64.1917


e*=[2,1,1,0.5,0.2,0.0003,1,3]:

Square matrix
Dimension: 8x8

131.2812 -35.0519 -33.4148 -15.8017 -5.8256 -0.0104 -32.5815  -98.7462
-75.1245  67.1805 -31.4264 -18.9382 -7.6646 -0.0093 -37.7444 -106.7552
-54.7411 -28.3326  67.6186 -14.6148 -7.3963 -0.0087 -41.3871 -117.8361
-65.7062 -32.0716 -28.5555  31.4036 -6.3629 -0.0088 -33.1166  -98.7125
-60.8307 -34.3269 -33.0750 -14.1871 13.6930 -0.0086 -31.0373 -104.8605
-77.1981 -34.3785 -32.0452 -17.3740 -6.8089  0.0197 -33.3420 -106.3331
-60.4837 -33.0095 -31.6468 -18.6115 -7.1742 -0.0098  60.5587 -102.6702
-59.2132 -27.7508 -31.0818 -15.9805 -7.5801 -0.0097 -26.0127  192.5750

e%=[2,2,2,2,1,1,1,1]

Square matrix
Dimension: 8x8

1.2812 4.9481 1.5852 4.1983 0.1744 2.9896 0.4185 0.2538
4.8755 2.1805 3.5736 1.0618 1.3354 2.9907 0.2556 0.2448
0.2589 1.6674 2.6186 0.3852 1.6037 2.9913 0.6129 0.1639
4.2938 2.9284 1.4445 1.4036 2.6371 2.9912 0.8834 0.2875
4.1693 0.6731 1.9250 0.8129 1.6930 2.9914 0.9627 0.1395
2.8019 0.6215 2.9548 2.6260 2.1911 0.0197 0.6580 0.6669
4.5163 1.9905 3.3532 1.3885 1.8258 2.9902 0.5587 0.3298
0.7868 2.2492 3.9182 4.0195 1.4199 2.9903 0.9873 0.5750

################

c%j

Dimension: 2x4

2.2886 1.9568 5.2643 0.3753
3.5781 1.4730 5.7752 4.0038


bool((f.lowtri@f.uptri).roundForm(4)==f.roundForm(4)):
True

################################
Strings' matrices:
################

validStr1:

Dimension: 2x3

34.0000 -52.0000 33.0000
 9.0000  88.0000 -3.0000

################
validStr2:

Dimension: 1x10

312.0000 45.0000 12.0000 44.0000 352.0000 45.0000 12.0000 44.0000 3.0000 -5.0000

################
validStr3:

Dimension: 1x4

34.0000 5.0000 44.0000 659.0000

################
validStr4:

Dimension: 22x3

  Height    Weight      Age
     130        30       10
     125        36       11
     135        34       10
     133        30        9
     129        38       12
     180        90       30
     190        80       25
     175        90       35
     177        60       22
     185       105       33
     165        55       27
     155        50       44
     160        58       39
     162        59       41
     167        62       55
     174        70       47
     193        90       23
     187        80       27
     183        88       28
     159        40       29
     164        66       32
     166        56       42

################

validStr4.ranged()
{'Height': [125, 193], 'Weight': [30, 105], 'Age': [9, 55]}

validStr4.mean()
{'Height': 163.36363636363637, 'Weight': 62.13636363636363, 'Age': 28.681818181818183}

validStr4.sdev()
{'Height': 20.592464320155067, 'Weight': 21.774245534462064, 'Age': 12.68996154316246}

validStr4.median()
{'Height': 166, 'Weight': 60, 'Age': 29}

validStr4.freq()
{'Height': {130: 1, 125: 1, 135: 1, 133: 1, 129: 1, 180: 1, 190: 1, 175: 1, 177: 1, 185: 1, 165: 1, 155: 1, 160: 1, 162: 1, 167: 1, 174: 1, 193: 1, 187: 1, 183: 1, 159: 1, 164: 1, 166: 1}, 'Weight': {30: 2, 36: 1, 34: 1, 38: 1, 90: 3, 80: 2, 60: 1, 105: 1, 55: 1, 50: 1, 58: 1, 59: 1, 62: 1, 70: 1, 88: 1, 40: 1, 66: 1, 56: 1}, 'Age': {10: 2, 11: 1, 9: 1, 12: 1, 30: 1, 25: 1, 35: 1, 22: 1, 33: 1, 27: 2, 44: 1, 39: 1, 41: 1, 55: 1, 47: 1, 23: 1, 28: 1, 29: 1, 32: 1, 42: 1}}

validStr4.mode()
{'Height': {'All': 1}, 'Weight': {90: 3}, 'Age': {(10, 27): 2}}

validStr4.iqr()
{'Height': 25, 'Weight': 40, 'Age': 17}

validStr4.iqr(as_quartiles=True)
{'Height': [155, 166, 180], 'Weight': [40, 60, 80], 'Age': [22, 29, 39]}

validStr4.var()
{'Height': 424.0495867768595, 'Weight': 474.1177685950411, 'Age': 161.03512396694214}

################
Linear model for validStr4:

validStr4.corr().p #First and second columns have strong positive correlation. Let's choose first column to be predicted

var = validStr4["Weight"]
var.add([1]*22,col=1,feature="bias")

out = validStr4["Height"]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]

print("Height={0} + {1}*{2}".format(coefs[0,0],coefs[1,0],"Weight"))
print("Model range:",var.ranged()["Weight"])
print("Average error:",err.mean()["Difference"])



Dimension: 3x4

Feature  Height  Weight     Age
 Height  1.0000  0.8992  0.5087
 Weight  0.8992  1.0000  0.4233
    Age  0.5087  0.4233  1.0000

Height=110.52445381620008 + 0.8503745538689572*Weight

Model range: [30, 105]

Average error: 4.11242601992192e-08
"""
# =============================================================================

