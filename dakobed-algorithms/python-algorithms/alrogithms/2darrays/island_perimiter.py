class Solution:
    def islandPerimeter(self, grid):
        nRows = len(grid)
        nCols = len(grid[0])
        perim = 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    localPerim = 0
                    localPerim +=1 if j ==0 or grid[i][j-1] == 0 else 0
                    localPerim +=1 if i == 0 or grid[i-1][j] == 0 else 0
                    localPerim +=1 if i == nRows -1 or grid[i+1][j] ==0 else 0
                    localPerim +=1 if j == nCols -1 or grid[i][j+1] ==0 else 0
                    perim += localPerim
        return perim

grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
solution = Solution()
solution.islandPerimeter(grid)