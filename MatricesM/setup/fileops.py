def readAll(d):
    try:
        data="" 
        with open(d,"r",encoding="utf8") as f:
            for lines in f:
                data+=lines
    except FileNotFoundError:
        raise FileNotFoundError("No such file or directory")
    else:
        f.close()
        return data