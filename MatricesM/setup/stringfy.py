def _stringfy(mat,dtyps=None):
    
    import re
    pre = "0:.{}f".format(mat.decimal)
    st = "{"+pre+"}"    
    string=""

    #Empty matrix check
    if mat.matrix in [ [], None ]:
        return "Empty matrix"

    #Tab sizes
    #Dataframe
    if mat._dfMat:
        bounds=[]
        ranges = mat.ranged()
        feats = mat.features[:]
        decimals = mat.decimal
        m = mat.matrix

        for dt in range(len(dtyps)):

            colbounds=[]
            if dtyps[dt] in [float,int]:
                colbounds.append(len(st.format(round(ranges[feats[dt]][0],decimals))))
                colbounds.append(len(st.format(round(ranges[feats[dt]][1],decimals))))

            elif dtyps[dt] == complex:
                ns=""
                for i in range(mat.d0):
                    num = m[i][dt]
                    ns+=str(round(num.real,mat.decimal))
                    im=num.imag
                    if im<0:
                        ns+=str(round(im,mat.decimal))+"j "
                    else:
                        ns+="+"+str(round(im,mat.decimal))+"j "
                            
                pattern=r"\-?[0-9]+(?:\.?[0-9]*)[-+][0-9]+(?:\.?[0-9]*)j"
                colbounds.append(max([len(a) for a in re.findall(pattern,ns)]))

            else:
                colbounds.append(max([len(str(a)) for a in mat.col(dt+1,0)]))

            colbounds.append(len(mat.features[dt]))
            bounds.append(max(colbounds))
                
    #Complex
    elif mat._cMat:
        #Update this nonsense :)
        try:
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

        except TypeError:
            msg = f"Invalid value for complex dtype matrix: '{j}'"
            raise TypeError(msg)
    #Float
    elif mat._fMat:
        try:
            bounds=[]
            for c in range(mat.dim[1]):
                colbounds=[]
                col = mat.col(c+1,0)
                colbounds.append(len(st.format(round(min(col),mat.decimal))))
                colbounds.append(len(st.format(round(max(col),mat.decimal))))
                bounds.append(max(colbounds))
        except TypeError:
            msg = f"Invalid values for float dtype in column: '{mat.features[c]}'"
            raise TypeError(msg)
    #Integer
    else:
        try:
            bounds=[]
            for c in range(mat.dim[1]):
                colbounds=[]
                col = mat.col(c+1,0)
                colbounds.append(len(str(min(col))))
                colbounds.append(len(str(max(col))))
                bounds.append(max(colbounds))
        except TypeError:
            msg = f"Invalid values for integer dtype in column: '{mat.features[c]}'"
            raise TypeError(msg)
    #-0.0 error interval set    
    if mat._fMat or mat._cMat:
        interval=[float("-0."+"0"*(mat.decimal-1)+"1"),float("0."+"0"*(mat.decimal-1)+"1")] 

    #Dataframe
    if mat._dfMat:
        #Add features
        string += "\n"
        for cols in range(mat.dim[1]):
            name = mat.features[cols]
            s = len(name)
            string += " "*(bounds[cols]-s)+name+"  "
        
        #Add elements
        for rows in range(mat.dim[0]):
            string += "\n"
            for cols in range(mat.dim[1]):
                num = mat._matrix[rows][cols]
                #float column
                if dtyps[cols] == float:
                    try:
                        item = st.format(num)
                    except:
                        item = str(num)
                    finally:
                        s = len(item)
                #integer column
                elif dtyps[cols] == int:
                    try:
                        item = str(int(num))
                    except:
                        item = str(num)
                    finally:
                        s = len(item)
                #complex column
                elif dtyps[cols] == complex:
                    try:
                        num = complex(num)
                        if num.imag == 0:
                            num = num.real
                        item = st.format(num)
                    except:
                        item = str(num)
                    finally:
                        s = len(item)
                #Any other type column
                else:
                    item = str(num)
                    s = len(item)
                string += " "*(bounds[cols]-s)+item+"  "
    #int/float/complex
    else:
        for rows in range(mat.dim[0]):
            string+="\n"
            for cols in range(mat.dim[1]):
                num=mat._matrix[rows][cols]

                #complex
                if mat._cMat:
                    if num.imag>=0:
                        item=str(round(num.real,mat.decimal))+"+"+str(round(num.imag,mat.decimal))+"j "
                    else:
                        item=str(round(num.real,mat.decimal))+str(round(num.imag,mat.decimal))+"j "
                    s=len(item)-4
                    string += " "*(bound-s)+item+" "
                    continue

                #float
                elif mat._fMat:
                    if num>interval[0] and num<interval[1]:
                        num=0.0
                    item = st.format(num)
                    s = len(item)

                #integer
                else:
                    item = str(int(num))
                    s = len(item)
                
                string += " "*(bounds[cols]-s)+item+" "

    return string