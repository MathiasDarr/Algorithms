class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = {}
        self.endhere = False

class Trie:
    def __init__(self):
        self.root = TreeNode(None)
    def insert(self, word):
        traversal = self.root
        for i, char in enumerate(word):
            if char not in traversal.children:
                traversal.children[char] = TreeNode(char)
            traversal = traversal.children[char]
            if i == len(word)-1:
                traversal.endhere = True

    def search(self, word):
        traversal = self.root
        for char in word:
            if char not in traversal.children:
                return False
            traversal = traversal.children[char]
        return traversal.endhere

    def startsWith(self, prefix):
        traversal = self.root
        for char in prefix:
            if char not in traversal.children:
                return False
            traversal = traversal.children[char]
        return True

trie = Trie()
trie.insert("apple")
trie.search("app")