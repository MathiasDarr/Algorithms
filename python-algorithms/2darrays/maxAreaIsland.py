class Solution:
    def maxAreaOfIsland(self, grid):
        mRows = len(grid)
        nCols = len(grid[0])

        directions = [[0,1], [0, -1], [-1, 0], [1, 0]]

        def dfs(x, y):
            if x >= 0 and x < mRows and y >= 0 and y < nCols and (x,y) and grid[x][y] ==1:
                grid[x][y] = 0
                count = 0
                for dx, dy in directions:
                    count += dfs(x + dx, y + dy)
                return count +1
            else:
                return 0
        maxIsland = 0
        for i in range(mRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    area = dfs(i,j)
                    maxIsland = max(maxIsland, area)
        return maxIsland


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

solution = Solution()
solution.maxAreaOfIsland(grid)