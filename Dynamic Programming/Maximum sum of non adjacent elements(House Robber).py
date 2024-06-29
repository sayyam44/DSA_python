# https://www.codingninjas.com/codestudio/problems/maximum-sum-of-non-adjacent-elements_843261
# https://leetcode.com/problems/house-robber/

#Normal recursive method (tc=2^n,sc=n)
def f(ind,nums):
    if (ind==0): return nums[ind]
    if (ind<0): return 0

    pick = nums[ind]+f(ind-2,nums)
    not_pick = 0 + f(ind-1,nums)

    return max(pick,not_pick) 

def maximumNonAdjacentSum(nums):  
    n=len(nums)
    return f(n-1,nums) #since the maximum sum will be stored on last index i.e. n-1

#Memoization method (TC= N, SC=n+n)
def f(ind,nums,dp):
    if (ind==0): return nums[ind]
    if (ind<0): return 0
    if dp[ind]!=-1:return dp[ind]
    pick = nums[ind]+f(ind-2,nums,dp)
    not_pick = 0 + f(ind-1,nums,dp)

    return dp[ind]==max(pick,not_pick) #initializing in dp array of whatever value of dp array is completed

def maximumNonAdjacentSum(nums):  
    n=len(nums)
    dp = [-1 for i in range(n + 1)]
    return f(n-1,nums,dp) #since the maximum sum will be stored on last index i.e. n-1

#Tabulation (tc=n,sc=n)
def maximumNonAdjacentSum(nums):
    n=len(nums)
    dp=[0 for i in range(n)]
    dp[0]=nums[0]
    neg=0
    for i in range(1,n):
        take=nums[i]
        if i>1:
            take+=dp[i-2]
        not_take=0+dp[i-1]
        dp[i]=max(take,not_take)

    return dp[n-1]


#Space optimized approach (tc=n,sc=1)
def maximumNonAdjacentSum(nums):
    n=len(nums)
    prev=nums[0]
    prev2=0
    for i in range(1,n):
        take=nums[i]
        if i>1:
            take+=prev2
        not_take=0+prev

        curri=max(take,not_take)
        prev2=prev
        prev=curri
    return prev
