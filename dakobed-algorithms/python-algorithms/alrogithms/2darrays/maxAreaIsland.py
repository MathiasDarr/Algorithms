"""
The key to the recursive DFS solution is that each cell contributes 1 + neighbors area.  Return this from the DFS call.
"""



class Solution:
    def maxAreaOfIsland(self, grid):
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        nRows = len(grid)
        nCols = len(grid[0])
        maxArea = 0

        def dfs(i, j):
            if i >= 0 and i < nRows and j >= 0 and j < nCols and grid[i][j] == 1:
                grid[i][j] = 0
                neighbors_area = 0
                for dx, dy in directions:
                    neighbors_area += dfs(i + dx, j + dy)
                return 1 + neighbors_area
            else:
                return 0
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1:
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea


grid = [[0, 1, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
        ]

solution = Solution()



grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

solution.maxAreaOfIsland(grid)