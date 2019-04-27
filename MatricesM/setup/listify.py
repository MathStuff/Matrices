def _listify(mat,stringold):
    """
    Finds all the numbers in the given string
    """
    #Get the features from the first row if header exists
    import re
    string=stringold[:]
    if mat._header:
        i=0
        for ch in string:
            if ch!="\n":
                i+=1
            else:
                if len(mat.features)!=mat.dim[1]:
                    pattern=r"(?:\w+ ?[0-9]*)+"
                    mat.features=re.findall(pattern,string[:i])
                    if len(mat.features)!=mat.dim[1]:
                        print("Can't get enough column names from the header")
                        mat.setFeatures()
                string=string[i:]
                break
            
    #Get all integer and float values
    if not mat._cMat:       
        pattern=r"-?\d+\.?\d*"
    else:
        pattern=r"[+-]?\d*\.?\d*[+-]*\d*\.?\d*j*"
    found=re.findall(pattern,string)
    found=[i for i in found if len(i)!=0]
    #String to number
    try:
        if mat._cMat:
            found=[complex(a) for a in found if len(a)!=0]
        elif mat._fMat:
            found=[float(a) for a in found if len(a)!=0]
        else:
            found=[int(a) for a in found if len(a)!=0]
    except ValueError as v:
        print("Choose the correct matrix for your data\n",v)
        return []
    #Fix dimensions to create a row matrix   
    if mat.dim==[0,0]:
        mat._Matrix__dim=[1,len(found)]
        mat.setFeatures()
    #Create the row matrix
    temp=[]
    e=0            
    for rows in range(mat.dim[0]):
        temp.append(list())
        for cols in range(mat.dim[1]):
            temp[rows].append(found[cols+e])
        e+=mat.dim[1]

    return temp