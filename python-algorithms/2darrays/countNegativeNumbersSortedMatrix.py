class Solution:
    # def countNegatives(self, grid):
    #     count = 0
    #     for row in grid:
    #         left = 0
    #         right = len(row)
    #         while left < right:
    #             mid = left + (right-left)//2
    #             if row[mid] <0:
    #                 right = mid
    #             elif row[mid] >=0:
    #                 left = mid+1
    #         count += len(row) - right
    #     return count
    def countNegatives(self, grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])-1, -1,-1):
                print(grid[i][j])
                if grid[i][j] >=0:
                    break
                count +=1
        return count

# grid = [[4, 3, 2, -1],
#         [3, 2, 1, -1],
#         [1, 1, -1, -2],
#         [-1, -1, -2, -3]]

grid = [[5,1,0],[-5,-5,-5]]
solution = Solution()
solution.countNegatives(grid)