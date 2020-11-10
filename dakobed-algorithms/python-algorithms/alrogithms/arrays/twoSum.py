class Solution:
    def twoSum(self, nums, target):
        complements = dict()
        for index, num in enumerate(nums):
            if num in complements:
                return [index, complements[num]]
            complements[target-num] = index

nums = [2,7,11,15]
target = 9

solution = Solution()
solution.twoSum(nums, target)