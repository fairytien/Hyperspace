def itranslate(dic, string):
    words = string.split()
    ans = ''
    for word in words:
        if word in dic.keys():
            ans = ans + ' ' + dic[word]
        else:
            raise KeyError("Missing word")
    return(ans[1:])
