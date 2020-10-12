class Solution:
    def removeDuplicates(self, nums):
        index = 1
        currentValue = nums[0]
        currentCount = 1

        for i, num in enumerate(nums[1:]):
            if num == currentValue:
                if currentCount == 2:
                    continue
                else:
                    nums[index] = currentValue
                    currentCount +=1
                    index +=1
            else:
                currentValue = num
                nums[index] = currentValue
                currentCount = 1
                index +=1
        return index

nums = [1,1,1,2,2,3]
# nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
solution.removeDuplicates(nums)