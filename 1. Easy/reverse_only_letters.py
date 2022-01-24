class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ans = []
        l = len(ans) - 1

        for i, x in enumerate(s):
            if x.isalpha():
                while not s[l].isalpha():
                    l -= 1
                ans.append(s[l])
                l -= 1
            else:
                ans.append(x)

        return "".join(ans)        
