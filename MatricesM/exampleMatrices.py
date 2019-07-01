# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 17:38:28 2018

@author: Semih
"""
from MatricesM import *

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
d=Matrix([4,3],dtype=float)
e=Matrix(8,fill=gauss,ranged=[0,3])
f=Matrix(dim=6,ranged=[-1250,1250],dtype=float)
g=Matrix(dim=[3,6],ranged=[2,10])
p=Matrix(5,ranged=[0,100])
q=Matrix(4,dtype=float)
q1=Matrix(9,decimal=2,dtype=float)
q2=Matrix(6,decimal=6,dtype=float)
y=Matrix(3,listed=[3,5,7,8,3,4,5,2,5])
c1=Matrix(5,dtype=complex)
c2=Matrix([7,3],ranged=[-10,10],dtype=complex)
# =============================================================================
# String inputs Matrices
# =============================================================================
proj=Matrix(20,listed=projectGrid,dtype=int)
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
""",features=["Height","Weight","Age"],dtype=dataframe,coldtypes=[int]*3)
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
e+=Matrix(e.dim,dtype=float)
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
print("Multivariate linear model for validStr4:")
print("""
validStr4.corr().p Correlation matrix

var = validStr4["Weight","Age"]
var.add([1]*22,col=1,feature="constant")

out = validStr4["Height"]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs

err = out-preds
err.features=["Difference"]

""")
print("Correlation Matrix")
validStr4.corr().p

n = validStr4.dim[0]

var = validStr4["Weight","Age"]
var.add([1 for _ in range(n)],col=1,feature="constant")

out = validStr4["Height"]

coefs = (((var.t@var).inv)@var.t)@out

preds = var@coefs
err = out-preds
err.features=["Difference"]

#95% reliability 
means = validStr4.mean()
sdevs = validStr4.sdev()

meanH = means["Height"]
rangeH = 1.96*sdevs["Height"]/(n**0.5)
heightrange95 = [meanH-rangeH,meanH+rangeH]

print(f"n: {n}, Reliability: 95%")
print("\nHeight = {0} + ({1})*{2} + ({3})*{4}".format(coefs[0,0],coefs[1,0],"Weight",coefs[2,0],"Age"))
print(f"\nHeight range: {heightrange95}")
err.describe.grid

# =============================================================================
