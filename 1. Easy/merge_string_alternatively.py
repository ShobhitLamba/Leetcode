class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        word1, word2 = list(word1), list(word2)

        ans = []
        for i in range(min(l1, l2)):
            ans.extend([word1[i], word2[i]])

        ans = ans + word1[l2:] if l2 < l1 else ans + word2[l1:]

        return "".join(ans)    
