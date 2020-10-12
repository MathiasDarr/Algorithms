class Solution:
    def reverseParentheses(self,s):
        left = []
        output = ''
        for index, c in enumerate(s):
            if c == '(':
                left.append('')
            elif c == ')':
                string = left.pop()
                if len(left) == 0:
                    output += string[::-1]
                else:
                    left[-1] += string[::-1]
            else:
                if len(left) == 0:
                    output += c
                else:
                    left[-1] += c
        return output

# s = "(u(love)i)"
s = 'a(bcdefghijkl(mno)p)q'

solution = Solution()
solution.reverseParentheses(s)