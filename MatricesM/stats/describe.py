def describe(mat,obj,dFrame,labelobj):

    if mat._cMat:
        raise TypeError("Can't use complex numbers to describe the matrix")
    if mat.dim[0]<=1:
        raise ValueError("Not enough rows to describe the matrix")

    #Create the base of the description matrix
    labels = mat.features.labels
    valid_feats_inds = [t for t in range(len(mat.coldtypes)) if mat.coldtypes[t] in [float,int]]
    valid_feats_names = [labels[i] for i in valid_feats_inds]
    if mat.features.level == 1:
        valid_feats_names = [row[0] for row in valid_feats_names]
        
    desc_mat = obj((len(valid_feats_inds),9),fill=0,
                  features=["dtype","count","mean","sdev","min","25%","50%","75%","max"],
                  dtype=dFrame,coldtypes=[type,int,float,float,float,float,float,float,float],
                  index=labelobj(valid_feats_names,mat.features.names[:]))

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
        temp.append([dtypes[i],counts[name],mean[name],sdev[name],ranges[name][0],iqrs[name][0],iqrs[name][1],iqrs[name][2],ranges[name][1]])

    desc_mat._matrix = temp
    desc_mat.decimal = mat.decimal

    unused_names = ",".join([str(labels[i]) for i in range(mat.d1) if not i in valid_feats_inds])
    unused = f"{mat.d1-len(valid_feats_names)} Unused columns : \n\t{unused_names}" if len(unused_names) else "" 
    desc_mat.NOTES = f"Size: {mat.dim}\n"+unused
    return desc_mat
