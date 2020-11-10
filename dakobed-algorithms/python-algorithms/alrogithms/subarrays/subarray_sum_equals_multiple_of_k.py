"""
Instead of finding a subarray whose sum is equal to k, we are tasked i finding a subarray whose sum is any multiple of k.

THe previous question asked to find i & j s.t
        sum(nums[i:j]) = k
        or sum(nums[i:j])/k = 1

In this question we are instead searching for a sub array w/ indices i & j s.t
        sum(nums[i:j]) % k == 0

Which is to say that the sum is divisible -by k > that the sum of the sub array is a multiple of k.


"""
from collections import defaultdict

class Solution:
    def checkSubarraySum(self, nums, k):
        cumsum_hash_map = defaultdict(int)
        cumsum_hash_map[0] = -1
        cumsum_mod_k = 0

        for i, num in enumerate(nums):
            cumsum_mod_k += (cumsum_mod_k + num) % abs(k) if k else cumsum_mod_k + num

            if cumsum_hash_map[]

            if cumsum - k in cumsum_hash_map:
                pass
solution = Solution()

[23, 2, 4, 6, 7]
k=6