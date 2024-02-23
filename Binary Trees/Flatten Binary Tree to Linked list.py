class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.prev = None

    def sol(self, root):
        if not root:
            return None
        self.sol(root.right)
        self.sol(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root
        return root

    def printtree(self, root):
        if not root:
            return 
        print(root.val, end=' ')
        self.printtree(root.left)
        self.printtree(root.right)

def main():
    # Create a tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    root = solution.sol(root)
    solution.printtree(root)

if __name__ == "__main__":
    main()
