def roundto(val,decimal:int=8,force:bool=False):
    """
    Better round function which works with complex numbers and lists
    val:Any; value to round
    decimal:int>=0; decimal places to round to
    force:bool; force value rounding as complex number rounding
    """
    if isinstance(val,complex) or force:
        return complex(round(val.real,decimal),round(val.imag,decimal))
    elif isinstance(val,(int,float)):
        return round(val,decimal)
    elif isinstance(val,list):
        return [roundto(value,decimal) for value in val]
    elif type(val).__name__ == 'null':
        return val
    else:
        try:
            if val.__name__ == "Matrix":
                return round(val,decimal)
            else:
                raise Exception
        except:
            raise TypeError(f"Can't round {val}.")

def overwrite_attributes(mat,kw):
    from MatricesM.errors.errors import ParameterError

    attributes = ["dim","data","fill","ranged",
                  "seed","features","decimal","dtype",
                  "coldtypes","index","indexname","implicit"]
                  
    options = ["PRECISION","ROW_LIMIT","EIGENVEC_ITERS",
               "QR_ITERS","NOTES","DIRECTORY",
               "DEFAULT_NULL"]
    
    #Override the attributes given in kwargs with new values
    for key,val in kw.items():
        if isinstance(val,dict) and key=="kwargs":
            for k,v in val.items():
                if k=="data":
                    mat._matrix = v
                elif k=="ranged":
                    mat._Matrix__initRange = v
                elif k in attributes:
                    exec(f"mat._Matrix__{k}=v")
                elif k in options:
                    exec(f"mat.{k}=v")
                else:
                    raise ParameterError(k,attributes+options)
        else:
            exec(f"mat.{key}=val")

def read_file(directory:str,encoding:str="utf8",delimiter:str=","):
    from MatricesM.setup.fileops import readAll
    from MatricesM.matrix import dataframe

    directory = directory.replace("\\","/")
    (feats,data,cdtypes) = readAll(directory,encoding,delimiter)
    return dataframe(data,feats,coldtypes=cdtypes,DIRECTORY=directory)

def save_file(matrix:object,directory:str,newline:str="",encoding:str="utf8",options:["no_name","no_index"]=[]):
    if ".csv" in directory:
        from MatricesM.setup.fileops import save_csv
        save_csv(matrix,directory,newline,encoding,options)
    
    elif ".txt" in directory:
        pass

    else:
        pass