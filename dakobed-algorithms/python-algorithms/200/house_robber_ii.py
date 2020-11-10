"""
LeetCode 213 House Robber II

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money
stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last
one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount
of money you can rob tonight without alerting the police.

Solution:


LeetCode 337 House Robber III




"""


class Solution:
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev_max = 0
        current_max = 0

        for i in range(len(nums) -1):
            tmp = current_max
            current_max = max(current_max, prev_max+nums[i])
            prev_max = tmp

        first_pass = current_max

        prev_max = 0
        current_max = 0

        for i in range(len(nums)-1, 0, -1):
            tmp = current_max
            current_max = max(current_max, prev_max + nums[i])
            prev_max = tmp

        return max(first_pass, current_max)

solution = Solution()
nums = [1,2,3,1]
solution.rob(nums)