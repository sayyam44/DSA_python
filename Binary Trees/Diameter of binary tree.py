# updated new
#Max_Diameter of a binary tree is the maximum distance bw any 2 nodes in 
#a given tree
#Diameter of a node is the sum of left height and the right height

# Time Complexity: O(n)
# Space Complexity: O(h) { here "h" is the height of the tree }
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter=[0]
        def height(root):
            if not root:
                return 0
            lh=height(root.left)
            rh=height(root.right)
            diameter=lh+rh
            max_diameter[0]=max(max_diameter[0],diameter)
            return 1+max(lh,rh)

        height(root)
        return max_diameter[0]