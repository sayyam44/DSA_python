# updated
class Treenode:
    def __init__(self,val=0,left=None,Right=None):
        self.val=val
        self.left=left
        self.right=Right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        def newfunc(root,level):
            if not root:
                return 
            if level==len(self.res):
                self.res.append(root.val)
            newfunc(root.right,level+1)
            newfunc(root.left,level+1)
        newfunc(root,0)
        return self.res