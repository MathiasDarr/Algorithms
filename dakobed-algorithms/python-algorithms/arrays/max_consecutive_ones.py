

class Solution:
    def findMaxConsecutiveOnes(self, nums):
        maximum_area = 0
        current = 0
        for num in nums:
            if num == 1:
                current +=1
                maximum_area = max(current, maximum_area)
            else:
                current = 0
        return maximum_area

    def longestOnes(self, A, K):
        left = 0
        maxLength = 0

        for right in range(len(A)):
            if A[right] == 0:
                if K >= 0:
                    K -= 1
                    while K < 0:
                        if A[left] ==0:
                            K +=1
                        left +=1
            maxLength = max(right-left+1, maxLength)
        return maxLength

        # current = 0
        # left = 0
        # max_ones = 0
        # for i,num in enumerate(nums):
        #     if num == 0:
        #         current +=1
        #         while current >= K:
        #             left +=1
        #             if nums[left] == 0:
        #                 current -=1
        #     else:
        #         max_ones = max(max_ones, )

A = [1,1,1,0,0,0,1,1,1,1,0]
K = 2
solution = Solution()
solution.longestOnes(A, K)