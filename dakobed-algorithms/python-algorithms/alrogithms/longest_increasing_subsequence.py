"""

"""

class Solution:
    def lengthOfLIS(self, nums):
        if len(nums) ==0:
            return 0
        dp = [1] * len(nums)
        lis = 1
        for j in range(len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] +1)
                lis = max(lis, dp[j])
        return lis


solution = Solution()
nums = [-1,3,4,5,2,2,2,2]

solution.lengthOfLIS(nums)