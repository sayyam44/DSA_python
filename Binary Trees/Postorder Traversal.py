# https://leetcode.com/problems/binary-tree-postorder-traversal/
#METHOD 1- POSTORDER RECURSIVE
#TC=N,SC=N(auxiliary stack space)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if root==None:
            return []
        
        res=[]
        res.extend(self.postorderTraversal(root.left))
        res.extend(self.postorderTraversal(root.right))
        res.append(root.val)
        return res

#METHOD 2- POSTORDER ITERATIVE
#TC=N,SC=N(auxiliary stack space)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# WE WILL MAKE OPPOSITE OF POSTORDER (ROOT,RIGHT,LEFT) THEN REVERSE IT 
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res=[]
        while stack:
            root = stack.pop()
            if root:
                res.append(root.val)
                stack.append(root.left)
                stack.append(root.right) #it will put the root's right value above root's left value in 
                # stack and this is what we want in reverse
        return res[::-1]


