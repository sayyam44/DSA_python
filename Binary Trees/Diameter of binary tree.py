# https://www.youtube.com/watch?v=Rezetez59Nk&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=18
#For a node a diameter is the sum of its left subtree and its right subtree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.diameter=0

    def height(self, node: Optional[TreeNode]) -> int:
        lh=self.height(node.left) if node.left else 0
        rh=self.height(node.right) if node.right else 0
        if lh+rh > self.diameter:
            self.diameter=lh+rh #here we are just updating the diameter with the maximum diameter
        return 1+max(lh,rh) #at every step we are returning the height 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.diameter