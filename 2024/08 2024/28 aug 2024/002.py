def longestCommonPrefix( strs) -> str:
    res = ""
    print(list(zip(*strs)))
    # zip returns a tuple of the elements with the same index

    for a in zip(*strs):
        if len(set(a)) == 1: 
            res += a[0]
        else: 
            return res
    return res
strs = ['flo', 'flower', 'flight']

print(longestCommonPrefix(strs))