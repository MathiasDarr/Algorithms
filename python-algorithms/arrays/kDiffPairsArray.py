class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) +1

        count = 0
        for key in hashmap.keys():
            if k ==0:
                if hashmap[key] >= 2:
                    count +=1
            else:
                if key + k in hashmap:
                    count +=1
        return count
    # def findPairs(self, nums, k):
    #     count = 0
    #     if k < 0:
    #         return 0
    #     hashmap = {}
    #     hashset = set()
    #     for num in nums:
    #         if num in hashmap:
    #             num2 = hashmap[num]
    #             hashset.add((num,num2))
    #             # hashset.add((min(num, num2), max(num,num2)))
    #             count +=1
    #         hashmap[num+k] =num
    #         hashmap[num-k] =num
    #     return len(hashset)

# nums =  [6,3,5,7,2,3,3,8,2,4]
nums = [1,1,1,2,1]
k = 2

solution = Solution()
solution.findPairs(nums, k)