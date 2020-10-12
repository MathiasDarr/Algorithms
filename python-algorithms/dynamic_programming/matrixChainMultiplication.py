class Solution:
    def matrixChainOrder(self, p, n):
        dp = [[0 for _ in range(n)] for _ in range(n)]

