# https://leetcode.com/problems/spiral-matrix/

#tc=m*n ,sc=1
class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        t,b=0,len(m) # for rows
        l,r=0,len(m[0]) # for columns
        res=[]
        
        while l<r and t<b:
            #iterating top row
            for i in range(l,r):
                res.append(m[t][i])
            t+=1
            
            #iterationg right column 
            for i in range(t,b):
                res.append(m[i][r-1])
            r-=1
            
            #if the given matrix is single column or single row matrix
            if not (l<r and t<b ):
                break
                
            #iterating bottom row
            for i in range(r-1,l-1,-1): 
                #r-1 as rth value is already added to result
                #l-1 = -1 as we need to add 0th value
                #-1 as we need to iterate backwards
                res.append(m[b-1][i])
            b-=1
            
            #iterating the left columns
            for i in range(b-1,t-1,-1):
                #b-1 as bth value is already added to result
                #t-1 = -1 as we need to add 0th value
                #-1 as we need to iterate backwards
                res.append(m[i][l])
            l+=1
        return res
            
            