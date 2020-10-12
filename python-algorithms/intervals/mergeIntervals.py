class Solution:
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x[0])
        newIntervals = [intervals[0]]
        print(newIntervals)
        for i in range(1, len(intervals)):
            if intervals[i][0] <= newIntervals[-1][1]:
                newIntervals[-1][1] = max(intervals[i][1], newIntervals[-1][1])
            else:
                newIntervals.append(intervals[i])
        return newIntervals


# intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals = [[1,4], [2,3]]
solution = Solution()

newIntervals = solution.merge(intervals)

