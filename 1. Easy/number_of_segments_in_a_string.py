class Solution:
    def countSegments(self, s: str) -> int:
        #Method 1 with counting number of segments
        #return len(s.split())

        #Method 2 with constant space
        ans = 0
        for i in range(len(s)):
            if s[i] != " " and (i == 0 or s[i-1] == " "):
                ans += 1

        return ans
