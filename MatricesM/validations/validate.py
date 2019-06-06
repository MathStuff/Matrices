def validlist(lis,throw=False):
    if lis == [] or lis == None:
        if throw:
            raise ValueError("Matrix is empty")
        else:
            return None
    else:
        return lis
