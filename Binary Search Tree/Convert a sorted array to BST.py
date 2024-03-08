class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def sortedArrayToBST(self,nums):
        def dfs(l,r):
            if l>r or l<0 or r<0 or r>=len(nums) or l>=len(nums):
                return None
            
            mid=(l+r)//2
            root=TreeNode(nums[mid])
            root.left=dfs(l,mid-1)
            root.right=dfs(mid+1,r)
            return root
        return dfs(0,len(nums)-1)

# Example usage
nums = [-10, -3, 0, 5, 9]
sol = Solution()
result = sol.sortedArrayToBST(nums)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

inorder_traversal(result)



            