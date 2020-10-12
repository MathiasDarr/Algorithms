from itertools import zip_longest
from collections import deque

class Solution:
    def addStrings(self, num1, num2):
        str_to_digit = {val:idx for idx, val in enumerate('0123456789')}
        carry = 0
        result = deque()
        for c1, c2 in zip_longest(reversed(num1), reversed(num2), fillvalue='0'):
            carry, remainder = divmod(str_to_digit[c1] + str_to_digit[c2] + carry, 10)
            result.appendleft(remainder)
        if carry:
            result.appendleft(carry)
        return ''.join(map(str, result))

    # def addStrings(self, num1, num2):
    #     if not num1 and not num2:
    #         return 0
    #     elif not num1:
    #         return num2
    #     elif not num2:
    #         return num1
    #     if(len(num1) < len(num2)):
    #         num1 , num2 = num2, num1
    #     carry = 0
    #     pointer1 = len(num1) -1
    #     pointer2 = len(num2) -1
    #     output =0
    #     count = 0
    #     while pointer1 >=0 and pointer2 >=0:
    #         print("iteration")
    #         d1 = int(num1[pointer1])
    #         d2 = int(num2[pointer2])
    #         newcarry = 0
    #         if d1 + d2 + carry>=10:
    #             newcarry = 1
    #         digit = (d1+d2+carry)%10
    #         output += digit * (10 ** count)
    #         carry = newcarry
    #         pointer1 -=1
    #         pointer2 -=1
    #         count +=1
    #
    #     while pointer1  >=0:
    #         d1 = int(num1[pointer1])
    #         newcarry= 0
    #         if d1 + carry >=10:
    #             newcarry =1
    #         output += (d1+carry) * (10 ** count)
    #         carry = newcarry
    #         pointer1 -=1
    #         count +=1
    #     return output
solution = Solution()
num1 = "999"
num2 = "9999"

solution.addStrings(num1, num2)