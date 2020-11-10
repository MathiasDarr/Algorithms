from collections import Counter
import string
class Solution:
    def sortString(self, s):
        counter = Counter(s)
        result = []
        ascending = True
        while counter:
            for char in sorted(counter.keys()) if ascending else reversed(sorted(counter.keys())):
                result.append(char)
                counter[char] -= 1
                if counter[char] == 0:
                    del counter[char]
            ascending = not ascending
        return ''.join(result)

s = "aaaabbbbcccc"
solution = Solution()
solution.sortString(s)

