from collections import Counter
class Solution:
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        sCounter = Counter(s)
        longestOdd = 0
        evenSum = 0
        for counts in sCounter.values():
            if counts % 2 == 0:
                evenSum += counts
            else:
                longestOdd = max(longestOdd, counts)

        return evenSum + longestOdd


solution = Solution()
s = "abccccdd"
solution.longestPalindrome(s)