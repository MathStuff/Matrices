def minor(mat,row=None,col=None):
    if not isinstance(row,int) or not isinstance(col,int):
        raise ValueError("Both row and col should be integers")
    if not (row>0 and row<=mat.dim[0]) or not (col>0 and col<=mat.dim[1]):
        raise ValueError("Parameters out of range, should be from 1 to dimension")
    if not mat.isSquare:
        return None

    temp=mat.copy

    if temp.dim[0]==1 and temp.dim[1]==1:
        return temp

    if temp.dim[0]>1:   
        temp.remove(row=row)
        temp.remove(col=col)
    return temp.det