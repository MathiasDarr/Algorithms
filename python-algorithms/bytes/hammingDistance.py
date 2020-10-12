from itertools import combinations

class Solution:
    def totalHammingDistance(self, nums):
        combs = combinations(nums, 2)
        memo = {}
        return sum([self.hammingDistance(x1, x2, memo) for x1, x2 in combs])
    def hammingDistance(self,x, y, memo):
        if (x,y) in memo:
            return memo[(x,y)]
        memo[(x,y)] = bin(x^y)[2:].count('1')
        return memo[(x,y)]
solution = Solution()
# solution.hammingDistance(1, 4)

numbers = [1,2,4]
solution.totalHammingDistance(numbers)
