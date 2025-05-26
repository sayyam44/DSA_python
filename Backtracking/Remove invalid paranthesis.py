# updated new
# https://leetcode.com/problems/remove-invalid-parentheses/description/

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        
        res=[]
        #This function checks how many left and right brackets should be removed
        def rem(s: str) -> tuple:
            l,r=0,0 #l->"(",r->")"
            for i in s:
                if i == "(":
                    l+=1
                elif i == ")":
                    if l==0:
                        r+=1
                    else:
                        l-=1
            return l,r
        
        #This function checks whether the given string is valid or not
        #Sting's validity is checked only on closing bracket should not
        #come before an opening bracket
        def isvalid(s: str):
            cnt=0
            for i in s:
                if i == "(":
                    cnt+=1
                elif i==")":
                    cnt-=1
                if cnt<0:#this means a closing bracket has occured before an opening bracket
                    return False
            return True

        def dfs(s: str, start: int, l: int, r: int) -> None:
            if l==0 and r==0 and isvalid(s):
                res.append(s)
                return 
            for i in range(start,len(s)):
                if i>start and s[i]==s[i-1]: #we have encountered 2 same brackets
                    continue
                if r>0 and s[i]==")": #this shows we have some more closing brackets to remove and we have emncountered the closing bracket now
                    dfs(s[:i]+s[i+1:],i,l,r-1)
                if l>0 and s[i]=="(": #this shows we have some more opening brackets to remove and we have emncountered the opening bracket now
                    dfs(s[:i]+s[i+1:],i,l-1,r)
        
        l,r=rem(s)
        dfs(s,0,l,r)
        return res