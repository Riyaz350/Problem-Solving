class Solution(object):
    def closeStrings(self, word1, word2):
        c1 = Counter(word1)
        c2 = Counter(word2)

        v1 = Counter([v for v in c1.values()])
        v2 = Counter([v for v in c2.values()])

        return c1 == c2 or (v1 == v2 and set(word1) == set(word2))