

def minPathSum(grid):
    # dp = [[float('inf') for _ in range(len(grid[0]) + 1) ] for _ in range(len(grid) +1 )]
    dp = [[float('inf') for _ in range(len(grid[0])) ] for _ in range(len(grid))]

    dp[0][0] = grid[0][0]
    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 and j ==0:
                continue
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    return dp[-1][-1]

matrix = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]

result = minPathSum(matrix)