class NumArray:
    def __init__(self, nums):
        self.cumSum = [0]
        for i in range(len(nums)):
            self.cumSum.append(self.cumSum[i] + nums[i])
        print(self.cumSum)
    def sumRange(self, i: int, j: int) -> int:
        return self.cumSum[j + 1] - self.cumSum[i]


class NumMatrix:
    def __init__(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) ==0: return
        nRows = len(matrix)
        nCols = len(matrix[0])
        dp= [[0 for _ in range(nCols +1)] for _ in range(nRows+1)]
        for row in  range(nRows):
            for col in range(nCols):
                dp[row+1][col+1] = dp[row+1][col] + dp[row][col+1] + matrix[row][col] - dp[row][col]
        self.dp = dp

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]

    # def __init__(self, matrix):
    #     if matrix:
    #         m, n = len(matrix), len(matrix[0])
    #         for j in range(1, n): matrix[0][j] += matrix[0][j - 1]
    #         for i in range(1, m): matrix[i][0] += matrix[i - 1][0]
    #         for i in range(1, m):
    #             for j in range(1, n):
    #                 matrix[i][j] += matrix[i - 1][j] + matrix[i][j - 1] - matrix[i - 1][j - 1]
    #     self.prefix = matrix
    #
    # def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
    #     ans = self.prefix[row2][col2]
    #     if row1: ans -= self.prefix[row1 - 1][col2]
    #     if col1: ans -= self.prefix[row2][col1 - 1]
    #     if row1 and col1: ans += self.prefix[row1 - 1][col1 - 1]
    #     return ans

    #     if len(matrix) == 0 or len(matrix[0]) ==0:
    #         return
    #     nRows = len(matrix)
    #     nCols = len(matrix[0])
    #     dp= [[0 for _ in range(nCols +1)] for _ in range(nRows)]
    #     for row in range(nRows):
    #         for col in range(nCols):
    #             dp[row][col+1] = dp[row][col] + matrix[row][col]
    #     self.dp = dp
    #
    # def getDP(self):
    #     return self.dp
    # def sumRegion(self, row1, col, row2, col2):
    #     csum = 0
    #     for row in range(row1, row2):
    #         csum += self.dp[row][col2+2] - self.dp[row][col]
    #     return csum
# nums = [-2, 0, 3, -5, 2, -1]
# numArray = NumArray(nums)
# numArray.sumRange(0,1)

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
numMatrix = NumMatrix(matrix)
csum = numMatrix.sumRegion(2,1,4,3)