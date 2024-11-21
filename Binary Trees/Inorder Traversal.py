# updated
# https://leetcode.com/problems/binary-tree-inorder-traversal/
#METHOD 1- RECURSIVE INORDER
#TC=N,SC=N(auxiliary stack space)
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
#tc=n,sc=n
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
