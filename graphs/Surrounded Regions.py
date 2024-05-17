#https://leetcode.com/problems/surrounded-regions/
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

