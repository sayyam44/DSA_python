# updated new
#A Binary tree is said to be balanced if for all the nodes the 
# difference bw the height of left subtree and the right subtree is <=1
# https://leetcode.com/problems/balanced-binary-tree/

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        isbalance=[True]
        def height(root):
            if not root:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            if abs(lh-rh)>1:
                isbalance[0]=False
            return 1+max(lh,rh)
        height(root)
        return isbalance[0]