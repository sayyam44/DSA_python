# https://leetcode.com/problems/subsets-ii/

#TC=n*2^n + nlogn
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def dfs(i,subset):
            if i==len(nums):
                res.append(subset.copy())
                return
            #including the element into the subset
            subset.append(nums[i])
            dfs(i+1,subset)
            subset.pop() #because till now we have reached at the end of the left 
            #side of the tree 
            #eg- we have [1,2,2,3], first i=1 then while loop wil run making i=2
            #but now while loop will not run so the next element to be added is 3
            #that is why we called the dfs at i+1
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1,subset)
        dfs(0,[])
        return res
            