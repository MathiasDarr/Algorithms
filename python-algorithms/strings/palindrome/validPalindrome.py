class Solution:
    def validPalindrome(self,s):
        def isPalindrome(left, right):
            while left<right:
                if s[left] != s[right]:
                    return False
                left +=1
                right -=1
            return True

        left =0
        right = len(s) -1
        while left<right:
            if s[left] != s[right]:
                return True if isPalindrome(left, right-1) or isPalindrome(left+1, right) else False
            left+=1
            right -=1
        return True

solution = Solution()
solution.validPalindrome("abbca")
