def addDim(mat,num):
    """
    Add dimensions to identity matrix
    """
    try:
        assert isinstance(num,int) and num>0
    except AssertionError:
        print("Invalid input in addDim")
    except Exception as err:
        print(err)
    else:
        goal=mat.dim[0]+num
        mat._Matrix__dim=[goal,goal]
        mat._setMatrix()
        return mat