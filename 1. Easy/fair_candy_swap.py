class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sum_a, sum_b, setB = sum(aliceSizes), sum(bobSizes), set(bobSizes)

        for candy in aliceSizes:
            if candy + (sum_b - sum_a) // 2 in setB:
                return [candy, candy + (sum_b - sum_a) // 2]
