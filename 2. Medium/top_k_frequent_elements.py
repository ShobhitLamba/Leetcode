class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap, ans = [], []

        for key in count.keys():
            heappush(heap, (count[key], key))

        freq_table = nlargest(k, heap)

        for i, j in freq_table:
            ans.append(j)

        return ans
            
