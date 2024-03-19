#see the code for bst iterator for left solution
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack=[]
        while root:
            self.stack.append(root)
            root=root.right

    def next(self) -> int: #since we are following inorder traversal
        node=self.stack.pop()
        x=node.left
        while x:
            self.stack.append(x)
            x=x.right
        return node.val

    def hasNext(self) -> bool:
        return len(self.stack)>0