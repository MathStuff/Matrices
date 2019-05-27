def describe(mat,obj):
    if mat._cMat:
        return None
    if mat.dim[0]<=1:
        return None
    #Create the base of the description matrix
    valid_feats_inds = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
    valid_feats_names = [mat.features[i] for i in valid_feats_inds]

    desc_mat = obj((len(valid_feats_inds),9),fill=0,
                  features=["Column","dtype","mean","sdev","min","max","25%","50%","75%"],
                  dtype="dataframe",coldtypes=[str,type]+[float]*7)

    #Gather the data
    dtypes = [mat.coldtypes[t] for t in valid_feats_inds]
    mean = mat.mean()
    sdev = mat.sdev()
    ranges = mat.ranged()
    iqrs = mat.iqr(as_quartiles=True)

    #Fill the matrix
    temp = []
    for i in range(len(valid_feats_inds)):
        name = valid_feats_names[i]
        temp.append([name,dtypes[i],mean[name],sdev[name],ranges[name][0],ranges[name][1],iqrs[name][0],iqrs[name][1],iqrs[name][2]])

    desc_mat._matrix = temp
    return desc_mat
