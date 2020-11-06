class Solution:
    def isSubsequence(self, s, t):
        if not s and not t:
            return True
        if not s and t:
            return True
        elif not t and s:
            return False
        s_index = 0
        for char in t:
            if char == s[s_index]:
                s_index +=1
                if s_index == len(s):
                    return True
        return False

s = "df"
t = ""
solution = Solution()
solution.isSubsequence(s, t)