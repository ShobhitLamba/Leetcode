class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 0:
            ans = []
        else:
            ans = [0]

        for i in range(n // 2):
            ans.extend([i + 1, -i - 1])

        return ans

            
