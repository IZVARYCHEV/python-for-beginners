def LevensteinDistance(s, t):
    n, m = len(t), len(s)
    v0 = list(range(n)) + [0]
    v1 = [0] * (n + 1)

    for i in range(m):
        v1[0] = i + 1
        for j in range(n):
            deletionCost = v0[j + 1] + 1
            insertionCost = v1[j] + 1
            if s[i] == t[j]:
                subtititionCost = v0[j]
            else:
                subtititionCost = v0[j] + 1
                v1[j + 1] = min(deletionCost,
                                insertionCost,
                                subtititionCost)
        v0, v1 = v1, v0
    return v0[n]
