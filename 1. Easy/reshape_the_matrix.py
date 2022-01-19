class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        r_, c_ = len(mat), len(mat[0])

        if r_ * c_ != r * c:
            return mat

        temp = [x for row in mat for x in row]

        return [temp[i * c: (i + 1) * c] for i in range(r)]
        
