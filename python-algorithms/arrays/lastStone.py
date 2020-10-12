import heapq
class Solution:
    def lastStoneWeight(self, stones):
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stone1 = heapq.heappop(heap)
            stone2 = heapq.heappop(heap)
            if stone1 != stone2:
                heapq.heappush(heap, -abs(stone1-stone2))
        return -heap[0] if heap else 0


stones = [2,7,4,1,8,1]
solution = Solution()
solution.lastStoneWeight(stones)