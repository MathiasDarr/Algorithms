from collections import defaultdict, deque
class Trie:
    class TrieNode(defaultdict):
        def __init__(self):
            super().__init__(Trie.TrieNode)
            self.eow = False

    def __init__(self):
        self.root = Trie.TrieNode()
        self.root.eow = True
    def insert(self, word):
        node = self.root
        for char in word:
            node = node[char]
        node.eow = True
class Solution:
    def longestWord(self, words):
        words = sorted(words)
        wordset = set()
        result = ''
        for word in words:
            wordLength = len(word)
            if wordLength ==1 or word[:wordLength-1] in wordset:
                if len(word) > len(result):
                    result = word
                wordset.add(word)
        return result

words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
solution = Solution()
solution.longestWord(words)