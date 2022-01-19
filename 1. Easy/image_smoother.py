class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        r, c = len(img), len(img[0])
        directions = ((0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(1,-1),(-1,1))

        ans = [[0] * c for i in range(r)]

        for i in range(r):
            for j in range(c):
                curr_sum, count = img[i][j], 1

                for d in directions:
                    i_ = i + d[0]
                    j_ = j + d[1]
                    if 0 <= i_< r and 0 <= j_ < c:
                        curr_sum += img[i_][j_]
                        count += 1

                    ans[i][j] = curr_sum // count

        return ans
