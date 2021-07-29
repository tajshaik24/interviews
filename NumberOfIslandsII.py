'''
LeetCode 305. Number of Islands II

A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Follow up:
Can you do it in time complexity O(k log mn), where k is the length of the positions?
(Uses Union Find Solution)
'''
class Solution:
  def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
      uf = dict()
      def hash(i, j):
          return i * (m*n) + j
      def union(i, j):
          uf[find(i)] = find(j)
      def find(i):
          if uf.get(i, i) != i:
              uf[i] = find(uf.get(i, i))
          return uf.get(i, i)
      ans = []
      added = set()
      islands = set()
      for i, j in positions:
          if (i, j) in added:
              ans.append(ans[-1])
              continue
          added.add((i, j))
          for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
              if ni < m and ni >= 0 and nj >= 0 and nj < n and (ni, nj) in added:
                  islands.discard(find(hash(ni, nj)))
                  union(hash(ni, nj), hash(i, j))
          islands.add(hash(i, j))
          ans.append(len(islands))
      return ans
