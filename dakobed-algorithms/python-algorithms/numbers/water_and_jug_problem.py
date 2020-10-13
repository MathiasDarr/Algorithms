import math

class Solution:
    def gcd(self, x, y):
        while y != 0:
            (x,y) = (y, x % y)
        return x
    def test(self):
        return 1 == 0 or 1==1 and 2 == 1


    def canMeasureWater(self, x , y , z):
        gcd, r = max(x,y), min(x,y)
        while r:
            gcd, r = r, gcd % r
            return z ==0 or x + y >= z and z % gcd == 0

    # def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    #     if z == 0:
    #         return True
    #     elif z > x + y:
    #         return False
    #     elif y == 0:
    #         if x == z:
    #             return True
    #         else:
    #             return False
    #     gcd_x_y = self.gcd(x, y)


solution = Solution()
solution.test()
# solution.gcd(18,12)
