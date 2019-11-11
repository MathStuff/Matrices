class MatrixError(Exception):
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message

class DimensionError(MatrixError):
    def __init__(self,err,*args):
        self.message  = err

class NotListOrTuple(MatrixError):
    """
    A list or a tuple is required
    """
    def __init__(self,err,*args):
        self.message = f"Given value should be a list or a tuple, not '{type(err).__name__}'"+". ".join(args)

class EmptyMatrix(MatrixError):
    """
    Matrix is empty
    """
    def __init__(self,err,*args):
        self.message  = str(err).join(args)

class InvalidColumn(MatrixError):
    """
    Invalid column name
    """
    def __init__(self,err,*args):
        self.message  = f"'{type(err).__name__}' type index '{err}' can't be used as a column index. "+". ".join(args)

class InvalidIndex(MatrixError):
    """
    Invalid row index
    """
    def __init__(self,err,*args):
        self.message  = f"'{type(err).__name__}' type index '{err}' can't be used as a row index. "+". ".join(args)

class FillError(MatrixError):
    """
    Error filling matrices
    """
    def __init__(self,err,*args):
        self.message  = f"'{type(err).__name__}' type '{err}' can't be used to fill matrices. "+". ".join(args)

class DtypeError(MatrixError):
    """
    dtype error
    """
    def __init__(self,err,*args):
        self.message = f"'{err}' isn't a valid value for dtype.\ndtype only accepts following values : int|float|complex|dataframe. "+". ".join(args)

class ColdtypeError(MatrixError):
    """
    Invalid column dtype
    """
    def __init__(self,err,*args):
        self.message = f"'{type(err).__name__}' type '{err}' can't be used as column dtype. \ncoldtypes should be all 'type' objects. "+". ".join(args)

class InconsistentValues(MatrixError):
    """
    Different value types in a column
    """
    def __init__(self,lis,typ,*args):
        self.message  = f"Given {lis} has inconsistent values. \nAll values inside should be '{type(typ).__name__}' type. "+". ".join(args)

class NotSubList(MatrixError):
    """
    Given list have values that aren't in the list used as look-up list
    """
    def __init__(self,sub,sup,*args):
        self.message  = f"Given {sub} has values that aren't in matrix's {sup}. \n"+". ".join(args)

class OutOfRangeList(MatrixError):
    """
    Given list have values that aren't in the given range
    """
    def __init__(self,lis,r,*args):
        self.message  = f"Given {lis} should have values in range {r} \n"+". ".join(args)
    
class InvalidList(MatrixError):
    """
    Invalid values to set for coldtypes,features etc.
    """
    def __init__(self,err,req,attribute,*args):
        import re
        given_dtypes = str(re.findall(r"'(?P<inner>\w+)'","{}".format(err))).replace("'","")
        self.message = f"'{type(err).__name__}' type {given_dtypes} can't be used as a length {req} list to replace {attribute}. Expected {req} items, got {len(err)}"+". ".join(args)

class ParameterError(MatrixError):
    """
    parameter error
    """
    def __init__(self,err,params,*args):
        self.message = f"'{err}' isn't a valid parameter name.\nAvailable parameter names:\n\t{params}. "+". ".join(args)
