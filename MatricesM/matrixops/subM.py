def subM(mat,rowS=None,rowE=None,colS=None,colE=None):
    """
    Get a sub matrix from the current matrix
    rowS:Desired matrix's starting row (starts from 1)
    rowE:Last row(included)
    colS:First column
    colE:Last column(included)
        |col1 col2 col3
        |---------------
    row1|1,1  1,2  1,3
    row2|2,1  2,2  2,3
    row3|3,1  3,2  3,3
    
    EXAMPLES:
        ->a.subM(1)==gets the first element of the first row
        ->a.subM(2,2)==2by2 square matrix from top left as starting point
    ***Returns a new grid class/matrix***
    """
    try:
        temp2=[]
        if (rowS,rowE,colS,colE)==(None,None,None,None):
            return None
        #IF 2 ARGUMENTS ARE GIVEN, SET THEM AS ENDING POINTS
        if (rowS,rowE)!=(None,None) and (colS,colE)==(None,None):
            colE=rowE
            rowE=rowS
            rowS=1
            colS=1
        #IF MORE THAN 2 ARGUMENTS ARE GIVEN MAKE SURE IT IS 4 OF THEM AND THEY ARE VALID
        else:
            assert (rowS,rowE,colS,colE)!=(None,None,None,None) and (rowS,rowE,colS,colE)>(0,0,0,0)
        assert rowS<=mat.dim[0] and rowE<=mat.dim[0] and colS<=mat.dim[1] and colE<=mat.dim[1]
        
    except AssertionError:
        print("Bad arguments")
        return ""
    except Exception as err:
        print(err)
        return ""
    else:
        temp=mat._matrix[rowS-1:rowE]
        if len(temp):
            temp2=[temp[c][colS-1:colE] for c in range(len(temp))]
            cop = mat.copy
            cop.setMatrix([rowE-rowS+1,colE-colS+1],None,temp2)
            cop.features = mat.features[colS-1:colE]
        return cop