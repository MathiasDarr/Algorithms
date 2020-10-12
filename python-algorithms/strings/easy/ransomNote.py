from collections import Counter

class Solution:
    def canConstruct(self, ransomNote, magazine):
        rCounter = Counter(ransomNote)
        mCounter = Counter(magazine)
        for key, value in rCounter.items():
            if key not in mCounter or value > mCounter.get(key):
                return False
        return True


ransomNote = "aa"
magazine = "aab"
solution = Solution()
solution.canConstruct(ransomNote, magazine)