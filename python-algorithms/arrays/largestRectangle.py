class Solution:
    def largestRectangleArea(self, heights):
        hstack = []
        pstack = []
        maxRectangle = 0
        for i, num in enumerate(heights):
            if len(hstack) == 0 or num > hstack[-1]:
                hstack.append(num)
                pstack.append(i)
            elif num < hstack[-1]:
                while len(hstack) >0 and num < hstack[-1]:
                    h = hstack.pop()
                    pos = pstack.pop()
                    tempSize = h * (i - pos)
                    maxRectangle = max(maxRectangle, tempSize)
                hstack.append(num)
                pstack.append(i)
        while len(hstack) >0:
            h = hstack.pop()
            pos = pstack.pop()
            tempSize = h * (len(heights) - pos)
            maxRectangle = max(maxRectangle, tempSize)
        return maxRectangle

solution = Solution()
heights = [2,1,2]

area = solution.largestRectangleArea(heights)