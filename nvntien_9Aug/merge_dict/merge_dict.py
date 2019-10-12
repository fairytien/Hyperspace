def merge_dict(dictionaries):
    fdict = {}
    for d in dictionaries:
        for k, v in d.items():
            fdict.setdefault(k, []).append(v)
    return(fdict)
