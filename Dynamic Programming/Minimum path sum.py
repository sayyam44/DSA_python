# https://www.codingninjas.com/codestudio/problems/minimum-path-sum_985349
# https://leetcode.com/problems/minimum-path-sum/description/ 
#UPDATED
#Recursive solution (TC= 2^m*n, SC= (m-1)+(n-1) (i.e path length) )

def f(i,j,grid):
    if (i==0 and j==0):
        return grid[i][j]
    if (i<0 or j <0):
        return float('inf')
    
    up = grid[i][j]+f(i-1,j)
    left=grid[i][j]+f(i,j-1)

    return min(up+left) 

def minPathSum(grid):
    n=len(grid)
    m=len(grid[0])
    return f(m-1,n-1,grid)


#Memoization (tc=n*m, sc=(m-1)+(n-1)+(n*m))

def f(i,j,grid,dp):
    if (i==0 and j==0):
        return grid[i][j]
    if (i<0 or j <0):
        return float('inf')
    if dp[i][j] != -1:
        return dp[i][j]
    up = grid[i][j]+f(i-1,j,dp)
    left=grid[i][j]+f(i,j-1,dp)

    return dp[i][j]==min(up+left) 

def minPathSum(grid):
    n=len(grid)
    m=len(grid[0])
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    return f(m-1,n-1,grid,dp)


#TABULATION (TC=N*M, SC=N*M)

def minPathSum(grid):
    n=len(grid)
    m=len(grid[0])
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    for i in range(n):
        for j in range(m):
            if i==0 and j==0:
                dp[i][j]=grid[i][j]
            else:
                up=grid[i][j]
                if (i>0): up+=dp[i-1][j]
                else: up += float('inf')
                left = grid[i][j]
                if (j>0): left += dp[i][j-1]
                else: left += float('inf')

                dp[i][j]=min(up,left)
    return dp[n-1][m-1]


#OPTIMIZED(space) APPROACH (TC=N*M, SC=N)

def minPathSum(grid):
    n=len(grid)
    m=len(grid[0])
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    prev= [0 for i in range(n)] #storing just the previous row 
    for i in range(n):
        curr = [0 for i in range(m)]   #storing just the current row 
        for j in range(m):
            if i==0 and j==0:
                curr[j]=grid[i][j]
            else:
                up=grid[i][j]
                #requiring previous row's j column
                if (i>0): up+=prev[j]
                else: up += float('inf')
                left = grid[i][j]

                #current row's j-1 column
                if (j>0): left += curr[j-1]
                else: left += float('inf')

                curr[j]=min(up,left)
        prev=curr
    return prev[m-1]