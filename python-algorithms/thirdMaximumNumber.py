import heapq
class Solution:
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return sorted(nums)[-1]
        heap = []
        for element in nums:
            if len(heap) < 3:
                heapq.heappush(heap, element)
            else:
                heapq.heappushpop(heap, element)
        return heapq.heappop(heap)




solution = Solution()
nums = [3,9,10,2,1]
solution.thirdMax(nums)