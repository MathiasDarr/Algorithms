class Solution:
    def increasingTriplet(self, nums):
        small = float('inf')
        big = float('inf')

        for n in nums:
            if n <= small:
                small = n
                print("small {} + big {}".format(small,big))

            elif n <= big:
                big = n
                print("small {} + big {}".format(small,big))

            else:
                print("small {} + big {}".format(small,big))
                return True
        return False
solution = Solution()
nums = [1,2,3]
solution.increasingTriplet(nums)