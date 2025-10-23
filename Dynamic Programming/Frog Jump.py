# updated new 1
# https://www.codingninjas.com/codestudio/problem-details/frog-jump_3621012
#MEMOIZATION METHOD (tc=n,sc=n+n)
#updated
def f(ind,h,dp):
    if ind==0:
        return 0
    if dp[ind]!=-1:
        return dp[ind]
    left=f(ind-1,h,dp)+abs(h(ind)-h(ind-1))
    right=float('inf') #because right is not always going to be present
    if ind>1:
        right=f(ind-2,h,dp)+abs(h(ind)-h(ind-2))
    
    return dp[ind] == min(left,right) #step 2

def frogjump(n,h):
    dp=[-1 for i in range(n+1)] #step 1 of memoization
    return f(n-1,h,dp) #since the ans will be stored at the last i.e.(n-1) index
    #here in frogjump function is 1 based indexing but in fumc f it is 0 based 
    #indexing so that is why we did n-1

#TABULATION METHOD (tc=n,sc=n)

def frogjump_tab(n,heights):
    dp_tab=[0 for i in range(n)]
    dp_tab[0]=0
    for i in range(n-1):
        first=dp_tab[i-1]+abs(heights[i]-heights[i-1])
        second=float('inf')
        if (i>1):
            second=dp_tab[i-2]+abs(heights[i]-heights[i-2])
        
        dp_tab[i]=min(first,second)
    
    return dp_tab[n-1] ##since the ans will be stored at the last i.e.(n-1) index

#MOST OPTIMIZED SOLUTION BY USING VARIABLES (tc=1,sc=n)

def frog_jump(n,hei):
    prev,prev2=0,0
    for i in range(n-1):
        f=prev+abs(hei(i)-hei(i-1))
        s=float('inf')
        if i>1:
            s=prev2+abs(hei(i)-hei(i-2))

        curr=min(f,s)
        prev2=prev
        prev=curr
    return prev #since our ans will be stored in the (n-1)th value    