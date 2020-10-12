class Solution:
    def canCross(self, stones):
        for i in range(3, len(stones)):
            if stones[i] > stones[i - 1] * 2:
                return False
        stonesSet = set(stones)
        lastStone = stones[-1]
        stack = [(0,0)]
        while stack:
            jumpDistance, position = stack.pop()
            for i in range(jumpDistance-1, jumpDistance+2):
                if i <= 0:
                    continue
                nextPosition = position + i
                if nextPosition == lastStone:
                    return True
                elif nextPosition in stonesSet:
                    stack.append((i, nextPosition))
        return False

solution = Solution()
stones = [0,1,3,5,6,8,12,17]
solution.canCross(stones)