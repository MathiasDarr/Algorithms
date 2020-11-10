"""
LeetCode 57

Given a list of intervals & a new interval, return a list of intervals w/ no overlapping


"""


class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
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


intervals = [[1,3],[6,9]]
newInterval = [2,5]

solution = Solution()
solution.insert(intervals, newInterval)