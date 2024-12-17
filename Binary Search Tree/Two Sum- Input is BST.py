# updated
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        self.res=[]

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)

        inorder(root)

        left=0
        right=len(self.res)-1
        while left<right:
            if self.res[left]+self.res[right]==k:
                return True
            elif self.res[left]+self.res[right]<k:
                left+=1
            else:
                right-=1
        return False