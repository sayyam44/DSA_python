# updated new 1
# https://leetcode.com/problems/longest-common-subsequence/description/

#RECURSION
def f(ind1, ind2, s1, s2):
    # Base case: if either index is negative, return 0
    if ind1 < 0 or ind2 < 0:
        return 0

    # Recursive case: characters match
    if s1[ind1] == s2[ind2]:
        return 1 + f(ind1 - 1, ind2 - 1, s1, s2)
    
    # Recursive case: characters do not match
    return max(f(ind1, ind2 - 1, s1, s2), f(ind1 - 1, ind2, s1, s2))

def longestCommonSubsequence(text1, text2):
    # Start recursion from the last indices of both strings
    return f(len(text1) - 1, len(text2) - 1, text1, text2)

# Example usage
text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))  # Output: 3


#Memoization
class Solution(object):
    def f(self,ind1,ind2,s1,s2,dp):
        if ind1<0 or ind2<0:
            return 0
        if dp[ind1][ind2]!=-1:
            return dp[ind1][ind2]
        if s1[ind1] == s2[ind2]:
            dp[ind1][ind2] = 1 + self.f(ind1 - 1, ind2 - 1, s1, s2, dp)
        else:
            dp[ind1][ind2] = max(self.f(ind1, ind2 - 1, s1, s2, dp), self.f(ind1 - 1, ind2, s1, s2, dp))
        return dp[ind1][ind2]

    def longestCommonSubsequence(self, text1, text2):
        dp=[[-1 for _ in range(len(text2))]for _ in range(len(text1))]
        return self.f(len(text1)-1,len(text2)-1,text1,text2,dp)


#TABULATION 
# In the recursive logic, we set the base case too if(i<0 ) and if(j<0) but we can’t set 
# the dp array’s index to -1. Therefore a hack for this issue is to shift every index 
# by 1 towards the right.
def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    #here dp matrix will increase i more columns and 1 more row
    dp=[[-1 for _ in range (m+1)]for _ in range (n+1)]
    
    for i in range(n+1): #1->n
        dp[i][0]==0
    for j in range(m+1): #1=>m
        dp[0][j]==0
    
    for ind1 in range(1,n+1): #including nth index
        for ind2 in range(1,m+1): #including mth index
            if s1[ind1-1]==s2[ind2-1]: #since we have shifted the index by 1
                dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
            else:
                dp[ind1][ind2] = max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])
    
    # The value in dp[n][m] represents the length of the Longest Common Subsequence
    return dp[n][m]

s1 = "acd"
s2 = "ced"
print("The Length of Longest Common Subsequence is", lcs(s1, s2))