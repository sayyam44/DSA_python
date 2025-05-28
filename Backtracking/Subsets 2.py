# updated new
# https://leetcode.com/problems/subsets-ii/

#TC=n*2^n + nlogn
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr=[]
        res=[]
        def dfs(i):
            if i>=len(nums):
                res.append(curr.copy())
                return 
            curr.append(nums[i])
            dfs(i+1)
            curr.pop()
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res