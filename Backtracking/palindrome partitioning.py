# https://leetcode.com/problems/palindrome-partitioning/

#TC=n(palindrome checking)*2^n(either we take an element or not)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        def dfs(ind):
            if ind==len(s):
                res.append(curr)
                return 
            for i in range(ind,len(s)):
                if ispalindrome(ind,i+1):
                    curr.append(s[ind:i+1])
                    dfs(ind+1)
                    curr.pop()
            dfs(0)
            return res

        def ispalindrome(s,i,ind):
            while i<=ind:
                if s[i]!=s[ind]:
                    return False
                i+=1
                ind-=1
            return True
