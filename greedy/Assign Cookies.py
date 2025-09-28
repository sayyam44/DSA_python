# Updated new
# https://leetcode.com/problems/assign-cookies/

#tc=nlogn+mlogm+max(m,n)
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        #g[i]-> children i want minimum of g[i] cookies(greed factor of ith child)
        #s[i]-> the cookies count that we have 
        #any s[i] can be assigned to any particular g[i]
        #We need to go through from g[i] and and we need the minimum element in s[i]
        #that can satisfy g[i] i.e. we are acting greedily

        #we will sort both the lists and the number of children that can be 
        #satisfied will be equal to the right pointer index 

        n=len(g) #greed of children 
        m=len(s) #cookies we have
        l=0 #cookies
        r=0 #greed
        g.sort()
        s.sort()

        while (l<m and r<n):
            if (s[l]>=g[r]): #if the greed is satisfied with cookies
                r+=1 #then we have to move on satisfying greed of next element
            l+=1 #move l until we find some l satisfying greed 
        return r
