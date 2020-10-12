from collections import Counter
class Solution:
    def minWindow(self, s, t):

        windowSize = float('inf')
        left = 0
        index = 0
        tCounter = Counter(t)

        targetCounts = {}

        while index < len(s):
            char = s[index]


S = "ADOBECODEBANC"
T = "ABC"