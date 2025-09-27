# Updated new
# https://leetcode.com/problems/word-search/description/
#This method is without using any extra scpace of visited set
#TC=n*m*dfs 
#dfs runs len(word) times everytime\
#and dfs is cased 4 times everytime 
#Therefore TC=n*m*4^n
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        directions=[[1,0],[0,1],[-1,0],[0,-1]]
        def dfs(row,col,ind):
            if ind==len(word):
                return True
            if row<0 or row>=len(board) or col<0 or col>=len(board[0]) or board[row][col]!=word[ind]:
                return False

            temp=board[row][col]
            board[row][col]="#"

            for r,c in directions:
                new_r,new_c=row+r,col+c
                if dfs(new_r,new_c,ind+1):
                    return True
            board[row][col]=temp
            return False

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col,0):
                    return True
        return False
        
        
#TC=n*m*dfs 
#dfs runs len(word) times everytime\
#and dfs is cased 4 times everytime 
#Therefore TC=n*m*4^n
# Space Complexity: O(L) (Depth of recursion stack + visited set)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS=len(board)
        COLS=len(board[0])
        visited=set()
        def dfs(i,j,k):
            if k==len(word):
                return True
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in visited or board[i][j] != word[k]: 
                return False
            visited.add((i,j))
            found=(dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1))
            visited.remove((i,j))
            return found


        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j]==word[0] and dfs(i,j,0):
                    return True
        return False




            

            