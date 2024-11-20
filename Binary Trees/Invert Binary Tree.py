# updated
# https://leetcode.com/problems/invert-binary-tree/
#DFS method
#tc=n(only traversing the tree)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    #use recursive methode 
    #step1- swap left with right subtree
    #step2- run the same on the left subtree and then on right sub tree
    if root is None:
        return None
    
    temp=root.left
    root.left=root.right
    root.right=temp
    
    invertTree(root.left)
    invertTree(root.right)
    return root

def printtree(root):
    if root is not None:
        print(root.val)
        printtree(root.left)
        printtree(root.right)
    
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

invertTree(root)
printtree(root)


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
