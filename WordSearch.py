'''
LeetCode 79. Word Search

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == word[0] and dfs(word, 0, row, col, board):
                    return True
        return False

def dfs(word, index, row, col, board):
    if(index == len(word)):
        return True
    if(row < 0 or row >= len(board) or col < 0 or col >= len(board[row]) or board[row][col] != word[index]):
        return False
    temp = board[row][col]
    board[row][col] = ' '
    result = dfs(word, index + 1, row + 1, col, board) or dfs(word, index + 1, row - 1, col, board) or dfs(word, index + 1, row, col + 1, board) or dfs(word, index + 1, row, col - 1, board)
    board[row][col] = temp
    return result
