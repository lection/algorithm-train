"""
经典DP 数组累加走到这里消耗最少的
f(n) = min(f(n-1), fn(n-2))
"""


class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        if not cost or len(cost) < 2:
            return 0

        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])

        return min(cost[-1], cost[-2])


tests = (
    ([10, 15], 10),
    ([10, 15, 20], 15),
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
)

for cost, r in tests:
    print(cost, Solution().minCostClimbingStairs(cost) == r)
