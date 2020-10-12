class Solution:
    def findUnsortedSubarray(self, nums):
        minValue = float('inf')
        maxValue = float('-inf')

        flag = False
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                flag = True
            if flag:
                minValue = min(minValue, nums[i])

        flag = False
        for i in range(len(nums)-2,-1,-1 ):
            if nums[i] > nums[i+1]:
                flag = True
            if flag:
                maxValue = max(maxValue, nums[i])
        left = 0
        right = 0
        for i,num in enumerate(nums):
            if num > minValue:
                left = i
                break
        for j in range(len(nums)-1, -1, -1):
            if nums[j] < maxValue:
                right = j
                break
        print(left)
        print(right)

        return right - left +1 if right-left > 0 else 0

# nums = [ 6, 8, 11, 10,2, 9, 15]
nums = [1,2,3,4]
solution = Solution()
solution.findUnsortedSubarray(nums)