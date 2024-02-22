class StackNode:
 
    # Constructor to initialize a node
    def __init__(self, data=0,next=None):
        self.data = data
        self.next = None
 
 
class Stack:
 
    # Constructor to initialize the root of linked list
    def __init__(self):
        self.head = None
 
    def isEmpty(self):
        return True if self.head is None else False 
        
    def push(self, data):
        newNode = StackNode(data)
        newNode.next = self.head #making newnode's next to root because 1stly we need to delete the newnode value 
        self.head = newNode #root will be pointing towards the topmost value
        print ("% d pushed to stack" % (data))
 
    def pop(self):
        if (self.isEmpty()):
            return float("-inf")
        temp = self.head
        self.head = self.head.next #now making the topmost value as the one lower than the actual topmost value
        popped = temp.data #deleting the topmost value
        return popped
 
    def peek(self):
        if self.isEmpty():
            return float("-inf")
        return self.head.data #since root is pointing towards the top of the stack.

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
 
print ("% d popped from stack" % (stack.pop()))
print ("Top element is % d " % (stack.peek()))
 