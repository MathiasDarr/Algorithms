class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) ==0:
            return ''
        minLength = min([len(s) for s in strs ])
        result = ''
        for i in range(minLength):
            char = strs[0][i]
            if all([s[i] == char for s in strs]):
                result += char
            else:
                return result
        return result


strs = ["flower","flow","eloght"]
solution = Solution()
result = solution.longestCommonPrefix(strs)