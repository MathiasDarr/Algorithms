class Solution:
    # def removeDuplicates(self, nums):
    #     index = 0
    #     for i in range(1,len(nums)):
    #         if nums[i] != nums[index]:
    #             index += 1
    #             nums[index],nums[i] = nums[i],nums[index]
    #     return index + 1

    def removeDuplicates(self,nums):
        if len(nums) == 0:
            return 0
        currentValue = nums[0]
        index = 0
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == currentValue:
                if count == 2:
                    continue
                else:
                    index += 1
                    nums[index] = currentValue
                    count +=1
            else:
                index +=1
                currentValue = nums[i]
                count = 1
                nums[index] = currentValue
        return index + 1



nums = [1,1,1,2,2,3]
solution = Solution()
solution.removeDuplicates(nums)