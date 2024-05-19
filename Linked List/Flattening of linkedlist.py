#use recursion flatten function and reach to the last linked list for root.right , then merger last and second last ll
# tc= summation of total number of nodes
class Node():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.down = None
 
class LinkedList():
    def __init__(self):
 
        self.head = None
 
    def push(self,head_ref,data):
 
        new_node = Node(data)
 
        new_node.down = head_ref
 
        head_ref = new_node
 
        return head_ref
 
    def printList(self):
 
        temp = self.head
        while(temp != None):
            print(temp.data,end=" ")
            temp = temp.down
 
        print()
 
    # An utility function to merge two sorted linked lists
    def merge(self, a, b): #2nd step
        # if first linked list is empty then second
        # is the answer
        if(a == None):
            return b
         
        # if second linked list is empty then first
        # is the result
        if(b == None):
            return a
 
        # compare the data members of the two linked lists
        # and put the larger one in the result
        result = None
 
        if (a.data < b.data):
            result = a
            result.down = self.merge(a.down,b)
        else:
            result = b
            result.down = self.merge(a,b.down)
 
        result.right = None
        return result
 
    def flatten(self, root): #1st step
 
        # Base Case
        if(root == None or root.right == None):
            return root
        # recur for list on right
 
        root.right = self.flatten(root.right) #root.right will reach to last ll
 
        # now merge
        root = self.merge(root, root.right) #if root.right is the last ll then the second last will be its root
 
        # return the root
        # it will be in turn merged with its left
        return root

L = LinkedList()

L.head = L.push(L.head, 30);
L.head = L.push(L.head, 8);
L.head = L.push(L.head, 7);
L.head = L.push(L.head, 5);
 
L.head.right = L.push(L.head.right, 20);
L.head.right = L.push(L.head.right, 10);
 
L.head.right.right = L.push(L.head.right.right, 50);
L.head.right.right = L.push(L.head.right.right, 22);
L.head.right.right = L.push(L.head.right.right, 19);
 
L.head.right.right.right = L.push(L.head.right.right.right, 45);
L.head.right.right.right = L.push(L.head.right.right.right, 40);
L.head.right.right.right = L.push(L.head.right.right.right, 35);
L.head.right.right.right = L.push(L.head.right.right.right, 20);

L.head = L.flatten(L.head);
 
L.printList()


