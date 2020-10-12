class Solution:
    def maximalRectangle(self, matrix):
        dp = [[0 for _ in range(len(matrix[0]) +1) ] for _ in range(len(matrix) +1)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "1":
                    dp[i][j] = (1, (i,j))
        return dp



    def maximalSquare(self, matrix):
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        maxLength = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] =="1":
                    dp[i][j] = min([dp[i][j-1], dp[i-1][j], dp[i-1][j-1]]) + 1
                    maxLength = dp[i][j] if dp[i][j] > maxLength else maxLength
        return maxLength **2

solution = Solution()
matrix = [["1","0","1","0","0"],
          ["1","0","1","1","1"],
          ["1","1","1","1","1"],
          ["1","0","0","1","0"]]
dp = solution.maximalRectangle(matrix)