class Solution:
    def multiply(self, num1, num2):
        result = [0] * (len(num1) + len(num2))

        for i,x in enumerate(reversed(num1)):
            for j, y in enumerate(reversed(num2)):
                a = int(x) * int(y)

num1 = "2"
num2 = "3"