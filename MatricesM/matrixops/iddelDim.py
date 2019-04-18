def delDim(mat,num):
    """
    Delete dimensions to identity matrix
    """
    try:
        if mat.matrix==[]:
            return "Empty matrix"
        assert isinstance(num,int) and num>0 and mat.dim[0]-num>=0
    except AssertionError:
        print("Invalid input in delDim")
    except Exception as err:
        print(err)
    else:
        goal=mat.dim[0]-num
        if goal==0:
            print("All rows have been deleted")
        mat._Matrix__dim=[goal,goal]
        mat._setMatrix()
        return mat