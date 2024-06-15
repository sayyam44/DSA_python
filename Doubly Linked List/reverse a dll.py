class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None
	def reverse(self):
        curr=self.head
        while curr:
            temp=curr.prev
            curr.prev=curr.next
            curr.next=temp
            curr=curr.prev
        return temp.prev
