'''
经典DP 类似多状态的斐波那契数列
f(n, True) = f(n-1, False) + nums[n]
f(n, False) = max(f(n-1, False), f(n-1, True))
'''


class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        steal, ignore = nums[0], 0
        for i in range(1, len(nums)):
            steal, ignore = ignore + nums[i], max(steal, ignore)

        return max(steal, ignore)

tests = (
    ([1, 2, 3, 1], 4),
    ([2, 7, 9, 3, 1], 12)
)

for nums, r in tests:
    print(nums, Solution().rob(nums) == r)
