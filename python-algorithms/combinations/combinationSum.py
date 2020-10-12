
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
        candidates.sort()
        results = []
        def dfs(candidates, target, combination):
            if target == 0:
                results.append(combination)
                return
            if target < 0:
                return
            for idx, i in enumerate(candidates):
                dfs(candidates[idx+1:], target -candidates[i], combination + [candidates[idx]])
                dfs(candidates[idx+1:],target,  combination )

        dfs(candidates, target, [])





    # def combinationSumII(self, candidates, target):
    #     candidates.sort()
    #     results = set()
    #     def dfs(index, target, combination):
    #         if target< 0 or index >= len(candidates):
    #             return
    #         if target == candidates[index]:
    #             results.add((*combination, candidates[index]))
    #             print(results)
    #             return
    #
    #         dfs(index+1, target-candidates[index],  combination + [candidates[index]])
    #         dfs(index+1, target, combination)
    #     dfs(0, target, [])
    #     return [list(result) for result in results]


nums = [10,1,2,7,6,1,5]
target = 8
solution = Solution()
results = solution.combinationSumII(nums, target)
