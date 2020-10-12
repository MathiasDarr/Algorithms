class Solution:
    def minInsertions(self, s: str):

        s = s.replace('))', ']')
        count = 0
        leftCount = 0
        for c in s:
            if c =='(':
                leftCount +=1
            elif c ==']':
                if leftCount == 0:
                    count +=1
                else:
                    leftCount -=1

            elif c ==')':
                if leftCount ==0:
                    count +=2
                else:
                    count +=1
                    leftCount -=1
        count += leftCount * 2

        return count

solution = Solution()
s = '()()()()()())'
solution.minInsertions(s)