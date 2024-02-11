# #sc=n,tc=n

# PLEASE SEE BOTTOM VIEW BEFORE THIS

# IN THIS CASE WE WILL FOLLOOW DFS FORMAT
from collections import deque
class Node:
    def __init__(self,key):
        self.data=key
        self.right=None
        self.left=None
        self.hd=0 #horizontal distance

class solution:
    def topview(self):
        if not root:
            return 

        hd=0
        q=deque([])
        m=dict()
        root.hd=hd
        q.append(root)

        while q:
            root=q[0] #here root=temp according to bottomview.
            q.pop(0)
            hd=root.hd

            if hd not in m: #this is the only difference from bottom view that here we are not updating if the 
                #new value comes with same hd.
                m[hd]=root.val
            
            if root.left:
                root.left.hd=hd-1
                q.append(root.left)

            if root.right:
                root.right.hd=hd+1
                q.append(root.right)

    for i in sorted(m.keys()):
        print(m[i], end=" ")


