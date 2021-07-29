'''
LeetCode 212. Word Search II

Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
'''
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for s in word:
            if s not in curr.children:
                curr.children[s] = TrieNode()
            curr = curr.children[s]
        curr.is_word = True

    def searchWord(self, word):
        curr = self.root
        for s in word:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return curr.is_word

    def searchPrefix(self, prefix):
        curr = self.root
        for s in prefix:
            if s not in curr.children:
                return False
            curr = curr.children[s]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if(len(board) == 0):
            return []
        rows, cols = len(board), len(board[0])
        seen, wordsFound = set(), set()

        trie = Trie()
        for word in words:
            trie.addWord(word)

        def dfs(prefix, row, col):
            seen.add((row,col))
            if trie.searchWord(prefix):
                wordsFound.add(prefix)
            nxt_points = {(row+1,col),(row-1,col),(row,col+1),(row,col-1)}
            for next_row, next_col in nxt_points:
                if 0 <= next_row < rows and 0 <= next_col < cols and trie.searchPrefix(prefix + board[next_row][next_col]) and (next_row,next_col) not in seen:
                    dfs(prefix + board[next_row][next_col], next_row, next_col)
            seen.remove((row,col))

        for row in range(rows):
            for col in range(cols):
                if trie.searchPrefix(board[row][col]):
                    dfs(board[row][col], row, col)
        return list(wordsFound)
