"""
3[a]2[bc]

Traverse the array, maintaining a number variable
    - append elements to the string at the top of the stack.
    - Once a '[' is encountered, add a new element to the stack
        - push an empty string to the stack w/ multiplicty equal to the number variable we found
        - reset the number variable
    - Once a ']' is encountered
        - pop string & multiplicty off the stack, appending to the string at the top of the stack
    - All non bracket, non digit characters are appended to the string on the top of the stack

"""



class Solution:
    def decodeString(self, s):
        stack = [['', 1]]
        i = 0
        num = ''
        while i < len(s):
            c = s[i]
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append(['', int(num)])
                num = ''
            elif c == ']':
                sequence, k = stack.pop()
                stack[-1][0] += sequence * k
            else:
                stack[-1][0] += c
            i += 1
        return stack[0][0]


s = "a2[bc]p"

solution = Solution()
solution.decodeString(s)
