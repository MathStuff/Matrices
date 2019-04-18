def mode(mat,col=None):
    """
    Returns the columns' most repeated elements in a dictionary
    col:integer>=1 and <=amount of columns
    """
    try:
        #Set feature name and the matrix to use dependent on the column desired
        if col==None:
            temp=mat.t
            feats=mat.features[:]
        else:
            assert col>=1 and col<=mat.dim[1]
            temp=mat.col(col)
            feats=mat.features[col-1]
        #Set keys in the dictionary which will be returned at the end
        mods={}
        if len(feats)!=0 and isinstance(feats,list):
            for fs in feats:
                mods[fs]=None
        elif len(feats)==0:
            for fs in range(mat.dim[1]):
                mods["Col "+str(fs+1)]=None
               
        #Set column amount
        if col==None:
            r=mat.dim[1]
        else:
            r=1
            
        #Loop through the transpozed matrices (From column to row matrices to make calculations easier)               
        for rows in range(r):
            #Variables to keep track of the frequency of the numbers
            a={}
            #Loop through the column to get frequencies
            for els in temp[rows]:
                if els not in a.keys():
                    a[els]=1
                else:
                    a[els]+=1
    
            #Get a list of the values from the frequency dictionary
            temp2=[]
            for k,v in a.items():
                temp2.append(v)
            
            #Find the maximum repetation
            m=max(temp2)
            #Create a dictionary to store the most repated key(s) as keys and frequency as the value
            n={}
            s=""
            allSame=0
            #Check if there are multiple most repeated elements
            for k,v in a.items(): 
                if v==m:
                    allSame+=1
                    if len(s)!=0:
                        s+=", "+str(k)
                    else:
                        s+=str(k)
            #If all the elements repeated same amount don't get all the numbers, just set the name to "All"          
            if allSame==len(temp2):
                n["All"]=temp2[0]
            else:
                n[s]=m
            
            #Set the final dictionary's key(s) and  value(s) calculated
            if len(feats)!=0 and isinstance(feats,list):
                mods[feats[rows]]=n
            elif len(feats)==0:
                mods["Col "+str(rows+1)]=n
            else:
                mods[feats]=n
            #END
    except Exception as err:
        print("Bad arguments given to mode method\n",err)
    else:
        return mods