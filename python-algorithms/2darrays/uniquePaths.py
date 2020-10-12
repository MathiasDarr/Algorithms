
class Solution:
    def uniquePaths(self, m, n):
        dp = [[0 if i > 0 and j> 0 else 1 for i in range(n)] for j in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        mRows = len(obstacleGrid)
        nCols = len(obstacleGrid[0])
        if obstacleGrid[0][0] ==1:
            return 0
        obstacleGrid[0][0] =1
        for i in range(1, mRows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] ==0 and obstacleGrid[i-1][0] == 1)
        for i in range(1, nCols):
            obstacleGrid[0][i] = int(obstacleGrid[0][i] ==0 and obstacleGrid[0][i-1] == 1)
        for i in range(1,mRows):
            for j in range(1,nCols):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = 0
        return obstacleGrid[mRows-1][nCols-1]

solution = Solution()
grid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
# dp = solution.uniquePathsWithObstacles(grid)
dp = solution.uniquePathsWithObstacles(grid)