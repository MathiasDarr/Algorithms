"""
Find a subsequence of integers nums[i], nums[j] and nums[k] s.t i < j < k and nums[i] < nums[k] < nums[j]

Approach #1:
Traverse array:
    Maintain a variable representing the minimum value up until the current iteration.  This will

    Traverse the remaining array in search of an element that is greater than the minimum but smaller than the element
    j of the outer loop.
    TLE

Approach 2, 


"""


class Solution:
    def find132pattern(self, nums):
        N = len(nums)
        min_array = list(nums)
        for i in range(1, N):
            min_array[i] = min(nums[i - 1], min_array[i - 1])

        j = N
        for i in range(N)[::-1]:
            if nums[i] <= min_array[i]:
                continue
            # while j < N and min_array[j] <= min_array[i]:
            #     j += 1
            if j < N and min_array[j] < nums[i]:
                return True
            if nums[i] > min_array[i - 1]:
                j -= 1
                min_array[j] = nums[i]

        return False


solution = Solution()
nums = [-1,3,2,0]
solution.find132pattern(nums)