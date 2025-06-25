# updated new
#tc=n,sc=H(height of tree)
class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        def newfunc(root,level):
            if not root:
                return 
            if level==len(self.res):
                self.res.append(root.val)
            newfunc(root.left,level+1)
            newfunc(root.right,level+1)
        newfunc(root,0)
        return self.res        

#Easy Method (just like finding the height of the binary tree)
from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def leftsideview(root):
    if not root:
        return []
    q=deque([root])
    res=[]
    while q:
        res.append(q[0].val)
        for i in range(len(q)):
            node=q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    return res

root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.right.left=Node(6)
root.left.left.right=Node(5)


print(leftsideview(root))

