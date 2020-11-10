class Solution:
    def isPowerOfThree(self,n):
        if n < 1:
            return False
        while n % 3 == 0:
            n /= 3
        return n ==1

solution = Solution()
solution.isPowerOfThree(27*27*81*81*81*5)