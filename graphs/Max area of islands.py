# Updated new
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
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited=set()
        max_area=0
        def bfs(i,j):
            visited.add((i,j))
            q=deque()
            q.append((i,j))
            area=1
            while q:
                r,c=q.popleft()
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for a,b in directions:
                    new_r,new_c=r+a,c+b
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c]==1 and (new_r,new_c) not in visited:
                        area+=1
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
            return area 
                

        for i in range(rows):
            for j in range(cols):
                if (i,j) not in visited and grid[i][j]==1:
                    max_area=max(max_area,bfs(i,j))
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
