"""
LeetCode 130 Surrounded regions

All '0's on the board will be turned to 'X's except for thos that are in a contiguous region of '0's that borders the
edge.

Search the edges of the board for elemetns that are '0' and perform a DFS, setting them to an intermediary
character in the meantime




"""


class Solution:
    def solve(self, board):
        nRows = len(board)
        nCols = len(board[0])

        if nRows == 0 or nCols == 0 or nRows == 1 or nCols == 1:
            return
        for i in range(nRows):
            if board[i][0] == 'O':
                self.boundaryDFS(i, 0, board)
            if board[i][nCols - 1] == 'O':
                self.boundaryDFS(i, nCols - 1, board)
        for j in range(nCols):
            if board[0][j] == 'O':
                self.boundaryDFS(0, j, board)
            if board[nRows - 1][j] == 'O':
                self.boundaryDFS(nRows - 1, j, board)

        for i in range(len(board)):
            for j in range(len(board[1])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == '*':
                    board[i][j] = 'O'

    def boundaryDFS(self, i, j, board):
        if i < 0 or i > len(board) or j < 0 or j > len(board[0]):
            return

        directions = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        if board[i][j] == 'O':
            board[i][j] = "*"
        for dx, dy in directions:
            x = dx + i
            y = dy + j
            if 0 < x < len(board) and 0 < y < len(board[0]) and board[x][y] == 'O':
                self.boundaryDFS(x, y, board)



board = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X']]

solution = Solution()

print(board)
solution.solve(board)
print('after solve')
print(board)
