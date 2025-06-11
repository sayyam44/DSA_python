# updated new
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        small = min(p.val, q.val)
        large = max(p.val, q.val)
        
        while root:
            if root.val > large:
                root = root.left
            elif root.val < small:
                root = root.right
            else:
                return root

        return None

# Create a sample binary search tree
def insert(root, key):
    if not root:
        return TreeNode(key)
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)
    return root

# Insert nodes into the BST
keys = [6, 2, 8, 0, 4, 7, 9, 3, 5]
bst_root = None
for key in keys:
    bst_root = insert(bst_root, key)

# Define nodes p and q
p = TreeNode(2)
q = TreeNode(8)

# Create a Solution instance
solution = Solution()
# Find the lowest common ancestor
lca = solution.lowestCommonAncestor(bst_root, p, q)

if lca:
    print("Lowest Common Ancestor:", lca.val)  # Output: 6
else:
    print("No Lowest Common Ancestor found.")
