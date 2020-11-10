"""
remove duplicates letter.

Smallest in lexigraphical order

s = "cbacdcbc"
output -> "acdb"

Find the last occurrence for each character.

Use a stack to keep the characters for reuslt

Traverse over the input string

    to ensure that we get the lexigraphically smallest result,

    If current character is smaller than the last character in the stack,
    and the last character exists in the sequence of letters (not seen yet in the traversal), we can pop this last character
    from the stack to get a smaller result


    s =  'jaj'

    iteration index = 1, current character is 'a', and stack[-1] = 'j' therefore we can pop from the stack to get the lexigraphically smaller
    result


"""



class Solution:
    def removeDuplicateLetters(self, s):
        char_last_index_map = {c: i for i, c in enumerate(s)}
        stack = []
        for i, char in enumerate(s):
            if char in stack:
                continue
            while stack and stack[-1] > char and i < char_last_index_map[stack[-1]]:
                stack.pop()
            stack.append(char)
        return ''.join(stack)

solution = Solution()
s = "bcabc"
solution.removeDuplicateLetters(s)