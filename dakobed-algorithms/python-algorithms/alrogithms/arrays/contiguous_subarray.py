"""
Given an array of 0s and 1s, find the maximum length of a contiguous subarray with equal numbers of 0's and 1's.

Maintain a variable count, whose value corresponds to the relative number of 0's & 1's encountered while traversing
the array.
Traverse the array:
    add one to count if a 1 is encountered, subtract one if a 0 is encountered


"""



class Solution:
    def findMaxLength(self, nums):
        maxCount = 0
        count = 0
        counts_dictionary = {0: -1}
        for i, num in enumerate(nums):
            count = count + (1 if num == 1 else -1)
            if count in counts_dictionary:
                maxCount = max(maxCount, i-counts_dictionary[count])
            else:
                counts_dictionary[count] = i
        return maxCount
solution = Solution()
nums = [0,1,0,1]
solution.findMaxLength(nums)