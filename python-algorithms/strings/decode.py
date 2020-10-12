stack = [('a', 3), ('c', 2)]
#stack = [('c',2)]
s = ''
tempString = ''
while len(stack) > 0:
    string, count = stack.pop()
    tempString = string + tempString
    tempString = tempString * count
    print(tempString)