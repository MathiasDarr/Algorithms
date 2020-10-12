class Solution:
    def decodeString(self, s):
        stack_str = []
        stack_vals = []
        curr_val = 0

        for val in s:
            if val.isdigit():
                curr_val = curr_val * 10 + int(val)
            elif val == ']':
                if curr_val != 0:
                    stack_vals.append(curr_val)
                    curr_val = 0
                curr_str = ''
                num_occurences = stack_vals.pop()
                while len(stack_str):
                    elem = stack_str.pop()
                    if elem == '[':
                        stack_str.append(curr_str * num_occurences);
                        break
                    else:
                        curr_str = elem + curr_str  # Important Step
            else:
                if curr_val != 0:
                    stack_vals.append(curr_val)
                    curr_val = 0
                stack_str.append(val)

        return ''.join(stack_str)




        # countStack = []
        # stringStack = []
        #
        # index = 0
        # currentString = ''
        #
        # while index < len(s):
        #     char = s[index]
        #
        #     if char.isdigit():
        #         nextIndex = index
        #         while s[nextIndex].isdigit():
        #             nextIndex += 1
        #         countStack.append(int(s[index:nextIndex]))
        #         index = nextIndex
        #
        #     elif char == '[':
        #         print(stringStack)
        #         print(currentString)
        #         stringStack.append(currentString)
        #         print(currentString)
        #
        #         print(stringStack)
        #
        #         currentString = ''
        #         index +=1
        #     elif char == ']':
        #
        #         # tempString = stringStack.pop()
        #         tempString = currentString
        #         count = countStack.pop()
        #         # tempString = string + tempString
        #         currentString = tempString * count
        #         index +=1
        #     else:
        #         currentString += char
        #         print(currentString)
        #         index +=1
        #
        # return currentString

solution = Solution()

s = "3[a]2[bc]"

solution.decodeString(s)
