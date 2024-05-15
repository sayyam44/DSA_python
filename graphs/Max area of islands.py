############## DFS APPROACH ##############33
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1))
                
        max_area = 0
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area, dfs(i, j))
        return max_area

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
solution = Solution()
max_area_of_island = solution.maxAreaOfIsland(grid)
print("Max area of island:", max_area_of_island)


########### BFS APPROACH #################
from typing import List
from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        max_area = 0
        
        def bfs(r, c):
            if r < 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or (r, c) in visit:
                return 0
            visit.add((r, c))
            queue = deque([(r, c)])
            area = 0
            while queue:
                row, col = queue.popleft()
                area += 1
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions:
                    new_r, new_c = row + dr, col + dc
                    if (0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == 1 and (new_r, new_c) not in visit):
                        visit.add((new_r, new_c))
                        queue.append((new_r, new_c))
            return area
                
        for i in range(rows):
            for j in range(cols):
                max_area = max(max_area, bfs(i, j))
        
        return max_area

grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
solution = Solution()
max_area_of_island = solution.maxAreaOfIsland(grid)
print("Max area of island (BFS):", max_area_of_island)
