class Solution:
    def constructRectangle(self,area):
        w1 = int(area **.5)
        while area % w1  != 0:
            w1 -=1
        w2 = area//w1
        return [w2, w1]

solution = Solution()
area = 4
solution.constructRectangle(area)