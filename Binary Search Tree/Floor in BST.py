# floor for a value in bst is the value that is just smaller or equal to that value
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

    def floor_(self, root, key):
        floor = -1  # Update floor whenever we find some value smaller than or equal to key
        while root:
            if root.val == key:
                floor = root.val
                return floor
            # Since we want to find just smaller value, we go towards root.right below
            # Though we have found some root.val that is just smaller than the key, there may be some
            # value that is greater than root.right but smaller than key.
            if root.val<key:  # We will update the value of floor every time we find some root value smaller than the key value
                # and we need to find the value (max) <= key
                floor = root.val  # Update floor
                root = root.right  # Because we need to find max value that is just less than key, so in BST, we will find max value on the right of root
            else:
                root = root.left
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
