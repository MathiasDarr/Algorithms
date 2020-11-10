class Solution:
    def removeDuplicates(self, s, k):
        if len(s) == 0:
            return ''
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] ==k:
                    stack.pop()
            else:
                stack.append([c,1])
        return ''.join([x[0] * x[1] for x in stack])


s = "deeedbbcccbdaa"
k = 3
solution = Solution()
solution.removeDuplicates(s, k)