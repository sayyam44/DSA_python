# https://leetcode.com/problems/word-search/description/

#TC=n*m*dfs 
#dfs runs len(word) times everytime\
#and dfs is cased 4 times everytime 
#Therefore TC=n*m*4^n
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS,COLS=len(board),len(board[0])
        path=set()
        
        def dfs(r,c,i): #i is what index of the given word we have already found
            if i==len(word):
                return True
            if (r<0 or c<0 or r>=ROWS or c>=COLS or board[r][c]!=word[i] or 
            (r,c) in path):
                return False
            
            path.add((r,c))
            res=(dfs(r+1,c,i+1) or 
            dfs(r,c+1,i+1) or 
            dfs(r-1,c,i+1) or 
            dfs(r,c-1,i+1))
            path.remove((r,c))
            return res 
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):return True 
        return False
        


            