class Solution:
    def removeElement(self, nums, val):
        left =0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[left] = nums[j]
                left +=1
        return left

nums = [3,2,2,3]
val = 3
solution = Solution()
length = solution.removeElement(nums, val)