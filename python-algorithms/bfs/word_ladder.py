

class Solution:

    def ladderLength(self, beginWord, endWord, wordList):
        if beginWord == endWord:
            return 0
        wordSet = set(wordList)
        seenWords = {beginWord}
        queue = [beginWord]
        letters = 'abcdefghijklmnopqrstuvwxyz'

        level = 0
        while queue:
            word = queue.pop(0)
            if word == endWord:
                return level
            for j, char in enumerate(word):
                for l in letters:
                    if l == char:
                        continue
                    tempword = word[:j] + l + word[j+1:]
                    if tempword in wordSet:
                        print(tempword)
                        queue.append(tempword)
                        wordSet.remove(tempword)
                        # if tempword not in seenWords:
                        #     print(tempword)
                        #     seenWords.add(tempword)
                        #     queue.append((tempword, level+1))
            level +=1
        return 0
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
solution = Solution()
solution.ladderLength(beginWord, endWord, wordList)
