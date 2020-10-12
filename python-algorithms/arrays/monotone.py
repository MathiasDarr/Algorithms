class Solution:
    def isMonotonic(self, A):
        increasing = True
        decreasing = True

        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                decreasing = False
            if A[i] < A[i-1]:
                increasing = False
        return increasing or decreasing

nums = [1,2,2,3]