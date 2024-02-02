#tc=p*q
# https://leetcode.com/problems/same-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #base cases
        if not p and not q: #if both p and q are empty then they are same 
            return True
        # if not p or not q or p.val!=q.val: #if only one among p and q is empty or value of p and value at q is not same then its false
            # return False
        if p and q and p.val==q.val:
            return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)) 
        return False
        #here recursively checking whether left and right subtrees of p and left and right subtrees of q are same then return true
        
        