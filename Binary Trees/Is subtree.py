#tc=r*s
#https://leetcode.com/problems/subtree-of-another-tree/
#https://www.youtube.com/watch?v=E36O5SWp-LE

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, r: Optional[TreeNode], s: Optional[TreeNode]) -> bool:
        #base cases
        if not s: return True #if subtree is empty then it always returns true
        if not r: return False #if tree is empty but subtree is not then always return false 
        if self.sametree(s,r): return True
        
        return (self.isSubtree(r.left,s) or self.isSubtree(r.right,s)) 
        #this case occurs if neither base case occurs nor the root values of r and s are same 
            
    def sametree(self,p,q): #same as same tree problem
        
        if not p and not q:
            return True
        if p and q and p.val==q.val:
            return(self.sametree(p.left,q.left) and self.sametree(p.right,q.right))
        return False