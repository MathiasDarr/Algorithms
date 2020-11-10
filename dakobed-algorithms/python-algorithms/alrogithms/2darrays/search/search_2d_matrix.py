"""
Elements in each row are sorted from left to right
the first integer of ech row is greater than the last integer of the previous row

Different binary search termination conditions in this





"""


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]: return False
        nRows = len(matrix)
        nCols = len(matrix[0])

        # Find the row in which the target may be fond w/ binary search w/ an additional termination condition that
        # takes into account the properties of the matrix (last element in a row is smaller than first element in next
        # row)
        row_left = 0
        row_right = nRows
        while row_left != row_right - 1:
            row_mid = (row_left + row_right) // 2
            if matrix[row_mid][0] <= target:
                row_left = row_mid
            else:
                row_right = row_mid

        # Perform a second binary search, this time narrowing down the range of the row found in the previous search.
        col_left = 0
        col_right =  nCols
        while col_left != col_right:
            col_mid = (col_left + col_right) // 2
            if matrix[row_left][col_mid] == target:
                return True
            elif matrix[row_left][col_mid] < target:
                col_left = col_mid + 1
            else:
                col_right = col_mid

        return False

        # nRows = len(matrix)
        # nCols = len(matrix[0])
        #
        # """
        # Find the row in which the target may be fond w/ binary search w/ an additional termination condition that
        # takes into account the properties of the matrix (last element in a row is smaller than first element in next
        # row)
        # """
        # left = 0
        # right = nRows - 1
        #
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     print(matrix[mid][0])
        #     if matrix[mid][0] <= target < matrix[mid][-1]:
        #         break
        #     elif matrix[mid][0] > target:
        #         right = mid - 1
        #     else:
        #         left = mid + 1
        #
        # column = mid
        # left = 0
        # right = nCols - 1
        # print("left: ".format(left))
        # """
        # Perform a second binary search, this time narrowing down the range of the row found in the previous search.
        # """
        #
        # while left <= right:
        #     mid = left + (right - left) // 2
        #     if matrix[column][mid] == target:
        #         return True
        #     elif matrix[column][mid] > target:
        #         right = mid-1
        #     else:
        #         left = mid+1
        # return False


solution = Solution()
# board = [[1, 3, 5, 7],
#          [10, 11, 16, 20],
#          [23, 30, 34, 60]
#         ]
board =  [[1], [3]]
# solution = Solution()

solution.searchMatrix(board, 1)

