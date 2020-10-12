class Solution:
    def largestSumOfAverages(self, A, K):
        A.sort()

        singleElements = [A.pop() for _ in range(K-1)]

        remainingAverage = sum(A)/len(A)
        return remainingAverage + sum(singleElements)

solution = Solution()
nums = [9,1,2,3,9]
solution.largestSumOfAverages(nums, 3)