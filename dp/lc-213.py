"""
经典DP 传统做法如下
fn(n, True) = fn(n-1, False) + nums[n]
fn(n, False) = max(fn(n-1, True), fn(n-1, False))
简单思路是 fn(0, True) 和 fn(0, False) 强制都计算
"""


class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        # 1 是第一家偷的情况 2 是第一家不偷的情况
        # 考虑到首家强制计算的情况 可以从第二家开始算
        steal1, ignore1, steal2, ignore2 = nums[0], nums[0], nums[1], 0
        for i in range(2, len(nums) - 1):
            n = nums[i]
            steal1, ignore1 = ignore1 + n, max(steal1, ignore1)
            steal2, ignore2 = ignore2 + n, max(steal2, ignore2)

        last = nums[-1]
        return max(steal1, ignore1, ignore2 + last, steal2)


tests = (
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([0], 0)
)

for nums, expire in tests:
    r = Solution().rob(nums)
    print(nums, expire, r, Solution().rob(nums) == expire)
