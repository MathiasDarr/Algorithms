

class Solution:
    def wordBreak(self, s, wordDict):
        wordDict = set(wordDict)
        dp = [False for _ in range(len(s) +1)]
        dp[0] = True
        for length in range(1, len(s)+1):
            for i in range(0, length):
                if dp[i] and s[i:length] in wordDict:
                    dp[length] = True
                    break
        return dp[-1]
    # def wordBreak(self,s, wordDict):
    #     wordDict = set(wordDict)
    #     hashmap = {}
    #     return self.wordBreakRecursive(s, wordDict, hashmap)
    #
    #
    # def wordBreakRecursive(self, s, wordDict, hashmap):
    #     wordDict = set(wordDict)
    #     if s == '':
    #         return True
    #     if s in hashmap:
    #         return hashmap[s]
    #
    #     wordLen = len(s)
    #     dictionaryContainsWord = any([(s[:i] in wordDict) and self.wordBreak(s[i:], wordDict) for i in range(1, wordLen + 1)])
    #     hashmap[s] = dictionaryContainsWord
    #     return dictionaryContainsWord

            # def wordBreak(self, s, wordDict):
    #     strings = set(wordDict)
    #     return self.recursiveWB(s, strings)
    # def recursiveWB(self, s, strings):
    #     print("I get called with s  " + s)
    #     if len(s) == 0:
    #         return True
    #     for i in range(1, len(s)):
    #         if s[:i] in strings and self.recursiveWB(s[i:], strings):
    #             return True
    #     return False


# s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
# dictionary = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]


s = 'code'
dictionary = ['c', 'od', 'e', 'x']

solution = Solution()
solution.wordBreak(s, dictionary)