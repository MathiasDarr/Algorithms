class Solution:
    def numbers_less_than_or_equal(self, matrix, m):
        count = 0
        i =0
        j = len(matrix[0]) -1

        while i < len(matrix) and j >= 0:
            print("i: {} j: {} ".format(i, j))
            if matrix[i][j] <= m:
                count += j +1
                i +=1
            else:
                j-=1
        return count
    def kthSmallest(self, matrix, k):
        if len(matrix) ==0 or len(matrix[0]) == 0:
            return -1
        left = matrix[0][0]
        right = matrix[-1][-1]

        while left < right:
            mid = left + (right-left)//2
            if self.numbers_less_than_or_equal(matrix, mid >=k):
                right = mid
            else:
                left = mid+1

        return left

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
solution = Solution()
solution.kthSmallest(matrix, 8)