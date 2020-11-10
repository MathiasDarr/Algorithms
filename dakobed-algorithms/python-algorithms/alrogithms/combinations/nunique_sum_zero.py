class Solution:
    def sumZero(self, n):
        if n % 2 == 1:
            output = [0]
            n -= 1
        else:
            output = []
        i = 1
        while n >0:
            output.append(-i)
            output.append(i)
            i +=1
            n -=2

        print("the array looks like {}".format(output))
        print(sum(output))

solution = Solution()
solution.sumZero(9)