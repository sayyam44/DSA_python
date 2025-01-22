# updated
# https://leetcode.com/problems/word-search/description/

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
        


            

            