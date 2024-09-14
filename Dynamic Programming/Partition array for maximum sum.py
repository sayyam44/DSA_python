# https://leetcode.com/problems/partition-array-for-maximum-sum/

#MEMOIZATION TC:O(N*k)-> Reason: There are a total of N states and for each state, we are running a loop from 0 to k.
#SC: O(N) + Auxiliary stack space O(N)

class Solution(object):
    def f(self, ind, dp, arr, k, n):
        if ind == n:  # if we reach the end of the array
            return 0
        if dp[ind] != -1:
            return dp[ind]
        
        max_val = float('-inf')
        max_ans = float('-inf')
        len_val = 0  # Initialize len_val before the loop
        
        # We are starting from ind=0
        # We need to move in the window of ind till ind+k or in case we have reached the end of the array, then j will be till n
        for j in range(ind, min(ind + k, n)):
            len_val += 1  # To track the length of the window we are taking
            max_val = max(max_val, arr[j])  # Finding the max value in the window
            summation = len_val * max_val + self.f(j + 1, dp, arr, k, n)  # Finding the summation of the window by len_val * max_val
            max_ans = max(max_ans, summation)  # Updating max_ans
        
        dp[ind] = max_ans  # Memoize the result
        return dp[ind]

    def maxSumAfterPartitioning(self, arr, k):
        n = len(arr)
        dp = [-1] * n  # Initialize the dp array with -1
        return self.f(0, dp, arr, k, n)

#Tabulation (TC=O(N*k),SC=O(N))
def max_sum_after_partitioning(num, k):
    n = len(num)
    dp = [0] * (n + 1)

    for ind in range(n - 1, -1, -1):
        len_val = 0
        max_val = float('-inf')
        max_ans = float('-inf')

        for j in range(ind, min(ind + k, n)):
            len_val += 1
            max_val = max(max_val, num[j])
            summation = len_val * max_val + dp[j + 1]
            max_ans = max(max_ans, summation)

        dp[ind] = max_ans

    return dp[0]

if __name__ == "__main__":
    num = [1, 15, 7, 9, 2, 5, 10]
    k = 3
    max_sum = max_sum_after_partitioning(num, k)
    print("The maximum sum is:", max_sum)


