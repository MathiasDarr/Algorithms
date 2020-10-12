class Solution:
    def longestPalindrome(self, s):
        if not s or len(s) < 1:
            return ""
        start = 0
        end = 0
        for i in range(len(s)):
            len1 = self.expandFromMiddle(s, i, i)
            len2 = self.expandFromMiddle(s, i, i+1)
            mlen = max(len1, len2)

            if mlen > end-start:
                start = i - ((mlen-1)/2)
                end = i + (mlen/2)
        return s[start:end+1]

    def expandFromMiddle(self, s, left, right):
        print("I get called wth left " + str(left) + " and right " + str(right) )
        if not s or left > right or right>= len(s):
            return 0
        while right >= 0 and left < len(s) and s[left] == s[right]:
            left +=1
            right -=1
        print("I return wth right -left -1 " )
        return right - left -1


solution = Solution()
s = 'cabba'
print("The longest palindrome is " + solution.longestPalindrome(s))