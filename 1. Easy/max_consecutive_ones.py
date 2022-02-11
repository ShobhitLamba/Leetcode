class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_count, count_max = 0, 0

        for num in nums:
            if num == 0 and curr_count != 0:
                count_max = max(count_max, curr_count)
                curr_count = 0

            if num == 1:
                curr_count += 1

        return max(count_max, curr_count)
