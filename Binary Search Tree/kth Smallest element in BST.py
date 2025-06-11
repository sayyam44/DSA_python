# updated new
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
#Method-1 
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def counting(node):
            if not node:
                return 0
            return 1+counting(node.left)+counting(node.right)
        while root:
            left_count=counting(root.left)
            if k<=left_count:
                root=root.left
            elif k==left_count+1:
                return root.val
            else:
                k-=left_count+1
                root=root.right
        

#USING INORDER TRAVERSAL , TC=O(n)
#METHOD-2 Using inorder traversal 
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
    def kthsmallest(self,root,k):
        self.res=[]
        self.inorder(root)
        return self.res[k-1] if 0 < k <= len(self.res) else None

    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)
    

def insert(root,key):
    if root is None:
        return TreeNode(key)
    if root.val<key:
        root.right=insert(root.right,key)
    else:
        root.left=insert(root.left,key)
    return root

arr=[3,5,6,2,19,13,1,14,16]
bst_root=None
for key in arr:
    bst_root=insert(bst_root,key)

treenode=TreeNode(None)
resultant=treenode.kthsmallest(bst_root,4)
print(resultant)


