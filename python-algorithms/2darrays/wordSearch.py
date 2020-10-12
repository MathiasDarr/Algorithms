class Solution:
    def exist(self, board, word):
        directions = [[0, 1], [-1, 0], [1, 0], [0, -1]]

        def dfs(index, i, j, visited):
            if index == len(word):
                return True
            if i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and (i, j) not in visited and board[i][j] == \
                    word[index]:
                visited.add((i, j))
                for dx, dy in directions:
                    if dfs(index + 1, i + dx, j + dy, visited):
                        return True

                visited.remove((i, j))
            else:
                return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited = {(i, j)}
                    for dx, dy in directions:
                        if dfs(1, i + dx, j + dy, visited):
                            return True
        return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

solution = Solution()
solution.exist(board, 'SEEC')
