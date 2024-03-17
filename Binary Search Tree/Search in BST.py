# tc= height of the tree
from collections import deque
#METHOD -1 : DFS APPROACH 
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        if root.val < val:
            return self.searchBST(root.right, val)

# Example usage
# Constructing a simple binary search tree
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
result = sol.searchBST(root, 2)

if result:
    print("Found node with value:", result.val)
else:
    print("Node with value not found")


#METHOD-2 :BFS APPROACH 
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        if not root:
            return None
        q = deque([root])
        while q:
            node=q.popleft()
            if node.val==val:
                return node
            if node.left:
                q.append([node.left])
            if node.right:
                q.append([node.right])
        return None

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

sol = Solution()
result = sol.searchBST(root, 2)

if result:
    print("Found node with value:", result.val)
else:
    print("Node with value not found")