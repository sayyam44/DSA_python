# updated new 1
# https://leetcode.com/problems/coin-change/

# We are given an array Arr with N distinct coins and a target. 
# We have an infinite supply of each coin denomination. We need to 
# find the number of ways we sum up the coin values to give us the 
# target.

# RECURSION
def f(ind,target,coins): 
    if ind==0:
        return 1 if (target%coins[0]==0) else 0
    not_take=f(ind-1,target,coins)
    take=0
    if coins[ind]<=target:
        take=f(ind,target-coins[ind],coins)
    return not_take+take
def coinChange(coins, amount):
    return f(len(coins)-1,amount,coins)

arr = [1, 2, 3]
target = 4
print(coinChange(arr,target))


# MEMOIZATION
def f(ind,target,coins,dp): 
    if ind==0:
        return 1 if (target%coins[0]==0) else 0
    if dp[ind][target] != -1:
        return dp[ind][target]

    not_take=f(ind-1,target,coins,dp)
    take=0
    if coins[ind]<=target:
        take=f(ind,target-coins[ind],coins,dp)
    dp[ind][target] = not_take+take
    return dp[ind][target]

def coinChange(coins, amount):
    dp=[[-1 for _ in range(amount+1)] for _ in range(len(coins)) ]
    return f(len(coins)-1,amount,coins,dp)

arr = [1, 2, 3]
target = 4
print(coinChange(arr,target))

#TABULATION
def coinChange(coins, T ):
    dp=[[0 for j in range(T+1)] for i in range(len(coins)) ]
    for i in range(T + 1):
        if i % coins[0] == 0: #Since we are checking with all the possibilities of 
            #the target in the target matrix 
            #that means if any target in the dp matrix is divisible by 
            # #coins[0] then store dp[0][i] as 1
            dp[0][i] = 1
    for ind in range(1,len(coins)):
        for target in range(T+1):
            not_take= dp[ind-1][target]
            taken=0
            if coins[ind]<=target:
                taken=dp[ind][target-coins[ind]]
            dp[ind][target] = not_take + taken
    return dp[len(coins)-1][T]
arr = [1, 2, 3]
T = 4
print(coinChange(arr,T))