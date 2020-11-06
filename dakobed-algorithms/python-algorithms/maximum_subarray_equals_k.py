"""
Given an array of nums and a target value k, find the maximum length of a subarry that sums to k

As we traverse the array, maintain a cumulative sum variable.

    each iteration if the current_sum is not in the hash table, insert it with the current index as its value

    hash_table = { current_sum : index}

    If we encounter an index i s.t that the cumulative sum at index i - k is in the hash table,
        cumsum - k in hashtable.
            THen we have a found a subarray between the indicies hashmap[cumsum] and i that has sum k.

"""


class Solution:
    def maximum_subarray_equals_k(self, nums, k):
        if not nums or len(nums) == 0:
            return 0
        max_length_subarry = 0
        cumulative_sum = 0

        hashmap = {0: -1}
        for i in range(len(nums)):
            cumulative_sum += nums[i]
            if cumulative_sum - k in hashmap:
                max_length_subarry = max(max_length_subarry, i - hashmap[cumulative_sum - k])
            if cumulative_sum not in hashmap:
                hashmap[cumulative_sum] = i
        return max_length_subarry

solution = Solution()
nums = [1,-1,5,-2,3]
solution.maximum_subarray_equals_k(nums, 3)