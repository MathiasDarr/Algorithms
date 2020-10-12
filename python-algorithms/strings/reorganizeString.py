from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, S):
        priorityQueue = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(priorityQueue)
        if any(-nc > (len(S) + 1) / 2 for nc, x in priorityQueue):
            return ""
        result = []
        while len(priorityQueue) >= 2:
            count1, char1 = heapq.heappop(priorityQueue)
            count2, char2 = heapq.heappop(priorityQueue)
            result.extend([char1, char2])
            if count1 + 1: heapq.heappush(priorityQueue, (count1 + 1, char1))
            if count2 + 1: heapq.heappush(priorityQueue, (count2 + 1, char2))
        return "".join(result) + (priorityQueue[0][1] if priorityQueue else '')

solution = Solution()
result = solution.reorganizeString('aaabb')