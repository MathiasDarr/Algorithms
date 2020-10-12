class Solution:
    def minPathSum(self, grid):
        nRows = len(grid)
        nCols = len(grid[0])
        dp = [[float('inf')] * nCols for _ in range(nRows) ]
        dp[0][0] = grid[0][0]
        # return dp
        for i in range(1,nRows):
            dp[i][0] = grid[i][0] + dp[i-1][0]
        for j in range(1,nCols):
            dp[0][j] = grid[0][j] + dp[0][j-1]
        for i in range(1,nRows):
            for j in range(1, nCols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[-1][-1]

# grid = [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]

grid = [[1,2,5],[3,2,1]]
solution = Solution()
solution.minPathSum(grid)