class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [float('inf')] * n
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]
        return min(dp[-2:])


cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
solution = Solution()
solution.minCostClimbingStairs(cost)