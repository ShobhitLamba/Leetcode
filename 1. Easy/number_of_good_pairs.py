class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = 0

        for v in count.values():
            ans += reduce(lambda x, y: x + y, range(v))

        return ans
        
