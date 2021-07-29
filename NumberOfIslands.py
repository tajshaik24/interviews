'''
LeetCode 200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numIslands = 0
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    numIslands += dfs(grid, row, col)
        return numIslands

def dfs(grid, row, col):
    if(row < 0 or row >= len(grid) or col < 0 or col >= len(grid[row]) or grid[row][col] == '0'):
        return 0
    grid[row][col] = '0'
    dfs(grid, row+1, col)
    dfs(grid, row-1, col)
    dfs(grid, row, col+1)
    dfs(grid, row, col-1)
    return 1
