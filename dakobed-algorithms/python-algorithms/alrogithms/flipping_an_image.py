"""
LeetCode 832 Flipping an Image

Flip the matrix horizonally & then invert it.


"""


class Solution:
    def flipAnInvertImage(self, A):
        result = []
        for row in A:
            result.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return result


        # nRows = len(A)
        # nCols = len(A[0])
        # def flip(A):
        #     for i in range(nRows):
        #         for j in range(nCols//2):
        #             A[i][j], A[i][nCols-j-1] = A[i][nCols-j-1], A[i][j]
        # def invert(A):
        #     for i in range(nRows):
        #         for j in range(nCols):
        #             A[i][j] = 1 - A[i][j]
        #
        # flip(A)
        # invert(A)
A = [[1,1,0],[1,0,1],[0,0,0]]
print(A)
result = []
for row in A:
    result.append(list(map(lambda x: 1-x, row[::-1])))
print(result)

solution = Solution()
print(A)
solution.flipAnInvertImage(A)
print(A)