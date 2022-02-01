class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        n, ans = len(grid), 0

        for i in range(n):
            for j in range(n):
                if grid[i][j]: ans += 2 + grid[i][j] * 4
                if i: ans -= min(grid[i][j], grid[i - 1][j]) * 2
                if j: ans -= min(grid[i][j], grid[i][j - 1]) * 2

        return ans
