class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count, ans = [0] * len(nums), []

        for num in nums:
            count[num - 1] += 1
            if count[num - 1] == 2:
                ans.append(num)

        ans.append(count.index(0) + 1)

        return ans
            
