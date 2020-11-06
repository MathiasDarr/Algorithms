from collections import Counter
class Solution:
    def intersect(self, nums1, nums2):
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        intersection = c1 & c2
        return intersection
nums1 = [1,2,2,1]
nums2 = [2,2]
solution = Solution()
intersection = solution.intersect(nums1, nums2)