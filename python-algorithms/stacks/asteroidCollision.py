
class Solution:
    def asteroiDCollision(self, asteroids):
        stack = []
        for a in asteroids:
            if len(stack) ==0 or a > 0:
                stack.append(a)
            else:
                while True:
                    topstack = stack[-1]
                    if topstack < 0:
                        stack.append(a)
                        break
                    elif topstack == abs(a):
                        stack.pop()
                        break
                    elif topstack > abs(a):
                        break
                    else:
                        stack.pop()
                        if abs(a) < topstack:
                            stack[-1]
        return stack
        # for a in asteroids:
        #     if a < 0:
        #         if len(stack) ==0 or stack[-1] < 0:
        #             stack.append(a)
        #         elif stack[-1] > 0:
        #             while True:
        #
        #                 if len(stack) ==0:
        #                     print('right hereebb')
        #                     stack.append(a)
        #                     break
        #                 elif stack[-1] < 0:
        #                     break
        #                 elif stack[-1] > abs(a):
        #                     print('right hereeaa')
        #                     break
        #                 elif stack[-1] < abs(a):
        #                     stack.pop()
        #                     stack.append(a)
        #                 elif stack[-1] == abs(a):
        #                     print('right heree')
        #                     stack.pop()
        #                     break
        #     else:
        #         stack.append(a)
        return stack


asteroids =[5, 10, -8]

solution = Solution()
solution.asteroiDCollision(asteroids)
