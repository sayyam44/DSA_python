# updated new
#tc=r*s
#https://leetcode.com/problems/subtree-of-another-tree/

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root,subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val==subRoot.val:
                return (isSame(root.left,subRoot.left) and isSame(root.right,subRoot.right))
            return False 

        if not subRoot:return True
        if not root:return False
        if self.isSame(root,subRoot):return True

        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))