# https://www.naukri.com/code360/problems/0-1-knapsack_920542
# A thief wants to rob a store. He is carrying a bag of capacity W. The store has ‘n’ 
# items. Its weight is given by the ‘wt’ array and its value by the ‘val’ array. He can 
# either include an item in its knapsack or exclude it but can’t partially have it as a 
# fraction. We need to find the maximum value of items that the thief can steal.

#RECURSION (TC = 2^N , SC=N)
def f(ind,W,wei,price): #Till ind index what is the maximum price thief can carry
    #where the target weight that needed to be achieved is W
    #since we are starting from n-1 till 0 , so we will write the base cases on the basis of 0
    if ind==0: #f(0,W) shows till index 0 what will be the max price the thief can carry
        if (wei[ind]<=W): # now thief have reached to index 0 where the weight of that 
            # element is smaller than the target value then yes the thief can steal that item 
            return price[0]
        return 0 #else the thief cannot steal it
    not_pick = 0 + f(ind-1,W,wei,price)
    pick=float('-inf') #since in begin we are assuming we did not take it 
    if wei[ind]<=W:
        pick=price[ind]+f(ind-1,W-wei[ind],wei,price)
    return max(not_pick,pick)

def thief(wei,price,Weight_of_sack):
    return f((len(wei))-1,Weight_of_sack,wei,price)

wt = [1, 2, 4, 5]
price = [5, 4, 8, 6]
W = 5
print(thief(wt,price,W))


#MEMOIZATION (TC = NXW, SC=NXW + N)
def f(ind,W,wei,price,dp): 
    if ind==0: 
        if (wei[ind]<=W):
            return price[0]
        return 0 
    if dp[ind][W] !=-1:
        return dp[ind][W]
    not_pick = 0 + f(ind-1,W,wei,price,dp)
    pick=float('-inf') 
    if wei[ind]<=W:
        pick=price[ind]+f(ind-1,W-wei[ind],wei,price,dp)
    dp[ind][W]= max(not_pick,pick)
    return dp[ind][W]

def thief(wei,price,Weight_of_sack):
    # Initialize a 2D DP array to store the maximum value for different capacities and items.
    #Dp array stores the values of all the possibilities
    # Create a dp array of size [n][W+1]. 
    # n rows because we only had n items 
    # columns specifies the possible capacities of knapsack 
    # Possible capacities of the knapsack can be from 0 t0 W therefore we took number of columns as W+1
    #Columns -> target+1 
    #rows -> len(array)+1
    dp = [[-1 for j in range(Weight_of_sack + 1)] for i in range(len(wei))]
    return f((len(wei))-1,Weight_of_sack,wei,price,dp)

wt = [1, 2, 4, 5]
price = [5, 4, 8, 6]
W = 5
print(thief(wt,price,W))

#TABULATION

import sys
def knapsack(wt, val, n, W):
    # Initialize a 2D DP array to store the maximum value for different capacities and items.
    dp = [[0 for i in range(W + 1)] for j in range(n)]
    
    # Base condition: Fill in the first row based on the capacity 'W'.
    for i in range(wt[0], W + 1): #Only for the weights that are >= wt[0] till W+1 can stral it
        dp[0][i] = val[0]
        
    # Iterate through the items and capacities.-TOP DOWN APPROACH
    for ind in range(1, n):
        for cap in range(W + 1):
            # Calculate the maximum value when the current item is not taken.
            not_taken = 0 + dp[ind - 1][cap]
            
            # Calculate the maximum value when the current item is taken (if its weight allows).
            taken = -sys.maxsize
            if wt[ind] <= cap:
                taken = val[ind] + dp[ind - 1][cap - wt[ind]]
                
            # Update the DP table with the maximum of not_taken and taken values.
            dp[ind][cap] = max(not_taken, taken)
    
    # The result is stored in the bottom-right cell of the DP array.
    return dp[n - 1][W]

wt = [1, 2, 4, 5]
val = [5, 4, 8, 6]
W = 5
n = len(wt)

print("The Maximum value of items the thief can steal is", knapsack(wt, val, n, W))


