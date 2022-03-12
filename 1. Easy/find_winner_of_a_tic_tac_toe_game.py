class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = 3
        rows, cols = [0] * n, [0] * n
        diag = anti_diag = 0
        player = 1
        for r, c in moves:
            rows[r] += player
            cols[c] += player
            if r == c:
                diag += player
            if r + c == n - 1:
                anti_diag += player

            if any(abs(line) == n for line in (rows[r], cols[c], diag, anti_diag)):
                return "A" if player == 1 else "B"

            player *= -1

        return "Draw" if len(moves) == 9 else "Pending"
