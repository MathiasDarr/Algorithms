


class Solution:
    def integerBreak(self, n):

        dp = [0] * (n+1)
        for i in range(1,n+1):
            for j in range(1,i):
                dp[i] = max([(i-j)*j, dp[i-j]*j, dp[i]])
        return dp[n]

solution = Solution()
solution.integerBreak(6)