"""
Given an array of distinct integers candidates, and a target,
return a list of all unique combinations of candidates

Combintations
    Given two integers n and k, return all possible combinations of k numbers out of 1....n

    Backtrack, adding an integer element at each backtracking step

    add element
    recurse
    pop element



Combination Sum:
    distinct integers, each element can be used any number of times

    Perform backtracking,
        add to combination list
        recurse w/ same index
        remove from combination list

Combination Sum II

    All unique combinations
    each number may be used only once

    How to deal with dupliates?


    Similar to above backtrack by

    ### Make the backtracking step explicit by adding to the combination array, recursing, removing from combination array


Combination Sum III
Fin


Combination Sum IV
Given integer array w/ no duplicates
find all possible combinations that sum to a target

"""


class Solution:
    def combine(self, n, k):
        def backtrack(number, combination):
            if len(combination) == k:
                combinations.append([*combination])
                return
            for i in range(number, n):
                combination.append(i+1)
                backtrack(i+1, combination)
                combination.pop()
        combinations = []
        backtrack(0, [])
        return combinations



    def combinationSum(self, candidates, target):
        def backtracking(index, combination,  current_sum):
            if current_sum == target:
                combinations.append([*combination])
                return
            if index >= len(candidates) or current_sum > target:
                return
            for i in range(index, len(candidates)):
                combination.append(candidates[i])
                backtracking(i,combination, current_sum + candidates[i])
                combination.pop()

        combinations = []
        backtracking(0, [], 0)
        return combinations

    def combinationSum2(self, candidates, target):
        if not candidates:
            return []

        def backtracking(index, combination, current_sum):
            if index >= len(candidates):
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] == target:
                    combinations.append(combination + [candidates[i]])
                    return
                elif current_sum + candidates[i] > target:
                    return
                else:
                    combination.append(candidates[i])
                    current_sum = current_sum + candidates[i]
                    backtracking(i + 1, combination, current_sum)
                    current_sum = current_sum - candidates[i]
                    combination.pop()
        candidates.sort()
        combinations = []

        backtracking(0, [], 0)
        return combinations


    def combinationSum4(self, nums, target):
        if not nums:
            return 0
        def backtrack(index, combination, current_sum):

            if index >= len(nums):
                return
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue
                if current_sum + nums[i] == target:
                    combinations.append(combination + [nums[i]])
                    return
                elif current_sum + nums[i] > target:
                    return
                else:
                    combination.append(nums[i])
                    current_sum = current_sum + nums[i]
                    backtrack(i, combination, current_sum)
                    current_sum = current_sum - nums[i]
                    combination.pop()

        nums.sort()
        combinations = []
        backtrack(0, [], 0)
        return combinations



solution = Solution()
nums = [1,2,3]
target = 4
solution.combinationSum4(nums, target)
# candidates = [10,1,2,7,6,1,5]
# target = 8
#
# combinations = solution.combinationSum2(candidates, target)

