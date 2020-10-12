class Solution:
    def maxSubArrayEqualsK(self, k, nums):
        cumSum = 0
        hashmap = {}
        hashmap[0] = -1
        minLength = float('inf')
        for i, num in enumerate(nums):
            cumSum += num
            hashmap[cumSum] = i
            print(cumSum)
            print(hashmap)
            if cumSum - s in hashmap:
                minLength = min(minLength, i-hashmap[cumSum-s] )
        return minLength #if minLength != float('inf') else 0