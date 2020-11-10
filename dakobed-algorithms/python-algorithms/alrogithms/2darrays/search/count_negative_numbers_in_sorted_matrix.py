"""

sorted in non increasing order both row and column wise

We can perform binary search on each row, searching for the first occurence of a negative number
the loop terminates when left is the index of the first negative number, meaning that nCols - left =


"""

class Solution:
    def countNegatives(self, grid):
        nCols = len(grid[0])
        nnegatives = 0
        for row in grid:
            left = 0
            right = nCols - 1

            while left <= right:
                mid = left + (right-left)//2
                if row[mid] > -1:
                    left = mid +1
                else:
                    right = mid - 1
            nnegatives += nCols-left
        return nnegatives

grid = [[4,3,2,-1],
        [3,2,1,-1],
        [1,1,-1,-2],
        [-1,-1,-2,-3]]

solution = Solution()
solution.countNegatives(grid)