# Updated
#sc=n,tc=n

# PLEASE SEE BOTTOM VIEW BEFORE THIS

#Method-1 using DFS
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def topview_dfs(root):
    def dfs(node, hd, level):
        if not node:
            return
        
        # If the hd is not in the map, or we find a node at the same hd but shallower, update the map
        if hd not in m or level < m[hd][1]:
            m[hd] = (node.data, level)
        
        # Traverse left and right with updated hd and level
        dfs(node.left, hd - 1, level + 1)
        dfs(node.right, hd + 1, level + 1)
    
    m = {}
    
    # Start DFS from the root
    dfs(root, 0, 0)
    
    # Traverse the map in sorted order of horizontal distances and print values
    for hd in sorted(m.keys()):
        print(m[hd][0], end=" ")

if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    
    print("Top view of the given binary tree:")
    topview_dfs(root)


#Method-2 BFS
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


