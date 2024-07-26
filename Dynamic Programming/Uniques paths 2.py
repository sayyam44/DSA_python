# https://www.codingninjas.com/codestudio/problems/maze-obstacles_977241
# https://leetcode.com/problems/unique-paths-ii/
#Recursive solution (TC= 2^m*n, SC= (m-1)+(n-1) (i.e path length) )

# adding one more base case rest all code is same as total unique paths
def f(i,j,mat):
    if (i>=0 and j>=0 and mat[i][j]==-1): #just checking if there is any obstacle(dead cell) then do not include that step
        return 0

    if (i==0 and j==0): 
        return 1
    if (i<0 or j <0):
        return 0
    
    up = f(i-1,j)
    left=f(i,j-1)

    return up+left 

def uniquePaths(m, n,mat):
    return f(m-1,n-1,mat)


#Memoization (tc=n*m, sc=(m-1)+(n-1)+(n*m))

def f(i,j,dp,mat):
    if (i>=0 and j>=0 and mat[i][j]==-1): #just checking if there is any obstacle(dead cell) then do not include that step
        return 0

    if (i==0 and j==0):
        return 1
    if (i<0 or j <0):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = f(i-1,j,dp)
    left=f(i,j-1,dp)

    return dp[i][j] == up+left 

def uniquePaths(m, n,mat):
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    return f(m-1,n-1,dp,mat)

#TABULATION (TC=N*M, SC=N*M)

def uniquePaths(m, n,mat):
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    for i in range(m):
        for j in range(n):
            if mat[i][j]==-1:#just checking if there is any obstacle(dead cell) then do not include that step
                dp[i][j] = 0

            elif i==0 and j==0:   #base case
                dp[i][j]=1
            else :
                up=0
                left=0
                if i>0:up=dp[i-1][j]
                elif j>0:left=dp[i][j-1]
                dp[i][j] = up+left

    return dp[n-1][m-1]


#OPTIMIZED(space) APPROACH (TC=N*M, SC=N)

def uniquePaths(m, n,mat):
    prev= [0 for i in range(n)] #storing just the previous row 
    for i in range(n):
        curr = [0 for i in range(m)]   #storing just the current row 
        for j in range(m):
            if mat[i][j]==-1 : curr[j]=0#just checking if there is any obstacle(dead cell) then do not include that step
            if i==0 and j==0: curr[j]=1  #we are not using dp here instead we are using curr because current row is now curr
            else :
                up=0
                left=0
                if i>0:up=prev[j] # as dp[i-1] is the previous array
                elif j>0:left= curr[j-1]  #dp[i] is the current array
                curr[j] = up+left  #dp[i] is the current array
        prev= curr #now prev array becomes the current now
    return prev[n-1] # as dp[m-1] is prev now