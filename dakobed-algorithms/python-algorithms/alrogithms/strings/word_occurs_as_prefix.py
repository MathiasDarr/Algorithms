class Solution:
    def isPrefixOfWord(self, sentence, searchWord):
        words = sentence.split(" ")
        for i, word in enumerate(words):
            if word.find(searchWord) == 0:
                return i + 1
        return -1

solution = Solution()
sentence = "i am tired"
searchWord = "you"



sentence = "hello from the other side"
searchWord = "sid"
solution.isPrefixOfWord(sentence, searchWord)