class Solution:
    def longestIncreasingPath(self, matrix):
        nRows = len(matrix)
        nCols = len(matrix[0])

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        self.longest = 0
        def dfs(i, j, length, memo):
            if (i,j) in memo:
                return memo[(i,j)]
            if i < 0 or i >= nRows or j < 0 or j >= nCols:
                return 0
            longestAdjacentPath = 0
            for dx, dy in directions:
                newX = dx + i
                newY = dy + j
                if newX >= 0 and newX < nRows and newY >= 0 and newY < nCols and matrix[newX][newY] < matrix[i][j]:
                    longestAdjacentPath = max(longestAdjacentPath, dfs(newX, newY, length+1, memo) )

            memo[(i,j)] = 1 + longestAdjacentPath
            self.longest = max(self.longest, memo[(i,j)])
            return memo[(i,j)]
        memo = {}
        for i in range(nRows):
            for j in range(nCols):
                dfs(i, j, 0, memo )
        return self.longest

nums = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
]


solution = Solution()
solution.longestIncreasingPath(nums)