class Treenode:
    def __init__(self,val=0,left=None,Right=None):
        self.val=val
        self.left=left
        self.right=Right

class Solution :
    def rsv(self,root):
        self.res=[]
        self.userfunc(root,0)
        return self.res
    
    def userfunc(self,root,level):
        if not root:
            return 
        if level==len(self.res):
            self.res.append(root.val)
        self.userfunc(root.right,level+1)
        self.userfunc(root.left,level+1)
