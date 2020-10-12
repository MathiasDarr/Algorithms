class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        maxCount = 0
        for num in nums:
            count = 0 if num ==0 else count +1
            maxCount = max(maxCount, count)
        return maxCount




nums = [1,1,0,1,1,1]
solution = Solution()
solution.findMaxConsecutiveOnes(nums)

