"""
LeetCode 1647
Return the number of deletions necessary to make frequency count unique.

"""
from collections import Counter

class Solution:
    def minDeletions(self, s):
        scounter = Counter(s)
        unique_counts_set = set()
        ndeletions = 0
        for key, count in scounter.items():
            deletions = 0

            while count in unique_counts_set and count > 0:
                count -= 1
                deletions += 1
            unique_counts_set.add(count)
            ndeletions += deletions
        return ndeletions
solution = Solution()
s = "ceabaacb"
solution.minDeletions(s)