from collections import defaultdict
import re


class Solution:
    def mostCommonWord(self, paragraph, banned):
        paragraph = re.sub(r'[^\w\s]', '', paragraph)
        words = paragraph.split(" ")
        words_frequency = defaultdict(int)
        maximum_seen = float('-inf')
        maximum_word = None

        for word in words:
            word = word.lower()
            words_frequency[word] += (1 if word not in banned else 0)
            if words_frequency[word] > maximum_seen:
                maximum_seen = words_frequency[word]
                maximum_word = word
        return maximum_word

paragraph = "Bob hit a ball, the hit BALL? It flew far after it was hit."
banned = ["hit"]

paragraph = "a, a, a, a, b,b,b,c, c"
delimiters = ",", ".", " "
regexPattern = '|'.join(map(re.escape, delimiters))
re.split(regexPattern, paragraph)



banned = ["a"]
solution = Solution()
solution.mostCommonWord(paragraph, banned)


import re
delimiters = ",", ".", ""
regexPattern = '|'.join(map(re.escape, delimiters))
re.split(regexPattern, paragraph)