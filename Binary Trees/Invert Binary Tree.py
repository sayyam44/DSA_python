# https://leetcode.com/problems/invert-binary-tree/
#DFS method
#tc=n(only traversing the tree)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        #use recursive methode 
        #step1- swap left with right subtree
        #step2- run the same on the left subtree and then on right sub tree
        
        if root is None:
            return None
        
        temp=root.left
        root.left=root.right
        root.right=temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

#BFS approach O(N)
from collections import deque
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        q=deque([root])

        while q:
            curr=q.popleft()
            curr.left,curr.right=curr.right,curr.left
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return root 
