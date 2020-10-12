class Solution:
    def reverseBits(self, n):
        ret, power  = 0 , 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret


n = 43261596
output2  = 964176192

solution = Solution()
solution.reverseBits(input1)