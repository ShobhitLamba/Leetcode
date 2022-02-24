class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones, ans = 0, 0

        for c in s:
            if c == '1':
                ones += 1
            else:
                ans += 1
            print(ones, ans)
            ans = min(ones, ans)

        return ans
