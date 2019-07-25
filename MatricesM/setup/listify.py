def _listify(mat,stringold):
    """
    Finds all the numbers in the given string
    """
    #Get the features from the first row if header exists
    import re
    string=stringold[:]
    d1 = mat.d1
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
        elif mat._fMat or mat._dfMat:
            found=[float(a) for a in found if len(a)!=0]
        else:
            found=[int(a) for a in found if len(a)!=0]
    except ValueError as v:
        raise ValueError(v)
    #Fix dimensions to create a row matrix   
    if mat.dim==[0,0]:
        mat._Matrix__dim=[1,len(found)]
        mat._Matrix__features=[f"col_{i+1}" for i in range(d1)]
    #Create the row matrix
    temp=[]
    e=0            
    for rows in range(mat.dim[0]):
        temp.append([])
        for cols in range(mat.dim[1]):
            temp[rows].append(found[cols+e])
        e+=d1
    return temp