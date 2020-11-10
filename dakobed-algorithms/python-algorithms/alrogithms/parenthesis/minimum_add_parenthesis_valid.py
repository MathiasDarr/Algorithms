class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        count = 0
        for c in S:
            if c == '(':
                stack.append(c)
            elif c == ')':
                if len(stack) ==0:
                    count +=1
                else:
                    stack.pop()
        return len(stack) + count

s= "((("
solution = Solution()
solution.minAddToMakeValid(s)