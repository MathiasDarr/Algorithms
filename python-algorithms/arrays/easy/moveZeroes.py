class Solution:
    def moveZeroes(self, nums):
        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[lastNonZero] = nums[lastNonZero], nums[i]
                lastNonZero += 1
            # if nums[i] ==0:
            #     l = i
            #     while l < len(nums) and nums[l] ==0:
            #         l +=1
            #         if l == len(nums):
            #             return
            #     nums[l], nums[i] = nums[i], nums[l]

nums = [0,1,0,3,12]
solution = Solution()
solution.moveZeroes(nums)