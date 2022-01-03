class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            if target - val in seen:
                return [i, seen[target - val]]
            else:
                seen[val] = i
