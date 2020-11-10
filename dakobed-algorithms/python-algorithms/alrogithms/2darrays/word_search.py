class Solution:
    def findWords(self, board, words):
        nRows = len(board)
        nCols = len(board[0])
        self.foundWords = set()
        diretions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        def dfs(index, windex, i, j, visited):
            if index == len(words[windex]):
                self.foundWords.add(words[windex])
                if len(self.foundWords) == len(words):
                    return True
                return False
            if i >= 0 and i < nRows and j >= 0 and j < nCols and (i, j) not in visited and board[i][j] == words[windex][index]:
                visited.add((i,j))
                for dx, dy in diretions:
                    if dfs(index +1, windex, i+dx, j+ dy, visited):
                        return True
                visited.remove((i,j))
            return False

        for i in range(nRows):
            for j in range(nCols):
                for windex, word in enumerate(words):
                    if board[i][j] == word[0] and word not in self.foundWords:
                        dfs(0, windex, i, j, set())

        return list(self.foundWords)

    def exist(self, board, word):
        diretions = [[0,1], [0,-1], [-1,0], [1,0]]
        nRows = len(board)
        nCols = len(board[0])

        def dfs(index,i, j, visited):
            if index == len(word):
                return True
            if i>= 0 and i < nRows and j >= 0 and j < nCols and (i,j) not in visited and board[i][j] == word[index]:
                visited.add((i,j))
                for dx, dy in diretions:
                    if dfs(index +1, i+dx, j+ dy, visited):
                        return True
                visited.remove((i,j))
            return False

        for i in range(nRows):
            for j in range(nCols):
                if board[i][j] == word[0]:
                    if dfs(0, i, j, set()):
                        return True
        return False

# board = [["A","B","C","E"],
#          ["S","F","C","S"],
#          ["A","D","E","E"]]

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

words = ["oath","pea","eat","rain"]
solution = Solution()
solution.findWords(board, words)