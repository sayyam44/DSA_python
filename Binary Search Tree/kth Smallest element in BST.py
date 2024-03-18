#USING INORDER TRAVERSAL , TC=O(n)
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


