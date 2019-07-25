def validlist(lis,throw=False):
    try:
        if lis == [] or lis == None:
            if throw:
                raise ValueError("Matrix is empty")
            else:
                return None
        else:
            return lis
    except Exception as err:
        if throw:
            raise err
        return False
        
def exactdimension(lis,d0,d1,throw=False):
    if len(lis)!=d0:
        if throw:
            from MatricesM.errors.errors import DimensionError    
            raise DimensionError(f"Expected {d0} rows, got {len(lis)}") 
        return False
    if not all([len(inner)==d1 for inner in lis]):
        if throw:
            from MatricesM.errors.errors import DimensionError    
            raise DimensionError(f"Rows in the list should have {d1} columns")
        return False
    return True

def consistentlist(lis,typ,lisname="indices",throw=False,*args):
    try:
        res = all([1 if isinstance(i,typ) else 0 for i in lis])
        if throw and not res:
            from MatricesM.errors.errors import InconsistentValues
            raise InconsistentValues(lisname,typ,". ".join(args))
        return res
    except Exception as err:
        if throw:
            raise err
        return False

def sublist(sub,sup,subname="list of indices",supname="indices",throw=False,*args):
    try:
        res = all([1 if i in sup else 0 for i in sub])
        if throw and not res:
            from MatricesM.errors.errors import NotSubList
            raise NotSubList(subname,supname,". ".join(args))
        return res
    except Exception as err:
        if throw:
            raise err
        return False
def rangedlist(lis,compare,lisname="indices",rangeas="[0,0]",throw=False,*args):
    try:
        res = all([1 if compare(i) else 0 for i in lis])
        if throw and not res:
            from MatricesM.errors.errors import OutOfRangeList
            raise OutOfRangeList(lisname,rangeas,". ".join(args))
        return res
    except Exception as err:
        if throw:
            raise err
        return False