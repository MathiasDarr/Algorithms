import heapq
from collections import Counter
class Solution:
    def kthLargest(self, nums, k):
        heap = []
        for num in nums:
            heapq.heappush(heap, -num)
        return [heapq.heappop(heap) for i in range(k)][-1] * -1

    def topKFrequentWords(self, words, k):
        heap = []
        counter = Counter(words)
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        return [heapq.heappop(heap)[1] for i in range(k) ]


    def topKFrequent(self, nums, k):
        heap = []
        counter = Counter(nums)
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        return [heapq.heappop(heap)[1] for i in range(k) ]

solution = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
solution.kthLargest(nums, k)


# k = 2
# solution = Solution()
# words = ["i", "love", "leetcode", "i", "love", "coding"]
# solution.topKFrequentWords(words, k)
