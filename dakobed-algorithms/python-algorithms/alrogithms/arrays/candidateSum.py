class Solution:
    def combintationSum(self, candidates, target):
        candidates.sort()
        output = []
        def dfs(index, combintation, current_sum):
            if current_sum == target:
                output.append(combintation)
                return
            if current_sum > target:
                return
            for i in range(index, len(candidates)):
                dfs(i, combintation + [candidates[index]], current_sum + candidates[i])
        dfs(0, [], 0)
        return output

solution = Solution()
solution.combintationSum([2,3,6,7], 7)