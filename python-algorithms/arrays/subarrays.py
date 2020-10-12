import collections
class Solution:
    def subarraySum(self, nums, k):
        # hashmap = collections.defaultdict(int)
        # cumSum = 0
        # count = 0
        # hashmap[0] = 1
        # for num in nums:
        #     cumSum = cumSum + num
        #     if cumSum-k in hashmap:
        #         count+=hashmap[cumSum-k]
        #     hashmap[cumSum] +=1
        # return count
        count = 0
        hashMap = {}
        hashMap[0] =1
        cumSum = 0
        for i in range(len(nums)):
            cumSum += nums[i]
            if cumSum - k in hashMap:
                count += hashMap.get(cumSum-k, 0)
            hashMap[cumSum] = hashMap.get(cumSum,0)+1
        return count

nums = [0,0,0,0,0,0,0,0,0,0]
solution = Solution()
solution.subarraySum(nums, 0)