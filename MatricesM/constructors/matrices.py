"""
Create special matrices
"""

def Identity(dim=1):
    """
    Identity matrix
    dim : integer or a list/tuple of integers (first element is used as dimensions)
    """
    if not isinstance(dim,int):
        dim = dim[0]

    matrix=[[0 for a in range(dim)] for b in range(dim)]
    for row in range(dim):
        matrix[row][row]=1
    return matrix

def Symmetrical(dim=None,ranged=[0,1],fill="uniform"):
    """
    Symmetrical matrix
    """
    if list(ranged) == [0,1] and fill == "uniform":
        from MatricesM.C_funcs.constructors import symzerone
        return symzerone(dim)
