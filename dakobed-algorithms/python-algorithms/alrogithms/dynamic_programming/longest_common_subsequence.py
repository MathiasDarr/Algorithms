"""
Longest Common Subsequence

Set up a dynamic programming array

"""


class Solution:
    def longestCommonSubsequence(self, text1, text2):
        l1 = len(text1)
        l2 = len(text2)

        dp = [[0 for _ in range(l1 +1)] for _ in range(l2 +1)]

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if text1[j-1] == text2[i-1]:
                     dp[i][j] = 1 + dp[i-1][j-1]
                else:
                     dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]



solution = Solution()
text1 = 'SHINCHAN'
text2 = 'NOHARAAA'


solution.longestCommonSubsequence(text1, text2)