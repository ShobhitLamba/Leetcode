class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        s = sum(nums)
        l_sum = 0

        for i, num in enumerate(nums):
            if l_sum == (s - l_sum - num):
                return i
            l_sum += num

        return -1
