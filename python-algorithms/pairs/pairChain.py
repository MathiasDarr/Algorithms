class Solution:
    def findLongestChain(self, pairs):
        pairs.sort()
        current = float('-inf')
        result = 0

        for p0, p1 in pairs:
            if p0 > current:
                current = p1
                result +=1
        return result

        # pairs.sort()
        # dp = [1] * len(pairs)
        #
        # for j in range(len(pairs)):
        #     for i in range(j):
        #         if pairs[i][1] < pairs[j][0]:
        #             dp[j] = max(dp[j], dp[i] + 1)
        # return max(dp)

solution = Solution()
pairs = [[1,2], [2,3], [3,4]]
solution.findLongestChain(pairs)
