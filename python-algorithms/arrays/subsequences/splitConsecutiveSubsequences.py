from collections import Counter

class Solution:
    def isPossible(self, nums):
        frequencyMap = Counter(nums)
        hMap = {}
        for i, num in enumerate(nums):
            if frequencyMap.get(num) ==0:
                continue
            if hMap.get(num, 0) > 0:
                hMap[num] -=1
                hMap[num+1] = hMap.get(num+1, 0) +1
                frequencyMap[num] = frequencyMap.get(num) -1
            elif frequencyMap.get(num,0) > 0 and  frequencyMap.get(num+1,0) > 0 and frequencyMap.get(num+2,0) > 0:
                frequencyMap[num] -=1
                frequencyMap[num+1]  -=1
                frequencyMap[num+2]  -=1
                hMap[num+3] = hMap.get(num+3, 0) + 1
            else:
                return False
        return True

nums = [1,2,3,4,4,5,5]
solution = Solution()
solution.isPossible(nums)