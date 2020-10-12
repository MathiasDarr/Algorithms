from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        string_dictionary = defaultdict(list)
        for string in strs:
            sortedString = "".join(sorted(string))
            string_dictionary[sortedString].append(string)

        return [value for value in string_dictionary.values()]

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
solution = Solution()
values = solution.groupAnagrams(strs)
