# https://leetcode.com/problems/climbing-stairs/description/
#updated
#same as fibonacci numbers
# Recursive function to find
# Nth fibonacci number (TC=2*N,SC=1)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)
 
# Returns no. of ways to
# reach sth stair
def countWays(s):
    return fib(s + 1)
 s = 4
print "Number of ways = ",
print countWays(s)


# MEMOIZATION METHOD (TC=N,SC=N)

def fib(n, dp):
 
    if (n <= 1):
        return 1
   
    if(dp[n] != -1 ):
        return dp[n]
 
    dp[n] = fib(n - 1, dp) + fib(n - 2, dp)
    return  dp[n]
 
# Returns number of ways to
# reach s'th stair
def countWays(n):
 
    dp = [-1 for i in range(n + 1)]
    fib(n, dp)
    return dp[n]

n = 4
 
print("Number of ways = " + str(countWays(n)))