class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbors = [(0,1),(1,0),(1,1),(-1,-1),(-1,0),(0,-1),(-1,1),(1,-1)]

        rows, cols = len(board), len(board[0])

        copy = [[board[r][c] for c in range(cols)] for r in range(rows)]

        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0

                for x, y in neighbors:
                    r, c = row + x, col + y

                    if (0 <= r < rows) and (0 <= c < cols) and (copy[r][c] == 1):
                        live_neighbors += 1

                # Rule 1 or Rule 3
                if copy[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = 0
                # Rule 4
                if copy[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 1
                    
