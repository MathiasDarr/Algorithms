class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        left = 0
        character_index_map = {}
        for i, char in enumerate(s):
            if char not in character_index_map: # or (char in character_index_map and character_index_map[char] < left):
                character_index_map[char] = i
            elif char in character_index_map and character_index_map[char] < left:
                character_index_map[char] = i
            else:
                left = character_index_map[char] +1
            print("left " + str(left))
            print("i " + str(i))
            print(character_index_map)
            maxLength = max(maxLength, i-left)
        return maxLength

solution = Solution()
s = 'bbbbb'
print("longest substring without repeating characters is " + str(solution.lengthOfLongestSubstring(s)))