class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x < 0 or (x % 10 ==0  and x != 0 )):
            return False;
        revertedNumber = 0

        while x > revertedNumber:
            revertedNumber = revertedNumber * 10 +  (x % 10)
            x //= 10
        print(x)
        print(revertedNumber)
        return x == revertedNumber or x == revertedNumber//10


solution = Solution()
x = 121
print("The number {} is a palindrome {}".format(x, solution.isPalindrome(x)))