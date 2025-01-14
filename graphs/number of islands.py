# updated
######### BFS APPROACH #############3
from typing import List
import collections

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        visit = set()
        isisland = 0

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visit.add((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # right, left, up, down
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r, new_c) not in visit):
                        q.append((new_r, new_c))
                        visit.add((new_r, new_c))

        rows, cols = len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    bfs(i, j)
                    isisland += 1

        return isisland

# Example usage:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
num_of_islands = solution.numIslands(grid)
print("Number of islands:", num_of_islands)


############# DFS APPROACH ################
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set()
        isisland = 0

        def dfs(r, c):
            if (r, c) in visit or r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
                return
            
            visit.add((r, c))
            dfs(r+1, c)  # down
            dfs(r-1, c)  # up
            dfs(r, c+1)  # right
            dfs(r, c-1)  # left

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visit:
                    dfs(i, j)
                    isisland += 1

        return isisland

# Example usage:
grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
solution = Solution()
num_of_islands = solution.numIslands(grid)
print("Number of islands:", num_of_islands)
