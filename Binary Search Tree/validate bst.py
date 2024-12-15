# Updated
#for each node we will define a range and the node must lie within that range 
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        def isValid(root, minVal, maxVal):
            if not root:
                return True
            if root.val <= minVal or root.val >= maxVal:
                return False
            else:
                return isValid(root.left, minVal, root.val) and isValid(root.right, root.val, maxVal)
        return isValid(root, -float("inf"), float("inf"))

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

sol = Solution()
result = sol.isValidBST(root)

print("Is valid BST?", result)