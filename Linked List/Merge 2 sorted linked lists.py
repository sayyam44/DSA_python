# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#tc=n,sc=1
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy=ListNode() 
        tail=dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next=l1
                l1=l1.next
            else:
                tail.next=l2
                l2=l2.next
            tail=tail.next
            
        if l1:
            tail.next=l1
        elif l2:
            tail.next=l2
        
        return dummy.next

#FULL CODE

class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	# Method to display the list
	def printList(self):
		temp = self.head
		while temp:
			print(temp.data, end=" ")
			temp = temp.next

	# Method to add element to list
	def addToList(self, newData):
		newNode = Node(newData)
		if self.head is None:
			self.head = newNode
			return

		last = self.head
		while last.next:
			last = last.next

		last.next = newNode


# Function to merge the lists
# Takes two lists which are sorted
# joins them to get a single sorted list
def mergeLists(headA, headB):

	# A dummy node to store the result
	dummyNode = Node(0)

	# Tail stores the last node
	tail = dummyNode
	while True:

		if headA is None:
			tail.next = headB
			break
		if headB is None:
			tail.next = headA
			break

		if headA.data <= headB.data:
			tail.next = headA
			headA = headA.next
		else:
			tail.next = headB
			headB = headB.next
		tail = tail.next

	return dummyNode.next


listA = LinkedList()
listB = LinkedList()

listA.addToList(5)
listA.addToList(10)
listA.addToList(15)

listB.addToList(2)
listB.addToList(3)
listB.addToList(20)

listA.head = mergeLists(listA.head, listB.head)

print("Merged Linked List is:")
listA.printList()
