"""
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

"""
from itertools import combinations


class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        minimum = arr[-1] - arr[0]
        output = []
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == minimum:
                output.append([arr[i-1], arr[i]])
            elif arr[i] - arr[i-1] < minimum:
                minimum = min(minimum, arr[i] - arr[i - 1])
                output = [[arr[i-1], arr[i]]]
        return output
    # def minimumAbsDifference(self, arr):
    #     pairs = [pair for pair in combinations(arr, r=2)]
    #     pairs.sort(key=lambda x: abs(x[0] - x[1]))
    #     output = []
    #     i = 0
    #     while abs(pairs[i][1] - pairs[i][0]) == abs(pairs[0][0] - pairs[0][1]):
    #         output.append([min(pairs[i]), max(pairs[i])])
    #         i += 1
    #     return sorted(output, key=lambda x:x[0])


array = [1,3,6,10,15]
solution = Solution()
solution.minimumAbsDifference(array)

