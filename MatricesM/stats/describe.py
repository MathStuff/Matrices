def describe(mat,obj):
    from MatricesM.matrix import dataframe
    if mat._cMat:
        return None
    if mat.dim[0]<=1:
        return None
    #Create the base of the description matrix
    valid_feats_inds = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
    valid_feats_names = [mat.features[i] for i in valid_feats_inds]

    desc_mat = obj((len(valid_feats_inds),10),fill=0,
                  features=["Column","dtype","count","mean","sdev","min","25%","50%","75%","max"],
                  dtype=dataframe,coldtypes=[str,type,int,float,float,float,float,float,float,float])

    #Gather the data
    dtypes = [mat.coldtypes[t] for t in valid_feats_inds]
    counts = mat.count()
    mean = mat.mean()
    sdev = mat.sdev()
    ranges = mat.ranged()
    iqrs = mat.iqr(as_quartiles=True)
    
    #Fill the matrix
    temp = []
    for i in range(len(valid_feats_inds)):
        name = valid_feats_names[i]
        temp.append([name,dtypes[i],counts[name],mean[name],sdev[name],ranges[name][0],iqrs[name][0],iqrs[name][1],iqrs[name][2],ranges[name][1]])

    desc_mat._matrix = temp
    return desc_mat
