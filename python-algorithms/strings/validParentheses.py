

def isValid(s):
    stack = []
    for char in s:
        charMap = {'}':'{', ')':'(', ']':'['}

        if char in {'(', '{', '['}:
            stack.append(char)
        elif char in {'}', ']', ')'}:
            if len(stack) == 0 or stack[-1] != charMap[char]:
                return False
            else:
                stack.pop()
    return len(stack) == 0


s = '()[]{}'
result = isValid(s)
print("The string {} has valid parenthesis {}".format(s, result))