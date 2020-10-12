class Solution:

    def binarySearch(self, nums, target, left):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] > target or (left and target == nums[mid]):
                hi = mid
            else:
                lo = mid+1

        return lo

    def searchRange(self, nums, target):
        leftIndex = self.binarySearch(nums, target, True)
        if leftIndex == len(nums) or nums[leftIndex] != target:
            return [-1, -1]
        return [leftIndex, self.binarySearch(nums, target, False)-1]


nums = [5,7,7,8,8,10]
target = 5
solution = Solution()
solution.searchRange(nums, target)