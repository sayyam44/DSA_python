# updated
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def ceil_(self, root, key):
        ceil = -1
        while root:
            if root.val == key:
                ceil = root.val
                return ceil
            if root.val < key:  # Every condition is the same, just update ceil while moving on the left
                root = root.right
            else:
                ceil = root.val
                root = root.left
        return ceil


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
keys = [50, 30, 20, 40, 70, 60, 80]
bst_root = None
for key in keys:
    bst_root = insert(bst_root, key)

tree_node = TreeNode(None)

# Example usage of ceil_ method
key_to_find = 65
ceil_value = tree_node.ceil_(bst_root, key_to_find)
print(f"Ceil value of {key_to_find}: {ceil_value}")  # Output: Ceil value of 65: 70