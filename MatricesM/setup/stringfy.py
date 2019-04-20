def _stringfy(mat):
    """
    Turns a square matrix shaped list into a grid-like form that is printable
    Returns a string
    """
    import re
    def __digits(num):
        dig=0
        if num==0:
            return 1
        if num<0:
            dig+=1
            num*=-1
        while num!=0:
            num=num//10
            dig+=1
        return dig

    string=""
    if mat._cMat:
        ns=""
        for i in mat._matrix:
            for j in i:
                ns+=str(round(j.real,mat.decimal))
                im=j.imag
                if im<0:
                    ns+=str(round(im,mat.decimal))+"j "
                else:
                    ns+="+"+str(round(im,mat.decimal))+"j "
                    
        pattern=r"\-?[0-9]+(?:\.?[0-9]*)[-+][0-9]+(?:\.?[0-9]*)j"
        bound=max([len(a) for a in re.findall(pattern,ns)])-2
    elif not mat._isIdentity:
        try:
            i=min([min(a) for a in mat._inRange.values()])
            j=max([max(a) for a in mat._inRange.values()])
            b1=__digits(i)
            b2=__digits(j)
            bound=max([b1,b2])
        except ValueError:
            print("Dimension parameter is required")
            return ""
    else:
        bound=2
        
    if mat._fMat or mat._cMat:
        pre="0:.{}f".format(mat.decimal)
        st="{"+pre+"}"
        interval=[float("-0."+"0"*(mat.decimal-1)+"1"),float("0."+"0"*(mat.decimal-1)+"1")] 
        
    for rows in range(mat.dim[0]):
        string+="\n"
        for cols in range(mat.dim[1]):
            num=mat._matrix[rows][cols]

            if mat._cMat:
                if num.imag>=0:
                    item=str(round(num.real,mat.decimal))+"+"+str(round(num.imag,mat.decimal))+"j "
                else:
                    item=str(round(num.real,mat.decimal))+str(round(num.imag,mat.decimal))+"j "
                s=len(item)-4
                
            elif mat._fMat:
                if num>interval[0] and num<interval[1]:
                    num=0.0
                item=st.format(round(num,mat.decimal))
                s=__digits(num)
                
            else:
                item=str(num)
                s=__digits(num)
                
            string += " "*(bound-s)+item+" "

    return string