"""

LeetCode 1247 Minimum Swaps to Make Strings Equal

You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make
these two strings equal to each other. You can swap any two characters that belong to different strings, which means:
swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

s1 = "xx"
s2 = "yy"

## Travere the two strings, taking note of the places where they are not the same
    - Variables x_count is the number of times x occurs in s1 at an index where 'y' is present in s2
        - similar y_count variable

    If the x_count + y_count is an odd number, than we cannot get equal strings


        # counter = Counter(zip(s1, s2))
        # # Count the number of times we see a 'x' in s1 & 'y' s2 at the same index
        # xs1_ys2 = counter['x','y']
        # # Count the number of times we see a 'y' in s1 & 'x' s2 at the same index
        # ys1_xs2 = counter['y','x']
        # x, m = divmod(counter['x', 'y'], 2)
        #
        #
        # y, n = divmod(counter['y', 'x'], 2)
        # return (x + y, -1, x + y + 2)[m + n]


"""
from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:

        xs1_ys2 = 0
        ys1_xs2 = 0

        # Count the number of times we see a 'x' in s1 & 'y' s2 at the same index
        # Count the number of times we see a 'y' in s1 & 'x' s2 at the same index

        for s1c, s2c in zip(s1, s2):
            if s1c != s2c:
                if s1c == 'x':
                    xs1_ys2 +=1
                else:
                    ys1_xs2 +=1

        ## If the sum of the counts is odd return -1, we need a pair
        ## xs1_ys2/2 +  ys1_xs2/2

        if (xs1_ys2 + ys1_xs2) % 2 == 1:
            return -1

        ## The counts will either both be even or both be odd
        ## If the count is odd, then there will be two swaps necessary
        return xs1_ys2//2 + ys1_xs2//2 + (2 if xs1_ys2 % 2 == 1 else 0)


s1 = "xxyyxyxyxx"
s2 = "xyyxyxxxyx"

solution = Solution()
solution.minimumSwap(s1, s2)