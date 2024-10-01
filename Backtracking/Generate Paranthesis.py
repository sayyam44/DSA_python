# https://leetcode.com/problems/generate-parentheses/
# ipad notes

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        
        def dfs(open_cnt,close_cnt,str_till_now):
            if open_cnt==n and close_cnt == n:
                res.append(str_till_now)
                return 
            if open_cnt<n:
                dfs(open_cnt+1,close_cnt,str_till_now+"(")
            if close_cnt<open_cnt:
                dfs(open_cnt,close_cnt+1,str_till_now+")")
            
        dfs(0,0,"")
        return res

                
                