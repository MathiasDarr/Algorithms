"""
Every unit of time infection spreads to all surrounding oranges

0 empty cell
1 fresh orange
2 rotten orange

At each iteration, perform a BFS.
For every cell in the rotten set:
    - check if it's neighbor are in the fresh set
        - if neighbor is in fresh, remove from fresh and add to temporary infected set
    - rotten is set to the temporary infected.

If at the end of the iteration there are still elements in the fresh set, return -1


"""


class Solution:
    def orangesRotting(self, grid):
        nRows = len(grid)
        nCols = len(grid[0])
        directions = [[0,1],[-1,0],[1,0],[0,-1]]

        rotten = set()
        fresh = set()

        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] ==2:
                    rotten.add((i,j))
                if grid[i][j] == 1:
                    fresh.add((i,j))

        minutes = 0

        while len(rotten) > 0:
            infected = set()
            while len(rotten) > 0:
                x, y = rotten.pop()
                for dx, dy in directions:
                    if (x+dx, y + dy) in fresh:
                        fresh.remove((x+dx, y+dy))
                        infected.add((x+dx, y+dy))
            minutes += 1
            if len(fresh) ==0:
                return minutes
            rotten = infected
        if len(fresh) > 0:
            return -1
        return minutes

solution = Solution()

grid = [[2,1,1],[1,1,0],[0,1,1]]

solution.orangesRotting(grid)
