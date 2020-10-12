class Solution:
    def longestPalindromeSubseq(self, s):
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1



        for i in range(2, n+1):
            for j in range(1,i+1):
                if s[i] == s[j]:


                    print((i,j))
    # def longestPalindromeSubseq(self, s):
    #
    #     def lps(seq, i, j, memo):
    #         if (i,j) in memo:
    #             return memo[(i, j)]
    #         # Base Case 1: If there is
    #         # only 1 character
    #         if (i == j):
    #             return 1
    #         elif (seq[i] == seq[j] and i + 1 == j):
    #             memo[(i,j)] =2
    #             return 2
    #
    #         elif (seq[i] == seq[j]):
    #             memo [(i,j)] = lps(seq, i + 1, j - 1, memo) + 2
    #             return memo[(i,j)]
    #
    #         else:
    #             memo[(i,j)] = max(lps(seq, i, j - 1, memo),
    #                    lps(seq, i + 1, j, memo))
    #             return memo[(i,j)]
    #     memo = {}
    #     return lps(s, 0, len(s)-1, memo)


seq = "bbbab"
solution = Solution()
solution.longestPalindromeSubseq(seq)