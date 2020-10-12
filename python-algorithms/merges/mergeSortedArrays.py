class Solution:
    def merge(self, nums1, m, nums2, n):
        index = m+n-1
        m -=1
        n -=1
        while m >= 0 and n >=0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                index -=1
                m -=1
            else:
                nums1[index] = nums2[n]
                index -=1
                n -=1
        while m >= 0:
            nums1[index] = nums1[m]
            index -=1
            m -=1
        while n >= 0:
            nums1[index] = nums2[n]
            index -=1
            n -=1

        # if m > 0 and n == 0:
        #     return
        #
        # if n > 0 and m == 0:
        #     nums1 = nums2
        #     return
        # i = m - 1
        # j = n - 1
        # pointer = len(nums1) - 1
        # while i >= 0 and j >= 0:
        #     if nums1[i] > nums2[j]:
        #         nums1[pointer] = nums1[i]
        #         i -= 1
        #     else:
        #         nums1[pointer] = nums2[j]
        #         j -= 1
        #     pointer -= 1
        # while i >= 0:
        #     nums1[pointer] = nums1[i]
        #     pointer -= 1
        #     i -= 1
        #
        # while j >= 0:
        #     nums1[pointer] = nums1[j]
        #     pointer -= 1
        #     j -= 1


solution = Solution()


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

solution.merge(nums1, m, nums2, n)