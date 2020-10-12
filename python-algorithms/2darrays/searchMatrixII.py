class Solution:
    def searchMatrix(self, matrix, target):
        mRows = len(matrix)
        if mRows == 0:
            return False
        nCols = len(matrix[0])
        if nCols == 0:
            return False

        if nCols == 0:
            return False
        y = mRows-1
        x = 0

        while x < nCols and y >=0:
            if matrix[y][x] == target:
                return True
            elif matrix[y][x] > target :
                y -=1
            else:
                x+=1
        return False

    # def searchMatrix(self, matrix, target):
    #     if len(matrix) == 0 or len(matrix[0]) ==0:
    #         return False
    #     left = 0
    #     right = len(matrix[0]) -1
    #     up = 0
    #     down = len(matrix) -1
    #
    #     while left < right or up < down:
    #         print("left: {} right: {} up: {} down: {}".format(left, right, up, down))
    #         # Find the first element in down row that is >= target
    #         l = left
    #         r = right
    #         while l < r:
    #             m = l + (r-l)//2
    #             if matrix[down][m] == target:
    #                 return True
    #             if matrix[down][m] > target:
    #                 r = m
    #             else:
    #                 l = m +1
    #         new_left = l
    #
    #         l = left
    #         r = right
    #
    #         ## Find last element in up row <= target
    #
    #         while l < r:
    #             print("l: {} r: {}".format(l, r))
    #             m = l + (r-l)//2
    #             if matrix[up][m] == target:
    #                 return True
    #             if matrix[up][m] < target:
    #                 l = m
    #             else:
    #                 r = m-1
    #         new_right = l
    #
    #         ## Find the first element in new right column that is >= target
    #         l = up
    #         r = down
    #
    #         while l < r:
    #             m = l + (r-l)//2
    #             if matrix[m][new_right] == target:
    #                 return True
    #             if matrix[m][new_right] > target:
    #                 r = m
    #             else:
    #                 l = m +1
    #
    #         new_up = l
    #
    #         ## Find last element in new left column that is <= target
    #         l = up
    #         r = down
    #         while l < r:
    #             m = l + (r-l)//2
    #             if matrix[m][new_left] == target:
    #                 return True
    #             if matrix[m][new_left] < target:
    #                 l = m
    #             else:
    #                 r = m -1
    #
    #         new_down = l
    #         ## Stopped updating
    #         if left == new_left and right == new_right and up == new_up and down ==new_down:
    #             return True
    #         up = new_up
    #         down = new_down
    #         left = new_left
    #         right = new_right
    #     return matrix[up][left] == target

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
solution = Solution()
solution.searchMatrix(matrix, 26)