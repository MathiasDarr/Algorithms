class Solution:

    def subsetsWithDup(self, nums):
        resultsSet = set()
        nums.sort()
        def recursiveSubsets(index, subset):
            if index == len(nums):
                resultsSet.add(subset)
                return
            recursiveSubsets(index+1, (*subset, nums[index]))
            recursiveSubsets(index+1,subset)
        recursiveSubsets(0, ())
        return [result for result in resultsSet]

    def subsets(self, nums):
        results = set()

        def subsetsRecursiveNoDups(nums, index, subset):
            if index == len(nums):
                results.add(subset)
                return
            # subsetsRecursiveNoDups(nums, index+1, (*subset,nums[index])) #   subset + [nums[index]])
            # subsetsRecursiveNoDups(nums, index+1, subset)

        def subsetsRecursive(nums, index, subset):
            if index == len(nums):
                results.add(subset)
                return
            subsetsRecursive(nums, index+1, subset + [nums[index]])
            subsetsRecursive(nums, index+1, subset)

        # subsetsRecursive(nums, 0, [])
        subsetsRecursiveNoDups(nums, 0, [])
        return [list(result) for result in results]





nums = [4,4,4,1,4]
solution = Solution()
results = solution.subsetsWithDup(nums)

