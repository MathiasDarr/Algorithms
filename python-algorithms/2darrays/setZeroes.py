class Solution:
    def setZeroes(self, matrix):
        nRows = len(matrix)
        nCols = len(matrix[0])

        rows = set()
        cols = set()
        for i in range(nRows):
            for j in range(nCols):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        for i in range(nRows):
            for j in range(nCols):
                if i in rows or j in cols:
                    matrix[i][j] = 0

matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]]
solution = Solution()
solution.setZeroes(matrix)