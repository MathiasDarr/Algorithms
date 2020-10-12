class Solution:
    def updateMatrix(self, matrix):
        nRows = len(matrix)
        nCols = len(matrix[0])
        dp = [[float('inf') for _ in range(nCols)] for _ in range(nRows)]

        for i in range(nRows):
            for j in range(nCols):
                if matrix[i][j] ==0:
                    dp[i][j] =0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i-1][j] +1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j-1] + 1)

        for i in range(nRows-1, -1, -1):
            for j in range(nCols-1, -1, -1):
                if i < nRows -1:
                    dp[i][j] = min(dp[i][j], dp[i+1][j] +1)
                if j < nCols -1:
                    dp[i][j] = min(dp[i][j], dp[i][j+1] + 1)
        return dp

    # def updateMatrix(self, matrix):
    #     nRows = len(matrix)
    #     nCols = len(matrix[0])
    #     output = [[float('inf') for _ in range(nCols)] for _ in range(nRows)]
    #     queue = []
    #
    #     for i in range(0, nRows):
    #         for j in range(0, nCols):
    #             if matrix[i][j] ==0:
    #                 queue.append((i, j))
    #                 output[i][j] = 0
    #     directions = [[0,1], [-1,0], [0,-1], [1,0]]
    #     while len(queue) > 0:
    #         currentI, currentJ = queue.pop(0)
    #         for dx, dy in directions:
    #             newX = dx + currentI
    #             newY = dy + currentJ
    #             if newX >= 0 and newX < nRows and newY >= 0 and newY < nCols:
    #                 if output[newX][newY] > output[currentI][currentJ] + 1:
    #                     output[newX][newY] = output[currentI][currentJ] + 1
    #                     queue.append((newX, newY))
    #     return output

    def updateMatrixBruteForce(self, matrix):
        nRows = len(matrix)
        nCols = len(matrix[0])
        output = [[float('inf') for _ in range(nCols)] for _ in range(nRows)]
        for i in range(nRows):
            for j in range(nCols):
                if matrix[i][j] == 0:
                    output[i][j] =0
                else:
                    for k in range(0, nRows ):
                        for l in range(0, nCols):
                            if matrix[k][l] == 0:
                                dist_01 = abs(k-i) + abs(l-j)
                                output[i][j] = min(output[i][j], dist_01)
        return output


matrix = [[0,0,0],
    [0,1,0],
    [1,1,1]]

solution = Solution()
solution.updateMatrix(matrix)