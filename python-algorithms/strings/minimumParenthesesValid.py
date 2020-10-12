class Solution:
    def minAddToMakeValid(self, S):
        count = 0
        leftOpen = 0
        for char in S:
            if char == ')' and leftOpen ==0:
                count +=1
            elif char == ')' and leftOpen >0:
                leftOpen -=1
            elif char == '(':
                leftOpen +=1
        return count + leftOpen

s = '()))(('
solution = Solution()
solution.minAddToMakeValid(s)