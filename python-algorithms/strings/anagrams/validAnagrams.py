class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        if sorted(s) != sorted(t):
            return False
        return True



solution = Solution()
s = "rat"
t = "car"
solution.isAnagram(s,t)