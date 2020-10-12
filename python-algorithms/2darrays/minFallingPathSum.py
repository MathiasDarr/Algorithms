class Solution:
    def minFallingPathSum(self, A):
        nRows = len(A)
        nCols = len(A[0])
        dp = [[float('inf')] * nCols  for _ in range(nRows)]
        for i in range(nCols):
            dp[0][i] = A[0][i]


        for i in range(1,nRows):
            for j in range(nCols):
                for c in range(j-1, j+2):
                    if c < 0 or c == nCols or c == j:
                        continue
                    dp[i][j] = min(dp[i][j], dp[i-1][c] + A[i][j])
        return min(dp[-1])


        # def recursive(row, c, pathSum):
        #     print("row: {} & column: {}".format(row, c))
        #     print(pathSum)
        #     if row == len(A):
        #         self.minPathSum = max(self.minPathSum, pathSum)
        #         return
        #     for column in range(c-1, c+2):
        #         if column <0 or column == len(A[0]):
        #             continue
        #         recursive(row+1, column, pathSum + A[row][column])


        # memo = {}
        #
        # recursive(0, 1, 0 )
        # return self.minFallingPathSum(A)
A= [[1,2,3],[6,5,4],[7,8,9]]
solution = Solution()
solution.minFallingPathSum(A)