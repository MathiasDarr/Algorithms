from collections import Counter

class Solution:
    def findTheDifference(self, s, t):
        sCounter = Counter(s)
        tCounter = Counter(t)
        diff = tCounter - sCounter
        return diff.popitem()[0]




s = 'abcd'
t = 'abcde'
solution = Solution()

solution.findTheDifference(s,t)