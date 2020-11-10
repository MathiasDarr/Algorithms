class Solution:
    def rob(self, nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp

nums = [1,2,3,1]
solution = Solution()
solution.rob(nums)