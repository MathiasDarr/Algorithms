"""
LeetCode 986 Interval List Intersections

Return the intersection of these two interval lists

We will use two pointes i & j
i: iteration index over array A
j: iteration index over array B

Search for areas of intersecion,

if the current end of interval element in A is less than interval B
    - increment i
Likewise increment j if B[j][1] < A

When we have found an intersecion, append the result, and increment the index of the lesser interval


"""


class Solution:
    def intervalIntersections(self, A,B):

        i = 0
        j = 0
        result = []
        while i < len(A) and j < len(B):
            if A[i][1] < B[j][0]:
                i +=1
            elif B[j][1] < A[i][0]:
                j +=1
            else:
                result.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
                if A[i][1] > B[j][1]:
                    j +=1
                else:
                    i +=1

        return result

A = [[0,2],[5,10],[13,23],[24,25]]
B = [[1,5],[8,12],[15,24],[25,26]]

solution = Solution()
solution.intervalIntersections(A,B)