# updated new
# https://leetcode.com/problems/combination-sum-ii/
#Read Subsets 2 solution before this

class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        curr=[]
        def dfs(i):
            if sum(curr)==target:
                res.append(curr.copy())
                return 
            if i>=len(nums) or sum(curr)>target:
                return 
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            while (i+1)<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res