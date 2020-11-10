"""
LeetCode 459 Repeated Substring Pattern

Given a non-empty string check if it can be constructed by taking a substring of it and appending
multiple copies of the substring together. You may assume the given string consists of lowercase English letters only
and its length will not exceed 10000.


"""



class Solution:
    def repeatedSubstringPattern(self, s):
        n = len(s)

        for i in range(1, n):
            if n % i == 0:
                niterations = n // i
                if s == s[:i] * niterations:
                    return True
        return False

solution = Solution()
s= "abadabad"
solution.repeatedSubstringPattern(s)
