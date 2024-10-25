# updated
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CreateLL:
    def __init__(self):
        self.head=None
    def createll(self,lst):
        for data in lst:
            newnode=Node(data)
            if not self.head: #if we have empty list till now
                self.head=newnode
            else: #if we already have some nodes in ll
                #then we have to add the new node at the end of ll
                curr=self.head
                while curr.next:
                    curr=curr.next
                curr.next=newnode
        return self.head
    
    def printll(self):
        curr=self.head
        while curr:
            print(curr.data,end="->")
            curr=curr.next
        print("None")

lst=[1,2,3,4]
newll=CreateLL()
newll.createll(lst)
newll.printll()

