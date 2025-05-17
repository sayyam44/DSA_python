# https://leetcode.com/problems/n-queens/
# updated
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        neg_col=set() #r-c remains same while moving in downwards diagnol
        pos_col=set() #r+c remians same while moving in upwards direction
        res=[]

        board=[["."] * n for _ in range (n)]

        def dfs(r):
            if r==n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r+c) in pos_col or (r-c) in neg_col:
                    continue
                
                col.add(c)
                pos_col.add(r+c)
                neg_col.add(r-c)
                board[r][c]="Q"

                dfs(r+1)

                col.remove(c)
                pos_col.remove(r+c)
                neg_col.remove(r-c)
                board[r][c]="."
            
        dfs(0)
        return res


