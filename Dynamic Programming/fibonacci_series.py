# updated new 1
#Updated
#DP - MEMOIZATION METHOD
#TC=N,SC=N
# Initialize array of dp
dp = [-1 for i in range(10)]
 
def fib(n):
    if (n <= 1):
        return n;
    global dp;
     
    # Temporary variables to store
    # values of fib(n-1) & fib(n-2)
    first = 0;
    second = 0;
 
    if (dp[n - 1] != -1):
        first = dp[n - 1];
    else:
        first = fib(n - 1);
    if (dp[n - 2] != -1):
        second = dp[n - 2];
    else:
        second = fib(n - 2);
    dp[n] = first + second;
 
    # Memoization
    return dp[n] ;
 
if __name__ == '__main__':
    n = 9;
    print(fib(n));

#CASE 2
#DP - TABULAR METHOD
#TC=N,SC=N
def fibonacci(n):
    # Taking 1st two fibonacci numbers as 0 and 1
    dp = [0, 1] #INITIALIZING THE BASE CASES 
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2]) #writing the recursion relatrionship in DP format
    return dp[n]
print(fibonacci(9))

#CASE 0
#SIMPLE - recursive method
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    n = 9
    print(fibonacci(n))

#CASE 3 (Most efficient method for SC i.e. without using the array and following the pattern )
##TC=N,SC=1 
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b