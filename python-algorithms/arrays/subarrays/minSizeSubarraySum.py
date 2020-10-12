class Solution:
    def minSubArray(self, s, nums):
        result = float('inf')
        left = 0
        valSum = 0
        for right, num in enumerate(nums):
            valSum += num
            while valSum >=s:
                result = min(result, right-left+1)
                valSum -= nums[left]
                left +=1
        return result if result != float('inf') else 0

    def minSubArrayLenEquals(self, s, nums):
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
# nums = [2,3,1,2,4,3]

# nums = [1,2,3,4,5]
# s = 11
s = 17
nums = [2,3,1,2,4,3]

solution = Solution()
solution.minSubArray(s, nums)