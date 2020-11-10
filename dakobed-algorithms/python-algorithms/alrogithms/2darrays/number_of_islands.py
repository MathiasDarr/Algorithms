class Solution:
    def numIslands(self, grid):
        nRows = len(grid)
        nCols = len(grid[0])

        directions = [[0,1], [0,-1], [-1, 0], [1,0]]

        def dfs(i, j):
            if i >=0 and i < nRows and j >= 0 and j < nCols and grid[i][j] == "1":
                grid[i][j] = "0"
                for dx, dy in directions:
                    dfs(i+dx, j + dy)


        count = 0

        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)
        return count

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]


solution = Solution()
solution.numIslands(grid)