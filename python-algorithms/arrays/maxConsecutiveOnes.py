class Solution:
    def findMaxConsecutiveOnes(self, nums):
        number = []
        while head:
            number.append(head.val)
            head = head.next
        return sum([(2 ** i) for i in range(len(number[::-1])) if number[i] == 1])




nums = [1,1,0,1,1,1]
solution = Solution()
solution.findMaxConsecutiveOnes(nums)

