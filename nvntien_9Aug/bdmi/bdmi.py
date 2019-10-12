def bdmi(dic):
    newdic = {}
    for key, value in dic.items():
        for string in value:
            newdic.setdefault(string, []).append(key)
    return(newdic)
