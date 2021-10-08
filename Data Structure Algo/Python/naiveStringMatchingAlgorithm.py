def naiveSearch(T,P):
    n = len(T)
    m = len(P)

    for s in range(n-m):
        if P[1:m] == T[s+1:s+m]: print("Pattern occurs at", str(s))


txt = "AABAACAADAABAAABAA"
pat = "AABA"
naiveSearch(txt,pat)
