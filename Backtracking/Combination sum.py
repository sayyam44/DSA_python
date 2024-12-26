# updated
# https://leetcode.com/problems/combination-sum/description/
# TC=2^target as the height of the tree is equal to the target
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        now=[]
        def dfs(i,now):
            if i>=len(nums) or sum(now)>target:
                return 
            elif sum(now)==target:
                res.append(now.copy())
                return 
            elif sum(now)<target:
                now.append(nums[i])
                dfs(i,now)
            now.pop()
            dfs(i+1,now)
        dfs(0,[])
        return res