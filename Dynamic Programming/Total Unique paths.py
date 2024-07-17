# https://www.codingninjas.com/codestudio/problems/total-unique-paths_1081470

#Recursive solution (TC= 2^m*n, SC= (m-1)+(n-1) (i.e path length) )

def f(i,j):
    if (i==0 and j==0):
        return 1
    if (i<0 or j <0):
        return 0
    
    up = f(i-1,j)
    left=f(i,j-1)

    return up+left 

def uniquePaths(m, n):
    return f(m-1,n-1)

#Memoization (tc=n*m, sc=(m-1)+(n-1)+(n*m))

def f(i,j,dp):
    if (i==0 and j==0):
        return 1
    if (i<0 or j <0):
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    up = f(i-1,j,dp)
    left=f(i,j-1,dp)

    return dp[i][j] == up+left 

def uniquePaths(m, n):
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    return f(m-1,n-1,dp)


#TABULATION (TC=N*M, SC=N*M)

def uniquePaths(m, n):
    dp = [[-1 for i in range(4)] for j in range(n)] #declaring the dp array of n*4 
    for i in range(m):
        for j in range(n):
            if i==0 and j==0:   #base case
                dp[i][j]=1
            else :
                up=0
                left=0
                if i>0:up=dp[i-1][j]
                elif j>0:left=dp[i][j-1]
                dp[i][j] = up+left

    return dp[n-1][m-1]

#OPTIMIZED(space) APPROACH (TC=N*M, SC=N)

def uniquePaths(m, n):
    prev= [0 for i in range(n)] #storing just the previous row 
    for i in range(n):
        curr = [0 for i in range(m)]   #storing just the current row 
        for j in range(m):
            if i==0 and j==0: curr[j]=1  #we are not using dp here instead we are using temp because current row is now temp
            else :
                up=0
                left=0
                if i>0:up=prev[j] # as dp[i-1] is the previous array
                elif j>0:left= curr[j-1]  #dp[i] is the current array
                curr[j] = up+left  #dp[i] is the current array
        prev= curr #now prev array becomes the current now
    return prev[n-1] # as dp[m-1] is prev now

