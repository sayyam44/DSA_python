# DO BST ITERATOR CODE - make a next stack same as bst iterator and another before named stack 
# Now check if st1.pop()+st2.pop()== k if yes then return true 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def pushLeft(st, root):
            while root:
                st.append(root)
                root = root.left

        def pushRight(st, root):
            while root:
                st.append(root)
                root = root.right

        def nextLeft(st): #this actually gives the leftmose element of bst that is inorder's 1st element
            node = st.pop()
            pushLeft(st, node.right)
            return node.val

        def nextRight(st):#this gives the last element of inorder of bst
            node = st.pop()
            pushRight(st, node.left)
            return node.val

        #step-1 creating the 2 stacks(for left side and for right side)
        stLeft, stRight = [], []
        pushLeft(stLeft, root)
        pushRight(stRight, root)

        #step-2  finding the left pointer(from st left stack) and the right pointer(from stRight stack)
        left, right = nextLeft(stLeft), nextRight(stRight)
        while left < right:
            if left + right == k: return True
            if left + right < k:
                left = nextLeft(stLeft)
            else:
                right = nextRight(stRight)
        return False

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

solution = Solution()
target_sum = 9
print(solution.findTarget(root, target_sum)) 