class Solution:
    def uniqueLetterString(self, s: str) -> int:
        d = defaultdict(lambda:(0, 0))
        res = a = 0
        for i, c in enumerate(s, 1):
            a += i - 2 * (d[c][1] - d[c][0]) - d[c][0]
            res += a
            d[c] = (d[c][1], i)
        return res
