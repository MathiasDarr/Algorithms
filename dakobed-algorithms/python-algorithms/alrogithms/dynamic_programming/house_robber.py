class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        previous = 0
        current = 0
        for i in range(len(nums)):
            previous, current = current, max(previous + nums[i], current )
        return current

nums = [2,3,2]

solution = Solution()
solution.rob(nums)