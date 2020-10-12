class Solution:
    def removePalindromeSub(self, s):
        if len(s) ==0:
            return 0
        if self.isPalindrome(s):
            return 1
        return 2
    def isPalindrome(self,s):
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left+=1
            right -=1
        return True

s= 'abbba'
solution = Solution()
solution.removePalindromeSub(s)
