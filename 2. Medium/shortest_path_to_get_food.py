class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "*":
                    q.append((i, j, 0))
                    break

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while q:
            r, c, cnt = q.popleft()
            if grid[r][c] == "X": continue
            elif grid[r][c] == "#": return cnt
            grid[r][c] = "X"
            for x, y in directions:
                nr, nc = r + x, c + y
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc] != "X":
                    q.append((nr, nc, cnt + 1))

        return -1
