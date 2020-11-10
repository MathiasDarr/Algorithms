"""
LeetCode 162: Find Peak Element


### Searching for a peak w/ binary search

numsm[mid] > nums[mid+1] , search to the left of mid for the peak element


Binary search,

right = mid
left = mid + 1



"""



class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right-left)//2

            ### Searching for a
            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1
        return left

solution = Solution()
solution.findPeakElement([1,2,3,1])