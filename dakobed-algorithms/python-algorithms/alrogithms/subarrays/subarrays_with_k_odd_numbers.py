"""
Given an array of integers nums and an integer k, return the number of subarrays such that there are k odd numbers
within it.

We follow the same approach as the problem of finding the number of subarrays whose sum is equal to k.  Instead of maintaining a cumulative sum we maintain a variable whose value is the number of of odds so far encountered.

Hash map keeps track of what exactly?
    keys -> nodds encountered
    values -> number of indices of the array nums which have this many nodds

Similarly as we traverse we search for entries of the hashmap that have a number of odds differing by k,
meaning that this value is the number of subarrays with k odds.


"""

from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums, k):
        cum_odds_map = defaultdict(int)
        cum_odds_map[0] = 1
        cum_odds = 0
        narrays = 0
        for num in nums:
            cum_odds += (1 if num % 2 == 1 else 0)
            cum_odds_map[cum_odds] +=1
            narrays += cum_odds_map[cum_odds - k]
        return narrays

solution = Solution()
nums = [1,1,1,1]#,2,1,1]
k = 3

solution.numberOfSubarrays(nums, k)