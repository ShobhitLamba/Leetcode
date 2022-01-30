class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min_cost = [0] * (len(cost) + 1)

        for i in range(2, len(cost) + 1):
            take_one = min_cost[i - 1] + cost[i - 1]
            take_two = min_cost[i - 2] + cost[i - 2]
            min_cost[i] = min(take_one, take_two)

        return min_cost[-1]
            
