class Solution:
    def removeInvalidParentheses(self, s):
        results = []
        stack = []
        deleteIndices = set()

        for index,char in enumerate(s):
            if char == ')' and len(stack) ==0:
                deleteIndices.add(index)
            elif char == ')' and len(stack) > 0:
                stack.pop()
            elif char == '(':
                stack.append(index)
        for index in stack:
            deleteIndices.add(index)
        return deleteIndices
s = "()())()"
solution = Solution()
solution.removeInvalidParentheses(s)