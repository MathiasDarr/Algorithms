class Solution:
    def hasPath(self, maze, start, destination):
        nRows = len(maze)
        nCols = len(maze[0])
        directions = [[0, 1], [-1, 0], [-1, 0], [1, 0]]

        def dfs(i, j, visited):
            if i == destination[0] and j == destination[1]:
                return True
            if 0 <= i < nRows and 0 <= j < nCols and maze[i][j] != 1 and (i, j) not in visited:
                visited.add((i, j))
                for dx, dy in directions:
                    if dfs(i+dx, j+dy, visited):
                        return True
                visited.remove((i, j))

            return False
        # if dfs(start[0], start[1], set())
        return dfs(start[0], start[1], set())


maze = [[0, 1, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
        ]
start = [0,0]
dest = [4, 4]
solution = Solution()
solution.hasPath(maze, start, dest)