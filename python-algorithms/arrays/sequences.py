class Solution:
    def longestConsecutive(self, nums):
        hashSet = set(nums)
        longest = 0

        for num in hashSet:
            print(num)
            if num -1 not in hashSet:
                current_number = num
                streak = 1
                while current_number +1 in hashSet:
                    streak+=1
                    current_number +=1
                longest = max(longest, streak)
        return longest

nums = [100,4,200,1,3,2]
solution = Solution()
solution.longestConsecutive(nums)
