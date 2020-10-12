class Solution:
    def transpose(self, A):
        nRows = len(A)
        nCols = len(A[0])
        output = [[None] * nRows  for _ in range(nCols)]
        for r, row in enumerate(A):
            for c, value in enumerate(row):
                output[c][r] = value
        return output
A = [[1,2,3],[4,5,6]]
solution = Solution()
solution.transpose(A)


from collections import Counter
s1 = "delete"
s2 = "leet"
s1Counter = Counter(s1)
s2Counter = Counter(s2)
newDict = {}

allKeys = set().union(s2Counter.keys(),s1Counter.keys())
for key in allKeys:
    if key in s1Counter and key in s2Counter:
        newDict[key] = min(s1Counter[key], s2Counter[key])
