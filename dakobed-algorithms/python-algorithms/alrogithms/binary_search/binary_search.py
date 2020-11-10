"""
Implement a binary search,
Things to keep in mind

termination of the while loop:
    left <= right

Updating left and right by incremting & decrementing mid by one.




"""


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return mid


solution = Solution()

nums = [1,3,5,6]
target = 2
solution.search(nums, target)