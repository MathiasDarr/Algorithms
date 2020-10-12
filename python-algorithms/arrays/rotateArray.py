class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1

    def rotate(self, num, k):
        n = len(nums)
        k %= n

        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)

    # def rotate(self, nums, k):
    #     n = len(nums)
    #     newArray = [0] * n
    #     newArray[:k] = nums[n-k:]
    #     newArray[k:] = nums[:n-k]
    #     nums[:] = newArray

solution = Solution()
nums = [1,2,3,4,5,6,7]
k = 3

solution.reverse(nums, 0, 5)
print(nums)
# rotatedArray = solution.rotate(nums, k)
