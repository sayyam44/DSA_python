# updated new
# https://leetcode.com/problems/non-decreasing-subsequences/
# https://leetcode.com/problems/non-decreasing-subsequences/
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        curr = []
        
        def dfs(i):
            if i >= len(nums) and len(curr) <= 1:  # Combined condition to add subsequence
                # res.add(tuple(curr))  # Convert list to tuple for uniqueness
                return
            if i >= len(nums) and len(curr) > 1:  # Combined condition to add subsequence
                res.add(tuple(curr))  # Convert list to tuple for uniqueness
                return
            
            if len(curr) == 0 or curr[-1] <= nums[i]:  # Check non-decreasing order
                curr.append(nums[i])
                dfs(i + 1)
                curr.pop()  # Backtrack
            
            dfs(i + 1)  # Explore without including nums[i]
        
        dfs(0)
        return [list(seq) for seq in res]  # Convert tuples back to lists