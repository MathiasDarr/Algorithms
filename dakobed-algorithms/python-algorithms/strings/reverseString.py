class Solution:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left+1, right -1)
        helper(0, len(s)-1)

    # def reverseString(self, s):
    #     left = 0
    #     right = len(s) -1
    #     while left < right:
    #         s[left], s[right] = s[right], s[left]
    #         left +=1
    #         right -=1


s = list('reverse')
solution = Solution()
solution.reverseString(s)
print(''.join(s))