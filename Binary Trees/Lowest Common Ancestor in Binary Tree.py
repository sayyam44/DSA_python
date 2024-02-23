#Lowest common ancestor is the deepest common node of 2 nodes 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root==None or root.val==p.val or root.val==q.val:
            return root
        
        # Look for keys in left and right subtrees
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)

        #if the left side of a node is none that means we found something on its right 
        if left == None:
            return right 
        if right==None:
            return left
        #this case is the final case when we got to know that for a node we have p on its left subtree and q on its right subtree
        else:
            return root

def main():
    # Create a tree
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    result = solution.lowestCommonAncestor(root, TreeNode(7), TreeNode(9))
    print("Lowest common ancestor:", result.val)
    

if __name__ == "__main__":
    main()
