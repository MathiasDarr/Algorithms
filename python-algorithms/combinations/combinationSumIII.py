class Solution:
    def combine(self, n, k):
        # nums = list(range(1,n+1))
        results = []
        def backtrack(comb, index):
            if len(comb) ==k:
                print(comb)
                results.append(list(comb))
                return
            for i in range(index, n):
                comb.append(i+1)
                backtrack(comb, i+1)
                comb.pop()
        backtrack([], 0)
        return results

    def combinationSum4(self, nums, target):
        dp = [0 for _ in range(0, target + 1)]
        for sub_target in range(1, target + 1):
            for num in nums:
                if sub_target - num > 0: # then look for the num ways to make sum of (sub_target - num)
                    dp[sub_target] += dp[sub_target - num]
                elif sub_target - num == 0:
                    dp[sub_target] += 1
        return dp


    def combinationSum3(self, k, n):
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                return
            for i in range(next_start, 9):
                backtrack(remain-i, comb + [i], i+1)

        backtrack(n, [], 1)

        return results

solution = Solution()
solution.combine(4,2)
# nums = [1,2,3]
# target = 4
# solution.combinationSum4(nums, target)
