from typing import List

def minCostClimbingStairs(self, cost: List[int]) -> int:
    # s: cumulative cost of step. prev is previous step
    prev, s = 0, 0
    # iterative DP - take one step at a time
    for i in range(len(cost)):
        # cumulative cost of step i is to take step i as the last step, either from
        # the previous step or the previous previous step
        prev, s = s, cost[i] + min(prev, s)
    return min(prev, s)
    