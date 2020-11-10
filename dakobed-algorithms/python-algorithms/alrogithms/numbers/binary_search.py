class Solution:
    def mySqrt(self, x):
        """
        If x list inbetween mid*mid <= (mid+1) * (mid +1)
        :param x:
        :return:
        """
        small = 0
        big = x

        while small <= big:
            mid = (small+big)/2
            mid_plus_one = mid+1
            mid_squared = mid ** 2
            mid_plus_one_squared = mid_plus_one ** 2
            if mid_squared == x:
                return mid
            if mid_plus_one **2:
                return mid_plus_one


            elif result < x:

        return small

solution = Solution()
solution.mySqrt(19)