
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        cache = [[-1] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        trace = [[(-1, -1)] * (len(str2) + 1) for _ in range(len(str1) + 1)]

        def dp(i: int, j: int) -> int:
            if i == len(str1):
                return len(str2) - j
            elif j == len(str2):
                return len(str1) - i
            elif cache[i][j] != -1:
                return cache[i][j]

            if str1[i] == str2[j]:
                result = dp(i + 1, j + 1) + 1
                trace[i][j] = i + 1, j + 1
            else:
                ps1 = dp(i + 1, j)
                ps2 = dp(i, j + 1)
                if ps1 < ps2:
                    result = ps1 + 1
                    trace[i][j] = i + 1, j
                else:
                    result = ps2 + 1
                    trace[i][j] = i, j + 1

            cache[i][j] = result
            return result

        dp(0, 0)

        res = ""
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            ii, jj = trace[i][j]
            if ii == i + 1:
                res += str1[i]
            else:
                res += str2[j]
            i, j = ii, jj
        return res + str1[i:] + str2[j:]
        # m = len(str1)
        # n = len(str2)
        # dp = [[0] * (n+1) for _ in range(m+1)]
        # print(m)
        # for i in range(1,m+1):
        #     dp[i][0] = i
        # for j in range(1,n+1):
        #     dp[0][j] = j
        #
        # for i in range(1,m+1):
        #     for j in range(1,n+1):
        #         print("i: " + str(i) + " j: " + str(j))
        #         if str1[i-1] == str2[j-1]:
        #             dp[i][j] = dp[i-1][j-1] + 1
        #         else:
        #             dp[i][j] = max(dp[i-1][j], dp[i][j-1])


solution = Solution()
dp = solution.shortestCommonSupersequence("abac", "cab")
