# updated new
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sol(self, preorder, inorder):
        if not inorder:
            return None
        root = TreeNode(preorder.pop(0))
        mid = inorder.index(root.val)
        root.left = self.sol( preorder, inorder[:mid])
        root.right = self.sol( preorder, inorder[mid + 1:])
        return root

    def print_tree(self, root):
        if root is None:
            return
        print(root.val)
        self.print_tree(root.left)
        self.print_tree(root.right)

def main():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution = Solution()
    root = solution.sol(preorder, inorder)
    solution.print_tree(root)

if __name__ == "__main__":
    main()
