'''
解法类似斐波那契数列
f(n) = f(n-1) + f(n-2)
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 1
        if n <= 0:
            return a

        if n == 1:
            return b

        for i in range(2, n + 1):
            a, b = b, a + b

        return b


tests = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 5),
    (30, 1346269),
)

solution = Solution()
for n, r in tests:
    print(n, solution.climbStairs(n) == r)
