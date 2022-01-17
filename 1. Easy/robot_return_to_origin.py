class Solution:
    def judgeCircle(self, moves: str) -> bool:
        moves = Counter(list(moves))
        return moves['L'] == moves['R'] and moves['U'] == moves['D']
