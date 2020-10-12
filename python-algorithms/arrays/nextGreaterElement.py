class Solution:
    def nextGreaterElement(self, nums1, nums2):
        next_greatest = {}
        stack = []

        for num in nums2:
            print(stack)
            print(next_greatest)
            if len(stack) > 0 and stack[-1] < num:
                next_greatest[stack.pop()] = num
            stack.append(num)

        for i in range(len(nums1)):
            nums1[i] = next_greatest.get(nums1[i], -1)
        return nums1

        numsum = sum(nums)
        if numsum % 2 == 1:
            return False

        nums.sort()
        memo = dict()

        # check if nums[i:] can have sum rem_sum
        def dp(i, rem_sum):
            if rem_sum == 0:
                return True
            if i >= len(nums):
                return False
            if rem_sum < nums[i]:
                return False

            if rem_sum in memo:
                return memo[rem_sum]

            memo[rem_sum] = dp(i + 1, rem_sum - nums[i]) or dp(i + 1, rem_sum)
            return memo[rem_sum]



solution = Solution()
nums1 = [4,1,2]
nums2 = [5,4,3,2,6]
solution.nextGreaterElement(nums1, nums2)