'''
LeetCode 51. N-Queens

The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
'''
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def compatible(positions, curr_col, curr_row):
            for prev_row in range(curr_row):
                if positions[prev_row] == curr_col or curr_row - prev_row == abs(positions[prev_row] - curr_col):
                    return False
            return True

        def backtracking(answers, positions, row, n):
            if row == n:
                answers.append(['.' * p + 'Q' + '.' * (n-1-p) for p in positions])
                return answers
            for col in range(n):
                if compatible(positions, col, row):
                    positions.append(col)
                    backtracking(answers, positions, row+1, n)
                    positions.pop()

        answers, positions = [], []
        backtracking(answers, positions, 0, n)
        return answers
