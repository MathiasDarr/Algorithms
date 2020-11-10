"""
Leet Code 658:  Find K Closest Elements
Sorted array, two integers k & x, find the k closest elements to x in array the result also be sorted in ascending order

use a HEAP
    20%,
heap = [(abs(arr[i] - x), arr[i]) for i in range(len(arr))]
heapq.heapify(heap)
solution.findClosestElements(arr, k, x)


values = []
while k > 0:
    k -=1
    distance, val = heapq.heappop(heap)
    values.append(val)
values.sort()


"""
import heapq


class Solution:
    def findClosestElements(self, arr, k, x):
        arr.sort(key=lambda v: abs(v - x))
        vals = arr[:k]
        return sorted(vals)

        # heap = [(abs(arr[i] - x), arr[i]) for i in range(len(arr))]
        # heapq.heapify(heap)
        # values = []
        # while k > 0:
        #     k -= 1
        #     distance, val = heapq.heappop(heap)
        #     values.append(val)
        # values.sort()
        # return values

solution = Solution()
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
solution.findClosestElements(arr, k, x)




