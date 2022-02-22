class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        for i in range(len(s)):
            ans += self.countPalindromesAroundCenter(s, i, i) + self.countPalindromesAroundCenter(s, i, i + 1)

        return ans

    def countPalindromesAroundCenter(self, s, lo, hi):
        ans = 0

        while lo >= 0 and hi < len(s):
            if s[lo] != s[hi]:
                break
            lo -= 1
            hi += 1

            ans += 1

        return ans
            
