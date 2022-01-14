class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(numRows):
            currRow = [None for _ in range(i + 1)]
            currRow[0], currRow[-1] = 1, 1

            for j in range(1, len(currRow) - 1):
                currRow[j] = ans[i-1][j-1] + ans[i-1][j]

            ans.append(currRow)

        return ans
