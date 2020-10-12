from collections import Counter

class Solution:
    def isPossibleDivide(self, nums, k):
        if len(nums) % k != 0:
            return False
        counts = Counter(nums)

        roots = []
        for num in nums:
            if counts[num-1] == 0:
                roots.append(num)

        while len(roots) > 0:
            r = roots.pop()
            if counts.get(r, 0) == 0:
                continue
            # visit every number in r..r+k
            for i in range(r, r+k+1):
                if i < r+k:
                    if counts.get(i,0) ==0:
                        return False
                    counts[i]-=1
                ##
                if counts.get(i, 0) > 0 and counts.get(i-1,0 ) ==0:
                    roots.append(i)
        return True
# nums = [1,2,3,3,4,4,5,6]
nums = [20,3,2,2,1,1]
k = 3

solution = Solution()
solution.isPossibleDivide(nums, k)