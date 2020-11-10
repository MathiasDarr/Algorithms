"""
LeetCode 409

Given a string s, return the length of the longest palindrome that can be build w/ those letters

The key insight to this problem is that a palindrome can be constructed w/ a maximum of a single odd numbered character

However we can subtract 1 from the counts of subsequent odd characters s.t they are even.

"""
from collections import Counter

class Solution:
    def longestPalindrome(self, s):
        scounter = Counter(s)
        count = 0
        found_maximum_odd_flag = False
        value_counts = sorted(list(scounter.items()), key=lambda x: x[1], reverse=True)
        for key, val in value_counts:
            if val % 2 == 1:
                if not found_maximum_odd_flag:
                    found_maximum_odd_flag = True
                    count += val
                else:
                    count += val -1
            else:
                count += val
        return count

s = "abccccdd"
solution = Solution()
solution.longestPalindrome(s)