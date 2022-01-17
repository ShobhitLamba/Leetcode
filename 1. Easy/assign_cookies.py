class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g, s = sorted(g), sorted(s)
        j, l_g = 0, len(g)
        
        for i in range(len(s)):
            if s[i] >= g[j]:
                j += 1

            if j == l_g:
                break

        return j
