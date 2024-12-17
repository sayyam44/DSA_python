# updated
# floor for a value in bst is the value that is just smaller or equal to that value
# https://www.geeksforgeeks.org/problems/floor-in-bst/0
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    class Solution:
        def floor(self, root, x):
            floor = -1
            while root:
                if root.val == x:
                    return root.val  # Exact match for x found
                elif root.val > x:
                    root = root.left  # Move to the left subtree
                else:
                    floor = root.val  # Update floor to the current value
                    root = root.right  # Move to the right subtree
            return floor


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

# Create an instance of TreeNode
tree_node = TreeNode(None)

# Example usage of floor_ method
key_to_find = 65
floor_value = tree_node.floor_(bst_root, key_to_find)
print(f"Floor value of {key_to_find}: {floor_value}")  # Output: Floor value of 65: 60
