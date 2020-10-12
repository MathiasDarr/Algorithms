from collections import defaultdict
class Solution:
    def numMatchingSubseq(self, S, words):
        count = 0
        hashMap = defaultdict(list)
        for word in words:
            hashMap[word[0]].append(word)
        for char in S:
            temp = hashMap[char]
            del hashMap[char]
            for word in temp:
                if len(word) ==1:
                    count +=1
                    continue
                hashMap[word[1]].append(word[1:])
        return count
    # def numMatchingSubseq(self, S, words):
    #     pointers = [0] * len(words)
    #
    #     completedWords = set()
    #     for i in range(len(S)):
    #         for k in range(len(words)):
    #             if k not in completedWords:
    #                 if S[i] == words[k][pointers[k]]:
    #                     pointers[k] +=1
    #                     if pointers[k] == len(words[k]):
    #                         completedWords.add(k)
    #
    #     return len(completedWords)

    def isSubsequence(self, s, t):
        sPointer = 0
        tPointer = 0

        if len(s) > len(t):
            return False

        while sPointer < len(s) and tPointer < len(t):
            if s[sPointer] == t[tPointer]:
                sPointer +=1
                if sPointer == len(s):
                    return True
            tPointer +=1
        return False


S = "abcde"
words = ["a", "bb", "acd", "ace"]
solution = Solution()
solution.numMatchingSubseq(S, words)