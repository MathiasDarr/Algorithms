class Solution:
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount + 1)
        dp[0] = 0
        for i in range(1, len(dp)):
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    dp[i] = min(dp[i], dp[i-coins[j]] +1)
        return dp[-1] if dp[-1] != amount + 1 else -1


solution = Solution()
solution.coinChange([2], 11)