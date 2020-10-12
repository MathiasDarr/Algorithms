class Solution:
    def findLengthOfShortestSubarray(self, arr):
        n = len(arr)
        left = 0

        while left < len(arr) and arr[left+1] >= arr[left]:
            left +=1
        if left == n -1: ## Strictly Increasing..
            return 0

        right = len(arr) -1
        while right >= left and arr[right-1] < arr[right]:
            right -=1

        result = min(n-1-left, right)

        i = 0
        j = right

        while i <= left and j < n:
            if arr[j] >= arr[i]:
                result = min(result, j -i-1)
                i +=1
            else:
                j +=1
        return result

solution = Solution()
arr = [1,2,3,10,4,2,3,5]

solution.findLengthOfShortestSubarray(arr)