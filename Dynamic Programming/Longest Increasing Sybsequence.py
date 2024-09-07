# https://leetcode.com/problems/longest-increasing-subsequence/description/

# BRUTE FORCE APPROACH
def new(lst):
    final=0
    for i in range(len(lst)):
        curr_len=1
        prev_val=lst[i]
        for j in range(i+1,len(lst)):
            if lst[j]>prev_val: 
                curr_len+=1
                prev_val=lst[j]
        final=max(curr_len,final)
    print (final)

new(lst=[8,6,5,6,7,4,3,5,6,7,8,9])


#RECURSION(TC=2^n(because for all the element we have 2 options take or not take)) 
# (SC = N(auxilury stack space))
def f(ind,prev_ind,arr): #length of the longest increasing subsequence 
#starting from index ind till end and having previous index as prev_ind
#example-> f(3,0)-> length of longest increasing subsequence starting from index 
#3 till length of the array with prev index pointing at 0th index
#Here we are including prev_ind because we need to check whether the element at index = ind
#can be included into this subsequence or not
    
    # Base case: if we have reached beyond the last index, return 0
    if (ind==len(arr)):
        return 0
    
    not_take=0+f(ind+1,prev_ind,arr)
    #we can only take the current ind element if we dont have anyprev element i.e.prev=-1
    #or we can take an element if the element at ind > element at prev_ind
    take=0
    if (prev_ind==-1 or arr[ind]>arr[prev_ind]):
        take=1+f(ind+1,ind,arr) #prev index becomes the ind
    return max(take,not_take)

nums=[10,9,2,5,3,7,101,18]
def new_func(nums):
    print(f(0,-1,nums))

new_func(nums)


#Memoization
#TC=O(N*N) 
#SC=(N*N)->for dp array+N->for recursion stack space
def get_longest_increasing_subsequence_length(arr, n, ind, prev_index, dp):
    # Base condition
    if ind == n:
        return 0

    if dp[ind][prev_index + 1] != -1:
        return dp[ind][prev_index + 1]

    not_take = 0 + get_longest_increasing_subsequence_length(arr, n, ind + 1, prev_index, dp)

    take = 0

    if prev_index == -1 or arr[ind] > arr[prev_index]:
        take = 1 + get_longest_increasing_subsequence_length(arr, n, ind + 1, ind, dp)

    dp[ind][prev_index + 1] = max(not_take, take)
    return dp[ind][prev_index + 1]


def longest_increasing_subsequence_length(arr):
    n = len(arr)
    #for ind index we are storing from 0 till n-1 elements
    #for prev index we are storing from -1 till n-1 index 
    #so for ind index we will make rows of N length
    #But for prev index we need to get a coordinate change i.e. store -1th element at 0th index and so on
    #so that is why we are creating columns of n+1 length
    dp = [[-1 for _ in range(n + 1)] for _ in range(n)]

    return get_longest_increasing_subsequence_length(arr, n, 0, -1, dp)


arr = [10, 9, 2, 5, 3, 7, 101, 18]

result = longest_increasing_subsequence_length(arr)
print("The length of the longest increasing subsequence is", result)


#TABULATION
class Solution(object):
    def lengthOfLIS(self, nums):
        n = len(nums)
        # Initialize dp table
        # dp[i][prev_ind + 1] will store the length of LIS starting from index i with prev_ind
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

        #here no base case as everything is already assigned to 0

        # Fill the dp table bottom-up(in the opposite fashion)
        #here we are again doing the coordinate change for prev_ind
        for ind in range(n - 1, -1, -1):  # Iterate from last index to the first
            for prev_ind in range(ind - 1, -2, -1):  # Previous index can be from ind-1 to -1 (no previous element)
                # Option 1: Not taking the current element
                not_take = dp[ind + 1][prev_ind + 1]

                # Option 2: Taking the current element if it's valid
                take = 0
                if prev_ind == -1 or nums[ind] > nums[prev_ind]:
                    take = 1 + dp[ind + 1][ind + 1]

                # Store the result in the dp table
                dp[ind][prev_ind + 1] = max(take, not_take)

        # The result is stored in dp[0][-1+1], i.e., dp[0][0], meaning starting from index 0 with no previous index
        return dp[0][0]

# Example usage
solution = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(solution.lengthOfLIS(nums))  # Output: 4
