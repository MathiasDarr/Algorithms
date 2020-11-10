"""
Given a binary string, count the number of substrings whose 0's and 1's are grouped and have equal numbers

1100 -> valid
1010 -> invalid



"""


class Solution:
    def countBinarySubstrings(self, s):

        for c in s:
            if c == '0':
                pass
            if c == '1':
                pass
solution = Solution()
s = "00110011"
solution.countBinarySubstrings(s)