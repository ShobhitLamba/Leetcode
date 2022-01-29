class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1
        ans = -1

        while l < r:
            curr_sum = nums[l] + nums[r]
            if curr_sum < k:
                ans = max(ans, curr_sum)
                l += 1
            else:
                r -= 1

        return ans
