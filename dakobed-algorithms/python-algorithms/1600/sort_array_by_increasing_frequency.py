"""
LeetCode 1636 Sort Array by Increasing Frequency

return elements of the array, sorted in increasing order based on the frequency of values.
If multiple values have the same frequency, sort them in decreasing order


Provide a second value on which to break ties in sorting



"""


from collections import Counter


class Solution:
    def frequencySort(self, nums):
        nums_counter = Counter(nums)
        items = list(nums_counter.items())
        sorted_counts = sorted(items, key=lambda x: (x[1], -x[0]))
        return [num[0] for num in sorted_counts for _ in range(num[1])]

nums = [1,1,2,2,2,3]
solution = Solution()
solution.frequencySort(nums)