class Solution:
    def sortColors(self, nums):
        if not nums:
            return nums
        leftIndex = 0
        rightIndex = len(nums) -1
        i = 0
        while i <= rightIndex:
            if nums[i] == 0 and i > leftIndex:
                nums[leftIndex], nums[i] = nums[i], nums[leftIndex]
                leftIndex +=1
            elif nums[i] ==2:
                nums[rightIndex], nums[i] = nums[i], nums[rightIndex]
                rightIndex -=1
            else:
                i +=1

nums = [2,0,2,1,1,0]
solution = Solution()
solution.sortColors(nums)
print(nums)