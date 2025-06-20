# updated new
# https://leetcode.com/problems/binary-tree-paths/
#1st method
def binarytreepaths(self,root):
    ans=[]
    def dfs(root,s):
        nonlocal ans
        if root.left:
            dfs(root.left,s+"->"+str(root.left.val))
        if root.right:
            dfs(root.right,s,"->"+str(root.right.val))
        if not root.left and not root.right:
            ans.append(s)
        return 
    dfs(root,str(root.val))
    return ans 


#2nd method
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def print_paths(self, root, path=[]):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right:  # Check if it's a leaf node
            print("->".join(map(str, path)))
        else:
            self.print_paths(root.left, path.copy())
            self.print_paths(root.right, path.copy())

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution = Solution()
    solution.print_paths(root)

if __name__ == '__main__':
    main()
