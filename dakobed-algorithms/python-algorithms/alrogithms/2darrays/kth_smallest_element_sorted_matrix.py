"""
Rows & Columns are sorted in ascending order, find the kth smallest element in the matrix

"""

import heapq

class Solution:
    def kthSmallest(self, matrix, k):

        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])
        while k > 0:
            element = heapq.heappop(heap)
            k -=1
        return element

matrix = [[1,5,9],
          [10,11,13],
          [12,13,15]]

solution = Solution()
solution.kthSmallest(matrix, 1)