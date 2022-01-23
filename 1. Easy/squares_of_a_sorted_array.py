class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [None] * len(nums)

        i, j, idx = 0, len(nums) - 1, len(nums) - 1

        while i <= j:
            if abs(nums[i]) >= abs(nums[j]):
                ans[idx] = nums[i] ** 2
                i += 1
            else:
                ans[idx] = nums[j] ** 2
                j -= 1
            idx -= 1

        return ans
