class Solution:
    def arraySign(self, nums: List[int]) -> int:
        flag = 1

        for num in nums:
            if num == 0:
                return 0
            elif num < 0:
                flag *= -1

        return flag
