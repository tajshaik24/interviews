'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1
        matrix = [[0] * n for _ in range(n)]
        if matrix:
            count = 1
            r1, r2 = 0, len(matrix) - 1
            c1, c2 = 0, len(matrix[0]) - 1
            while r1 <= r2 and c1 <= c2:
                for r, c in spiral_coords(r1, c1, r2, c2):
                    matrix[r][c] = count
                    count += 1
                r1 += 1; r2 -= 1
                c1 += 1; c2 -= 1
        return matrix
