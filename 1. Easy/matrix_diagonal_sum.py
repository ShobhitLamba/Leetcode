class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        l = len(mat)
        l2r = sum([mat[i][i] for i in range(l)])
        r2l = sum([mat[i][~i] for i in range(l)])
        if l % 2 == 0:
            return l2r + r2l
        else:
            return l2r + r2l - mat[l//2][l//2]
