"""

Find the number of subarrays whos sum is equal to k

Consider the array & k = 0
[1, -1, 0] which has cumulative sum of [0, 1,0,0]

There are 3 different subarrays s.t that the cusum is equal to 0

If we have encounter a cumulativesum - k in the hashmap,
    - instead of incrmeenting the nomber of subarrays by one, we increment by the number of subarrays already found
    with equivalent subarray sum.


"""

from collections import defaultdict
class Solution:
    def subarraysum(self, nums, k):
        cumulativesum_occurence_hashmap = defaultdict(int)
        cumulativesum_occurence_hashmap[0] = 1
        nsubarrays = 0
        csum = 0

        for num in nums:
            csum += num
            nsubarrays += cumulativesum_occurence_hashmap[csum - k]
            cumulativesum_occurence_hashmap[csum] += 1

        return nsubarrays


nums = [1,-1,0, 0 ]
solution = Solution()
solution.subarraysum(nums, 0)