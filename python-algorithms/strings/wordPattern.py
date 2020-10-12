class Solution:
    def wordPattern(self, pattern, string):
        words = string.split(" ")
        if len(pattern) != len(words):
            return False
        forwardMapping = {}
        backwardMapping = {}
        for i in range(len(words)):
            word = words[i]
            letter = pattern[i]
            if letter not in forwardMapping:
                forwardMapping[letter] = word
                if word in backwardMapping:
                    return False
                backwardMapping[word] = letter
            elif letter in forwardMapping:
                    if forwardMapping[letter] != word or backwardMapping[word] != letter:
                        return False
        return True

pattern = "abc"
string = "dog cat dog"

solution = Solution()
solution.wordPattern(pattern, string )