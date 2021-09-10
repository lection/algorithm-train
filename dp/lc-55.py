"""
当身处下标i的位置时
之前能走到的最大坐标如果小于i 则终止 无法继续前进
当前i能走到最远的下标是 i + nums[i]
这种可以不用维护一个dp数组的递推 效率更快一点
"""


class Solution:
    def canJump(self, nums) -> bool:
        if not nums:
            return False
        max_index = 0
        for i in range(len(nums) - 1):
            if i > max_index:
                return False
            max_index = max(max_index, i + nums[i])
        return max_index >= (len(nums) - 1)


tests = (
    ([2, 3, 1, 1, 4], True),
    ([3, 2, 1, 0, 4], False),
    ([1], True),
    ([0], True),
    ([0, 1], False),
)

for nums, r in tests:
    print(nums, Solution().canJump(nums) == r)
