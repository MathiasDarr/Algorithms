class Solution:
    def isPerfectSquare(self, num):

        if num < 0: return False
        if num == 0 or num == 1: return True

        # # quickly find a boundary
        # index = 1
        # while index ** 2 < num:
        #     index <<= 1
        #
        # if index ** 2 == num: return True

        small = 0
        big = num
        while small < big - 1:
            mid = (small + big) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                small = mid
            else:
                big = mid
        return False

solution = Solution()
solution.isPerfectSquare(1)
