"""
LeeteCode


"""

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
        intervals.sort(key=lambda x: x[0])
        output = [[intervals[0][0],intervals[0][1]]]
        for i in range(1,len(intervals)):
            low = intervals[i][0]
            high = intervals[i][1]
            if low <= output[-1][1]:
                output[-1][1] = max(high, output[-1][1])
            else:
                output.append(intervals[i])
        return output

intervals = [[1,5], [4,5]]
solution = Solution()
solution.merge(intervals)