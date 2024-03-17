class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def insertIntoBST(root, val):
    if root is None:
        return TreeNode(val)
    
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    elif val > root.val:
        root.right = insertIntoBST(root.right, val)
    
    return root

def constructBST(nums):
    if not nums:
        return None
    
    root = None
    for num in nums:
        root = insertIntoBST(root, num)
    
    return root

# Example usage:
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
root = constructBST(nums)


# Print the inorder traversal of the BST to verify its correctness
def inorderTraversal(node):
    if node:
        inorderTraversal(node.left)
        print(node.val, end=' ')
        inorderTraversal(node.right)

inorderTraversal(root)  # Output: 1 2 3 4 5 6 9