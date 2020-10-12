class Solution:
    def isValid(self, s):
        stack = []
        for char in s:
            if char is 'c':
                if len(stack) < 2 or stack.pop() != 'b' or stack.pop() != 'a':
                    return False
            else:
                stack.append(char)
        if stack:
            return False
        return True
        # indicesToDelete = set()
        # for i in range(len(s)-2):
        #     substr = s[i:i+3]
        #     if substr =='abc':
        #         indicesToDelete.add(i)
        #         indicesToDelete.add(i+1)
        #         indicesToDelete.add(i+2)
        # newS = ''
        # for i in range(len(s)-1,-1,-1):
        #     if i not in indicesToDelete:
        #         newS += s[i]
        # s = newS[::-1]
        # left = 0
        # right = len(s) -1
        #
        # while left < right:
        #     if s[left] =='a' and s[right] =='c':
        #         if s[left+1] =='b' and s[left+2] =='c':
        #             left +=3
        #         elif s[right-1] =='b' and s[right-2] =='a':
        #             right -=3
        #         elif s[left+1] == 'b':
        #             left +=2
        #             right -=1
        #         elif s[right-1] =='b':
        #             left +=1
        #             right -=2
        #         else:
        #             return False
        #     else:
        #         return False
        # return True

solution = Solution()
s = "abccba"
solution.isValid(s)