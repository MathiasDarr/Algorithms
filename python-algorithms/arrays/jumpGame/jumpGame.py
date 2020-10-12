class Solution:
    # def maxJumps(self, arr, d: int):
    #     if len(arr) == 1: return 1
    #     n = len(arr)
    #     dic = {}
    #
    #     def bfs(index):
    #         if index in dic: return dic[index]
    #         left, right = -1, 1
    #         res = 0
    #         while True:
    #             if index + left < 0 or arr[index + left] >= arr[index]:
    #                 break
    #             res = max(res, bfs(index + left) + 1)
    #             left -= 1
    #             if abs(left) >= d + 1: break
    #
    #         while True:
    #             if index + right >= n or arr[index + right] >= arr[index]:
    #                 break
    #             res = max(res, bfs(index + right) + 1)
    #             right += 1
    #             if abs(right) >= d + 1: break
    #         dic[index] = res
    #         return res
    #
    #     for i in range(n):
    #         if i not in dic:
    #             bfs(i)
    #     return dic

    def maxJumps(self, arr, d):
        memo = {}
        def recursiveVisit(index):
            if index in memo:
                return memo[index]
            maxv = 0
            for x in range(1,d+1):
                if 0<= index + x < len(arr):
                    if arr[index+x] >= arr[index]:
                        break
                    maxv = max(maxv, recursiveVisit(index+x) + 1)
            for x in range(1,d+1):
                if 0<=index < len(arr) and  0<= index - x < len(arr):
                    if arr[index-x] >= arr[index]:
                        break
                    maxv = max(maxv, recursiveVisit(index+x) +1)
            memo[index] = maxv
            return maxv
        maxVisited = 0
        memo = {}
        for i in range(len(arr)):
            if i not in memo:
                maxVisited = max(maxVisited, recursiveVisit(i))
            # maxVisited = max(maxVisited, len(visited))
        return memo

    def canReach(self, arr, start):
        queue = [start]
        visited = {start}
        while len(queue) >0:

            index= queue.pop(0)
            print(index)
            val = arr[index]
            if val ==0:
                return True

            for i in [index + val, index-val]:
                if i >= 0 and i < len(arr) and i not in visited:
                    queue.append(i)
        return False

    def jump(self, nums):
        n = len(nums)
        if n <2:
            return 0
        maxPosReach = nums[0]
        currentStep = 1
        maxPosCanReachWithCurrentSteps = nums[0]
        for i in range(1, n):
            if maxPosCanReachWithCurrentSteps < i:
                currentStep +=1
                maxPosCanReachWithCurrentSteps = maxPosReach
            maxPosReach = max(maxPosReach, i+nums[i])
        return currentStep

solution = Solution()
# arr = [4,2,3,0,3,1,2]
# arr = [3,0,2,1,2]
# solution.canReach(nums, 2)

# nums = [2,3,1,1,4]
# nums = [1,1,1,1]
# solution.jump(nums)

arr = [6,4,14,6,8,13,9,7,10,6,12]
d = 2
memo = solution.maxJumps(arr, d)
#
# arr = [3,3,3,3,3]
# d = 3
# print(solution.maxJumps(arr, d))
#
# arr = [7,6,5,4,3,2,1]
# d = 1
# print(solution.maxJumps(arr, d))
#
# arr = [7,1,7,1,7,1]
# d = 2
# print(solution.maxJumps(arr, d))
