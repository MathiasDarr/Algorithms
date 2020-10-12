class Solution:
    def numSubarraysWithSum(self, A, S):
        cumSum = [0]
        for x in A:
            cumSum.append(cumSum[-1] + x)
        counts = {}
        result = 0
        for x in cumSum:
            result += counts.get(x,0)
            counts[x+S] = counts.get(x+S, 0) +1
        return result

A = [1,1,1,1,1]
solution = Solution()
solution.numSubarraysWithSum(A,2)