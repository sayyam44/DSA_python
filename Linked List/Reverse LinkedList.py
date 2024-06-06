class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# #optimized sol- tc=n,sc=1 
class Solution:
    def reverseList(self, head):
        
        prev,curr=None,head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr= nxt
        return prev

#https://www.youtube.com/watch?v=D2vI2DNJGd8
# #recursive method-tc=n,sc=n
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newhead=self.reverseList(head.next)
        front=head.next
        front.next=head
        head.next=None
        return newhead
            

#FULL CODE 
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
class LinkedList:

	def __init__(self):
		self.head = None

	def reverse(self):
		prev = None
		current = self.head
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def printList(self):
		temp = self.head
		while(temp):
			print(temp.data, end=" ")
			temp = temp.next

llist = LinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)

print ("Given linked list")
llist.printList()
llist.reverse()
print ("\nReversed linked list")
llist.printList()
