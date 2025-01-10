class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost) == 2:
            return min(cost)

        def helper(cost: List[int]):
            last_cost = cost[1]
            second_last = cost[0]
            for c in cost[2:]:
                tmp = last_cost
                last_cost = min(last_cost + c, second_last + c)
                second_last = tmp
            
            return last_cost

        return min(helper(cost[:-1]), helper(cost))
