class Solution:
    def permute(self, nums):
        n=len(nums)
        result = set()
        def backtrack(left,right,nums) :
            if left==right :
                return result.add(tuple(list(nums))) #We reached the end of the recursion
                                                 #tree
            else :
                for i in range(left,right+1) :
                    nums[left], nums[i] = nums[i], nums[left]
                    backtrack(left+1,right,nums)
                    nums[i],nums[left] = nums[left], nums[i]
        backtrack(0,n-1,nums)
        return [list(r) for r in result]
nums = [1,1,2]
solution = Solution()
solution.permute(nums)