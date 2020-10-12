class Solution:
    def findShortestSubArray(self, nums):
        left = {}
        right = {}
        count = {}
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            count[num] = count.get(num,0)+1
            right[num] = i
        degree = max(count.values())
        minLength = len(nums)
        for num in count:
            if count[num] == degree:
                minLength = min(minLength, right[num]-left[num]+1)
        return minLength


nums = [1,2,2,3,1]
solution = Solution()
minLength = solution.findShortestSubArray(nums)