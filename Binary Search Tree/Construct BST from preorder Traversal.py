# updated
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/

# tc= height of the tree
class TreeNode:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None

#the node will move towards left if the current value to be inserted is smaller than the upper bound 
# if the node is added towards left then upper bound is updated by the currents value
# if the node is to be added on the right then the upper bound will remain same 
class solution:
    def insert(self,root,k):
        if not root:
            return Treenode(val=k)
        if root.val>k: #if the value to be added that is k is smaller than the root value 
            root.left=self.insert(root.left,k)
        if root.val<k:
            root.right=self.insert(root.right,k)
        return root
    def bstFromPreorder(self,preorder):
        root=TreeNode(preorder[0])
        for i in preorder[1:]:
            self.insert(root,i)
        return root  