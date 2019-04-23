"""
Create special matrices
"""

def Identity(dim=1):
    """
    Identity matrix
    """
    if not isinstance(dim,int):
        return None
    matrix=[[0 for a in range(dim)] for b in range(dim)]
    for row in range(dim):
        matrix[row][row]=1
    return matrix
