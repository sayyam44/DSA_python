#tc=p*q
# https://leetcode.com/problems/same-tree/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #if both p and q are empty then they are same 
            return True
        if p and q and p.val==q.val:
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) 
        return False
        
        