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
                  "coldtypes","index","implicit"]
                  
    options = ["PRECISION","ROW_LIMIT","EIGENVEC_ITERS",
               "QR_ITERS","NOTES","DIRECTORY",
               "DEFAULT_NULL"]

    display_keys = ['allow_label_dupes','dupe_place_holder','label_seperator',
                    'left_top_corner','left_seperator','top_seperator',
                    'col_place_holder','row_place_holder']
                    
    #Override the attributes given in kwargs with new values
    for k,v in kw.items():
        if k=="data":
            mat._matrix = v
        elif k=="ranged":
            mat._Matrix__initRange = v
        elif k in attributes:
            exec(f"mat._Matrix__{k}=v")
        elif k in options:
            exec(f"mat.{k}=v")
        elif k == "DISPLAY_OPTIONS":
            if not isinstance(v,dict):
                raise TypeError("'DISPLAY_OPTIONS' options requires a dict")
            
            if not all([key in display_keys for key in list(v.keys())]):
                raise TypeError("'DISPLAY_OPTIONS' options requires a dict with following keys:\n"+str(display_keys))

            for option,value in v.items():
                mat.DISPLAY_OPTIONS[option] = value
        else:
            raise ParameterError(k,attributes+options+["DISPLAY_OPTIONS"])

def read_file(directory:str,encoding:str="utf8",delimiter:str=",",**kwargs):
    from MatricesM.setup.fileops import readAll
    from MatricesM.matrix import dataframe

    directory = directory.replace("\\","/")
    (feats,data,cdtypes) = readAll(directory,encoding,delimiter)
    return dataframe(data,feats,coldtypes=cdtypes,DIRECTORY=directory,**kwargs)

def save_file(matrix:object,directory:str,newline:str="",encoding:str="utf8",options:["no_name","no_index"]=[]):
    if ".csv" in directory:
        from MatricesM.setup.fileops import save_csv
        
        save_csv(matrix,directory,newline,encoding,options)
        
        matrix.DIRECTORY = directory

    elif ".txt" in directory:
        pass

    else:
        pass