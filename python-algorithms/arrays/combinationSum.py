
class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        def subSum(index, target, combination):
            for j in range(index, len(candidates)):
                if target > candidates[j]:
                    subSum(j, target - candidates[j],  combination + [candidates[j]])
                elif target == candidates[j]:
                    res.append(combination + [candidates[j]])
                else:
                    break
        subSum(0, target, [])
        return res

    def combinationSumII(self, candidates, target):
        result = []
        def findCombinations(candidates, index, target, current):
            if target == 0:
                result.append(current)
                return
            if target < 0:
                return
            for i in range(index, len(candidates), 1):
                if i == index or candidates[i] != candidates[i - 1]:
                    current.append(candidates[i])
                    findCombinations(candidates, i + 1, target - candidates[i], current)
                    current.pop()

        candidates.sort()
        findCombinations(candidates, 0, target, [])
        return result
    # def combinationSum(self, candidates, target):
    #     candidates.sort()
    #     resultSet =set()
    #     def dfs(target, index, combinationSum, combination):
    #         if index >= len(candidates) or combinationSum + candidates[index]> target:
    #             return
    #         if combinationSum + candidates[index] == target:
    #             resultSet.add((*combination, candidates[index]))
    #         dfs(target, index, combinationSum + candidates[index], (*combination, candidates[index]))
    #         dfs(target, index+1, combinationSum + candidates[index], (*combination, candidates[index]))
    #         dfs(target, index+1, combinationSum, combination)
    #     dfs(target, 0, 0, ())
    #     return [result for result in resultSet]


nums = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
results = solution.combinationSumII(nums, target)