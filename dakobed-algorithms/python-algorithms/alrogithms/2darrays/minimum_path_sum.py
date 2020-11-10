class Solution:
    def minPathSum(self, grid):
        nRows = len(grid)
        nCols = len(grid[0])
        dp = [[0 for _ in range(nCols)] for _ in range(nRows)]
        dp[0][0] = grid[0][0]
        for i in range(1, nRows):
            dp[i][0] =  dp[i-1][0] + grid[i][0]
        for j in range(1, nCols):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        for i in range(1,nRows):
            for j in range(1, nCols):
                print("i: {} j: {}".format(i,j))

                dp[i][j] = grid[i][j] +min(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

grid = [[1,2,5],[3,2,1]]

solution = Solution()
solution.minPathSum(grid)
