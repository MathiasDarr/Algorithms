"""
Best time to buy and sell stock I

    Given an array whose value at index i represents the price of a given stock on day i.
    Allowed a single transaction,

    Find largest difference between two numbers in the array, given that the second number is larger


Best time to buy and sell stock II
    If you are allowed unlimited transactions it's a matter of finding the difference between each valley and peak.

    Initially we are looking for a valley because we do not own any stock initially.

    Traverse from left to right incrmenting the iteration index as prices[i+1] < prices[i+1].
        one loop terminates we are at a valley so recording the value of this valley in a variable

Best time to buy and sell stock III
    At most k transactions

    This is a dynamic programming problem

    Single DP column
    profit[i][1] = profit of a single transcation including on any day up to and including day i

    Perform a backwards traversal over prices for the second iteration.
    dp[i] = max profit of first transcation.






    profit[i][t] represents the the amount of profit derived from at most t transactions up to and including day i.

    profit[i][t] = max( profit[i-1][t],   ## no transcation on day i
                        prices[i] - prices[j] + profit[j][t]




"""

class Solution:
    def maxProfit(self, prices):
        if not k or not prices or len(prices) < 2:
            return 0
        if k > len(prices) >> 1:  # You got enough transaction times to capture all possible profit
            return sum(prices[i + 1] - prices[i] for i in range(len(prices) - 1) if prices[i + 1] > prices[i])

        NH = [0] * len(prices)
        res = 0
        for j in range(k):
            H = [-float('inf')]
            cur_NH = [-float('inf')]
            for idx, p in enumerate(prices):
                H.append(max(NH[idx] - p, H[-1]))
                cur_NH.append(max(H[idx] + p, cur_NH[-1]))
            res = max(res, cur_NH[-1])
            NH = cur_NH
        return res

    def maxProfitIII(self, prices):
        profits = []
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
            profits.append(max_profit)

        # backward traversal, max_profit records the max profit
        # after the ith day, this is the second transaction

        max_profit = 0
        current_max = prices[-1]
        total_max = 0
        for i in range(len(prices)-1, -1,-1):
            current_max = max(current_max, prices[i])
            max_profit = max(current_max-prices[i], max_profit)
            total_max = max(total_max, max_profit + profits[i])
        return total_max

    def maxProfit(self, prices):
        max_profit = 0
        current_min = prices[0]
        for price in prices:
            current_min = min(current_min, price)
            max_profit = max(max_profit, price - current_min)
        return max_profit

    #     profit = 0
    #     i = 0
    #     while i < len(prices)-1:
    #         while i < len(prices) -1 and prices[i] >= prices[i+1]:
    #             i +=1
    #         valley = prices[i]
    #         while i < len(prices) -1 and prices[i] <= prices[i+1]:
    #             i +=1
    #         profit += prices[i] - valley
    #     return profit

prices = [3,3,5,0,0,3,1,4]
solution = Solution()
solution.maxProfitIII(prices)