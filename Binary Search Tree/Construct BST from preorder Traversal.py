# updated new
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

# tc= height of the tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def insert(self, root: TreeNode, i: int) -> TreeNode:
        if not root:
            return TreeNode(val=i)
        if i < root.val:
            root.left = self.insert(root.left, i)
        elif i > root.val:
            root.right = self.insert(root.right, i)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        # Create the root node
        root = TreeNode(preorder[0])
        # Insert the remaining elements
        for i in preorder[1:]:
            self.insert(root, i)
        return root
