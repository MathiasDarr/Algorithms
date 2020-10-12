class Solution:

    def binary_search_lower_bound(self, nums, start: int, end: int, num: int):
        if start > end or len(nums) == 0:
            return
        mid = (start + end) // 2
        if nums[mid] == num \
                or (mid > 0 and nums[mid - 1] < num < nums[mid]) \
                or (mid == 0 and nums[mid] > num):
            return mid
        if nums[mid] > num:
            return self.binary_search_lower_bound(nums, start, mid - 1, num)
        else:
            return self.binary_search_lower_bound(nums, mid + 1, end, num)

    def lisBinarySearch(self, nums):
        tmp = []
        for num in nums:
            insertPosition = self.binary_search_lower_bound(tmp, 0, len(tmp) -1, num )
            if insertPosition is None:
                tmp.append(num)
            else:
                tmp[insertPosition] = num
        return len(tmp)

    def lengthOfLIS(self, nums):
        dp = [1] * len(nums)
        lis = 1
        for j in range(len(nums)):
            for i in range(j):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] +1)
                lis = max(lis, dp[j])
        return lis
# nums = [-1,3,4,5,2,2,2,2,2]
nums = [10,9,2,5,3,7,101,18]
solution = Solution()
dp = solution.lisBinarySearch(nums)