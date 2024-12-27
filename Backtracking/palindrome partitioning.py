# updated
# https://leetcode.com/problems/palindrome-partitioning/

#TC=n(palindrome checking)*2^n(either we take an element or not)

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        curr=[]
        def dfs(start): #ind->prev ind
            if start == len(s):
                res.append(curr[:])
                return 
            for end in range(start,len(s)):
                if ispalin(start,end):
                    curr.append(s[start:end+1])
                    dfs(end+1)
                    curr.pop()
            return res
            
        def ispalin(i,j):
            while i<j:         
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        return dfs(0)