# updated
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
    
class Solution:
    def sol(self,root,k,arr):
        if not root:
            return False
        arr.append(root.val)
        if (root.val)==k:
            return True
        if self.sol(root.left,k,arr) or self.sol(root.right,k,arr):
            return True

        arr.pop(-1)
        return False


    def printpath(self,root,k):
        arr=[]
        if self.sol(root,k,arr):
            print("->".join(map(str,arr)))
        else:
            print('k is not present in the tree')

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    solution=Solution()
    solution.printpath(root,4)


if __name__=='__main__':
    main()
        
