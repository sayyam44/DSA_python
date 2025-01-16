# updated
# https://leetcode.com/problems/surrounded-regions/
# BFS Approach
import collections
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            visited = set()
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            is_surrounded = True  # Assume the region is surrounded unless proven otherwise

            while q:
                a, b = q.popleft()
                
                # Check if the current cell is on the boundary
                if a == 0 or a == rows - 1 or b == 0 or b == cols - 1:
                    is_surrounded = False  # Mark as not surrounded if a boundary is reached

                for i, j in directions:
                    new_r, new_c = a + i, b + j
                    # Explore neighbors that are within bounds, unvisited, and "O"
                    if 0 <= new_r < rows and 0 <= new_c < cols and board[new_r][new_c] == "O" and (new_r, new_c) not in visited:
                        q.append((new_r, new_c))
                        visited.add((new_r, new_c))

            # Update the board if the region is surrounded
            if is_surrounded:
                for i, j in visited:
                    board[i][j] = "X"

        # Main loop to start BFS from each "O"
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    bfs(r, c)
        return board
    
# dfs(more easy)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #we will capture everything except the unsurrounded region eg:the collection of zeroes lying on the border 
        #we will be moving on the border and we will find if any collection of zeroes that lies on border using dfs and will mark all thes zeroes as 'T'
        #then do double nested loop to change the  remaining zeroes other than "T" will be converted to x as required 
        #dfs
        
        def dfs(r, c):
            if (r < 0 or c < 0 or r == ROWS or c == COLS 
                or board[r][c] != "O"):
                return
            board[r][c] = "T"
            dfs(r + 1, c) #now checking in all directions i.e. finding a collection of 0's on border
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        ROWS, COLS = len(board), len(board[0])
        # 1. (DFS) Capture unsurrounded regions (O -> T)
        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == "O" and
                    (r in [0, ROWS - 1] or c in [0, COLS - 1])): #here we are checking the border zeroes only
                    dfs(r, c)
        
        # 2. Capture surrounded regions (O -> X)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
                    
        # 3. Uncapture unsurrounded regions (T -> O)
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"

