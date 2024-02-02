# https://leetcode.com/problems/binary-tree-inorder-traversal/
#METHOD 1- RECURSIVE INORDER
#TC=N,SC=N(auxiliary stack space)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        res=[]
        res.extend(self.inorderTraversal(root.left))
        res.append(root.val)
        res.extend(self.inorderTraversal(root.right))
        return res

#METHOD 2-ITERATIVE INORDER
#TC=N,SC=N(auxiliary stack space)
# https://www.youtube.com/watch?v=lxTGsVXjwvM&list=PLgUwDviBIf0q8Hkd7bK2Bpryj2xVJk8Vk&index=12
#tc=n,sc=n

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res=[]
        while stack or root:
            while root:
                stack.append(root)
                root=root.left #till all the left values are appended into stack until leaf node is reached
            root=stack.pop() #pop the 1st leaf node 
            res.append(root.val)
            root=root.right #repeat the process for right node of the last popped value
        return res
