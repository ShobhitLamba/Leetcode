class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = 0

        for k, v in count.items():
            if k + 1 in count:
                ans += v

        return ans        
