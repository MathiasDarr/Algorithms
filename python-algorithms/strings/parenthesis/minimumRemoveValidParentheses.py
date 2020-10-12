class Solution:
    def minRemoveToMakeValid(self, s):
        deleteIndices = set()
        stack = []
        for index in range(len(s)):
            if s[index] == ')' and len(stack) ==0:
                deleteIndices.add(index)
            elif s[index] ==  ')' and len(stack) >0:
                stack.pop()
            elif s[index] == '(':
                stack.append(index)
        for index in stack:
            deleteIndices.add(index)

        newString = ''
        for i in range(len(s)-1,-1, -1 ):
            if i not in deleteIndices:
                newString += s[i]
        return newString[::-1]

solution = Solution()
s = "lee(t(c)o)de)"
newString = solution.minRemoveToMakeValid(s)
# s = "))(("
# solution.minRemoveToMakeValid(s)
