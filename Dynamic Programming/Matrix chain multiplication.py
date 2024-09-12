# https://www.geeksforgeeks.org/problems/matrix-chain-multiplication0303/1

#MEMOIZATION (tc=n3, SC=n2+N(auxiliary stack space))
import sys

def matrix_chain_multiplication(arr, i, j, dp):
    # base condition
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    mini = sys.maxsize

    # partitioning loop
    for k in range(i, j):
        ans = (matrix_chain_multiplication(arr, i, k, dp) +
               matrix_chain_multiplication(arr, k+1, j, dp) +
               arr[i-1] * arr[k] * arr[j])

        mini = min(mini, ans)

    dp[i][j] = mini
    return mini


def matrix_multiplication(arr, N):
    dp = [[-1 for _ in range(N)] for _ in range(N)]

    i = 1
    j = N - 1

    return matrix_chain_multiplication(arr, i, j, dp)

arr = [10, 20, 30, 40, 50]
n = len(arr)
print("The minimum number of operations are",
        matrix_multiplication(arr, n))



#TABULATION  (tc=n3, SC=n2)
def matrix_multiplication(arr):
    N = len(arr)
    
    # Initialize a 2D dp list with -1 values
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    
    # Initialize the diagonal elements of the dp table to 0
    for i in range(N):
        dp[i][i] = 0
    
    # Loop through the dp table to calculate the minimum number of operations
    for i in range(N - 1, 0, -1):
        for j in range(i + 1, N):
            mini = float('inf')
            
            # Partitioning loop
            for k in range(i, j):
                ans = dp[i][k] + dp[k + 1][j] + arr[i - 1] * arr[k] * arr[j]
                mini = min(mini, ans)
            
            dp[i][j] = mini
    
    # The result is stored in the top-right corner of the dp table
    return dp[1][N - 1]

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]

    print("The minimum number of operations is:", matrix_multiplication(arr))