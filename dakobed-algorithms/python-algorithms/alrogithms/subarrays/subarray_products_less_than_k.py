"""
LeetCode 713. Subarray Product Less Than K

Find the number of subarrays whose product is less than k

Traverse the array maintaining a cumulative product variable and a left variable which will be the left index of the
sliding window





"""




class Solution:
    def numSubarrayProductLessThanK(self, nums, k):

        narrays = 0
        left = 0
        cproduct = 1
        for right, num in enumerate(nums):
            cproduct *= num
            while cproduct >= k:
                cproduct /= nums[left]
                left +=1
            narrays += right-left +1
        return narrays


nums = [10, 5, 2, 6]
k = 100
solution = Solution()
solution.numSubarrayProductLessThanK(nums, k)