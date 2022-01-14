class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        ans, nums, i = 0, sorted(nums), 0

        while i < len(nums):
            ans += nums[i]
            i += 2

        return ans
        
