# updated
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh, time = 0, 0
        rows, cols = len(grid), len(grid[0])
        q = deque()
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up
        
        while q and fresh > 0:
            for _ in range(len(q)):  # Process all oranges currently in the queue at the same time
                dr, dc = q.popleft()
                for m, n in directions:
                    r, c = dr + m, dc + n
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1

# Example usage:
grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
solution = Solution()
minutes = solution.orangesRotting(grid)
print("Minutes:", minutes)
