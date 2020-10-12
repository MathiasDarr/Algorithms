

class Solution:
    def searchMatrix(self, matrix, target):
        nrows = len(matrix)
        targetRow = -1
        for i in range(nrows):
            if target >= matrix[i][0] and target <= matrix[i][-1]:
                targetRow = i
        print("The target row is {}".format(targetRow))

        if targetRow == -1:
            return False
        row = matrix[targetRow]
        left  = 0
        right = len(row) -1
        while left <= right:
            mid = left + (right-left)//2
            if row[mid] == target:
                return True
            elif row[mid] > target:
                right = mid - 1
            else:
                left = mid +1
        return False


target = 50
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

solution = Solution()
solution.searchMatrix(matrix, target)
