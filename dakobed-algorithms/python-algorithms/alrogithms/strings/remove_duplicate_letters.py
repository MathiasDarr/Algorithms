"""
Remove duplicate letters and return the lexicographically smallest string as a result.

Create a hash map mapping x -> index of last occurrence of x in the string.

Traverse the array:
    push elements on to the stack.

Consider the example of
    'jaj'
Once we see 'a', as we are looking to minimize lexigraphcilly and 'j' occurs later on in the string, we can safely pop
the existing 'j' from the stack



"""



class Solution:
    def removeDuplicateLetters(self, s):
        character_last_index_map = {c: i for i,c in enumerate(s)}
        stack = []
        for i, char in enumerate(s):
            if char in stack:
                continue
            while stack and stack[-1] > char and i < character_last_index_map[stack[-1]]:
                stack.pop()
            stack.append(char)
        return ''.join(stack)

solution = Solution()
s = "bcabc"
solution.removeDuplicateLetters(s)