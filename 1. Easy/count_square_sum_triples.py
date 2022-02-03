class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0

        for a in range(1, n):
            for b in range(a + 1, n):
                c = int(sqrt(a * a + b * b))
                if a * a + b * b == c * c and c <= n:
                    ans += 2

        return ans 
