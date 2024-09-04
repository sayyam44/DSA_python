# https://leetcode.com/problems/edit-distance/description/

#RECURSION(TC=exponential,SC=N+M)
#MEMOIZATION(TC=NxM, SC=(NxM)+(N+M))
def f(ind1, ind2, s1, s2, dp): 
    # Base Cases
    if ind1 < 0: # if ind1 is -ve that means string 1 got exhausted
        return ind2 + 1 # To make a string of length ind2+1 from an empty string will require ind2+1 insert operations
    if ind2 < 0: # similarly to make a string of length ind2+1 to an empty string 
        return ind1 + 1 # it will require ind1+1 delete operations
    
    if dp[ind1][ind2] != -1:
        return dp[ind1][ind2]
    
    if s1[ind1] == s2[ind2]: # If we get the same char at ind1 and ind2 of s1 and s2 respectively
        dp[ind1][ind2] = f(ind1 - 1, ind2 - 1, s1, s2, dp) # No operation needed, just move 1 step back
    else:
        # 1+f(ind1,ind2-1) #insert (if we insert an element at ind1+1 in s1 then ind2 of s2 moves the ind1 in s1 remains unchanged)
        # 1+f(ind1-1,ind2) #delete (if we delete an element from s1 ind1 moves back by 1 ind2 remains unchanged)
        # 1+f(ind1-1,ind2-1) #replace (if ind1 in s1 is replaced by same char at ind2 ins2 then both ind1 and ind2 are same char then we move both ind1 and ind2 back by 1)
        #Now find the min of all the above 3 cases
        dp[ind1][ind2] = 1 + min(
            f(ind1 - 1, ind2, s1, s2, dp),   # Delete operation
            f(ind1, ind2 - 1, s1, s2, dp),   # Insert operation
            f(ind1 - 1, ind2 - 1, s1, s2, dp) # Replace operation
        )
    
    return dp[ind1][ind2]

def editDistance(S1, S2):
    n = len(S1)
    m = len(S2)

    # Initialize a 2D DP array with -1 values
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    # Calculate and return the edit distance
    return f(n - 1, m - 1, S1, S2, dp)

s1 = "horse"
s2 = "ros"
print("The minimum number of operations required is:", editDistance(s1, s2))


#TABULATION 
# In the recursive logic, we set the base case too if(i<0 ) and if(j<0) but we can’t set 
# the dp array’s index to -1. Therefore a hack for this issue is to shift every index 
# by 1 towards the right.
#TC=NxM, SC=NxM
def editDistance(S1, S2):
    n = len(S1)
    m = len(S2)

    # Initialize a 2D DP array of size (n+1) x (m+1) with all elements set to 0
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)] #new changes

    # Initialize the first row and first column of the DP array
    for i in range(n + 1):
        dp[i][0] = i #new changes
    for j in range(m + 1):
        dp[0][j] = j #new changes

    # Fill in the DP array using dynamic programming
    for i in range(1, n + 1): #new changes
        for j in range(1, m + 1): #new changes
            # If the characters at the current positions match, no operation is needed
            if S1[i - 1] == S2[j - 1]: #new changes
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Calculate the minimum of three choices:
                # 1. Replace the current character (diagonal move)
                # 2. Insert a character into S1 (move up)
                # 3. Delete a character from S1 (move left)
                dp[i][j] = 1 + min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))

    # The final value in dp[n][m] is the minimum number of operations required
    return dp[n][m] #new changes

s1 = "horse"
s2 = "ros"

# Calculate and print the minimum number of operations required
print("The minimum number of operations required is:", editDistance(s1, s2))



