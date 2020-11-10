"""
num = "1432219"
k = 3

Attempt to make use of a greedy algorithm


"""


class Solution:
    def removeKdigits(self, num, k):
        size = len(num)

        if k == size:
            return "0"

        stack = []
        counter = 0
        while counter < size:
            while k > 0 and stack and stack[-1] > num[counter]:
                stack.pop()
                k -=1
            stack.append(num[counter])
            counter +=1

        while k >0:
            stack.pop()
            k -=1

        result_string = []
        while stack:
            current_character = stack.pop()
            result_string.append(current_character)
        result_string.reverse()
        while len(result_string) > 1 and result_string[0] =='0':
            result_string.pop(0)


        return ''.join(result_string)



solution = Solution()
k = 1
num = "111"
solution.removeKdigits(num, k)