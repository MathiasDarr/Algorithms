class Solution:
    def characterReplacement(self,s, k):
        left = 0
        maxLength = 0
        charCounts = [0] * 26
        max_count = 0
        for index in range(len(s)):
            charCounts[ord(s[index]) -ord('A')] += 1
            current_char_count = charCounts[ord(s[index]) - ord('A')]
            max_count = max(max_count, current_char_count)

            while index - left - max_count +1 > k:
                charCounts[ord(s[left]) - ord('A')] -=1
                left +=1
            maxLength = max(maxLength, index-left+1)
        return maxLength


solution = Solution()
s = 'ABABC'
solution.characterReplacement(s, 2)