# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 17:43:33 2019

@author: Semih
"""
# Run matrices.py and exampleMatrices.py first and then run this script
from matrices import Matrix,FMatrix,Identity,CMatrix
from exampleMatrices import *

try:
    #Enable/disable printing
    PRINTING=bool(int(input("Enable printing ? (1/0)")))
    print("##########################################################################################################")
    #Get all properties declared for the Matrix class
    props=[]
    data = FMatrix([1599,12],directory=r"F:\data science\python\Data Science\Data\winequality-red.csv",header=1,decimal=3)
    for keys,vals in vars(Matrix).items():
        if "property" in str(vals):
            props.append(keys)
            
    #Properties that are currently unstable        
    del props[props.index("eigenvectors")]
    if not PRINTING:
        del props[props.index("p")]
        del props[props.index("grid")]
    
    #Add desired methods
    props.append("nilpotency()")    
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
    
    data.head(15).p
    print("Standardization")
    data.stdize(inplace=0).head(15).p
    print("Normalization")
    data.normalize(inplace=0).head(15).p
except Exception as err:
    print("\nTest was NOT successfull")
    print("Error at '{}' matrix's '{}' property".format(matrix,prop))
    print("Error message:\n\t",err)
    input("Press any key to quit")

else:
    print("Test was successfull")
    input("Press any key to quit")