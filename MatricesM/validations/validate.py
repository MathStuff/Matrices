def validlist(lis,throw=False):
    if lis == [] or lis == None:
        if throw:
            raise ValueError("Matrix is empty")
        else:
            return None
    else:
        return lis

def consistentlist(lis,typ,lisname="",throw=False,*args):
    res = all([1 if isinstance(i,typ) else 0 for i in lis])
    if throw and not res:
        from MatricesM.errors.errors import InconsistentValues
        raise InconsistentValues(lisname,typ,". ".join(args))
    return res

def sublist(sub,sup,subname="",supname="",throw=False,*args):
    res = all([1 if i in sup else 0 for i in sub])
    if throw and not res:
        from MatricesM.errors.errors import NotSubList
        raise NotSubList(subname,supname,". ".join(args))
    return res

def rangedlist(lis,compare,lisname="",rangeas="",throw=False,*args):
    res = all([1 if compare(i) else 0 for i in lis])
    if throw and not res:
        from MatricesM.errors.errors import OutOfRangeList
        raise OutOfRangeList(lisname,rangeas,". ".join(args))
    return res