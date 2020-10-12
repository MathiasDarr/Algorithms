class Solution:
    def findNumberOfLIS(self, nums):
        N = len(nums)
        if N <= 1: return N
        dp = [1] * N #lengths[i] = longest ending in nums[i]
        counts = [1] * N #count[i] = number of longest ending in nums[i]

        for j in range(len(nums) -1):
            for i in range(j):
                if nums[i] < nums[j]:
                    if dp[i] >= dp[j]:
                        dp[j] = 1 + dp[i]
                        counts[j] = counts[i]
                    elif dp[i] + 1 == dp[j]:
                        counts[j] += counts[i]
        longest = max(dp)
        return sum(c for i, c in enumerate(counts) if dp[i] == longest)

        # for j in range(len(nums)):
        #     for i in range(j):
        #         if nums[j] > nums[i]:
        #             # if dp[j] < dp[i]:
        #             #     dp[j] = max(dp[j], dp[i]+1)
        #             # elif dp[i] +1 == dp[j]:
        #             #     counts[]
        #             if dp[i] >= dp[j]:
        #                 dp[j] = 1 + dp[i]
        #                 counts[j] = counts[i]
        #             elif dp[i] + 1 == dp[j]:
        #                 counts[j] += counts[i]
        # longest = max(dp)
        # return sum(c for i, c in enumerate(counts) if lengths[i] == longest)
    def LIS(self, nums):
        dp = [1] * len(nums)
        lis = 1
        for j in range(len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] +1)
                lis = max(lis, dp[j])
        return dp

solution = Solution()
nums = [1,3,5,4,7] #,-8,-4,-3,-1,100]

#nums = [-1,3,4,5,2,2,2,2,-5,-4,-3,-2]
nLIS = solution.findNumberOfLIS(nums)
# longest = max(lengths)
# print(sum(c for i, c in enumerate(counts) if lengths[i] == longest))
# dp = solution.LIS(nums)