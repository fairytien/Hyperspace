def count_occurrences(string):
    counts = dict()
    words = string.split()
    rcounts = dict()
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    for k1, v1 in counts.items():
        rcounts.setdefault(v1, []).append(k1)
    return(rcounts)
