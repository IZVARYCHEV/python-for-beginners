class Sr:
    def compare(self, S1, S2):
        #        a1 = self.arg1
        #        a2 = self.arg2
        #        print(a1)
        #        print(a2)
        ngrams = [S1[i:i + 3] for i in range(len(S1))]
        count = 0
        for ngram in ngrams:
            count += S2.count(ngram)
        return count / max(len(S1), len(S2))
