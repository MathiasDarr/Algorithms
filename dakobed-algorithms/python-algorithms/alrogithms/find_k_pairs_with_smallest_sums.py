"""
Find K Pairs with smallest sums

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3

The insight behind this solution is as follows.
Instead of adding all pairs of elements to the heap, make use of the fact that the arrays are sorted.

Initialize a heap whose values are sum, and the indices i1 & i2 of nums1, nums2
    - The smallest sum between elements will be nums1[0] + nums2[0], since the elements are sorted.

Perform K iterations,
    Pop from the priority queue, the pair of elements with the smallest sum will be at the top of the heap.
    Next notice that the pair of elements with the next smallest sum will either be the pair whose indices are
        i1 + 1 , i2
        i1, i2 + 1
    Therefore we just have two add these two heap elements.

"""

import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):

        if not nums1 or not nums2:
            return []

        heap = [(nums1[0] + nums2[0], 0,0)]
        results = []
        visited = set()

        while len(results) < k and heap:
            v, index1, index2 = heapq.heappop(heap)
            results.append([nums1[index1], nums2[index2]])
            # Next smallest sum is either going to be (index1 + 1, index2) or (index1, index2+1)
            # Verify that the indices are not out of bounds, add

            if index1 + 1 < len(nums1) and (index1 + 1, index2) not in visited:
                visited.add((index1+1, index2))
                heapq.heappush(heap, (nums1[index1+1] + nums2[index2], index1+1, index2))

            if index2 + 1 < len(nums2) and (index1, index2 + 1) not in visited:
                visited.add((index1, index2+1))
                heapq.heappush(heap, (nums1[index1] + nums2[index2+1], index1, index2+1))

        return results

solution = Solution()
nums1 = [1, 7, 11]
nums2 = [2,4,6]

solution.kSmallestPairs(nums1, nums2, 3)