# updated new
#Method-1 
class Solution:
    def kthLargest(self, root: Optional[TreeNode], k: int) -> int:
        # Helper function to count the nodes in a subtree
        def count_nodes(node):
            if not node:
                return 0
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        while root:
            right_count = count_nodes(root.right)  # Size of the right subtree
            
            if k <= right_count:  # If k lies in the right subtree
                root = root.right
            elif k == right_count + 1:  # If the current root is the kth largest
                return root.val
            else:  # If k lies in the left subtree
                k -= (right_count + 1)  # Adjust k to skip the current root and right subtree
                root = root.left
        
        return -1  # If k is invalid


#Kth largest element in BST using reverse inorder traversal.
#Method-2 using Inorder Traversal 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def kthlargest(self, root, k):
        self.res = []
        self.reverse_inorder(root)
        return self.res[k - 1] if 0 < k <= len(self.res) else None

    def reverse_inorder(self, root):
        if root is None:
            return
        self.reverse_inorder(root.right)
        self.res.append(root.val)
        self.reverse_inorder(root.left)

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# Example usage:
arr = [3, 5, 6, 2, 19, 13, 1, 14, 16]
bst_root = None
for key in arr:
    bst_root = insert(bst_root, key)

treenode = TreeNode(None)
resultant = treenode.kthlargest(bst_root, 4)
print(resultant)  # Output: 13
