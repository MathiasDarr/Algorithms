from collections import Counter
class Solution:
    def canConstruct(self, s, k):
        if len(s) < k:
            return False
        sCounter=  Counter(s)
        oddCount = 0
        for key, value in sCounter.items():
            if value % 2 == 1:
                oddCount+=1
        return False if oddCount > k else True


s = "cr"
k = 7
solution = Solution()
solution.canConstruct(s, k)