class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        index = 0

        for i in range(len(heights)):
            if len(stack) == 0 or heights[stack[-1]] <= heights[index]:
                stack.append(index)
                index +=1


        while index < len(heights):
            if len(stack) == 0 or heights[stack[-1]] <= heights[index]
                stack.append(index)
                index +=1
            else:
                poppedIndex = stack.pop()
                area = (heights[poppedIndex] * ((index - stack[-1] )))


    # def popFromStack(self, hstack, pstack, i):
    #     tempH = hstack.pop()
    #     tempPos = pstack.pop()
    #     tempSize = tempH * (i - tempPos)
    #     self.maxSize = max(tempSize, self.maxSize)
    #     return tempPos
    #
    #
    # def largestRectangleArea(self, heights):
    #     hstack = []
    #     pstack = []
    #     self.maxSize = 0
    #     for i, h in enumerate(heights):
    #         print(hstack)
    #         print(i)
    #         if len(hstack) ==0 or hstack[-1] < h:
    #             hstack.append(h)
    #             pstack.append(i)
    #         elif h < hstack[-1]:
    #             while len(hstack) > 0 and h < hstack[-1]:
    #                 tempPos = self.popFromStack(hstack, pstack, i)
    #             if len(hstack) == 0:
    #                 hstack.append(h)
    #                 pstack.append(tempPos)
    #     print(hstack)
    #     while len(hstack) >0:
    #         self.popFromStack(hstack, pstack,i+1)
    #     return self.maxSize

solution = Solution()
nums = [4,2,0,3,2,5]
solution.largestRectangleArea(nums)