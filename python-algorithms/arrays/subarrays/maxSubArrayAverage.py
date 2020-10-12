class Solution:
    def findMaxAverage(self, nums, k):
        if k > len(nums):
            return 0
        first_sum = sum(nums[0:k])
        maxAvg = first_sum
        removeIndex = 0
        for i in range(k, len(nums)):
            maxAvg = max(maxAvg, maxAvg + nums[i] - nums[removeIndex])
            removeIndex +=1
        return maxAvg/k

nums = [1,12,-5,-6,50,3]
k = 4
solution = Solution()
solution.findMaxAverage(nums, k)
