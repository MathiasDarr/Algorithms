"""
Find K-th smallest pair distance

given array, return the k-th smallest distance among all pairs


NlogN

Binary Search + Prefix sum

Let's binary search for the answer, which is in the range [0,W] where W = max(nums) - min(nums)





"""

import heapq



class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()

        heap = [(nums[i+1] - nums[i], i, i+1) for i in range(len(nums)-1)]
        heapq.heapify(heap)

        while k >0:
            distance, index1, index2 = heapq.heappop(heap)

            k-=1
            ## We add another pair of elements to heap, along w/ their distances from each other
            ## Add the pair of elements at index1, and element at index2+1
            if index2 + 1 < len(nums):
                heapq.heappush(heap, (nums[index2+1] - nums[index1], index1, index2+1))

        return distance
solution = Solution()

nums = [1,3,6]

solution.smallestDistancePair(nums, 2)