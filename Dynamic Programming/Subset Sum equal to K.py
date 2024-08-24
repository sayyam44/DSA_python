#https://www.naukri.com/code360/problems/subset-sum-equal-to-k_1550954
#Memoization 
def subsetSumUtil(ind, target, arr, dp):
    # Check if the target sum has been achieved.
    if target == 0:
        return True

    # If we have reached the first element in the array.
    if ind == 0:
        return arr[0] == target

    # Check if the result for this combination of 'ind' and 'target' has already been computed.
    if dp[ind][target] != -1:
        return dp[ind][target]

    # Recursively try not taking the current element.
    notTaken = subsetSumUtil(ind - 1, target, arr, dp)

    taken = False
    # Check if the current element can be taken without exceeding the target.
    if arr[ind] <= target:
        taken = subsetSumUtil(ind - 1, target - arr[ind], arr, dp)

    # Store the result in the dp array to avoid recomputation.
    dp[ind][target] = notTaken or taken #if either or taken or non taken is true then the output will also be true
    return dp[ind][target]

def subsetSumToK(n, k, arr):
    # Initialize a memoization table with -1.
    dp = [[-1 for j in range(k + 1)] for i in range(n)]

    # Call the utility function to find if a subset with the given target sum exists.
    return subsetSumUtil(n - 1, k, arr, dp)

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")

if __name__ == "__main__":
    main()


#Tabulation 
def subsetSumToK(n, k, arr):
    # Initialize a 2D DP table with False values.
    dp = [[False for j in range(k + 1)] for i in range(n)]
    
    # Set the first column to True since a sum of 0 is always possible with an empty subset.
    for i in range(n):
        dp[i][0] = True
    
    # Check if the first element of the array can be used to make the target sum.
    if arr[0] <= k:
        dp[0][arr[0]] = True
    
    # Fill in the DP table iteratively.
    for ind in range(1, n):
        for target in range(1, k + 1):
            notTaken = dp[ind - 1][target]  # Not taking the current element.
            taken = False
            # Check if taking the current element is possible without exceeding the target.
            if arr[ind] <= target:
                taken = dp[ind - 1][target - arr[ind]]
            dp[ind][target] = notTaken or taken  # Update the DP table with the result.
    
    # The final result is stored in the bottom-right cell of the DP table.
    return dp[n - 1][k]

def main():
    arr = [1, 2, 3, 4]
    k = 4
    n = len(arr)

    if subsetSumToK(n, k, arr):
        print("Subset with the given target found")
    else:
        print("Subset with the given target not found")

if __name__ == '__main__':
    main()

