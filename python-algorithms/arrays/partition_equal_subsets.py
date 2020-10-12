# class Solution:
#     def canPartition(self, nums):
#         sumNums = sum(nums)
#         def dfs(nums, target, index, total, hashmap):
#             if (index,total) in hashmap:
#                 return hashmap[(index,total)]
#             if index >= len(nums) or target//2 < total:
#                 return False
#             if target == total:
#                 hashmap[(index, total)] = True
#                 return True
#             foundPartition = dfs(nums, target, index + 1, total + nums[index], hashmap) or \
#             dfs(nums, target, index + 1, total, hashmap)
#             hashmap[(index, target)] = foundPartition
#             return foundPartition
#         hashmap = {}
#         return dfs(nums, sumNums, 0, 0, hashmap )


class Solution:
    def canPartition(self, nums):
        numsum = sum(nums)
        if numsum % 2 == 1:
            return False
        nums.sort()
        memo = dict = {}
        # check if nums[i:] can have sum rem_sum
        def dfs(index, rem_sum, memo):
            if rem_sum == 0:
                return True
            if index >= len(nums):
                return False
            if rem_sum < nums[index]:
                return False
            if rem_sum in memo:
                return memo[rem_sum]
            memo[rem_sum] = dfs(index + 1, rem_sum - nums[index], memo) or dfs(index + 1, rem_sum, memo)
            return memo[rem_sum]
        return dfs(0, numsum // 2, memo)

nums = [21,5,10,5]
solution = Solution()
solution.canPartition(nums)