class Solution:
    def firstUniqChar(self,s):
        hashMap = {}
        for char in s:
            hashMap[char] = hashMap.get(char, 0) +1
        for i, char in enumerate(s):
            if hashMap[char] ==1:
                return i
        return -1



solution = Solution()
s = 'loveleetcode'
solution.firstUniqChar(s)