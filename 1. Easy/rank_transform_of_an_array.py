class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        arr_sorted = sorted(list(set(arr)))

        ans = []

        for num in arr:
            ans.append(1 + bisect_left(arr_sorted, num))

        return ans
