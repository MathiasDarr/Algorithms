class Solution:
    def numTrees(self, n):
        memo = {0:1, 1:1}
        def num_unique(n):
            if n in memo:
                return memo[n]
            else:
                total = 0
                for i in range(1, n + 1):
                    total += num_unique(i - 1) * num_unique(n - i)
                memo[n] = total
                return total
        return num_unique(n)

    def numTreesIterative(self, n):
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += dp[j] * dp[i - 1 - j]
        return dp[n]

    def generateTrees(self, n):
        if n ==0:
            return []
        results = []
        def recursive(number):
            pass




solution = Solution()
solution.numTreesIterative(3)