#updated
#https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
#The logic is move to left then to right as soon as we find any node
#that is equal to either p or q we will return the root val and when 
#at some node we find both the left and right side as not null then 
#that will be the lowest common ancestor
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        #If root'svalue is equal to p or q value then just retrun the root while iterating
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
