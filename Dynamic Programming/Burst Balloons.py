# https://leetcode.com/problems/burst-balloons/

#MEMOIZATION
class Solution(object):
    def f(self, i, j, dp, arr, n):  # Add self here
        if i > j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        maxi = float('-inf')
        for ind in range(i, j + 1):
            coins = (arr[i-1] * arr[ind] * arr[j+1]) + self.f(i, ind-1, dp, arr, n) + self.f(ind+1, j, dp, arr, n)
            maxi = max(maxi, coins)
        dp[i][j] = maxi
        return maxi
    
    def maxCoins(self, nums):
        n = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        dp = [[-1 for _ in range(n+2)] for _ in range(n+2)]
        return self.f(1, n, dp, nums, n)


#TABULATION
class Solution(object):
    def maxCoins(self, nums):
        n = len(nums)
        nums.insert(0, 1)  # Add boundary balloon with value 1
        nums.append(1)     # Add boundary balloon with value 1
        dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)]  # DP table initialized with 0

        for i in range(n, 0, -1):  # Loop in reverse for the left index
            for j in range(1, n + 1):  # Loop for the right index
                if i > j:  # Skip invalid subproblems where left index is greater than right
                    continue
                maxi = float('-inf')  # Initialize maxi as negative infinity to find max
                for ind in range(i, j + 1):  # Loop over each balloon as the last to burst
                    cost = nums[i - 1] * nums[ind] * nums[j + 1] + dp[i][ind - 1] + dp[ind + 1][j]
                    maxi = max(maxi, cost)  # Find the maximum coins
                dp[i][j] = maxi  # Store the result in the DP table

        return dp[1][n]  # The answer for bursting all balloons is stored here
