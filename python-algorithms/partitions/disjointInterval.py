class Solution:
    def partitionDisjoint(self, A):
        left = []
        maximumLeft = 0

        for num in A[:-1]:
            maximumLeft = max(maximumLeft, num)
            left.append(num)
        minimumRight = A[-1]
        right = 1
        pointer = A[-2]
        while pointer >= 0:
            if nums[pointer] >=
            pointer -=1


        return left, maximumLeft
solution = Solution()
nums = [5,0,3,8,6]
solution.partitionDisjoint(nums)