

class Solution:
    def findMaxLength(self, nums):
        maxCount = 0
        count = 0
        counts_dictionary = {}
        counts_dictionary[0] = -1
        for i, num in enumerate(nums):
            count = count + (1 if num == 1 else -1)
            if count in counts_dictionary:
                maxCount = max(maxCount, i - counts_dictionary[count])
            else:
                counts_dictionary[count] = i
        return maxCount

nums = [0,0,1,1]
solution = Solution()
count = solution.findMaxLength(nums)