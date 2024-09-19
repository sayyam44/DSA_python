# https://leetcode.com/problems/combination-sum-ii/
#Read Subsets 2 solution before this

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(ind, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            if total > target or ind == len(candidates):
                return
            curr.append(candidates[ind])
            dfs(ind+1, curr, total + candidates[ind])
            curr.pop()
            while ind+1<len(candidates) and candidates[ind]==candidates[ind+1]:
                ind+=1
            dfs(ind + 1, curr, total)

        dfs(0, [], 0)
        return res