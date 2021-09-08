"""
变体DP 目前的思路是将数组转化为sum_map 去重后获得key_nums从小到大的进行递推
变成数组后就类似打家劫舍

if map(nums[i-1]):
    fn(i, True) = fn(i-1, False) + map[nums[i]]
else:
    fn(i, True) = max(fn(i-1, False), fn(i-1, False)) + map[nums[i]]

fn(i, False) = max(fn(i-1, True), fn(i-1, False))
"""


class Solution:
    def deleteAndEarn(self, nums) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        sum_map = {}
        for n in nums:
            if n not in sum_map:
                sum_map[n] = 0
            sum_map[n] += n
        nums = sorted(sum_map.keys())

        # 变量起名费劲 继续沿用打家劫舍的变量名
        steal, ignore = sum_map[nums[0]], 0
        for i in range(1, len(nums)):
            n = nums[i]
            sum_value = sum_map[n]
            last_max = max(steal, ignore)
            if n - 1 in sum_map:
                steal, ignore = ignore + sum_value, last_max
            else:
                steal, ignore = last_max + sum_value, last_max
        return max(steal, ignore)


tests = (
    ([[3, 4, 2], 6]),
    ([[2, 2, 3, 3, 3, 4], 9]),
    ([[3, 1], 4]),
)

for nums, r in tests:
    print(nums, Solution().deleteAndEarn(nums) == r)
