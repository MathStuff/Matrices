# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:43:33 2019

@author: Semih
"""
# Run matrices.py and exampleMatrices.py first and then run this script
from matrices import *
from exampleMatrices import *

#Enable/disable printing
PRINTING=1
print("##########################################################################################################")
#Get all properties declared for the Matrix class
props=[]
for keys,vals in vars(Matrix).items():
    if "property" in str(vals):
        props.append(keys)
        
#Properties that are currently unstable        
del props[props.index("chareq")]
del props[props.index("eigenvalues")]
if not PRINTING:
    del props[props.index("p")]
    del props[props.index("grid")]
    
#Matrix names from examples
#proj,o,b,c,d,e,f,g,p,q,q1,q2,y,c1,c2,id1,id2,id3,id4,validStr1,validStr2,validStr3,validStr4
l=["proj","o","b","c","d","e","f","g","p","q","q1","q2","y","c1","c2","id1","id2","id3","id4","validStr1","validStr2","validStr3","validStr4"]

#Try and print properties of each matrix
for matrix in l:
    if PRINTING:
        print("#######################################################")
        print("MATRIX NAME:",matrix)
        print("###############")

    for prop in props:
        TEMP=eval(matrix + "." + prop)
        if PRINTING:
            print("-------------------------------------------------")
            print(prop,":")
            print(TEMP)

print("Test was successfull")
input("Press any key to quit")