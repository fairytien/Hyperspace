def generate_autocomplete(words):
    ans = {}
    for i in words:
        for j in range(1, len(i) + 1):
            s = i[:j]
            ans[s] = {k for k in words if k.startswith(s)}
    return(ans)
