"""
LeetCode 70 Climbing Stairs

Climb n stairs, each time can take 1 or two 2 steps, how many distinct ways to climb to the top?

"""


class Solution:
    def climbStairs(self, n):
        if n == 1 or n == 2:
            return n

        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp

solution = Solution()
solution.climbStairs(3)