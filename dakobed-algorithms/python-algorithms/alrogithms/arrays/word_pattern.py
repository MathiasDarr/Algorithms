class Solution:
    def wordPattern(self, pattern, s):
        words = s.split()

        if len(pattern) != len(words):
            return False
        map_index = {}

        backward_mapping = {}
        forward_mapping = {}

        for i in range(len(words)):
            word = words[i]
            letter = pattern[i]
            if letter not in forward_mapping:
                forward_mapping[letter] = word
                if word in backward_mapping:
                    return False
                backward_mapping[word] = letter
            else:
                if forward_mapping[letter] != word or backward_mapping[word] != letter:
                    return False
        return True



pattern = "aaaa"
s = "dog cat cat dog"

solution = Solution()

solution.wordPattern(pattern, s)