class Solution:
    def numSquaresBFS(self, n):
        squares = [i ** 2 for i in range(1, int(n ** .5) + 1)]  # O(sqrt(n))
        level = [n]
        count = 0

        # 1->sqrt(n)->sqrt(n)^2->sqrt(n)^3->...-> O(sqrt(n)^h) = O(n^(h/2))
        while level:
            next_level = set()
            for remainder in level:
                if remainder == 0: return count
                for square in squares:
                    if remainder < square: break
                    next_level.add(remainder - square)
            count += 1
            level = next_level
        return count

    def numSquares(self, n):
        dp = [float('inf')] * (n+1 )
        dp[0] = 0
        maxSquare = int(n**.5)
        squares = [x**2 for x in range(1,maxSquare +1)]
        for i in range(1,len(dp)):
            for square in squares:
                if i - square >= 0:
                    dp[i] = min(dp[i], dp[i-square] +1)
        return dp[-1]
    def coinChange(self, coins, amount):
        dp = [amount+1] * (amount +1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin] +1)
        return dp[-1] if dp[-1] != amount+1 else -1

solution =Solution()
coins = [1,2,5]
amount = 11

# ncoins = solution.coinChange(coins, amount)
solution.numSquaresBFS(13)