# sc=n,tc=n

#vertical order traversal is followed over here we will create a vertical line '0' throught the root node
# covering all the nodes directly below it and like that make vertical line to its left by -1,-2,....
#and also on the right side draw vertical lines with +1,+2,...
#and we need to find the last elements of all these vertical lines.

#append all the values in form of node,hd(hosrizontal distance) into the queue and all its child nodes along
# with left's child's level -1,-2,-3 and also add its right child along with its level +1,+2,...

#now pop from the queue and append one by one the values into the dict in hd,node format and if some 
#other element comes while traversing the queue with same hd we need to update it like in level order traversal
#but vertically.

# IN THIS CASE WE WILL FOLLOOW DFS FORMAT
from collections import deque
class Node:
     
    def __init__(self, key):
         
        self.data = key
        self.hd = float('inf') #horizontal distance
        self.left = None
        self.right = None

def bottomview(root):
    if not root:
        return 
    
    hd=0

    m=dict() # for storing hd,node and will update it when some other node comes with the same hd.
    q=deque([]) # for storing node,hd 

    root.hd=hd # Assign initialized horizontal distance value to root node and add it to the queue.
    q.append(root) # storing node,hd as we have already defined hd in __init__ class

    while q:
        #in the below steps we are poping the top value of queue and storing it in the opposite way into dict m 
        temp=q.popleft()
        hd=temp.hd
        m[hd]=temp.data #here updation of the nodes with same hd value is happening

        if (temp.left): #storing the left side in the queue
            temp.left.hd=hd-1
            q.append(temp.left)

        if (temp.right): #storing the right side in the queue
            temp.right.hd=hd+1
            q.append(temp.right)

    for i in sorted(m.keys()):   # Traverse the map elements iterating over the hd in sorted way
        print(m[i], end = ' ')
    
if __name__=='__main__':
    
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.left = Node(4)
    root.right.right = Node(25)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
        
    print("Bottom view of the given binary tree :")
        
    bottomview(root)
