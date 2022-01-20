class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c_max = max(candies)
        ans = []

        for candy in candies:
            if candy + extraCandies >= c_max:
                ans.append(True)
            else:
                ans.append(False)

        return ans
        
