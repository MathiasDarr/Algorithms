class Solution:
    def removeDuplicates(self, S):
        stack = []
        for char in S:
            if len(stack) > 0 and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)

    def removeDuplicatesII(self, s, k):
        if len(s) == 0:
            return ''
        stack = [[s[0], 1]]
        for char in s[1:]:
            if len(stack) >0 and stack[-1][0] == char:
                if stack[-1][1] == k-1:
                    stack.pop()
                else:
                    stack[-1][1] +=1
            else:
                stack.append([char,1])
        return ''.join([char[0]*char[1] for char in stack])


solution = Solution()

# s = "deeedbbcccbdaa"
# k = 3

s = "deeedbbcccbdaa"
k = 3

solution.removeDuplicatesII(s, k)

# S = "abbaca"
# solution.removeDuplicates(S)