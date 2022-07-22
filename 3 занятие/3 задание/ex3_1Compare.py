def compare(S1, S2):
    ngrams = [S1[i:i + 3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)
    return count / max(len(S1), len(S2))
