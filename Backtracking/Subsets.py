# https://leetcode.com/problems/subsets/
#TC=2^N (as for each element we have 2 possibilities that is either take it or not take it)
#Backtracking is just like recursion but the only difference is we try to put in the conditions 
#if the conditions are satisfied then we move forward and if the condition 
#is not satisfied then we backtrack from that point only to the last step

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                # we are appending the copy of this subset as we need to 
                #change this subset further 
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
