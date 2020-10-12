class Solution:
    def canPartition(self, nums, k, bucketSum, target, visited):
        if k ==0:
            return True
        elif bucketSum < 0:
            return False
        elif bucketSum ==0:
            return self.canPartition(nums, k-1,target, target, visited)
        else:
            for i in range(0, len(nums)):
                if i not in visited:
                    visited.add(i)
                    if self.canPartition(nums, k-1, target-nums[i], target, visited):
                        return True
                    visited.remove(i)
            return False

    def canPartitionKSubsets(self, nums, k):
        numsSum = sum(nums)

        if k<=0 or k > len(nums) or numsSum  % k != 0:
            return False
        nums = sorted(nums, reverse=True)
        target = numsSum/k
        return self.canPartition(nums, k, target, target, set())


nums = [4,3,2,3,5,2,1]
solution = Solution()
solution.canPartitionKSubsets(nums,4)