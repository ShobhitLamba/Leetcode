class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        ans = 0

        for box in boxTypes:
            ans += min(box[0], truckSize) * box[1]
            truckSize = max(0, truckSize - box[0])
            if truckSize == 0:
                return ans

        return ans
