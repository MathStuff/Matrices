def joins(mat,table,method,obj):
    if not method in ["inner","left","left-ex","right","right-ex","outer","outer-ex"]:
        raise ValueError(f"{method} is not a join method.")
    if not isinstance(table,obj):
        raise TypeError(f"Can't use type {type(table).__name__} as a Matrix")
    
    