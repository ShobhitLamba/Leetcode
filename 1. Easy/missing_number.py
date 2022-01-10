class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        expected_sum = l * (l + 1) // 2
        actual_sum = reduce(lambda x, y: x + y, nums)

        return expected_sum - actual_sum
